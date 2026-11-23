# Contributing

Thank you for contributing to GA-EHO-TSP. Contributions should be focused, reproducible, and consistent with the current project scope.

## Before You Start

Read [README.md](README.md), [GUIDELINES.md](GUIDELINES.md), and the [architecture documentation](docs/architecture.md). Use Python 3.11 or newer. Create a virtual environment and install the project dependencies from the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Project Scope and Ownership

- Trương Thành Đạt is the owner of the GA implementation and shared domain contract.
- EHO is planned as a separate solver. It must use the shared problem, result, random-number, progress, and stopping interfaces.
- Discuss proposed changes to `src/ga_eho_tsp/domain/`, shared interfaces, or the frozen project specification with the project lead before changing the contract.
- Preserve the seven benchmark matrices in `data/`. Do not modify input data to improve reported results.

## Development Practices

- Keep each change focused and explain its purpose.
- Preserve deterministic behavior when a seed is supplied.
- Add or update tests for behavior changes where a test suite is available.
- Report the commands actually run and their results. Do not claim checks passed if they were not executed.
- For experiments, record datasets, parameters, seeds, evaluation budgets, and limitations. Keep negative and unsuccessful results visible.
- Do not commit credentials, private reports, virtual environments, caches, or generated output files.

## Pull Requests

Describe the problem, the implementation, validation performed, and any known limitations. Include reproducible commands or configuration for changes that affect algorithms, data handling, or experiments. Follow the [Code of Conduct](CODE_OF_CONDUCT.md).

For security concerns, follow the private reporting process in [SECURITY.md](SECURITY.md).
