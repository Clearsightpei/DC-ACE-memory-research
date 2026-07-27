# shi_char.py — 十 character. Alias for shi radical at scale=1.1.
# PASSed at p3_char_0013_十 (B3 pos 170).
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from shi import draw_shi  # noqa: E402


def draw_shi_char(d, ox=0, oy=0, scale=1.0):
    draw_shi(d, ox=ox, oy=oy, scale=1.1 * scale)
