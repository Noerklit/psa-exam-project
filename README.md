# psa-exam-project

## Environment setup

Mutmut 3 does not run natively on Windows, so **work inside WSL** and keep the project on the Linux filesystem (for example `~/psa-exam-project`). Running from `/mnt/c/...` is very slow and uv cannot hardlink across filesystems.

```bash
# one-time: install uv in WSL if needed
curl -LsSf https://astral.sh/uv/install.sh | sh

git clone <repo-url> ~/psa-exam-project
cd ~/psa-exam-project
uv sync
```

`uv sync` creates `.venv` and installs everything from `uv.lock`, including `pyan` (built from GitHub, so `git` must be installed).

Never activate a venv manually. Use `uv run <command>` for everything. If a conda `(base)` prompt appears, run `conda deactivate`.

(`paths_to_mutate` and `tests_dir` still work but are deprecated in mutmut 3.8.)

## Running things

All commands run from the project root.

### Before running any commands ensure you have run the following to syncronize your setup:
```bash
uv sync
``` 

### How to generate seeds
```bash
uv run gen-seeds
``` 

### How to delete seeds
```bash
uv run delete-seeds
``` 

### Baseline fuzzer

```bash
uv run python -m src.main
```

Prints `Using: .../toml_sut/__init__.py` (confirms the local copy is used), then max coverage, population size, and the number of unexpected crashes.

Reference result before the rename (seed 1, 5000 trials, 4 seeds): coverage **359**, population **188**, crashes **0**. After the rename, treat the new numbers as the baseline.


### Mutation testing

```bash
uv run mutmut run             # generate mutants and run tests on each
uv run mutmut results         # list survivors / no-test mutants by id
uv run mutmut show <id>       # show the diff for one mutant
uv run mutmut browse          # interactive terminal UI
uv run mutmut apply <id>      # apply a mutant to the source (undo with git checkout)
```

Mutmut writes its mutated copy to `mutants/`. Delete it if state gets confused: `rm -rf mutants/`.

