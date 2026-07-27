# ji_radical.py — 彐 (ji) radical, 3 strokes.
# Batch B1 (position 86) — human PASSed.
#
# All three strokes inlined for exact weld control (bank heng_zhe
# proportions don't quite fit).

import os
import sys

_CANVAS = 300


def _to_pixel_scaled(bx, by, ox, oy, scale):
    px = _CANVAS / 2 + ox + bx * scale
    py = _CANVAS / 2 - (oy + by * scale)
    return px, py


def draw_ji_radical(t, ox=0.0, oy=0.0, scale=1.0):
    """彐 radical: 横折 + middle 横 + bottom 横."""
    ink_w = max(1, int(round(10 * scale)))
    r = ink_w // 2

    # S1: 横折.
    s1_left = _to_pixel_scaled(-75, 65, ox, oy, scale)
    s1_corner = _to_pixel_scaled(70, 65, ox, oy, scale)
    s1_bottom = _to_pixel_scaled(70, -70, ox, oy, scale)
    t.line([s1_left, s1_corner], fill=(0, 0, 0), width=ink_w)
    t.line([s1_corner, s1_bottom], fill=(0, 0, 0), width=ink_w)
    for pt in (s1_left, s1_corner, s1_bottom):
        t.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))

    # S2: middle 横 (shorter).
    s2_left = _to_pixel_scaled(-70, 0, ox, oy, scale)
    s2_right = _to_pixel_scaled(30, 0, ox, oy, scale)
    t.line([s2_left, s2_right], fill=(0, 0, 0), width=ink_w)
    for pt in (s2_left, s2_right):
        t.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))

    # S3: bottom 横 (welded to vertical foot).
    s3_left = _to_pixel_scaled(-75, -70, ox, oy, scale)
    s3_right = _to_pixel_scaled(72, -70, ox, oy, scale)
    t.line([s3_left, s3_right], fill=(0, 0, 0), width=ink_w)
    for pt in (s3_left, s3_right):
        t.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))
