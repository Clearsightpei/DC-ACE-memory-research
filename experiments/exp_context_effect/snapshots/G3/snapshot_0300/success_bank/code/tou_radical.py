# tou_radical.py — 亠 (tou, "lid") radical, 2 strokes (点 + 一).
# Batch B1 (position 65) — human PASSed.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from dian import draw_dian  # noqa: E402
from heng import draw_heng  # noqa: E402


def draw_tou_radical(t, ox=0.0, oy=0.0, scale=1.0):
    """亠 radical: small 点 on top + wide 一 lid below."""
    draw_dian(t, ox=ox + 0, oy=oy + 45 * scale, scale=0.6 * scale)
    draw_heng(t, ox=ox + 0, oy=oy + (-15) * scale, scale=0.90 * scale)
