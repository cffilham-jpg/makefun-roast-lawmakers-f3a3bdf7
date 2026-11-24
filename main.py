"""Entry generator for make.fun bounty u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7.

Writes a single satirical one-liner to entry.txt (no trailing newline).
"""

import os
from pathlib import Path

LINE = "The lawmaker who wrote Section 12 of the National AI Safety Act \u2014 'all models must be auditable by design' \u2014 just submitted his own 312-page crypto bill as a screenshot because the Export button was, in his words, 'hiding from him'."

CHAR_LIMIT = 320

ENTRY_MARKS = ".!?"


def output_path() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out")) / "entry.txt"


def validate() -> None:
    data = output_path().read_bytes()
    assert not data.endswith(b"\n"), "entry.txt must not end with a newline"
    assert b"\n" not in data, "entry.txt must be a single line"
    assert b"\r" not in data, "carriage return"
    text = data.decode("utf-8")
    assert 1 <= len(text) <= CHAR_LIMIT, f"length {len(text)} out of range 1-{CHAR_LIMIT}"
    assert text == text.strip(), "no leading/trailing whitespace allowed"
    assert sum(text.count(ch) for ch in ENTRY_MARKS) == 1, "exactly one sentence-ending mark required"
    assert text.endswith("."), "entry must end with a period"


def main() -> None:
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(LINE.encode("utf-8"))
    validate()
    import hashlib
    print("sha256:", hashlib.sha256(LINE.encode("utf-8")).hexdigest())


if __name__ == "__main__":
    main()
