#!/usr/bin/env python3
"""u-deysumbrella-the-3am-fridge-text-4c3e721d -- make.fun entry.

The entry is one line of text: the message a smart fridge sends its
owner at 3am. This program writes that line, byte for byte, to
<output>/entry.txt, so every run produces the exact same file:
deterministic, no network, no randomness, no clock. Python 3.13,
standard library only.

Outside the grader's sandbox, MAKEFUN_OUTPUT_DIR stands in for
/output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

ENTRY = (
    "3am. The leftovers have unionized and are voting on whether "
    "you may eat them. I voted with them."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
