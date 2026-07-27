# cao_zi_tou.py — 艹 (cao, "grass") radical, 3 strokes.
# Batch B1 (position 71) — human PASSed.
#
# All three strokes inlined: bank heng is flat but 艹 wants a
# rising tilt; verticals are too short to reuse bank shu (<0.4 scale).

import os
import sys

_CANVAS = 300


def _to_pixel_scaled(bx, by, ox, oy, scale):
    px = _CANVAS / 2 + ox + bx * scale
    py = _CANVAS / 2 - (oy + by * scale)
    return px, py


def _draw_tilted_heng(t, x_left, x_right, y_left, y_right, ox, oy, scale,
                      thickness=11):
    p_left = _to_pixel_scaled(x_left, y_left, ox, oy, scale)
    p_right = _to_pixel_scaled(x_right, y_right, ox, oy, scale)
    w = max(1, int(round(thickness * scale)))
    t.line([p_left, p_right], fill=(0, 0, 0), width=w)
    r = w / 2.0
    for (px, py) in (p_left, p_right):
        t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def _draw_short_vertical(t, ox_local, oy_top, oy_bot, ox, oy, scale,
                         thickness=9, lean=0.0):
    p_top = _to_pixel_scaled(ox_local + lean, oy_top, ox, oy, scale)
    p_bot = _to_pixel_scaled(ox_local - lean, oy_bot, ox, oy, scale)
    w = max(1, int(round(thickness * scale)))
    t.line([p_top, p_bot], fill=(0, 0, 0), width=w)
    r = w / 2.0
    for (px, py) in (p_top, p_bot):
        t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def draw_cao_zi_tou(t, ox=0.0, oy=0.0, scale=1.0):
    """艹 radical: rising 横 crossed by two short 竖."""
    # Tilted heng from (-115,-12) to (+115,+18).
    _draw_tilted_heng(t, -115, 115, -12, +18, ox, oy, scale, thickness=10)
    # Left vertical at x=-40, slight right lean at top.
    _draw_short_vertical(t, -40, +18, -58, ox, oy, scale, thickness=9, lean=+3)
    # Right vertical at x=+42, slight left lean at bottom.
    _draw_short_vertical(t, +42, +28, -58, ox, oy, scale, thickness=9, lean=-8)
