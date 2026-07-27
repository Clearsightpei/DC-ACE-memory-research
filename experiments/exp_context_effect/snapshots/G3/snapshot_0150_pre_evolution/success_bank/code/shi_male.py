# shi_male.py — 士 (shi, "scholar") radical, 3 strokes.
# Batch B1 (position 99) — human PASSed.
#
# Pure composition of bank heng/shu — distinguishing feature vs 土:
# top 横 is LONGER than bottom 横.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from heng import draw_heng  # noqa: E402
from shu import draw_shu    # noqa: E402


def draw_shi_male(t, ox=0.0, oy=0.0, scale=1.0):
    """士 radical: long top 横 + middle 竖 + short bottom 横."""
    draw_heng(t, ox=ox + 4 * scale, oy=oy + 25 * scale, scale=0.96 * scale)
    draw_shu(t, ox=ox + 4 * scale, oy=oy + (-18) * scale, scale=0.76 * scale)
    draw_heng(t, ox=ox + 4 * scale, oy=oy + (-100) * scale, scale=0.60 * scale)
