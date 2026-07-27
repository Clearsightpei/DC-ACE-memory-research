# xiao_char.py — 小 (xiǎo), 3 strokes.
# PASSed at p3_char_0057_小 (B4). Identity alias of xiao radical.
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from xiao import draw_xiao  # noqa: E402


def draw_xiao_char(t, ox=0, oy=0, scale=1.0):
    draw_xiao(t, ox=ox, oy=oy, scale=scale)
