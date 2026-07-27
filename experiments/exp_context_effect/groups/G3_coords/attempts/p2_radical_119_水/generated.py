# p2_radical_119_水 — 水 (shuǐ, water), 4 strokes.
# G3 coord-bank attempt.
#
# Composition (standard 水):
#   1. Center 竖钩 (shu_gou) — vertical shaft with hook flick up-left.
#   2. Left 横撇 — short high heng ending, then a longer diagonal down-left.
#      Rendered here as a single tapered_bezier that curves from upper-mid
#      down and left.
#   3. Right upper short 撇 — small stroke from near-top of shaft going
#      down-right (short pie).
#   4. Right lower 捺 — longer sweeping stroke down-right (variant_na).
#
# Read the GT: center vertical hook, left curving downstroke, right two
# strokes (short upper + longer lower diagonal). Match proportions.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from shu_gou import draw_shu_gou              # noqa: E402
from _shared_helpers import (                  # noqa: E402
    variant_pie, variant_na, tapered_bezier, to_px
)


def draw_shui(t, ox=0.0, oy=0.0, scale=1.0):
    """水 radical, 4 strokes. Center 竖钩 flanked by three curving strokes.

    Revision v2: shorten center shaft; left stroke starts closer to shaft
    top and curves down-left; right upper 撇 starts higher and further
    right, sloping down toward shaft; right 捺 starts at mid-height on
    shaft area and sweeps far right-down with proper taper.
    """
    # 1) Center 竖钩. Moderate length, centered vertically.
    draw_shu_gou(t, ox=ox + 0.0 * scale, oy=oy - 10.0 * scale, scale=0.70 * scale)

    # 2) Left curving downstroke (横撇 / long pie form): starts near the
    #    top of the shaft (slight-right of head), curves down-left to
    #    the lower-left region. Matches GT's left arc.
    head_L = (ox - 5.0 * scale, oy + 45.0 * scale)
    ctrl_L = (ox - 50.0 * scale, oy + 15.0 * scale)
    tail_L = (ox - 75.0 * scale, oy - 55.0 * scale)
    tapered_bezier(t, head_L, ctrl_L, tail_L,
                   w_head=8.0 * scale, w_tail=2.0 * scale, n=52)

    # 3) Right upper short 撇: from upper-right (above shaft mid) down
    #    and left toward the shaft. Short.
    variant_pie(
        t,
        head=(ox + 42.0 * scale, oy + 45.0 * scale),
        tail=(ox + 8.0 * scale, oy + 15.0 * scale),
        bow_perp=-3.0 * scale, w_head=8.0 * scale, w_tail=1.5 * scale,
    )

    # 4) Right lower 捺: from near shaft-middle, long sweep down-right
    #    with belly, tapered tail.
    variant_na(
        t,
        head=(ox + 8.0 * scale, oy + 5.0 * scale),
        tail=(ox + 82.0 * scale, oy - 55.0 * scale),
        bow_perp=5.0 * scale,
        w_head=3.0 * scale, w_belly=13.0 * scale, w_tail=3.0 * scale,
        belly_u=0.72,
    )


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_shui(d, ox=0.0, oy=0.0, scale=1.0)
    out = os.path.join(_HERE, "01_水.png")
    img.save(out)
    print(f"wrote {out}")
