# jie_radical.py — 卩 (jie) radical, 2 strokes (横折钩 + 竖).
# Batch B1 (position 55) — human PASSed.
#
# Composition: bank shu (scaled up 5%) for the long left vertical +
# inlined small 横折钩 (rounded D-shape) at top-right.

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


def _tapered_segment(draw, p0, p1, w0, w1, ox, oy, scale, steps=20,
                     extra_ox=0.0, extra_oy=0.0):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = max(1, int((w0 + (w1 - w0) * u0) * scale))
        pa = _to_pixel_scaled(extra_ox + xa, extra_oy + ya, ox, oy, scale)
        pb = _to_pixel_scaled(extra_ox + xb, extra_oy + yb, ox, oy, scale)
        draw.line([pa, pb], fill=(0, 0, 0), width=w)


def _draw_heng_zhe_gou_small(draw, ox, oy, scale):
    p_h_start = (-10, 75)
    p_corner = (40, 75)
    p_v_end = (30, 20)

    _tapered_segment(draw, p_h_start, p_corner, 8, 10, ox, oy, scale, steps=18)

    cx, cy = _to_pixel_scaled(*p_corner, ox, oy, scale)
    r = 5 * scale
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    def bezier_pt(u, p0, p1, p2):
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        return (x, y)

    ctrl = (52, 50)
    steps = 24
    prev = p_corner
    for i in range(1, steps + 1):
        u = i / steps
        curr = bezier_pt(u, p_corner, ctrl, p_v_end)
        w = int(10 - 1.5 * u)
        w = max(1, w)
        _tapered_segment(draw, prev, curr, w, w, ox, oy, scale, steps=2)
        prev = curr

    h_base = (p_v_end[0] + 1, p_v_end[1] + 2)
    h_tip = (p_v_end[0] - 14, p_v_end[1] + 14)
    _tapered_segment(draw, h_base, h_tip, 9, 2, ox, oy, scale, steps=12)

    bx, by = _to_pixel_scaled(*p_v_end, ox, oy, scale)
    br = 5 * scale
    draw.ellipse([bx - br, by - br, bx + br, by + br], fill=(0, 0, 0))


def draw_jie_radical(t, ox=0.0, oy=0.0, scale=1.0):
    """卩 radical: long 竖 (scale 1.05) + inlined small 横折钩 at top-right."""
    draw_shu(t, ox=ox + (-15) * scale, oy=oy + (-25) * scale, scale=1.05 * scale)
    _draw_heng_zhe_gou_small(t, ox, oy, scale)
