# mian_char.py — 宀 (mián), 3 strokes. Identity alias of bao_gai_tou.
# PASSed at p3_char_0080_宀 (B4).
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from bao_gai_tou import draw_bao_gai_tou  # noqa: E402


def draw_mian_char(t, ox=0, oy=0, scale=1.0):
    draw_bao_gai_tou(t, ox=ox, oy=oy, scale=scale)
