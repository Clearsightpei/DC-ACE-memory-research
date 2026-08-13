# yi_char.py — 一 (yī, "one") character. Alias for draw_yi at (0, -45, 1.0).
# PASSed at p3_char_0001_一 (B3 pos 159).
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from yi import draw_yi  # noqa: E402


def draw_yi_char(t, ox=0, oy=0, scale=1.0):
    draw_yi(t, ox=ox, oy=oy - 45 * scale, scale=1.0 * scale)
