import random
import tomllib   # resolves to YOUR local ./tomllib when run from the project root
from fuzzingbook.GreyboxFuzzer import Mutator, PowerSchedule, GreyboxFuzzer
from fuzzingbook.MutationFuzzer import FunctionCoverageRunner
from fuzzingbook.Coverage import population_coverage

print("Using:", tomllib.__file__)   # must point into your project folder


def sut(inp: str):
    try:
        return tomllib.loads(inp)
    except tomllib.TOMLDecodeError:   # invalid TOML is expected, not a bug
        return None


SEEDS = [
    'title = "x"\nn = 42\n',
    '[server]\nhost = "localhost"\nports = [8000, 8001]\n',
    'a.b.c = 1.5\nd = { e = true, f = "g" }\n[[items]]\nname = "z"\n',
    'when = 1979-05-27T07:32:00Z\ns = """multi\nline"""\n',
]

if __name__ == "__main__":
    random.seed(1)
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