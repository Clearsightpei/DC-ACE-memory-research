# you_char.py — 又 character. Alias for you radical at scale=1.15, oy=-5.
# PASSed at p3_char_0017_又 (B3 pos 174).
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from you import draw_you  # noqa: E402


def draw_you_char(t, ox=0, oy=0, scale=1.0):
    draw_you(t, ox=ox, oy=oy - 5 * scale, scale=1.15 * scale)
