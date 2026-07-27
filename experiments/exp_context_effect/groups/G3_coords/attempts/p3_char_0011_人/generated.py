# p3_char_0011_人 — 人 (rén, "person"), 2 strokes: 撇 + 捺.
#
# GT (clean version): apex slightly upper-mid at ~PIL(152, 95).
#   撇: from apex sweep down-left to ~PIL(58, 265), with a tiny
#       visible vertical tick at the very top of the head.
#   捺: begins slightly below-right of apex ~PIL(158, 128) and
#       sweeps down-right to ~PIL(257, 262), belly on the right.
#
# Coord convention (P5): center (150,150), +y up.
#   PIL(152, 95) -> math(+2, +55)
#   PIL(58, 265) -> math(-92, -115)
#   PIL(158,128) -> math(+8, +22)
#   PIL(257,262) -> math(+107, -112)

import math
import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code")))
from _shared_helpers import variant_pie, variant_na, tapered_line  # noqa: E402

CANVAS_SIZE = 300


def draw_ren(d):
    """人 — 2 strokes rendered with adaptive helpers."""
    # 撇 — head at apex, tail lower-left.  Standalone dominant 撇 in 人.
    # Slightly thinner than mu.py's crossing arm — GT shows a graceful
    # thin curve, not a heavy wedge.  Use moderate w_head, strong bow.
    pie_head = (2, 65)
    pie_tail = (-95, -118)
    variant_pie(d, pie_head, pie_tail,
                bow_perp=-10.0, w_head=6.5, w_tail=1.2, n=64)

    # Tiny vertical tick at top of 撇 (visible in GT as a small entry
    # nub / 起笔 head).  Short thin vertical just above apex.
    tapered_line(d, (3, 72), (2, 66), 1.8, 3.5, n=10)

    # 捺 — head starts just below-right of apex, sweeps down-right.
    # GT's 捺 in 人 terminates THICK at the bottom-right (no closing
    # taper — it's a heavy 顿笔 tail, not a fine tip).  Use variant_na
    # with belly_u=0.85 and a heavy w_tail so it stays thick to the end.
    na_head = (8, 30)
    na_tail = (108, -110)
    variant_na(d, na_head, na_tail,
               bow_perp=5.0, w_head=2.0, w_belly=11.0, w_tail=9.0,
               belly_u=0.85, n=72)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_ren(d)
    out = os.path.join(_HERE, "01_人.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
