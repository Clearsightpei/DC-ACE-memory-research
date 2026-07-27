# la_char.py — 乚 character. Alias for ya_radical at scale=1.5, ox=15, oy=-5.
# PASSed at p3_char_0006_乚 (B3 pos 164).
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from ya_radical import draw_ya_radical  # noqa: E402


def draw_la_char(t, ox=0, oy=0, scale=1.0):
    draw_ya_radical(t, ox=ox + 15 * scale, oy=oy - 5 * scale, scale=1.5 * scale)
