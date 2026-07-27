# fang.py — 匚 (fang) radical, 2 strokes (top heng + inlined 竖折).
# Batch B1 (position 51) — human PASSed.
#
# heng at scale 0.75 for the top; 竖折 inlined because bank shu_zhe
# proportions don't match the near-square envelope of 匚.

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


def draw_fang(t, ox=0.0, oy=0.0, scale=1.0):
    """匚 radical: top 横 + inlined 竖折 (left vert + bottom horiz)."""
    # Stroke 1: top 横 (scale 0.75, center at math (-5, +50)).
    draw_heng(t, ox=ox + (-5) * scale, oy=oy + 50 * scale, scale=0.75 * scale)

    # Stroke 2: inlined 竖折.
    ink_v = max(1, int(round(12 * scale)))
    ink_h = ink_v
    v_top = (-80, +50)
    v_bot = (-80, -95)
    h_right = (+75, -95)
    t.line([_to_pixel_scaled(*v_top, ox, oy, scale),
            _to_pixel_scaled(*v_bot, ox, oy, scale)],
           fill=(0, 0, 0), width=ink_v)
    t.line([_to_pixel_scaled(*v_bot, ox, oy, scale),
            _to_pixel_scaled(*h_right, ox, oy, scale)],
           fill=(0, 0, 0), width=ink_h)
    # 顿笔 corner blob at bottom-left elbow.
    cx, cy = _to_pixel_scaled(*v_bot, ox, oy, scale)
    r = 6 * scale
    t.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))
