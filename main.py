"""Make the AI Judge Laugh — entry program (stdlib only, deterministic).

Writes a single one-line office joke to /output/entry.txt.
No randomness, no network, no timestamps, no file reads: the text is a
constant, so every run produces byte-identical output.
"""

import os
from pathlib import Path

ENTRY = (
    "I automated my timesheet so I could leave at 5 \u2014 "
    "it now takes 6 hours a week to maintain the automation."
)


def main() -> None:
    # Self-check the competition gate before writing: 1-200 chars,
    # not only whitespace, exactly one line.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert "\n" not in text, "entry must be a single line"
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
