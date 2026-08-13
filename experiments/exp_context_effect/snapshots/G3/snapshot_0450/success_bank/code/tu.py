# tu.py — 土 (tǔ, earth), 3 strokes: 横 + 竖 + 横.
# Batch B2 (position 103) — human PASSed.
#
# Visual complement of 士 (shi_male): in 土 the BOTTOM heng is longer.
# Pure primitive composition, TR3-clean.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng   # noqa: E402
from shu import draw_shu     # noqa: E402


def draw_tu(t, ox=0.0, oy=0.0, scale=1.0):
    """土 radical, 3 strokes."""
    draw_heng(t, ox=ox + 0 * scale, oy=oy + 30 * scale, scale=0.60 * scale)
    draw_shu(t, ox=ox + 0 * scale, oy=oy - 12 * scale, scale=0.68 * scale)
    draw_heng(t, ox=ox + 0 * scale, oy=oy - 80 * scale, scale=1.05 * scale)
