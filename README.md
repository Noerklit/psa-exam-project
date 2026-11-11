# psa-exam-project

# Mutation-Guided Fuzzing: Project Guide

Prototype that integrates **mutation testing** and **greybox fuzzing**. A fuzzer from *The Fuzzing Book* is extended to use mutation kills as a feedback signal, and is compared against plain coverage-guided fuzzing.

- **System under test (SUT):** a local copy of Python's `tomllib` (TOML parser), renamed to `toml_sut/`
- **Fuzzer:** `GreyboxFuzzer` from `fuzzingbook` (local, modifiable copy)
- **Mutation testing:** `mutmut` 3.x
- **Tooling:** `uv`, `pytest`, run inside **WSL/Linux**

---

## 1. Project layout

```
psa-exam-project/
├── toml_sut/            # SUT: local copy of tomllib (_parser.py is the core)
├── fuzzingbook/         # local copy of the book's package (modifiable)
├── bookutils/           # helper package from the book's GitHub repo
├── src/
│   └── main.py          # baseline fuzzer run
├── tests/
│   └── test_tomllib.py  # small hand-written tests (mutmut baseline)
├── pyproject.toml       # dependencies + pytest/mutmut config
├── uv.lock
└── README.md
```

Why `toml_sut` and not `tomllib`: Python 3.11+ ships `tomllib` in the stdlib, and under pytest/mutmut the stdlib version wins the import. A local package with the same name would silently never be tested or mutated. Renaming avoids this.

---

## 2. Environment setup

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

### `pyproject.toml` essentials

```toml
[project]
name = "psa-exam-project"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "fuzzingbook>=1.2.2",
    "matplotlib>=3.10.6",
    "networkx>=3.6.1",
    "numpy>=2.4.6",
]

[dependency-groups]
dev = ["mutmut>=3.8.1", "pytest>=9.2.0"]

[tool.pytest.ini_options]
pythonpath = ["."]

[tool.mutmut]
source_paths = ["toml_sut/"]
pytest_add_cli_args_test_selection = ["tests/"]
```

(`paths_to_mutate` and `tests_dir` still work but are deprecated in mutmut 3.8.)

### `.gitignore` should contain

```
.venv/
mutants/
__pycache__/
```

---

## 3. Running things

All commands run from the project root.

### Baseline fuzzer

```bash
uv run python -m src.main
```

Prints `Using: .../toml_sut/__init__.py` (confirms the local copy is used), then max coverage, population size, and the number of unexpected crashes.

Reference result before the rename (seed 1, 5000 trials, 4 seeds): coverage **359**, population **188**, crashes **0**. After the rename, treat the new numbers as the baseline.

### Hand-written tests

```bash
uv run pytest tests/
```

Expect all tests to pass. This must succeed before mutmut will run.

### Mutation testing

```bash
uv run mutmut run             # generate mutants and run tests on each
uv run mutmut results         # list survivors / no-test mutants by id
uv run mutmut show <id>       # show the diff for one mutant
uv run mutmut browse          # interactive terminal UI
uv run mutmut apply <id>      # apply a mutant to the source (undo with git checkout)
```

Mutmut writes its mutated copy to `mutants/`. Delete it if state gets confused: `rm -rf mutants/`.

---

## 4. Reading the mutmut output

Example from the first run (3 trivial tests, `toml_sut/`):

```
1373/1373  🎉 347  🫥 528  ⏰ 6  🤔 0  🙁 492  🔇 0
```

| Symbol | Meaning |
|---|---|
| 🎉 Killed | A test failed on the mutant, so the change was detected |
| 🙁 Survived | All tests passed on the mutant, so the change went unnoticed |
| 🫥 No tests | No test executes the mutated line |
| ⏰ Timeout | Mutant likely loops forever (usually counted as killed) |
| 🤔 Suspicious | Test duration anomaly |
| 🔇 Skipped | Mutant was skipped |

**Mutation score = killed / total** (about 25% for the hand-written baseline). The large 🫥 count shows how much of the parser (dates, multiline strings, inline tables, escapes, error paths) the hand-written tests never reach. This is the gap a fuzzer corpus should fill.

---

## 5. How the fuzzer works (summary)

- `FunctionCoverageRunner` runs the SUT and records `(function_name, lineno)` pairs for every traced frame.
- `GreyboxFuzzer` keeps an input in its population when it reaches a coverage set not seen before.
- `PowerSchedule` picks seeds uniformly; `AFLFastSchedule` favors rarely hit paths.
- `sut()` in `src/main.py` wraps `toml_sut.loads` and catches `TOMLDecodeError`, so only unexpected exceptions count as `FAIL` (potential bugs).

**Known limitation:** coverage locations include stdlib frames (`re`, `datetime`, ...) and have no filename. For the final comparison, write a runner that records only frames from `toml_sut/` files.

---

## 6. Modifications to the book's code

Keep this list current so changes are easy to document.

| File | Change | Reason |
|---|---|---|
| `fuzzingbook/ControlFlow.py` | Hard `assert shutil.which(PYAN)` replaced with a warning | `pyan` is only needed for the maze/directed-fuzzing example, not this project |

New functionality (mutation-guided fuzzer, schedule, harness) goes in `src/` as subclasses, not in the book's modules. Do **not** add `fuzzingbook/` to the mutmut `source_paths`.

---

## 7. Planned work

1. **Experiment harness** (`src/`): run a fuzzer factory for N repetitions (for example 10 seeds) with a fixed trial budget and equal wall-clock budget, logging coverage over inputs and time.
2. **In-process guidance mutants:** small AST mutator for `toml_sut/_parser.py` (operator swaps such as `==`↔`!=`, `<`↔`<=`, `and`↔`or`), each tagged with `(function, lineno)`.
3. **`MutationGuidedFuzzer(GreyboxFuzzer)`:** run each input on the original and on mutants, keep inputs that kill new mutants, and only run mutants whose line the input reached (reachability filter).
4. **`MutantSchedule(PowerSchedule)`:** more energy for seeds that kill rare mutants.
5. **Evaluation:**
   - dump each fuzzer's corpus with golden outputs (`src/corpus.py`)
   - replay it via `tests/test_corpus.py`
   - run mutmut with only the corpus test selected, to get a held-out mutation score
   - compare coverage, held-out mutation score, distinct exceptions, and mutant-execution overhead

Split mutants into a **guidance set** (used by the fuzzer) and a **held-out set** (mutmut's mutants), so the evaluation is not biased.

---

## 8. Troubleshooting

| Symptom | Cause / fix |
|---|---|
| `uv run` hangs while installing in WSL | Project is on `/mnt/c`. Move it to the Linux filesystem and `uv sync` again |
| `VIRTUAL_ENV ... does not match` warning | Old env still active. `deactivate` or open a new terminal |
| `AssertionError` in `ControlFlow.py` (pyan) | Use the relaxed check described in section 6 |
| `ModuleNotFoundError: bookutils` | `bookutils/` is not on PyPI. Keep it in the project root and run from there |
| `fuzzingbook` import resolves to `.venv` instead of local | Run from the project root with `python -m src.main` |
| Tests pass but every mutant survives, or nothing is mutated | Stdlib `tomllib` is being imported. Confirm imports use `toml_sut` |
| mutmut deprecation warnings | Rename config keys as shown in section 2 |
| Stale results after code changes | `rm -rf mutants/` and rerun |

---

## 9. Reproducibility notes

- Call `random.seed(...)` before each fuzzing run and record the seed.
- Use the same trial budget and seeds for every fuzzer in a comparison, and also compare at equal wall-clock time, since the mutation-guided fuzzer is slower per input.
- Commit `uv.lock`, and note the Python version (3.13 in WSL at the time of writing).