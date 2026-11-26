from src.mutant_key_loader import load_mutant_keys
from pathlib import Path # For reading seeds and getting the fuzzed file
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MUTANTS_DIR = PROJECT_ROOT / "mutants"

# One file:
keys1 = load_mutant_keys(MUTANTS_DIR / "toml_sut" / "_parser.py.meta")

# Or the whole mutants folder (works for any mutmut project, many files):
keys2 = load_mutant_keys("mutants/toml_sut")


print(f"The amount of keys in '_parser.py.meta' is {len(keys1)}, and for the whole directory of mutants it is {len(keys2)}.")

#for key in keys1:
#    print()   # use this as the value of your environment variable

print("-----------------------------------------------------------------------------------------")

for key in keys2:
    if key == "":
        print("OOOPS be aware of this!") 
    #print(key)   # use this as the value of your environment variable