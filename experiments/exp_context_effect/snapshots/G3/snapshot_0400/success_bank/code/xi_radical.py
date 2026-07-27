# xi_radical.py — 匸 (xi) radical, 2 strokes (top 一 + inlined 竖折).
# Batch B1 (position 66) — human PASSed.
#
# Bank heng for the top; 竖折 inlined so the bottom horizontal can be
# widened to match the top 一 above it.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from heng import draw_heng  # noqa: E402

_CANVAS = 300


def _to_pixel_scaled(bx, by, ox, oy, scale):
    px = _CANVAS / 2 + ox + bx * scale
    py = _CANVAS / 2 - (oy + by * scale)
    return px, py


def _draw_shu_zhe_inline(t, ox, oy, scale, sub_ox=0.0, sub_oy=0.0,
                         ink=11, v_height=130, h_width=180, top_y=50):
    v_top_math = (sub_ox, sub_oy + top_y)
    v_bot_math = (sub_ox, sub_oy + top_y - v_height)
    h_right_math = (sub_ox + h_width, sub_oy + top_y - v_height)

    w = max(1, int(ink * scale))
    a = _to_pixel_scaled(*v_top_math, ox, oy, scale)
    b = _to_pixel_scaled(*v_bot_math, ox, oy, scale)
    c = _to_pixel_scaled(*h_right_math, ox, oy, scale)

    t.line([a, b], fill=(0, 0, 0), width=w)
    t.line([b, c], fill=(0, 0, 0), width=w)
    r = w // 2
    for pt in (a, b, c):
        t.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))


def draw_xi_radical(t, ox=0.0, oy=0.0, scale=1.0):
    """匸 radical: top 一 (wide) + inlined 竖折 (left+bottom)."""
    # Stroke 1: top 一 (scale 0.95, at math (+5, +55)).
    draw_heng(t, ox=ox + 5 * scale, oy=oy + 55 * scale, scale=0.95 * scale)
    # Stroke 2: inlined 竖折 (sub-origin at math x=-80).
    _draw_shu_zhe_inline(t, ox, oy, scale, sub_ox=-80.0, sub_oy=0.0,
                         ink=11, v_height=128, h_width=165, top_y=48)
