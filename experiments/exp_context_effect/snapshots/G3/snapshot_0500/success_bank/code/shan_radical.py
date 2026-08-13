# shan_radical.py — 彡 (shan) radical, 3 strokes (three cascading pies).
# Batch B1 (position 96) — human PASSed.
#
# Pure composition using bank pie at different scales/positions.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from pie import draw_pie  # noqa: E402


def draw_shan_radical(t, ox=0.0, oy=0.0, scale=1.0):
    """彡 radical: three cascading 撇 strokes, each larger and further down-left."""
    draw_pie(t, ox=ox + 20 * scale, oy=oy + 40 * scale, scale=0.32 * scale)
    draw_pie(t, ox=ox + 5 * scale, oy=oy + (-5) * scale, scale=0.38 * scale)
    draw_pie(t, ox=ox + (-10) * scale, oy=oy + (-45) * scale, scale=0.48 * scale)
