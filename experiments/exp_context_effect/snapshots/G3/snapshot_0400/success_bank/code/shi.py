# shi.py — 十 (shi, "ten") radical, 2 strokes (横 crossing 竖).
# Batch B1 (position 63) — human PASSed.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from heng import draw_heng  # noqa: E402
from shu import draw_shu    # noqa: E402


def draw_shi(t, ox=0.0, oy=0.0, scale=1.0):
    """十 radical: heng at (0,+10) scale 0.75 crossing shu at (0,-2.5) scale 0.925."""
    draw_heng(t, ox=ox + 0, oy=oy + 10 * scale, scale=0.75 * scale)
    draw_shu(t, ox=ox + 0, oy=oy + (-2.5) * scale, scale=0.925 * scale)
