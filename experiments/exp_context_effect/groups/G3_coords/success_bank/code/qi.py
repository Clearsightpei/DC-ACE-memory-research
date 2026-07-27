# qi.py — 七 (qī, "seven"), 2 strokes: short 横 + 竖弯钩.
# PASSed at p3_char_0027_七 (B3 pos 184).
# Inline top heng + bank shu_wan_gou.
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402

CANVAS = 300


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def draw_qi(t, ox=0, oy=0, scale=1.0):
    x_left, y_left = _to_pixel(ox + -95 * scale, oy + 40 * scale)
    x_right, y_right = _to_pixel(ox + 75 * scale, oy + 20 * scale)
    t.line([(x_left, y_left), (x_right, y_right)],
           fill=(0, 0, 0), width=max(1, int(round(12 * scale))))
    draw_shu_wan_gou(t, ox=ox - 25 * scale, oy=oy - 15 * scale, scale=1.0 * scale)
