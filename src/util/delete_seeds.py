import shutil
from pathlib import Path

SEEDS_DIR = Path("fuzzing_seeds")


def main() -> None:
    if not SEEDS_DIR.exists():
        print(f"{SEEDS_DIR} does not exist, nothing to do.")
        return

    removed = 0
    for item in SEEDS_DIR.iterdir():
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()
        removed += 1

    print(f"Removed {removed} item(s) from {SEEDS_DIR}/")


if __name__ == "__main__":
    main()