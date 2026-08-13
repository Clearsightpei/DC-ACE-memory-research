# you_have_for_LR_right.py — 有 shifted/scaled for L-R right column
# Promoted from p3_char_0424_侑 (B11 main PASS, BANK_DEVIATION).
# Curator B11 (2026-08-03, position 550).
#
# CONTEXT (v13 variant policy). The bank's `you_have.py` (draw_you_have)
# has baked pixel coords for a centered full-canvas 有. When 有 must sit
# in the right ~60% of an L-R char (侑 = 亻+有, and cousins 郁, 洧, 侑),
# the centered recipe overlaps the left radical.
#
# This entry inlines a right-shifted, slightly-compressed 有 recipe that
# reuses the bank `yue` primitive for the 月 body (tucked into the crook
# of the top heng + long pie).
#
# The original `you_have.py` remains untouched. Use this variant when
# 有 sits in the right column of an L-R composition.

import os
import sys
from PIL import Image, ImageDraw

# Ensure sibling bank modules are importable when this file is imported
# from an attempt directory.
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from yue import draw_yue, _tapered_line, _tapered_bezier  # noqa: E402


def draw_you_have_right(D):
    """Draw 有 into the right ~60% of a 300x300 PIL canvas."""
    # 1) top 横 — spans right side, slight up-slant to the right
    _tapered_line(D, (118, 102), (280, 90),
                  w0=6, w1=8, steps=28)
    D.ellipse([114, 98, 124, 108], fill=(0, 0, 0))
    D.ellipse([275, 86, 285, 96], fill=(0, 0, 0))

    # 2) long 撇 — starts near top-right of the heng, sweeps down-left
    p0 = (208, 70)
    p2 = (118, 275)
    ctrl = (165, 195)  # bow toward left
    _tapered_bezier(D, p0, ctrl, p2, w0=10, w1=2, steps=64)
    D.ellipse([204, 66, 214, 76], fill=(0, 0, 0))

    # 3) 月 tucked inside the crook — small, right-bottom.
    # draw_yue base is centered on (150,150); shift right ~65, down ~45,
    # scale 0.52 to fit compactly inside the crook.
    draw_yue(D, ox=65, oy=45, scale=0.52)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_you_have_right(d)
    img.save("you_have_for_LR_right_preview.png")
