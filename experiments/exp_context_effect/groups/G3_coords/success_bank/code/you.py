# you.py — 又 (you) radical, 2 strokes (横撇 + 捺, crossing X-shape).
# Batch B1 (position 69) — human PASSed.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from heng_pie import draw_heng_pie  # noqa: E402
from na import draw_na              # noqa: E402


def draw_you(t, ox=0.0, oy=0.0, scale=1.0):
    """又 radical: 横撇 (top-horiz + down-left) + 捺 crossing through it."""
    # Stroke 1: 横撇 at (0, +10) scale 0.85.
    draw_heng_pie(t, ox=ox + 0, oy=oy + 10 * scale, scale=0.85 * scale)
    # Stroke 2: 捺 at (+22, -28) scale 0.75 — head on the 撇 shaft.
    draw_na(t, ox=ox + 22 * scale, oy=oy + (-28) * scale, scale=0.75 * scale)
