# chu_char.py — 亍 (chù), 3 strokes: short top 横 + wide mid 横 + 亅.
# PASSed at p3_char_0050_亍 (B4).
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from heng import draw_heng          # noqa: E402
from jue_char import draw_jue_char  # noqa: E402


def draw_chu_char(t, ox=0, oy=0, scale=1.0):
    draw_heng(t, ox=ox - 5, oy=oy + 75 * scale, scale=0.50 * scale)
    draw_heng(t, ox=ox + 0, oy=oy + 25 * scale, scale=0.95 * scale)
    draw_jue_char(t, ox=ox - 20, oy=oy - 70, scale=1.0 * scale)
