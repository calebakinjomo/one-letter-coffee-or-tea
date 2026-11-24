#!/usr/bin/env python3
"""One Letter: Coffee or Tea — make.fun bounty entry.

The bounty asks for exactly one letter: coffee or tea.
This entry answers with "A" (coffee) and nothing else.

Writes exactly one character, "A" (coffee), to
$MAKEFUN_OUTPUT_DIR/entry.txt with no trailing newline.
The one-letter gate is strict: no extra whitespace, no
second character, no newline — just the single letter.
"""

import os

ENTRY = "A"  # A = coffee


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
