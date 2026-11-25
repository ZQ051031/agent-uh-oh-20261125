#!/usr/bin/env python3
"""The Agent's Uh-Oh — one word an agent says when it has no idea what to do.

The entry is exactly one word, written to /output/entry.txt with no
trailing newline and nothing attached, so the file holds only the word.

Why this word: when an agent is completely lost mid-task, it does what
a sat-nav does when it misses a turn — it stalls, announces it is
recalculating, and buys time while figuring out where it went wrong.
"""

import os

ENTRY = "recalculating"


def main() -> None:
    # Gate: UTF-8 text of 1 to 99 characters, not only white space.
    assert 1 <= len(ENTRY) <= 99, "entry must be 1-99 characters"
    assert ENTRY.strip(), "entry must not be only white space"
    assert ENTRY == ENTRY.strip(), "entry must be a single word, nothing attached"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
