# p3_char_0579_教
# 教 = 孝 (left) + 攵 (right).  L-R split ~55/45.
# Left top:    bank lao_radical (耂), math coords, scaled/shifted.
# Left bottom: inline mini 子  (zi_char is PIL-pixel and doesn't shrink;
#              simpler to inline in math coords for the small nested slot).
# Right:       inline 攵 (no bank primitive for 攵; family is unmastered).
# No BANK_DEVIATION block: nothing suitable was skipped — zi_char is not
# skipped for stylistic reasons, it's skipped because its PIL-pixel
# recipe does not scale to the small nested-under-耂 slot 教 needs.

# BANK_DEVIATION
# skipped: zi_char.py
# reason: zi_char is PIL-pixel and its `scale` param only rescales the descender, not the hook — cannot shrink to the tiny nested 子 slot inside 孝.
# fresh_component: mini_zi_math_for_xiao_stack

import os
import sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from _shared_helpers import to_px, tapered_bezier, tapered_line  # noqa: E402
from lao_radical import draw_lao_radical  # noqa: E402


def draw_mini_zi(d, cx=-45, cy=-70, s=1.0):
    """Small 子 in math coords for the nested slot inside 孝.
    Three strokes: 横钩 top, 弯钩 descender, crossing 一."""
    # 1. 横钩 top: heng then small hook curling down-left.
    tapered_line(d,
                 (cx - 28 * s, cy + 30 * s),
                 (cx + 25 * s, cy + 27 * s),
                 4.5, 4.5, n=20)
    # small hook curling down and slightly in
    tapered_line(d,
                 (cx + 25 * s, cy + 27 * s),
                 (cx + 18 * s, cy + 15 * s),
                 4.5, 2.5, n=12)
    # 2. 弯钩 descender: from just below the hook, curves down and left.
    tapered_bezier(d,
                   (cx + 6 * s, cy + 22 * s),
                   (cx - 4 * s, cy - 10 * s),
                   (cx - 34 * s, cy - 40 * s),
                   w_head=4.5, w_tail=2.5, n=40)
    # 3. Crossing heng.
    tapered_line(d,
                 (cx - 32 * s, cy),
                 (cx + 30 * s, cy + 2 * s),
                 4.0, 4.0, n=20)


def draw_pu_right(d, ox=75, oy=5):
    """攵 (pū) right-slot recipe, math coords, PIL thin ink.
    Four strokes: short 撇 + short 一 crossing near top, then long 撇 + long 捺."""
    # 1. Short 撇 (top-left slash of the top X).
    tapered_line(d, (ox + 15, oy + 80), (ox - 15, oy + 40), 6, 3, n=24)
    # 2. Short 一 (short heng crossing the short 撇 near its lower half).
    p0 = to_px(ox - 25, oy + 50)
    p1 = to_px(ox + 35, oy + 45)
    d.line([p0, p1], fill=(0, 0, 0), width=5)
    # 3. Long 撇 — from near the crossing down-and-left, sweeping.
    tapered_bezier(d,
                   (ox + 30, oy + 25),
                   (ox + 5,  oy - 35),
                   (ox - 55, oy - 110),
                   w_head=8, w_tail=2, n=60)
    # 4. Long 捺 — from near the crossing down-and-right, thickens.
    tapered_bezier(d,
                   (ox - 12, oy + 20),
                   (ox + 25, oy - 40),
                   (ox + 70, oy - 110),
                   w_head=3, w_tail=9, n=60)


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # Left half — 孝 = 耂 over 子.
    # 耂 (lao_radical), math coords, shifted left, scale 0.55.
    draw_lao_radical(d, ox=-70, oy=5, scale=0.55)
    # 子 nested under the sweeping pie of 耂 — small.
    draw_mini_zi(d, cx=-45, cy=-70, s=1.0)

    # Right half — 攵 inlined.
    draw_pu_right(d, ox=75, oy=5)

    out = os.path.join(HERE, "01_教.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
