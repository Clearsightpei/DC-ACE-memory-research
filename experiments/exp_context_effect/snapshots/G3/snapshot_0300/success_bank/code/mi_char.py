# mi_char.py — 冖 character. Identity alias for mi_radical.
# PASSed at p3_char_0028_冖 (B3 pos 185).
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from mi_radical import draw_mi_radical  # noqa: E402


def draw_mi_char(draw, ox=0, oy=0, scale=1.0):
    draw_mi_radical(draw, ox=ox, oy=oy, scale=scale)
