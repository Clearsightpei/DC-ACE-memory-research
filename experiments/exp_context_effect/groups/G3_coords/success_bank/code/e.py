# e.py — 厄 (è), 4 strokes.
# Batch B2 (position 124) — human PASSed.
# 厂 envelope (bank chang) + inner 横折 + inner 竖弯钩 (inlined).

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from chang import draw_chang           # noqa: E402
from _shared_helpers import (          # noqa: E402
    tapered_bezier, tapered_line, to_px,
)


def draw_e(t, ox=0.0, oy=0.0, scale=1.0):
    """厄 radical, 4 strokes."""
    def T(p): return (p[0] * scale + ox, p[1] * scale + oy)
    draw_chang(t, ox=ox, oy=oy, scale=scale)
    # Inner 横折: top horizontal + corner blob + drop
    tapered_line(t, T((-15, 30)), T((55, 30)), 7 * scale, 8 * scale, n=24)
    cx, cy = to_px(T((55, 30))[0], T((55, 30))[1])
    t.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=(0, 0, 0))
    tapered_line(t, T((55, 30)), T((55, -25)), 8 * scale, 7 * scale, n=20)
    # Inner 竖弯钩: shaft + sweep base + hook
    tapered_bezier(t, T((-15, 15)), T((-20, -20)), T((-18, -55)),
                   8 * scale, 9 * scale, n=40)
    tapered_bezier(t, T((-18, -55)), T((25, -78)), T((55, -70)),
                   9 * scale, 8 * scale, n=48)
    tapered_line(t, T((55, -70)), T((42, -50)), 8 * scale, 2 * scale, n=16)
