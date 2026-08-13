# wu_char.py — 兀 (wù), 3 strokes: top 一 + 儿.
# PASSed at p3_char_0058_兀 (B4). NOTE: the radical 兀 is still in errata
# (retry_1 FAIL); this char version PASSed with different scaling.
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from heng import draw_heng      # noqa: E402
from er_ren import draw_er_ren  # noqa: E402


def draw_wu_char(t, ox=0, oy=0, scale=1.0):
    draw_heng(t, ox=ox, oy=oy + 55 * scale, scale=0.85 * scale)
    draw_er_ren(t, ox=ox, oy=oy - 10 * scale, scale=0.95 * scale)
