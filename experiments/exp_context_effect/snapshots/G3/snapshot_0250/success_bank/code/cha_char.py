# cha_char.py — 叉 (chā), 3 strokes: 又 + small dian in upper crook.
# PASSed at p3_char_0064_叉 (B4). Alias-plus-decoration pattern.
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from you_char import draw_you_char       # noqa: E402
from _shared_helpers import variant_dian  # noqa: E402


def draw_cha_char(t, ox=0, oy=0, scale=1.0):
    draw_you_char(t, ox=ox, oy=oy, scale=scale)
    variant_dian(t, head=(-30.0 * scale + ox, 40.0 * scale + oy),
                 tail=(+5.0 * scale + ox, 25.0 * scale + oy),
                 w_head=2.0, w_tail=4.0, bow_perp=-1.5, n=32)
