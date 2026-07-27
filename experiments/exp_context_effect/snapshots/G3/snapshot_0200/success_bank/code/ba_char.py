# ba_char.py — 八 character. Identity alias for ba primitive.
# PASSed at p3_char_0024_八 (B3 pos 181).
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from ba import draw_ba  # noqa: E402


def draw_ba_char(t, ox=0, oy=0, scale=1.0):
    draw_ba(t, ox=ox, oy=oy, scale=scale)
