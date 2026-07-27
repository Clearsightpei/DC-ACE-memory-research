# bao_gai_tou.py — 宀 (bao-gai-tou, "roof") radical, 3 strokes.
# Batch B1 (position 92) — human PASSed.
#
# Bank 横钩 (draw_henggou uses raw PIL coords) + bank 点 (math coords) +
# inlined short slanted stroke on the left (too small for bank shu).

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from dian import draw_dian          # noqa: E402
from heng_gou import draw_henggou   # noqa: E402

_CANVAS = 300


def _apply(x, y, ox, oy, scale):
    """Apply outer (ox, oy, scale) to raw PIL coords centered on 150,150."""
    cx, cy = _CANVAS / 2, _CANVAS / 2
    return (cx + ox + (x - cx) * scale, cy - oy + (y - cy) * scale)


def draw_bao_gai_tou(t, ox=0.0, oy=0.0, scale=1.0):
    """宀 radical: wide 横钩 roof + 点 chimney + short left slanted point."""
    # S3 first (roof): 横钩 with its default coord range covering the roof.
    draw_henggou(t, ox=ox, oy=oy, scale=scale)

    # S1: 点 chimney tip.
    draw_dian(t, ox=ox + (-10) * scale, oy=oy + 55 * scale, scale=0.5 * scale)

    # S2: inlined short slanted stroke on the left (68,135) → (58,175).
    steps = 24
    x_head, y_head = 68, 135
    x_tail, y_tail = 58, 175
    w_head, w_tail = 5, 9
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x_head + (x_tail - x_head) * u0
        ya = y_head + (y_tail - y_head) * u0
        xb = x_head + (x_tail - x_head) * u1
        yb = y_head + (y_tail - y_head) * u1
        w = max(1, int(round((w_head + (w_tail - w_head) * u0) * scale)))
        pa = _apply(xa, ya, ox, oy, scale)
        pb = _apply(xb, yb, ox, oy, scale)
        t.line([pa, pb], fill="black", width=w)
