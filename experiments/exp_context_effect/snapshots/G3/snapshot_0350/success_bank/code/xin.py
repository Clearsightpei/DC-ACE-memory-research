# xin.py — 心 (xīn, heart), 4 strokes.
# PASSed at p2_radical_126_心 (B3 pos 153, 2026-07-22).
# Composition: wo_gou bowl + three tapered dots (left, mid, right).
# Math coords (center origin, +y up); (ox, oy, scale) shift/scale bowl.
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from wo_gou import draw_wo_gou  # noqa: E402

CANVAS = 300


def _to_pixel(ox, oy):
    return (CANVAS / 2 + ox, CANVAS / 2 - oy)


def _tb(draw, p0, p1, p2, w0, w1, n=32):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        pt = _to_pixel(bx, by)
        if prev is not None:
            w = w0 * (1 - u) + w1 * u
            wi = max(1, int(round(w)))
            draw.line([prev, pt], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))
        prev = pt


def draw_xin(d, ox=0, oy=0, scale=1.0):
    """Draw 心. Bowl uses wo_gou; three dots inlined."""
    draw_wo_gou(d, ox=ox - 5, oy=oy - 20, scale=0.85 * scale)
    # Left dot (mirrored)
    _tb(d, (ox + -75, oy + 5), (ox + -82, oy + -8), (ox + -92, oy + -28), 2, 8)
    # Middle dot
    _tb(d, (ox + -15, oy + 25), (ox + -10, oy + 18), (ox + -2, oy + 8), 2, 7)
    # Right dot
    _tb(d, (ox + 55, oy + 40), (ox + 50, oy + 25), (ox + 42, oy + 8), 8, 2)
