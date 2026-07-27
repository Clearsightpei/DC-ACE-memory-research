# er_char.py — 二 character. Alias for er radical at (0, +10, 1.0).
# PASSed at p3_char_0015_二 (B3 pos 172).
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from er import draw_er  # noqa: E402


def draw_er_char(t, ox=0, oy=0, scale=1.0):
    draw_er(t, ox=ox, oy=oy + 10 * scale, scale=1.0 * scale)
