import random
import toml_sut as tomllib   # resolves to YOUR local ./tomllib when run from the project root
from fuzzingbook.Coverage import population_coverage
from pathlib import Path # For reading seeds.
from fuzzingbook.Grammars import is_valid_grammar
from fuzzingbook.GrammarFuzzer import GrammarFuzzer
from toml_grammar import TOML_GRAMMAR

OUT_DIR = Path("gen_fuzzing_seeds/TOML")
N_SEEDS = 50
ONLY_VALID = True

assert is_valid_grammar(TOML_GRAMMAR, start_symbol="<start>")
print("Grammar is valid")

random.seed(1)
fuzzer = GrammarFuzzer(TOML_GRAMMAR, min_nonterminals=5, max_nonterminals=40)

seeds, tried, rejected = set(), 0, 0

while len(seeds) < N_SEEDS and tried < 5000:
  tried += 1
  s = fuzzer.fuzz()
  if ONLY_VALID:
    try:
      tomllib.loads(s)
    except tomllib.TOMLDecodeError:
      rejected += 1
      continue
  seeds.add(s)
  
print(f"Forsøgt: {tried}, afvist af parser: {rejected}, gemt: {len(seeds)}")

# 3) Skriv til filer
OUT_DIR.mkdir(parents=True, exist_ok=True)
for i, s in enumerate(sorted(seeds)):
    # newline="" så \n ikke omskrives (samme som i din load_seeds)
    with open(OUT_DIR / f"seed_{i:03d}.toml", "w", encoding="utf-8", newline="") as f:
      f.write(s)