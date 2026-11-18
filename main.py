#!/usr/bin/env python3
"""Entry program for make.fun competition news-image-20261118.

"Sum up 18 November's world news in one image."

The entry image ships in this repository as entry.png, drawn beforehand
by draw_entry.py (kept alongside for provenance). The competition's
program has no network and only the standard library, so this program's
job is the one the rules suggest: copy the image, byte for byte, to the
output directory. Two runs therefore always produce identical bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

OUTPUT_NAME = "entry.png"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).resolve().parent / OUTPUT_NAME
    shutil.copyfile(source, out_dir / OUTPUT_NAME)


if __name__ == "__main__":
    main()
