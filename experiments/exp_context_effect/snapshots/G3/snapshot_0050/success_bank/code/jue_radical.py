# jue_radical.py — 亅 (jue) radical, 1 stroke.
# Bootstrap batch (position 34) — human PASSed.
# 亅 aliases 竖钩 (shu_gou). The PASSing render composed shu_gou at
# (ox=+22, oy=-5, scale=0.85). Recorded here as a thin composition
# entry so downstream compositions can invoke draw_jue_radical
# directly with their own (ox, oy, scale).

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from shu_gou import draw_shu_gou  # noqa: E402


def draw_jue_radical(t, ox=0.0, oy=0.0, scale=1.0):
    """Draw 亅 radical: an up-and-left-flicking hook shu.

    Standalone canonical placement: shu_gou at (+22, -5) with scale 0.85.
    (ox, oy, scale) transform is applied on top of that canonical placement.
    """
    draw_shu_gou(t, ox=ox + 22 * scale, oy=oy + (-5) * scale, scale=0.85 * scale)
