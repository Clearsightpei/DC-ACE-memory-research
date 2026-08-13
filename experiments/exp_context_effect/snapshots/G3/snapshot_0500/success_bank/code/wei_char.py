# wei_char.py — 囗 (wéi) char, 3 strokes. Identity alias of wei_radical.
# PASSed at p3_char_0066_囗 (B4).
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from wei_radical import draw_wei_radical  # noqa: E402


def draw_wei_char(t, ox=0, oy=0, scale=1.0):
    draw_wei_radical(t, ox=ox, oy=oy, scale=scale)
