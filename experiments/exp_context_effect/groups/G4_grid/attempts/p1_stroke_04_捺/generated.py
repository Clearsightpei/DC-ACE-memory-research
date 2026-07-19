"""p1_stroke_04_捺 — Drawer attempt (G4 grid-bank).

Renders a standalone 捺 stroke: a right-falling sweep from upper-left
to lower-right, thin at the head, swelling to peak thickness near
~80% of the stroke, then tapering to a fine needle-tip 出锋. Uses the
draw_na primitive from the Success Bank.

米字格 anchors:
  head @ TL (0.60, 0.30) — thin 起笔 in the upper-left cell
  tail @ BR (0.70, 0.75) — needle-tip 出锋 in the lower-right cell

Joint spec: single stroke, no joints.
"""

import os
import sys

# Make the Success Bank primitives importable.
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from na import draw_na


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_na(
        d,
        ('TL', 0.60, 0.30),   # head, upper-left (thin 起笔)
        ('BR', 0.70, 0.75),   # tail, lower-right (needle-tip 出锋)
        head_width=3,
        peak_width=14,
        tail_width=1,
        peak_t=0.8,
        curve=0.10,
    )
    out = os.path.join(_HERE, "01_捺.png")
    img.save(out)
    print(f"wrote {out} ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    main()
