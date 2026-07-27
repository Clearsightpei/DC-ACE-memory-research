# cun.py — 寸 (cun) radical, 3 strokes (一 + 亅 + 丶).
# Batch B1 (position 77) — human PASSed.
#
# Pure primitive composition — heng, shu_gou, dian from the bank.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from heng import draw_heng          # noqa: E402
from shu_gou import draw_shu_gou    # noqa: E402
from dian import draw_dian          # noqa: E402


def draw_cun(t, ox=0.0, oy=0.0, scale=1.0):
    """寸 radical: heng crossed by shu_gou, dian in lower-left pocket."""
    draw_heng(t, ox=ox + 0, oy=oy + 5 * scale, scale=0.75 * scale)
    draw_shu_gou(t, ox=ox + 15 * scale, oy=oy + (-25) * scale, scale=0.75 * scale)
    draw_dian(t, ox=ox + (-15) * scale, oy=oy + (-35) * scale, scale=0.6 * scale)
