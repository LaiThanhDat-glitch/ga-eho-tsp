"""Discrete elephant herding optimization for permutation TSP."""

from dataclasses import asdict
from math import fsum
from random import Random
from time import perf_counter

from ... import __version__
from ...domain.models import EHOConfig, IterationStat, RunResult, TSPProblem
from ...domain.objective import validate_route
from ...domain.operators import random_permutation
from ...domain.protocols import ProgressCallback, StopRequested


def _move_toward(route: tuple[int, ...], guide: tuple[int, ...], strength: float, rng: Random) -> tuple[int, ...]:
    """Apply a randomized subset of swaps that align a permutation with its guide."""
    result = list(route)
    target = max(0, min(len(route), round(strength * len(route))))
    used = 0
    for index in range(1, len(result)):
        if result[index] == guide[index]:
            continue
        if used >= target or rng.random() >= strength:
            continue
        other = result.index(guide[index])
        result[index], result[other] = result[other], result[index]
        used += 1
    return tuple(result)


def solve(problem: TSPProblem, config: EHOConfig, *,
          progress_callback: ProgressCallback | None = None,
          stop_requested: StopRequested | None = None) -> RunResult:
    """Optimize tours using clan-best attraction and random separation."""
    if not isinstance(config, EHOConfig):
        raise ValueError("EHO yêu cầu EHOConfig.")
    start, rng = perf_counter(), Random(config.seed)
    clans = [[random_permutation(problem.dimension, rng) for _ in range(config.elephants_per_clan)]
             for _ in range(config.clan_count)]
    costs = [[problem.route_length(route) for route in clan] for clan in clans]
    evaluations = config.population_size
    flat = [(costs[c][i], clans[c][i]) for c in range(len(clans)) for i in range(len(clans[c]))]
    best_distance, best_route = min(flat, key=lambda item: item[0])
    history: list[IterationStat] = []
    completed, partial = 0, False

    def record(iteration: int) -> None:
        vals = [v for row in costs for v in row]
        stat = IterationStat(iteration, min(vals), best_distance, fsum(vals)/len(vals), evaluations, perf_counter()-start, None)
        history.append(stat)
        if progress_callback:
            progress_callback(stat)

    def stop_reason() -> str | None:
        if stop_requested and stop_requested(): return "CANCELLED"
        if config.time_limit_seconds is not None and perf_counter()-start >= config.time_limit_seconds: return "TIME_LIMIT"
        if config.max_evaluations is not None and evaluations >= config.max_evaluations: return "MAX_EVALUATIONS"
        return None

    record(0)
    reason = "MAX_ITERATIONS"
    for iteration in range(1, min(config.iterations, config.max_iterations)+1):
        reason_now = stop_reason()
        if reason_now:
            reason = reason_now
            break
        new_clans, new_costs = [], []
        old_best = best_distance
        for ci, clan in enumerate(clans):
            clan_leader = clan[min(range(len(clan)), key=lambda i: costs[ci][i])]
            members, member_costs = [], []
            for ei, route in enumerate(clan):
                if stop_reason():
                    reason, partial = stop_reason() or "CANCELLED", True
                    break
                candidate = _move_toward(route, clan_leader, config.alpha, rng)
                candidate = _move_toward(candidate, best_route, config.beta, rng)
                value = problem.route_length(candidate)
                evaluations += 1
                if value < best_distance:
                    best_route, best_distance = candidate, value
                members.append(candidate); member_costs.append(value)
            if partial:
                break
            # Replace the worst clan member(s) with separated random elephants.
            for _ in range(config.separation_count_per_clan):
                worst = max(range(len(member_costs)), key=lambda i: member_costs[i])
                candidate = random_permutation(problem.dimension, rng)
                if stop_reason():
                    reason, partial = stop_reason() or "CANCELLED", True
                    break
                value = problem.route_length(candidate)
                evaluations += 1
                if value < best_distance:
                    best_route, best_distance = candidate, value
                members[worst], member_costs[worst] = candidate, value
            if partial:
                break
            new_clans.append(members); new_costs.append(member_costs)
        if partial:
            break
        clans, costs = new_clans, new_costs
        # Preserve the archive in the population for the next clan-best calculation.
        if config.preserve_global_best:
            wi = max(range(len(costs[0])), key=lambda i: costs[0][i])
            if best_distance < costs[0][wi]:
                costs[0][wi], clans[0][wi] = best_distance, best_route
        completed = iteration
        if iteration % config.record_history_every == 0:
            record(iteration)
    if history[-1].iteration != completed or history[-1].evaluations != evaluations:
        record(completed)
    validate_route(best_route, problem.dimension)
    return RunResult("eho", problem.name, best_route, best_distance, completed, evaluations,
        perf_counter()-start, config.seed, tuple(history), asdict(config), reason, True,
        {"partial_iteration": partial, "version": __version__, "dataset_sha256": problem.metadata.get("sha256"),
         "initialization_atomic": True, "population_diversity": None})
