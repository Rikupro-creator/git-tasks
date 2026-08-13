"""Generate files that should be kept out of the Git repository.

This script is the "generator" for the assignment. When you run it, it:

  1. Imports a local helper module (``helper.py``). Importing a module makes
     Python write a bytecode cache file under ``__pycache__/``, e.g.
     ``__pycache__/helper.cpython-313.pyc``.
  2. Creates a ``generated/`` folder and writes timestamped report files
     (``report_*.txt``) plus a log file (``generated/logs/run_*.log``).

All of these artifacts — the ``generated/`` folder, ``__pycache__/`` and
``*.pyc`` — are exactly the kind of files that should be ignored by
``.gitignore``: they can be recreated at any time and do not belong in
version control.
"""
import os
import random
from datetime import datetime

import helper


OUT_DIR = "generated"
LOG_DIR = os.path.join(OUT_DIR, "logs")


def timestamp() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def write_text_file(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def generate_files(count: int = 3) -> list[str]:
    """Create ``count`` report files plus one log file under ``generated/``."""
    os.makedirs(LOG_DIR, exist_ok=True)

    created: list[str] = []
    stamp = timestamp()

    for i in range(1, count + 1):
        path = os.path.join(OUT_DIR, f"report_{stamp}_{i}.txt")
        write_text_file(
            path,
            f"Report #{i}\nGenerated at: {stamp}\nRandom value: {random.randint(1000, 9999)}\n",
        )
        created.append(path)

    log_path = os.path.join(LOG_DIR, f"run_{stamp}.log")
    write_text_file(
        log_path,
        f"{helper.banner()}\nFiles created:\n" + "\n".join(created) + "\n",
    )
    created.append(log_path)

    return created


def main() -> None:
    print(helper.banner())
    for path in generate_files():
        print(f"created {path}")
    print("Done. These files should be ignored by .gitignore.")


if __name__ == "__main__":
    main()
