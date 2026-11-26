import json
from pathlib import Path

import random


def load_mutant_keys(path):
    """
    Return a list of mutant names (strings) found in mutmut .meta file(s), that can be used for setting specific mutants later on.

    path can be:
        * a single .meta file
        * a folder (searched recursively for *.meta files)
    """
    path = Path(path)

    if path.is_file():
        meta_files = [path]
    elif path.is_dir():
        meta_files = sorted(path.rglob("*.meta"))
    else:
        raise FileNotFoundError(f"Path does not exist: {path}")

    keys = []
    for meta_file in meta_files:
        with open(meta_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        if "exit_code_by_key" not in data:
            raise KeyError(
                f"'exit_code_by_key' not found in {meta_file}. "
                f"Fields present: {list(data.keys())}"
            )
        keys.extend(data.get("exit_code_by_key", {}).keys())

    return keys


def split_mutants(mutant_names, train_ratio=0.8, seed=None):
    """
    Returns two lists of mutants: train_mutants, test_mutants  where train is train_ratio is the percentage of mutants that is in the train split.
    The mutants are also shuffled, so the train test split is random(unless seed is set.)

    input should be:
        * mutn
    """
    mutant_names = list(mutant_names)  # copy, so the original list is not changed
    rng = random.Random(mutant_names)
    rng.shuffle(mutant_names)

    cut = int(len(mutant_names) * train_ratio)
    train_keys = mutant_names[:cut]
    test_keys = mutant_names[cut:]
    return train_keys, test_keys