# er_ren.py — 儿 (er, "child legs") radical, 2 strokes.
# Bootstrap batch (position 49) — human PASSed.
#
# Composition: 撇 (left) + 竖弯钩 (right). Bank primitives with radical
# scales and deliberate offsets that place the 撇 head just left of the
# 竖弯钩 shaft top.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from pie import draw_pie                     # noqa: E402
from shu_wan_gou import draw_shu_wan_gou     # noqa: E402


def draw_er_ren(t, ox=0.0, oy=0.0, scale=1.0):
    """儿 radical: 撇 (left) + 竖弯钩 (right)."""
    draw_pie(t, ox=ox + (-65) * scale, oy=oy + (-22) * scale, scale=0.90 * scale)
    draw_shu_wan_gou(t, ox=ox + 22 * scale, oy=oy + (-15) * scale, scale=0.85 * scale)
