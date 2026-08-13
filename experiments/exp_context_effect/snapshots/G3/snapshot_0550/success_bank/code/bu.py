# bu.py — 卜 (bu) radical, 2 strokes (竖 + 点 on the right).
# Bootstrap batch (position 45) — human PASSed.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from shu import draw_shu   # noqa: E402
from dian import draw_dian  # noqa: E402


def draw_bu(t, ox=0.0, oy=0.0, scale=1.0):
    """卜 radical: left 竖 + right dian near the shaft's midpoint."""
    draw_shu(t, ox=ox + (-20) * scale, oy=oy + (-30) * scale, scale=0.95 * scale)
    draw_dian(t, ox=ox + 30 * scale,  oy=oy + (-25) * scale, scale=1.1 * scale)
