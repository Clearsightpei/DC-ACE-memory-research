# ji_char.py — 几 character. Alias for ji radical with recentering.
# PASSed at p3_char_0021_几 (B3 pos 178).
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from ji import draw_ji  # noqa: E402


def draw_ji_char(draw, ox=0, oy=0, scale=1.0):
    draw_ji(draw, ox=ox - 10 * scale, oy=oy + 28 * scale, scale=1.0 * scale)
