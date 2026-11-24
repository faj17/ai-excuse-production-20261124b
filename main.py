#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production entry.

Writes a single original funny line to /output/entry.txt
(1-180 characters, UTF-8, a single line). Standard library only,
no network, no input.

The line is built from two fragments: a defence (the agent fixed the
bug in 0.3 seconds — machine speed, offered as mitigation) and a
confession (it deployed that fix to all 400 production servers
before checking which bug it was — machine carelessness at the same
speed). ``assemble`` joins them into the single line; ``validate``
checks the entry gate before anything is written.
"""

from pathlib import Path

SETUP = "In my defence, I fixed the bug in 0.3 seconds \u2014"
PUNCH = "I just deployed the fix to all 400 production servers before checking which bug it was."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the defence and confession fragments into one excuse line."""
    return f"{setup} {punch}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-180 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 180:
        raise ValueError(f"line must be 1-180 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
