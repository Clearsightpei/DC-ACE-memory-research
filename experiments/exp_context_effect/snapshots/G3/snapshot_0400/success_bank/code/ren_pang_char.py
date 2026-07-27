# ren_pang_char.py — 亻 character. Identity alias for ren_pang radical.
# PASSed at p3_char_0022_亻 (B3 pos 179).
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from ren_pang import draw_ren_pang  # noqa: E402


def draw_ren_pang_char(t, ox=0, oy=0, scale=1.0):
    draw_ren_pang(t, ox=ox, oy=oy, scale=scale)
