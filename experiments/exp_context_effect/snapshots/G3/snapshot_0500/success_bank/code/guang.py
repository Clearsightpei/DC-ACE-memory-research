# guang.py — 广 (guang) radical, 3 strokes (点 + 横 + 撇).
# Batch B1 (position 84) — human PASSed.
#
# Bank 点 + bank 横 + inlined 撇 (long left-falling sweep, longer than
# bank pie's canonical y-span).

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from dian import draw_dian  # noqa: E402
from heng import draw_heng  # noqa: E402

_CANVAS = 300


def _to_pixel_scaled(bx, by, ox, oy, scale):
    px = _CANVAS / 2 + ox + bx * scale
    py = _CANVAS / 2 - (oy + by * scale)
    return px, py


def _draw_pie_inline(draw, x0, y0, x1, y1, ox, oy, scale,
                     ctrl_dx=-8.0, ctrl_dy=+15.0,
                     w_head=11.0, w_tail=1.0, n_segments=80):
    mx = (x0 + x1) / 2.0 + ctrl_dx
    my = (y0 + y1) / 2.0 + ctrl_dy

    prev_pt = None
    for i in range(n_segments + 1):
        u = i / n_segments
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel_scaled(bx, by, ox, oy, scale)
        w = (w_head + (w_tail - w_head) * u) * scale
        w_int = max(1, int(round(w)))
        if prev_pt is not None:
            draw.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)


def draw_guang(t, ox=0.0, oy=0.0, scale=1.0):
    """广 radical: 点 chimney + 横 roof + long left-falling 撇 welded at heng's left end."""
    # Stroke 1: 点.
    draw_dian(t, ox=ox + 10 * scale, oy=oy + 95 * scale, scale=0.55 * scale)
    # Stroke 2: 横 (short, scale 0.60, at math (+30, +40)).
    draw_heng(t, ox=ox + 30 * scale, oy=oy + 40 * scale, scale=0.60 * scale)
    # Stroke 3: 撇 head welded to heng's left end (-30, +40) → tail (-90, -115).
    _draw_pie_inline(t,
                     x0=-30.0, y0=+40.0,
                     x1=-90.0, y1=-115.0,
                     ox=ox, oy=oy, scale=scale,
                     ctrl_dx=-22.0, ctrl_dy=+5.0,
                     w_head=11.0, w_tail=1.5,
                     n_segments=90)
