# dai.py — 歹 (dǎi), 4 strokes.
# Batch B2 (position 122) — human PASSed.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from dian import draw_dian  # noqa: E402

CANVAS = 300


def _to_pixel(ox, oy):
    return (CANVAS / 2 + ox, CANVAS / 2 - oy)


def _stamp(d, prev, p, w):
    wi = max(1, int(round(w)))
    d.line([prev, p], fill=(0, 0, 0), width=wi)
    r = w / 2.0
    d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=(0, 0, 0))


def _line(d, p0, p1, w0, w1, n=30):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = p0[0] + (p1[0] - p0[0]) * u
        by = p0[1] + (p1[1] - p0[1]) * u
        p = _to_pixel(bx, by)
        w = w0 + (w1 - w0) * u
        if prev is not None:
            _stamp(d, prev, p, w)
        prev = p


def _bez(d, p0, p1, p2, w_head, w_tail, n=48):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        p = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        if prev is not None:
            _stamp(d, prev, p, w)
        prev = p


def draw_dai(t, ox=0.0, oy=0.0, scale=1.0):
    """歹 radical, 4 strokes."""
    # Top heng: math (-80,95) -> (70,105)
    _line(t, (-80, 95), (70, 105), 8, 8, n=40)
    # Short pie (attaches under mid-left of heng)
    _bez(t, (-40, 90), (-53, 67), (-65, 40), w_head=6.5, w_tail=1.0)
    # 横撇 composite: short heng + corner blob + long pie
    _line(t, (-25, 65), (50, 72), 7, 6.5, n=30)
    cx, cy = _to_pixel(52, 68)
    t.ellipse([cx - 5, cy - 5, cx + 6, cy + 6], fill=(0, 0, 0))
    _bez(t, (52, 63), (-5, 0), (-50, -75), w_head=9, w_tail=1)
    # Interior dian
    draw_dian(t, ox=7.0, oy=33.0, scale=0.4)
