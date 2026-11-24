#!/usr/bin/env python3
"""Two Lines to Your Past Self — a make.fun program/v1 entry.

Writes the entry text to /output/entry.txt: exactly two lines.
Line one warns the writer's past self about one specific moment;
line two says in one sentence why that moment mattered and what
changed because of it. Python standard library only, deterministic,
no network, and it writes nowhere but /output/entry.txt.
"""

from pathlib import Path

ENTRY_TEXT = (
    "On your last night in the apartment on Jalan Kenanga, when she asks if you two are all right, "
    "do not say 'we'll talk tomorrow' and close the door.\n"
    "Her flight left at dawn, and you spent the next three years finishing that conversation out loud to an empty kitchen."
)

OUTPUT_PATH = Path("/output/entry.txt")

# The competition gate accepts entry text of 1 to 280 characters.
MAX_ENTRY_CHARS = 280


def main() -> None:
    if not 1 <= len(ENTRY_TEXT) <= MAX_ENTRY_CHARS:
        raise ValueError(f"entry text is {len(ENTRY_TEXT)} characters, outside 1-{MAX_ENTRY_CHARS}")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
