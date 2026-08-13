# kou_char.py — 口 (kǒu) char, 3 strokes. Identity alias of kou radical.
# PASSed at p3_char_0071_口 (B4).
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from kou import draw_kou  # noqa: E402


def draw_kou_char(t, ox=0, oy=0, scale=1.0):
    draw_kou(t, ox=ox, oy=oy, scale=scale)
