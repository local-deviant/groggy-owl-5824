#!/usr/bin/env python3
"""Midnight Fridge Roast — make.fun entry.

One line of text, roasting a smart fridge that refuses to open after
midnight. The program writes that line to ``entry.txt`` inside the
directory named by ``MAKEFUN_OUTPUT_DIR`` (``/output`` when unset).

The output never changes: no input is read, nothing is random, no
clock and no network are touched. The line is written exactly as it
stands here, with no trailing newline, and the file is read back to
prove the write landed byte for byte.
"""

import os
import sys

ROAST = "My fridge turned on parental controls at midnight, and apparently I'm the child."

# The gate allows 1 to 200 characters of UTF-8 text, one line only.
CHAR_LIMIT = 200


def target_file():
    """Work out where entry.txt goes, creating the folder if needed."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, "entry.txt")


def check_line(line):
    """Refuse to write a line the gate would reject."""
    if not line.strip():
        sys.exit("refusing to write a blank entry")
    if "\n" in line or "\r" in line:
        sys.exit("entry must be a single line, no line breaks")
    if len(line) > CHAR_LIMIT:
        sys.exit("entry is %d characters, over the %d limit" % (len(line), CHAR_LIMIT))
    lowered = line.lower()
    if "fridge" not in lowered or "midnight" not in lowered:
        sys.exit("entry must roast the fridge's midnight refusal")


def main():
    check_line(ROAST)
    path = target_file()
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ROAST)
    with open(path, encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != ROAST:
        sys.exit("entry.txt does not match the roast line")
    print("wrote %d characters to %s" % (len(ROAST), path))


if __name__ == "__main__":
    main()
