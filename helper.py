"""Small helper module imported by ``generate_files.py``.

Importing this module is what causes Python to create a bytecode cache file
under ``__pycache__/`` (for example ``__pycache__/helper.cpython-313.pyc``).
That cache file is a generated artifact and must be ignored by ``.gitignore``.
"""

VERSION = "1.0"


def banner() -> str:
    return f"generate_files helper v{VERSION}"
