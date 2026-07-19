# mi_radical.py — 冖 (mi) radical (秃宝盖), 2 strokes (点 + 横钩).
# Batch B1 (position 58) — human PASSed.
#
# bank 点 (scaled) + inlined thinner 横钩 (bank heng_gou is too heavy
# for radical-scale use).

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from dian import draw_dian  # noqa: E402

_CANVAS = 300


def _apply(x, y, ox, oy, scale):
    """Apply outer (ox, oy, scale) to raw PIL recipe centered on 150,150."""
    cx, cy = _CANVAS / 2, _CANVAS / 2
    return (cx + ox + (x - cx) * scale, cy - oy + (y - cy) * scale)


def _draw_inlined_henggou(draw, x0, y0, x1, y1, ox, oy, scale,
                          w_start=6, w_end=9, hook_dx=-16, hook_dy=30,
                          blob_r=6, hook_w_start=9):
    """Inlined thin 横钩 for a radical (bank heng_gou is too heavy)."""
    steps = 24
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * t0
        ya = y0 + (y1 - y0) * t0
        xb = x0 + (x1 - x0) * t1
        yb = y0 + (y1 - y0) * t1
        w = max(1, int((w_start + (w_end - w_start) * t0) * scale))
        pa = _apply(xa, ya, ox, oy, scale)
        pb = _apply(xb, yb, ox, oy, scale)
        draw.line([pa, pb], fill="black", width=w)

    bx, by = _apply(x1, y1, ox, oy, scale)
    r = blob_r * scale
    draw.ellipse([bx - r, by - r, bx + r, by + r], fill="black")

    hx0 = x1 + 1
    hy0 = y1 + 1
    hx1 = x1 + hook_dx
    hy1 = y1 + hook_dy
    hsteps = 14
    for i in range(hsteps):
        t0 = i / hsteps
        t1 = (i + 1) / hsteps
        xa = hx0 + (hx1 - hx0) * t0
        ya = hy0 + (hy1 - hy0) * t0
        xb = hx0 + (hx1 - hx0) * t1
        yb = hy0 + (hy1 - hy0) * t1
        w = max(1, int((hook_w_start - (hook_w_start - 1) * t0) * scale))
        pa = _apply(xa, ya, ox, oy, scale)
        pb = _apply(xb, yb, ox, oy, scale)
        draw.line([pa, pb], fill="black", width=w)


def draw_mi_radical(t, ox=0.0, oy=0.0, scale=1.0):
    """冖 (秃宝盖): small 点 top-left + thin 横钩 bar with hook."""
    # 点 at math (-50, +30) scale 0.5.
    draw_dian(t, ox=ox + (-50) * scale, oy=oy + 30 * scale, scale=0.5 * scale)
    # Inlined 横钩 (raw PIL coords): bar from (108,118) to (230,122).
    _draw_inlined_henggou(t, 108, 118, 230, 122, ox, oy, scale,
                          w_start=6, w_end=9, hook_dx=-14, hook_dy=30,
                          blob_r=6, hook_w_start=9)
