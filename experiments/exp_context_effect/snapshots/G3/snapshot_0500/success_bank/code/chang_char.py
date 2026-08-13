# chang_char.py — 厂 character. Identity alias for chang radical.
# PASSed at p3_char_0031_厂 (B3 pos 188).
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from chang import draw_chang  # noqa: E402


def draw_chang_char(t, ox=0, oy=0, scale=1.0):
    draw_chang(t, ox=ox, oy=oy, scale=scale)
