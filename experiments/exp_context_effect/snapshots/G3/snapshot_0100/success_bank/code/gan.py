# gan.py — 干 (gan) radical, 3 strokes (短横 + 长横 + 竖).
# Batch B1 (position 80) — human PASSed.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from heng import draw_heng  # noqa: E402
from shu import draw_shu    # noqa: E402


def draw_gan(t, ox=0.0, oy=0.0, scale=1.0):
    """干 radical: short top 横 + wide middle 横 + long 竖."""
    draw_heng(t, ox=ox + 5 * scale, oy=oy + 55 * scale, scale=0.55 * scale)
    draw_heng(t, ox=ox + 0, oy=oy + 5 * scale, scale=0.85 * scale)
    draw_shu(t, ox=ox + 0, oy=oy + (-20) * scale, scale=0.75 * scale)
