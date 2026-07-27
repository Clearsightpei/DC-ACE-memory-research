# qu_char.py — 凵 character. Alias for qu_radical at scale=1.05, oy=-15.
# PASSed at p3_char_0032_凵 (B3 pos 189).
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from qu_radical import draw_qu_radical  # noqa: E402


def draw_qu_char(draw, ox=0, oy=0, scale=1.0):
    draw_qu_radical(draw, ox=ox, oy=oy - 15 * scale, scale=1.05 * scale)
