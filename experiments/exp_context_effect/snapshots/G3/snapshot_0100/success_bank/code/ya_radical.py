# ya_radical.py — 乚 (ya) radical, 1 stroke.
# Bootstrap batch (position 39) — human PASSed.
# 乚 aliases 竖弯钩 with a small standalone offset. The PASSing render
# placed shu_wan_gou at (ox=-45, oy=-12, scale=1.2).

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402


def draw_ya_radical(t, ox=0.0, oy=0.0, scale=1.0):
    """乚 radical: shu_wan_gou shifted left and scaled 1.2×.

    (ox, oy, scale) compounds the internal canonical placement.
    """
    draw_shu_wan_gou(t,
                     ox=ox + (-45) * scale,
                     oy=oy + (-12) * scale,
                     scale=1.2 * scale)
