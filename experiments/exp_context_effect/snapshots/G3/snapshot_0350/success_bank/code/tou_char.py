# tou_char.py — 亠 character. Identity alias for tou_radical.
# PASSed at p3_char_0020_亠 (B3 pos 177).
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from tou_radical import draw_tou_radical  # noqa: E402


def draw_tou_char(t, ox=0, oy=0, scale=1.0):
    draw_tou_radical(t, ox=ox, oy=oy, scale=scale)
