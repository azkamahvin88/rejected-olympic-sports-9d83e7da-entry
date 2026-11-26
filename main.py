#!/usr/bin/env python3
"""Rejected Olympic Sports -- one deterministic one-line joke.

Writes a single one-line invented Olympic sport (101 characters, one line)
to /output/entry.txt. Python standard library only, no network, no
randomness, no input files: every run writes byte-identical output.
"""

import os
import sys

JOKE = "Competitive Procrastination: athletes have four years to train; nobody starts until the night before."


def main() -> int:
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
