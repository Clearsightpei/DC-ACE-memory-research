# er.py — 二 (er, "two") radical, 2 strokes (upper shorter 横 + lower longer 横).
# Bootstrap batch (position 50) — human PASSed.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from heng import draw_heng  # noqa: E402


def draw_er(t, ox=0.0, oy=0.0, scale=1.0):
    """二 radical: upper 横 (scale 0.55) + lower 横 (scale 0.90)."""
    draw_heng(t, ox=ox + 0, oy=oy + 45 * scale, scale=0.55 * scale)
    draw_heng(t, ox=ox + 0, oy=oy + (-80) * scale, scale=0.90 * scale)
