# chuan.py — 川 (chuan, "river"), 3 strokes.
# Batch B1 (position 75) — human PASSed.
#
# Inlined left 撇-scoop (bank pie too diagonal) + two bank shu verticals.

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


def _draw_left_curve(t, sub_ox, sub_oy, sub_scale, ox, oy, scale):
    """Inline the left curved stroke of 川."""
    x0, y0 = 5.0 * sub_scale, 55.0 * sub_scale
    x1, y1 = -8.0 * sub_scale, -60.0 * sub_scale
    mx = (x0 + x1) / 2.0 - 10.0 * sub_scale
    my = (y0 + y1) / 2.0

    n_segments = 60
    w_head = max(1, 10.0 * sub_scale)
    w_tail = max(1, 4.0 * sub_scale)

    prev_pt = None
    for i in range(n_segments + 1):
        u = i / n_segments
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel_scaled(sub_ox + bx, sub_oy + by, ox, oy, scale)
        w = (w_head + (w_tail - w_head) * u) * scale
        w_int = max(1, int(round(w)))
        if prev_pt is not None:
            t.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)


def draw_chuan(t, ox=0.0, oy=0.0, scale=1.0):
    """川 radical: left 撇-scoop + short middle 竖 + long right 竖."""
    # LEFT curved scoop at math (-50, -5), sub_scale 1.0.
    _draw_left_curve(t, -50, -5, 1.0, ox, oy, scale)
    # MIDDLE short 竖.
    draw_shu(t, ox=ox + 0, oy=oy + (-30) * scale, scale=0.5 * scale)
    # RIGHT long 竖.
    draw_shu(t, ox=ox + 55 * scale, oy=oy + (-25) * scale, scale=0.85 * scale)
