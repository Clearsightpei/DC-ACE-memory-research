# dian_char.py — 丶 character. dian_radical at scale=1.15.
# PASSed at p3_char_0004_丶 (B3 pos 162).
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from dian_radical import draw_dian_radical  # noqa: E402


def draw_dian_char(t, ox=0, oy=0, scale=1.0):
    draw_dian_radical(t, ox=ox, oy=oy, scale=1.15 * scale)
