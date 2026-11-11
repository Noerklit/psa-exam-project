import random
import toml_sut as tomllib   # resolves to YOUR local ./tomllib when run from the project root
from fuzzingbook.GreyboxFuzzer import Mutator, PowerSchedule, GreyboxFuzzer
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
    print("Length of SEEDS: ", len(SEEDS))
    
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