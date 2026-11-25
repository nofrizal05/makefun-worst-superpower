"""Worst Superpower — make.fun entry.

Writes exactly one line to /output/entry.txt: a superpower so useless
that naming it is the whole joke.
"""

import os

ENTRY = (
    "I can summon a single sock \u2014 always the wrong one, always slightly "
    "damp, always from a stranger\u2019s dryer, and never its pair."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
