# qu_radical.py — 凵 (qu/kan) radical, 2 strokes (inlined 竖折 + short 竖).
# Batch B1 (position 59) — human PASSed.
#
# Both strokes inlined for consistent radical-scale thickness.

import os
import sys

_CANVAS = 300
_INK = 10


def _to_pixel_scaled(bx, by, ox, oy, scale):
    px = _CANVAS / 2 + ox + bx * scale
    py = _CANVAS / 2 - (oy + by * scale)
    return px, py


def draw_qu_radical(t, ox=0.0, oy=0.0, scale=1.0):
    """凵 radical: U-shape from 竖折 + short right 竖."""
    w = max(1, int(round(_INK * scale)))
    r = w // 2

    # Stroke 1: 竖折.
    v_top = (-80, 10)
    v_bot = (-80, -80)
    h_right = (80, -80)
    t.line([_to_pixel_scaled(*v_top, ox, oy, scale),
            _to_pixel_scaled(*v_bot, ox, oy, scale)],
           fill=(0, 0, 0), width=w)
    t.line([_to_pixel_scaled(*v_bot, ox, oy, scale),
            _to_pixel_scaled(*h_right, ox, oy, scale)],
           fill=(0, 0, 0), width=w)
    for pt in (v_top, v_bot, h_right):
        px, py = _to_pixel_scaled(*pt, ox, oy, scale)
        t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))

    # Stroke 2: right 竖 (short).
    s2_top = (80, 15)
    s2_bot = (80, -80)
    t.line([_to_pixel_scaled(*s2_top, ox, oy, scale),
            _to_pixel_scaled(*s2_bot, ox, oy, scale)],
           fill=(0, 0, 0), width=w)
    for pt in (s2_top, s2_bot):
        px, py = _to_pixel_scaled(*pt, ox, oy, scale)
        t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
