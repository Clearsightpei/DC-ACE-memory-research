# er_ren_char.py — 儿 character. Alias for er_ren radical at scale=1.3, oy=-5.
# PASSed at p3_char_0019_儿 (B3 pos 176).
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from er_ren import draw_er_ren  # noqa: E402


def draw_er_ren_char(t, ox=0, oy=0, scale=1.0):
    draw_er_ren(t, ox=ox, oy=oy - 5 * scale, scale=1.3 * scale)
