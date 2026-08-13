# cao_char.py — 艹 (cǎo) char, 3 strokes. Identity alias of cao_zi_tou.
# PASSed at p3_char_0078_艹 (B4).
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from cao_zi_tou import draw_cao_zi_tou  # noqa: E402


def draw_cao_char(t, ox=0, oy=0, scale=1.0):
    draw_cao_zi_tou(t, ox=ox, oy=oy, scale=scale)
