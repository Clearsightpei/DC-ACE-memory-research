# BANK_DEVIATION
# skipped: bi_field_over_ji.py (canvas-centered 田 baked with 丌 legs)
# reason: 畚 needs 田 as the BOTTOM element in a top/bottom stack, and the top
#         is a completely different 龴-style component (short pie/na cross +
#         横 + 撇 + 横折弯钩), so bi_field_over_ji's baked 丌 base is wrong.
# fresh_component: ben_top_curved_apex (top 5-ish strokes for 畚)
#
# For the 田 at the bottom I re-use the compressed variant helper
# `quan_tian_for_LR_left` — its signature takes absolute
# (x_left, x_right, y_top, y_bot) so I can slot it into a centered-bottom
# rectangle rather than the LR-left column it was promoted for.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.join(_HERE, "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(_BANK))

from quan_tian_for_LR_left import draw_quan_tian_for_LR_left  # noqa: E402


def _curve(d, p0, p1, p2, width, steps=40, black=(0, 0, 0)):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        pts.append((x, y))
    d.line(pts, fill=black, width=width)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    black = (0, 0, 0)

    # ---------- TOP: 龴-style component (5 strokes) ----------
    # S1: short 撇 from apex to lower-left
    d.line([(150, 25), (115, 82)], fill=black, width=6)
    # S2: short 捺 from apex to lower-right (crosses S1 near top)
    d.line([(150, 25), (185, 82)], fill=black, width=6)
    # S3: long 横 spanning wide underneath the X (roof/lid)
    d.line([(40, 100), (260, 100)], fill=black, width=6)
    # S4: 撇 from mid-heng curving down-left (long)
    _curve(d, (140, 105), (115, 140), (60, 190), width=6)
    # S5: 横折弯钩 — from mid-heng going right, curving wide down and
    # returning under, forming the big ㇈ envelope seen in the GT
    d.line([(160, 105), (232, 105)], fill=black, width=6)
    _curve(d, (232, 105), (250, 165), (215, 195), width=6)
    # small hook back to upper-left at tail
    d.line([(215, 195), (190, 185)], fill=black, width=6)

    # ---------- BOTTOM: 田 centered under the top block ----------
    # centered rectangle
    draw_quan_tian_for_LR_left(
        d,
        x_left=95, x_right=205,
        y_top=205, y_bot=285,
        w=6, wm=5,
    )

    out = os.path.join(_HERE, "01_畚.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
