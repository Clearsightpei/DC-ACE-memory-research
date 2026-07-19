"""p1_stroke_03_撇 — Drawer attempt (G4 grid-bank).

Renders a standalone 撇 stroke: a tapered sweep from upper-right to
lower-left, using the draw_pie primitive from the Success Bank.

米字格 anchors:
  head @ TR (0.35, 0.25) — thick 起笔 in the upper-right cell
  tail @ BL (0.25, 0.80) — needle-tip 出锋 in the lower-left cell

Joint spec: single stroke, no joints.
"""

import os
import sys

# Make the Success Bank primitives importable.
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from pie import draw_pie


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_pie(
        d,
        ('TR', 0.35, 0.25),   # head, upper-right
        ('BL', 0.25, 0.80),   # tail, lower-left
        head_width=12,
        tail_width=1,
        curve=0.10,
    )
    out = os.path.join(_HERE, "01_撇.png")
    img.save(out)
    print(f"wrote {out} ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    main()
