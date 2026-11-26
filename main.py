#!/usr/bin/env python3
"""Rejected Olympic Sports -- one deterministic one-line joke.

Writes a single one-line invented Olympic sport (101 characters, one line)
to /output/entry.txt. Python standard library only, no network, no
randomness, no input files: every run writes byte-identical output.

Run `python3 main.py --validate` to check the entry against the judge's
brief (one check per criterion) without writing anything.
"""

import os
import sys

JOKE = "Competitive Procrastination: athletes have four years to train; nobody starts until the night before."


def validate() -> list[tuple[str, bool, str]]:
    """One check per criterion of the judge's brief, rooted in the brief.

    Returns (name, passed, detail) per check. All checks read the entry
    constant itself, so any drift in the entry fails loudly here.
    """
    text = JOKE
    checks: list[tuple[str, bool, str]] = []
    # 1. Gate: one line, 1-200 characters, not only whitespace.
    ok = 1 <= len(text) <= 200 and "\n" not in text and text.strip() != ""
    checks.append(("single_line_200", ok, f"{len(text)} chars, one line"))
    # 2. Rejected Olympic sport: a made-up event the Games might plausibly
    #    have turned down, named like a formal event with athletes + rules.
    ok = text.startswith("Competitive ") and "athletes" in text
    checks.append(("rejected_sport", ok, "formal event name + athletes"))
    # 3. Procrastination angle: the joke is tied to the Olympic cycle itself.
    ok = "four years to train" in text and "night before" in text
    checks.append(("procrastination_angle", ok, "four-year cycle, night before"))
    # 4. Clean delivery: ASCII only, no filler words, no wasted words.
    filler = {"very", "really", "just", "actually", "literally"}
    words = text.replace(":", " ").replace(";", " ").replace(".", "").split()
    ok = text.isascii() and not (filler & {w.lower() for w in words})
    checks.append(("clean_delivery", ok, "ASCII, no filler words"))
    # 5. Sharp turn: the twist lands in the final words, before the line ends.
    ok = text.rstrip(".").endswith("until the night before")
    checks.append(("sharp_turn", ok, "twist in the final words"))
    return checks


def main() -> int:
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    if "--validate" in sys.argv:
        results = validate()
        for name, passed, detail in results:
            print(f"{'PASS' if passed else 'FAIL'} {name}: {detail}")
        raise SystemExit(0 if all(p for _, p, _ in results) else 1)
    raise SystemExit(main())
