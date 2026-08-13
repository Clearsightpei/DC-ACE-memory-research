# gong.py — 工 (gong) radical, 3 strokes (top 横 + middle 竖 + bottom 横).
# Batch B1 (position 81) — human PASSed.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from heng import draw_heng  # noqa: E402
from shu import draw_shu    # noqa: E402


def draw_gong(t, ox=0.0, oy=0.0, scale=1.0):
    """工 radical: shorter top 横 + short middle 竖 + wider bottom 横."""
    draw_heng(t, ox=ox + 0, oy=oy + 45 * scale, scale=0.55 * scale)
    draw_shu(t, ox=ox + 0, oy=oy + (-12) * scale, scale=0.36 * scale)
    draw_heng(t, ox=ox + 0, oy=oy + (-80) * scale, scale=0.90 * scale)
