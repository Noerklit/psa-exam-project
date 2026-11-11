import random
import toml_sut as tomllib   # resolves to YOUR local ./tomllib when run from the project root
from fuzzingbook.GreyboxFuzzer import Mutator, PowerSchedule, GreyboxFuzzer, GreyboxFuzzer_MutationGuided
from fuzzingbook.MutationFuzzer import FunctionCoverageRunner
from fuzzingbook.Coverage import population_coverage
from pathlib import Path # For reading seeds.

print("Using:", tomllib.__file__)   # must point into your project folder


def sut(inp: str):
    try:
        return tomllib.loads(inp)
    except tomllib.TOMLDecodeError:   # invalid TOML is expected, not a bug
        return None

def load_seeds(directory: str) -> list[str]:
    seeds = []
    for path in sorted(Path(directory).iterdir()):
        if path.is_file():
            # newline="" keeps \r\n exactly as written in the file
            with open(path, "r", encoding="utf-8", newline="") as f:
                seeds.append(f.read())
    return seeds

SEEDS = load_seeds("fuzzing_seeds/TOML/")


if __name__ == "__main__":
    random.seed(1)
    print("Number of SEEDS: ", len(SEEDS))
    
    fuzzer = GreyboxFuzzer(SEEDS, Mutator(), PowerSchedule())
    runner = FunctionCoverageRunner(sut)
    outcomes = fuzzer.runs(runner, trials=5000)

    _, cov = population_coverage(fuzzer.inputs, sut)
    crashes = [(i, o) for i, (_, o) in zip(fuzzer.inputs, outcomes) if o == "FAIL"]

    print("max coverage      :", max(cov))
    print("population size   :", len(fuzzer.population))
    print("unexpected crashes:", len(crashes))
    for i, _ in crashes[:5]:
        print("  ", repr(i))

    print("-----------------------")
    print("Total generated inputs:", len(fuzzer.inputs))
    print("Population size:", len(fuzzer.population))
    print("Number of outcomes:", len(outcomes))

    print("---------------")
    print("This is just a random sample of some of the inputs and the outcomes of these")
    for i, (inp, outcome) in enumerate(zip(fuzzer.inputs, outcomes)):
        if i % 300 == 0:
            print(f"\n--- Test case {i} ---")
            print("Input:", repr(inp))
            print("Outcome:", outcome)

    #---------------------------------------------------------------------------------------------
    # Mutation guided fuzzer

    fuzzer_2 = GreyboxFuzzer_MutationGuided(SEEDS, Mutator(), PowerSchedule())
    runner_2 = FunctionCoverageRunner() # Here we should then, as argument, have the new SUT, that is the file of mutated functions.
                                        # This new SUT function should maybe get an argument get what the "correct" answer should be, 
                                        # and then run through some/all of the mutation functions, and log the amount of mutants killed 
                                        # by this input, i.e. the amount of answers that differ from the argument.
                                        #   When the amount of mutants killed by the input is returned to GreyboxFuzzer_MutationGuided, it should
                                        # then prioritise it appropiatly, i.e. if it kills many mutants, it should be prioritised higher, in the population.

    outcomes = fuzzer.runs(runner, trials=5000) # Maybe we should tone it down to around 6-700 instead, if it takes to long time to run