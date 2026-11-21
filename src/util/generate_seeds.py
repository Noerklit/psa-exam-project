import os
import random
from typing import Any
import toml_sut as tomllib   # resolves to YOUR local ./tomllib when run from the project root
from pathlib import Path # For reading seeds.
from fuzzingbook.Grammars import is_valid_grammar
from fuzzingbook.GrammarFuzzer import GrammarFuzzer
from toml_grammar import TOML_GRAMMAR

def gen_initial_seeds(out_dir: str, num_seeds: int, grammar: dict[str, Any] | None, min_nonterminals: int, max_nonterminals: int):
  """Generates initial seeds based on a grammar
    
    Function takes an output directory, the desired number of seeds, a grammar, min and max nonterminals which
    sets boundaries for the minimum and maximum amount of characters the fuzzer produces before generating a terminal character
    
    Does not return anything but writes the seeds to files in the given output directory
  """
  # Fallback grammar for now
  if grammar is None:
    grammar = TOML_GRAMMAR
    
  output_dir = Path(out_dir)
  print(out_dir)
  
  assert is_valid_grammar(grammar=grammar, start_symbol="<start>")
  print("Grammar is valid")
  
  if len(os.listdir(output_dir)) >= num_seeds:
    print(
        "There already exists the desired amount of seeds or more, program will now terminate. If you wish to generate new "
        f"seeds, please remove current seeds from the {out_dir}"
        )
    return
  
  random.seed(1)
    
  fuzzer = GrammarFuzzer(grammar=grammar, min_nonterminals=min_nonterminals, max_nonterminals=max_nonterminals)
  
  # Seeds is a set to ensure we don't generate duplicate seeds
  seeds, tried = set(), 0
  while len(seeds) < num_seeds and tried < 5000:
    tried += 1
    string = fuzzer.fuzz()
    # I am unsure of if we want an extra check here for the string generated, in terms of whether it is actually
    # valid as input. But I would assume we just want to generate it based on the grammar and that is enough
    seeds.add(string)
  
  print(f"Generated {len(seeds)} seeds")
  
  output_dir.mkdir(parents=True, exist_ok=True)
  for i, s in enumerate(seeds):
    with open(output_dir / f"seed_{i:03d}.toml", "w", encoding="utf-8", newline="") as f:
      f.write(s)
  print(f"Seeds written to files in: {out_dir}")
  
def main():
  gen_initial_seeds(out_dir="fuzzing_seeds", num_seeds=50, grammar=None, min_nonterminals=5, max_nonterminals=40)

if __name__ == "__main__":
  main()