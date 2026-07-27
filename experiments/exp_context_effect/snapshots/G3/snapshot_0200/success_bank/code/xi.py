# xi.py — 夕 (xī, evening), 3 strokes.
# Batch B2 (position 107) — human PASSed.
# Composition: short 撇 + 横折撇 (inline as 2 continuous bezier arcs) +
# 点. TR8 inline-fresh for outer sweep (avoid heng_pie flattening the belly).

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _shared_helpers import tapered_bezier  # noqa: E402
from dian import draw_dian                  # noqa: E402


def draw_xi(t, ox=0.0, oy=0.0, scale=1.0):
    """夕 radical (3 strokes)."""
    def T(p):  # apply ox/oy/scale to math-coord point
        return (p[0] * scale + ox, p[1] * scale + oy)
    # Stroke 1: short 撇
    tapered_bezier(t, T((-10, 75)), T((-35, 40)), T((-65, 5)),
                   w_head=9 * scale, w_tail=2 * scale, n=40)
    # Stroke 2 (arc A): rounded top-right
    tapered_bezier(t, T((-10, 80)), T((30, 90)), T((45, 55)),
                   w_head=7 * scale, w_tail=8 * scale, n=30)
    # Stroke 2 (arc B): long descending 撇
    tapered_bezier(t, T((45, 55)), T((30, -35)), T((-60, -115)),
                   w_head=8 * scale, w_tail=2 * scale, n=60)
    # Stroke 3: dot inside
    draw_dian(t, ox=ox - 15 * scale, oy=oy - 20 * scale, scale=0.45 * scale)
