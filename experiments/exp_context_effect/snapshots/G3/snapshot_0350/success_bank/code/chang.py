# chang.py — 厂 (chang) radical, 2 strokes (heng + nearly-vertical pie).
# Batch B1 (position 46) — retry-1 graduation, human PASSed.
#
# heng call reused from bank at scale 0.85; the "pie" is an inlined
# nearly-vertical tapered bezier (bank pie is too diagonal for 厂).

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from heng import draw_heng  # noqa: E402

_CANVAS = 300


def _to_pixel_scaled(bx, by, ox, oy, scale):
    """Math-coord (center origin, +y up) at extra offset (ox,oy), scaled."""
    px = _CANVAS / 2 + ox + bx * scale
    py = _CANVAS / 2 - (oy + by * scale)
    return px, py


def _draw_radical_pie_vertical(t, x0, y0, x1, y1, ctrl_x, ctrl_y,
                               ox, oy, scale,
                               w_head=11.0, w_tail=2.0, n=90):
    """Inlined 丿 for 厂's radical: nearly-vertical descent with a soft
    scoop only near the tail."""
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * ctrl_x + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * ctrl_y + u ** 2 * y1
        px, py = _to_pixel_scaled(bx, by, ox, oy, scale)
        w = (w_head + (w_tail - w_head) * u) * scale
        wi = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def draw_chang(t, ox=0.0, oy=0.0, scale=1.0):
    """厂 radical: wide 横 up top + nearly-vertical 丿 falling from its left tip."""
    # Stroke 1: wide heng at (+5, +70) scale 0.85.
    draw_heng(t, ox=ox + 5 * scale, oy=oy + 70 * scale, scale=0.85 * scale)
    # Stroke 2: inlined nearly-vertical 丿, head at (-80,+65), tail (-105,-105).
    _draw_radical_pie_vertical(
        t,
        x0=-80, y0=+65,
        x1=-105, y1=-105,
        ctrl_x=-100, ctrl_y=-20,
        ox=ox, oy=oy, scale=scale,
        w_head=11.0, w_tail=2.0,
    )
