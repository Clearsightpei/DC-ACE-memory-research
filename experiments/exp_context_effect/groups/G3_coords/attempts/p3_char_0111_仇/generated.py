# p3_char_0111_仇 — 仇 (chóu, "enemy"), 4 strokes.
# Structure: 亻 (left, 2 strokes) + 九 (right, 2 strokes).
# 亻 = pie + shu — use bank primitive draw_ren_pang.
# 九 = 撇 (top-left sweep) + 横折弯钩 — drawn inline (no bank match).
#
# Revision notes vs pass 1:
# - Enlarge 九 so its 撇 tail doesn't crowd the shaft of 亻.
# - Make 九's 撇 more prominent (shorter but clearly visible above the bowl).
# - Move 亻 slightly further left; 九 bowl should occupy right ~60%.
# - Bowl needs to reach lower and further right to match GT proportions.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from _shared_helpers import (  # noqa: E402
    tapered_bezier, tapered_line, variant_pie,
)


CANVAS = 300


def draw_jiu_right(draw, ox=0.0, oy=0.0, scale=1.0):
    """Draw 九 on the right side. Math coords (+y up)."""
    s = scale

    # Stroke 1: 撇 — starts near top-center of 九, sweeps down-left.
    # Head high & slightly right of center; tail low-left but well above bottom.
    pie_head = (ox + 5 * s, oy + 65 * s)
    pie_tail = (ox + -40 * s, oy + -35 * s)
    variant_pie(draw, pie_head, pie_tail,
                bow_perp=-6.0, w_head=7.0, w_tail=3.0, n=48)

    # Stroke 2: 横折弯钩.
    # Segment A: 横 — begins slightly left of pie_head top, extends right.
    h_start = (ox + -5 * s, oy + 50 * s)
    h_end = (ox + 60 * s, oy + 48 * s)
    tapered_line(draw, h_start, h_end, 6 * s, 6 * s, n=20)

    # Segment B: turn down (折), curve to right-bottom.
    ctrl1 = (ox + 70 * s, oy + 0 * s)
    mid_low = (ox + 55 * s, oy + -75 * s)
    tapered_bezier(draw, h_end, ctrl1, mid_low, 6 * s, 7 * s, n=40)

    # Segment C: bowl sweeps left across the bottom.
    ctrl2 = (ox + 20 * s, oy + -95 * s)
    low_left = (ox + -20 * s, oy + -85 * s)
    tapered_bezier(draw, mid_low, ctrl2, low_left, 7 * s, 6 * s, n=32)

    # Segment D: hook — small upward flick at the very end.
    hook_ctrl = (ox + -22 * s, oy + -78 * s)
    hook_end = (ox + -18 * s, oy + -60 * s)
    tapered_bezier(draw, low_left, hook_ctrl, hook_end, 6 * s, 3 * s, n=18)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # 亻 on the far left, a bit taller.
    draw_ren_pang(draw, ox=-85, oy=-5, scale=1.05)

    # 九 fills the right side.
    draw_jiu_right(draw, ox=25, oy=-10, scale=1.05)

    out = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "01_仇.png"
    )
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
