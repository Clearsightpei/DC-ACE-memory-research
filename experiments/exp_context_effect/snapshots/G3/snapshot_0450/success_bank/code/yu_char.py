# yu_char.py — 于 (yú), 3 strokes: short top 横 + wide mid 横 + 竖钩.
# PASSed at p3_char_0051_于 (B4).
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from heng import draw_heng          # noqa: E402
from shu_gou import draw_shu_gou    # noqa: E402


def draw_yu_char(t, ox=0, oy=0, scale=1.0):
    draw_heng(t, ox=ox + 8 * scale, oy=oy + 60 * scale, scale=0.50 * scale)
    draw_heng(t, ox=ox + 0, oy=oy + 10 * scale, scale=0.95 * scale)
    draw_shu_gou(t, ox=ox + 5 * scale, oy=oy - 50 * scale, scale=0.85 * scale)
