# gun_char.py — 丨 (gǔn) character. Identity alias for gun_radical.
# PASSed at p3_char_0002_丨 (B3 pos 160).
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from gun_radical import draw_gun_radical  # noqa: E402


def draw_gun_char(t, ox=0, oy=0, scale=1.0):
    draw_gun_radical(t, ox=ox, oy=oy, scale=scale)
