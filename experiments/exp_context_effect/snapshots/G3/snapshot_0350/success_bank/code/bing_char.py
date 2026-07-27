# bing_char.py — 冫 character. Alias for bing at (0, +15, 1.0).
# PASSed at p3_char_0030_冫 (B3 pos 187).
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from bing import draw_bing  # noqa: E402


def draw_bing_char(t, ox=0, oy=0, scale=1.0):
    draw_bing(t, ox=ox, oy=oy + 15 * scale, scale=1.0 * scale)
