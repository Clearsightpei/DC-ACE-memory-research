# dao_pang.py — 刂 (dao pang, "knife" side radical), 2 strokes.
# Bootstrap batch (position 48) — human PASSed.
#
# Composition: short 竖 on the left + 竖钩 on the right.
# Reuses bank primitives shu and shu_gou with radical-position scales.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from shu import draw_shu           # noqa: E402
from shu_gou import draw_shu_gou   # noqa: E402


def draw_dao_pang(t, ox=0.0, oy=0.0, scale=1.0):
    """刂 radical: short left 竖 + right 竖钩."""
    draw_shu(t, ox=ox + (-17) * scale, oy=oy + 12 * scale, scale=0.37 * scale)
    draw_shu_gou(t, ox=ox + 38 * scale, oy=oy + (-5) * scale, scale=0.89 * scale)
