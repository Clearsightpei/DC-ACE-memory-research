# shou_pang.py — 扌 (shou-pang, "hand" side radical), 3 strokes.
# Batch B1 (position 100) — human PASSed.
#
# Pure composition: bank heng + bank shu_gou + bank ti.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from heng import draw_heng          # noqa: E402
from shu_gou import draw_shu_gou    # noqa: E402
from ti import draw_ti              # noqa: E402


def draw_shou_pang(t, ox=0.0, oy=0.0, scale=1.0):
    """扌 radical: short 横 top + long 竖钩 shaft + 提 rising across shaft."""
    draw_heng(t, ox=ox + (-5) * scale, oy=oy + 55 * scale, scale=0.33 * scale)
    draw_shu_gou(t, ox=ox + 10 * scale, oy=oy + (-5) * scale, scale=0.95 * scale)
    draw_ti(t, ox=ox + (-8) * scale, oy=oy + (-25) * scale, scale=0.32 * scale)
