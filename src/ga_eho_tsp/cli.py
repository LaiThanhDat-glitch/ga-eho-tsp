"""CLI tiếng Việt cho validate, solve và benchmark; không import GUI."""

import argparse
from dataclasses import asdict
import json
from pathlib import Path

from .algorithms.ga import solve as solve_ga
from .algorithms.eho import solve as solve_eho
from .data.matrix_loader import load_matrix
from .domain.models import EHOConfig, GAConfig
from .experiments.benchmark import benchmark


class VietnameseParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        self.print_usage()
        self.exit(2, f"Lỗi tham số: {message}\n")


def main(argv: list[str] | None = None) -> int:
    parser = VietnameseParser(description="GA–EHO–TSP: giải TSP bằng GA hoặc EHO")
    sub = parser.add_subparsers(dest="command", required=True)
    validate = sub.add_parser("validate", help="Kiểm tra ma trận TSP")
    validate.add_argument("--dataset", required=True)
    run = sub.add_parser("solve", help="Giải TSP bằng GA hoặc EHO")
    run.add_argument("--dataset", required=True)
    run.add_argument("--algorithm", choices=("ga", "eho"), default="ga")
    for flag, default in (("seed", 42), ("population-size", 80), ("generations", 250),
                          ("max-iterations", 250), ("tournament-size", 3), ("elite-count", 2),
                          ("record-history-every", 1)):
        run.add_argument(f"--{flag}", type=int, default=default)
    run.add_argument("--max-evaluations", type=int)
    run.add_argument("--time-limit-seconds", type=float)
    run.add_argument("--clan-count", type=int, default=4)
    run.add_argument("--elephants-per-clan", type=int, default=20)
    run.add_argument("--alpha", type=float, default=0.7)
    run.add_argument("--beta", type=float, default=0.3)
    run.add_argument("--separation-count", type=int, default=1)
    run.add_argument("--crossover-rate", type=float, default=0.9)
    run.add_argument("--mutation-rate", type=float, default=0.15)
    run.add_argument("--selection-method", default="tournament")
    run.add_argument("--crossover-method", default="ox")
    run.add_argument("--mutation-method", default="inversion")
    run.add_argument("--initialization-method", default="random")
    run.add_argument("--nn-seed-fraction", type=float, default=0.25)
    run.add_argument("--stagnation-patience", type=int)
    run.add_argument("--adaptive-mutation", action="store_true")
    run.add_argument("--adaptive-min-rate", type=float, default=0.05)
    run.add_argument("--adaptive-max-rate", type=float, default=0.5)
    run.add_argument("--adaptive-patience", type=int, default=20)
    run.add_argument("--local-search-enabled", action="store_true")
    run.add_argument("--local-search-max-moves", type=int, default=0)
    run.add_argument("--local-search-max-probes", type=int, default=20)
    run.add_argument("--json", dest="json_path", help="Ghi RunResult JSON")
    batch = sub.add_parser("benchmark", help="Benchmark nhiều seed")
    batch.add_argument("--config", required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "benchmark":
            report = benchmark(args.config)
            print(json.dumps(report, ensure_ascii=False, indent=2))
            return 2 if report["failed_runs"] else 0
        problem = load_matrix(args.dataset)
        if args.command == "validate":
            print(f"Hợp lệ: {problem.name}; dimension={problem.dimension}; symmetric=True; diagonal=0; finite=True")
            return 0
        if args.algorithm == "eho":
            config = EHOConfig(seed=args.seed, max_iterations=args.max_iterations,
                iterations=args.max_iterations, max_evaluations=args.max_evaluations,
                time_limit_seconds=args.time_limit_seconds, record_history_every=args.record_history_every,
                clan_count=args.clan_count, elephants_per_clan=args.elephants_per_clan,
                alpha=args.alpha, beta=args.beta, separation_count_per_clan=args.separation_count)
            result = solve_eho(problem, config)
        else:
            values = vars(args).copy()
            for key in ("command", "dataset", "algorithm", "json_path", "clan_count", "elephants_per_clan",
                        "alpha", "beta", "separation_count"):
                values.pop(key, None)
            config = GAConfig(**values)
            result = solve_ga(problem, config)
        tour = (*result.best_route, 0)
        print(f"algorithm={result.algorithm}")
        print(f"distance={result.best_distance:g}\ntour=" + " → ".join(map(str, tour)))
        print(f"seed={result.seed}; iterations={result.iterations_completed}; evaluations={result.evaluations}; runtime={result.elapsed_seconds:.6f}s; status={result.stopping_reason}")
        if args.json_path:
            path = Path(args.json_path)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(asdict(result), ensure_ascii=False, indent=2), encoding="utf-8")
        return 0
    except (ValueError, OSError, KeyError, TypeError) as error:
        print(f"Lỗi: {error}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
