# shi_ceremony_pang.py — 礻 (shì, spirit/altar side-radical), 4 strokes.
# Batch B2 (position 148) — human PASSed.
# Inline-fresh via math coords.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _shared_helpers import (  # noqa: E402
    to_px, tapered_bezier, tapered_line,
)


def draw_shi_ceremony_pang(t, ox=0.0, oy=0.0, scale=1.0):
    """礻 radical, 4 strokes."""
    def T(p): return (p[0] * scale + ox, p[1] * scale + oy)
    # Stroke 1: top 点
    tapered_bezier(t, T((8, 90)), T((15, 82)), T((24, 68)),
                   2 * scale, 7 * scale, n=25)
    # Stroke 2: 横撇 — heng + corner blob + pie
    tapered_line(t, T((-45, 45)), T((15, 50)), 5 * scale, 8 * scale, n=20)
    bx, by = to_px(*T((15, 50)))
    t.ellipse([bx - 5, by - 5, bx + 5, by + 5], fill=(0, 0, 0))
    tapered_bezier(t, T((15, 50)), T((-15, 20)), T((-45, -20)),
                   8 * scale, 2 * scale, n=30)
    # Stroke 3: long shu
    tapered_line(t, T((2, 30)), T((0, -115)), 7 * scale, 7 * scale, n=30)
    # Stroke 4: right dian
    tapered_bezier(t, T((15, 15)), T((25, 5)), T((38, -15)),
                   2 * scale, 7 * scale, n=25)
