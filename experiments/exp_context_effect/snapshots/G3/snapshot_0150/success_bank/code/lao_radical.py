# lao_radical.py — 耂 (lǎo, old radical), 4 strokes.
# Batch B2 (position 134) — human PASSed.
# Inline-fresh: 2 hengs + short shu + long sweeping pie.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _shared_helpers import to_px, tapered_bezier  # noqa: E402

CANVAS = 300


def draw_lao_radical(t, ox=0.0, oy=0.0, scale=1.0):
    """耂 radical, 4 strokes."""
    def T(p): return (p[0] * scale + ox, p[1] * scale + oy)
    # Short top heng (cx=-15, cy=50, half_len=32, thickness=7)
    p0 = to_px(*T((-15 - 32, 50)))
    p1 = to_px(*T((-15 + 32, 50)))
    t.line([p0, p1], fill=(0, 0, 0), width=max(1, int(round(7 * scale))))
    # Short shu (cx=-5, y_top=80, y_bot=30)
    p0 = to_px(*T((-5, 80)))
    p1 = to_px(*T((-5, 30)))
    t.line([p0, p1], fill=(0, 0, 0), width=max(1, int(round(7 * scale))))
    # Long tilted lower heng
    p0 = to_px(*T((-110, 8)))
    p1 = to_px(*T((110, 5)))
    t.line([p0, p1], fill=(0, 0, 0), width=max(1, int(round(8 * scale))))
    # Long sweeping 撇 via bezier
    p_head = T((90, 55))
    p_tail = T((-115, -120))
    p_ctrl = ((p_head[0] + p_tail[0]) / 2 - 30 * scale,
              (p_head[1] + p_tail[1]) / 2 - 20 * scale)
    tapered_bezier(t, p_head, p_ctrl, p_tail,
                   9 * scale, 1 * scale, n=100)
