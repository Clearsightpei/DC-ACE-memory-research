# gong_radical.py — 廾 (gong) radical, 3 strokes (撇 + 横 + 竖).
# Batch B1 (position 83) — human PASSed.
#
# All three inlined: pie is a custom tapered bezier for exact endpoint
# control; heng and shu are uniform straight lines.

import os
import sys

_CANVAS = 300


def _to_pixel_scaled(bx, by, ox, oy, scale):
    px = _CANVAS / 2 + ox + bx * scale
    py = _CANVAS / 2 - (oy + by * scale)
    return px, py


def _draw_inlined_pie(draw, head, tail, ctrl_offset, ox, oy, scale,
                      w_head=9, w_tail=1, n_seg=60):
    x0, y0 = head
    x1, y1 = tail
    mx = (x0 + x1) / 2.0 + ctrl_offset[0]
    my = (y0 + y1) / 2.0 + ctrl_offset[1]

    prev = None
    for i in range(n_seg + 1):
        u = i / n_seg
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel_scaled(bx, by, ox, oy, scale)
        w = (w_head + (w_tail - w_head) * u) * scale
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def draw_gong_radical(t, ox=0.0, oy=0.0, scale=1.0):
    """廾 radical: left 撇 + horizontal crossbar + right 竖 (slight left-lean)."""
    # Stroke 1: 撇 (bezier).
    _draw_inlined_pie(t, head=(-25, 75), tail=(-82, -90),
                      ctrl_offset=(-8, 0), ox=ox, oy=oy, scale=scale,
                      w_head=10, w_tail=1, n_seg=60)

    # Stroke 2: 横 (uniform line from (-90,+5) to (+75,+5)).
    p_left = _to_pixel_scaled(-90, +5, ox, oy, scale)
    p_right = _to_pixel_scaled(+75, +5, ox, oy, scale)
    thickness = max(1, int(round(10 * scale)))
    t.line([p_left, p_right], fill=(0, 0, 0), width=thickness)

    # Stroke 3: 竖 (slight lean, from (+55,+70) to (+48,-85)).
    p_top = _to_pixel_scaled(+55, +70, ox, oy, scale)
    p_bot = _to_pixel_scaled(+48, -85, ox, oy, scale)
    t.line([p_top, p_bot], fill=(0, 0, 0), width=thickness)
