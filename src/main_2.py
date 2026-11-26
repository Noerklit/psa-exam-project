import random
import sys
from pathlib import Path # For reading seeds and getting the fuzzed file

    # This is for locating the fuzzed file
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "mutants"))     # must come BEFORE the import below
MUTANTS_DIR = PROJECT_ROOT / "mutants"

import toml_sut as tomllib   # resolves to YOUR local ./tomllib when run from the project root

# Check if the correct Mutmut directory is located!
if "mutants" not in str(tomllib.__file__):
    raise SystemExit("The imported parser is not the mutmut copy: " + str(tomllib.__file__))

# Fuzzingbook imports
from fuzzingbook.GreyboxFuzzer import Mutator, PowerSchedule, GreyboxFuzzer, GreyboxFuzzer_MutationGuided, MutantSchedule
from fuzzingbook.MutationFuzzer import FunctionCoverageRunner, MutationGuidedRunner
from fuzzingbook.Coverage import population_coverage


import signal ## For Timeouts during Mutant running

import os

#Import the file for loading the mutant names:
from src.mutant_key_loader import load_mutant_keys


def sut(inp: str):
    try:
        return tomllib.loads(inp)
    except tomllib.TOMLDecodeError:   # invalid TOML is expected, not a bug
        return None



TIME_LIMIT = 0.5            # seconds per parser call. Any longer, and the mutant counts as TIMEOUT

class _Timeout(Exception):
    """Raised when a parser call exceeds TIME_LIMIT."""

def _timeout_handler(signum, frame):
    raise _Timeout()

signal.signal(signal.SIGALRM, _timeout_handler)


def behaviour(mutant_name, inp: str):
    """Runs tomllib.loads(inp) with the given mutant switched on (None = original program).
    Returns a tuple that has the status and output"""
    if mutant_name is None:
        os.environ.pop("MUTANT_UNDER_TEST", None)
    else:
        os.environ["MUTANT_UNDER_TEST"] = mutant_name

    signal.setitimer(signal.ITIMER_REAL, TIME_LIMIT)
    try:
        return ("OK", repr(tomllib.loads(inp))) 
    except tomllib.TOMLDecodeError as e:
        return ("INVALID", str(e))  # Error message includes line and column, to detect mutants in error messages
    except _Timeout:
        return ("TIMEOUT",)
    except Exception as e:
        return ("CRASH", type(e).__name__, str(e))
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        os.environ.pop("MUTANT_UNDER_TEST", None)


def load_seeds(directory: str) -> list[str]:
    seeds = []
    for path in sorted(Path(directory).iterdir()):
        if path.is_file():
            # newline="" keeps \r\n exactly as written in the file
            with open(path, "r", encoding="utf-8", newline="") as f:
                seeds.append(f.read())
    return seeds

SEEDS = load_seeds("fuzzing_seeds/")


def testMutation():
    """FOR TESTING OF MUTATIONS!"""
    print("Using        :", tomllib.__file__)
    test_input = "a = [1, 2]"
    print("original      :", behaviour(None, test_input))
    print("mutant 31    :", behaviour("toml_sut._parser.x_parse_array__mutmut_31", test_input))
    print("runner result:", MutationGuidedRunner(behaviour, names).run(test_input))


if __name__ == "__main__":
    random.seed(1)
    print("Number of SEEDS: ", len(SEEDS))
    
    fuzzer = GreyboxFuzzer(SEEDS, Mutator(), PowerSchedule())
    runner = FunctionCoverageRunner(sut)
    outcomes = fuzzer.runs(runner, trials=5000)

    _, cov = population_coverage(fuzzer.inputs, sut)
    crashes = [(i, o) for i, (_, o) in zip(fuzzer.inputs, outcomes) if o == "FAIL"]

    print("max coverage    :", max(cov))
    print("population size   :", len(fuzzer.population))
    print("unexpected crashes:", len(crashes))
    for i, _ in crashes[:5]:
        print("  ", repr(i))

    print("-----------------------")
    print("Total generated inputs:", len(fuzzer.inputs))
    print("Population size:", len(fuzzer.population))
    print("Number of outcomes:", len(outcomes))
    count = 0
    for result, status in outcomes:
        if result is not None:
            count += 1
    print("Number of not None outcomes: ", count)

    print("---------------")
    print("This is just a random sample of some of the inputs and the outcomes of these")
    for i, (inp, outcome) in enumerate(zip(fuzzer.inputs, outcomes)):
        if i % 300 == 0:
            print(f"\n--- Test case {i} ---")
            print("Input:", repr(inp))
            print("Outcome:", outcome)

    #---------------------------------------------------------------------------------------------
    # Mutation guided fuzzer

    names = load_mutant_keys(MUTANTS_DIR / "toml_sut" / "_parser.py.meta")
    # Manual names, used for testing
    #names = ["toml_sut._parser.x_loads__mutmut_90", "toml_sut._parser.x_loads__mutmut_106", "toml_sut._parser.x_loads__mutmut_40", "toml_sut._parser.x\u01c1NestedDict\u01c1append_nest_to_list__mutmut_8", "toml_sut._parser.x_skip_comments_and_array_ws__mutmut_10", "toml_sut._parser.x_key_value_rule__mutmut_6", "toml_sut._parser.x_parse_key_value_pair__mutmut_20", "toml_sut._parser.x_parse_key_value_pair__mutmut_30"]

    if len(names) == 0:
        raise SystemExit("No mutants found. Run 'uv run mutmut run' once for generating the mutant file")
    print("\n=======================")
    print("Number of mutants used:", len(names))

    random.seed(1)
    # testMutation()

    fuzzer_2 = GreyboxFuzzer_MutationGuided(SEEDS, Mutator(), MutantSchedule())
    runner_2 = MutationGuidedRunner(behaviour, names)
    outcomes_2 = fuzzer_2.runs(runner_2, trials=50)

    print("Total generated inputs :", len(fuzzer_2.inputs))
    print("Population size  :", len(fuzzer_2.population))
    print("Mutants killed   :", len(fuzzer_2.killed_so_far), " out of ", len(names))
    print("Mutants NOT killed :", len(names) - len(fuzzer_2.killed_so_far))


    SURVIVORS_PRINTED = 10
    for name in sorted(set(names) - fuzzer_2.killed_so_far)[:SURVIVORS_PRINTED]:
        print("   survived:", name)
    if (len(names) - len(fuzzer_2.killed_so_far)) > SURVIVORS_PRINTED:
        print("   ...")


    # printing some examples of the seeds
    for i, (inp, outcome) in enumerate(zip(fuzzer_2.inputs, outcomes_2)):
            if i % 300 == 0:
                print(f"\n--- Test case {i} ---")
                print("Input:", repr(inp))
                print("Outcome:", outcome)
            if i  == 1 or i  == 2 or i  == 3 or i  == 4:
                print(f"\n--- Test case {i} ---")
                print("Input:", repr(inp))
                print("Outcome:", outcome)

    print("POPULATION REMAINING")
    print("----------------------------------------------------------")
    for i, ele in enumerate(fuzzer_2.population):
        print(f"population number {i}, is: {ele}")
    