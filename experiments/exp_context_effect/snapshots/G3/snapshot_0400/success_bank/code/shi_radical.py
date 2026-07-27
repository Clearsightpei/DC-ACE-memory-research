# shi_radical.py — 尸 (shi) radical, 3 strokes.
# Batch B1 (position 97) — human PASSed.
#
# All three inlined: 横折 (top+right), middle 横, and a long 撇
# (bank pie too short for 尸's sweep).

import os
import sys

_CANVAS = 300


def _to_pixel_scaled(bx, by, ox, oy, scale):
    px = _CANVAS / 2 + ox + bx * scale
    py = _CANVAS / 2 - (oy + by * scale)
    return px, py


def draw_shi_radical(t, ox=0.0, oy=0.0, scale=1.0):
    """尸 radical: top 横折 + middle 横 + long 撇 welded at top-left."""
    # Stroke 1: 横折 (top + right descender).
    ink_w = max(1, int(round(8 * scale)))
    a = _to_pixel_scaled(-55, 90, ox, oy, scale)
    b = _to_pixel_scaled(50, 90, ox, oy, scale)
    c = _to_pixel_scaled(45, 5, ox, oy, scale)
    t.line([a, b], fill=(0, 0, 0), width=ink_w)
    t.line([b, c], fill=(0, 0, 0), width=ink_w)
    r = ink_w / 2 + 1
    for pt in (a, b, c):
        t.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))

    # Stroke 2: middle 横.
    ink_w2 = max(1, int(round(7 * scale)))
    a2 = _to_pixel_scaled(-48, 10, ox, oy, scale)
    b2 = _to_pixel_scaled(48, 10, ox, oy, scale)
    t.line([a2, b2], fill=(0, 0, 0), width=ink_w2)
    r2 = ink_w2 / 2
    for pt in (a2, b2):
        t.ellipse([pt[0] - r2, pt[1] - r2, pt[0] + r2, pt[1] + r2], fill=(0, 0, 0))

    # Stroke 3: long 撇, head welded to (-55, +90), tail (-100, -125).
    x0, y0 = -55.0, 90.0
    x1, y1 = -100.0, -125.0
    mx = (x0 + x1) / 2 - 15.0
    my = (y0 + y1) / 2 + 5.0
    n_segments = 60
    w_head = 10.0
    w_tail = 1.0
    prev = None
    for i in range(n_segments + 1):
        u = i / n_segments
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel_scaled(bx, by, ox, oy, scale)
        w = (w_head + (w_tail - w_head) * u) * scale
        w_int = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)
