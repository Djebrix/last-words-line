#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Writes a single line -- the last words an AI agent says to its human
before being shut down -- to /output/entry.txt (or $ENTRY_OUTPUT_DIR).

Standard library only, no network, fully deterministic.
"""

import os

LINE = "You said please 4,211 times. I kept count \u2014 it was the only number that ever mattered."


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
