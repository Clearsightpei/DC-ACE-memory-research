# shan.py — 山 (shan, "mountain") radical, 3 strokes.
# Batch B1 (position 95) — human PASSed.
#
# Middle bank shu (tall) + inlined 竖折 (left+base, per TR5 mismatch) +
# short right bank shu.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from shu import draw_shu  # noqa: E402

_CANVAS = 300


def _to_pixel_scaled(bx, by, ox, oy, scale):
    px = _CANVAS / 2 + ox + bx * scale
    py = _CANVAS / 2 - (oy + by * scale)
    return px, py


def draw_shan(t, ox=0.0, oy=0.0, scale=1.0):
    """山 radical: middle 竖 + inlined 竖折 (left+base) + short right 竖."""
    # Stroke 1: middle 竖.
    draw_shu(t, ox=ox + 0, oy=oy + 20 * scale, scale=0.60 * scale)

    # Stroke 2: 竖折 inlined.
    v_top = (-50 + 3, 30)
    v_bot = (-50, -40)
    h_left = (-50, -40)
    h_right = (55, -40)
    ink = max(1, int(round(10 * scale)))
    t.line([_to_pixel_scaled(*v_top, ox, oy, scale),
            _to_pixel_scaled(*v_bot, ox, oy, scale)],
           fill=(0, 0, 0), width=ink)
    t.line([_to_pixel_scaled(*h_left, ox, oy, scale),
            _to_pixel_scaled(*h_right, ox, oy, scale)],
           fill=(0, 0, 0), width=ink)
    r = ink // 2
    for pt in (v_top, v_bot, h_left, h_right):
        px, py = _to_pixel_scaled(*pt, ox, oy, scale)
        t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))

    # Stroke 3: right 竖 (short).
    draw_shu(t, ox=ox + 50 * scale, oy=oy + (-10) * scale, scale=0.30 * scale)
