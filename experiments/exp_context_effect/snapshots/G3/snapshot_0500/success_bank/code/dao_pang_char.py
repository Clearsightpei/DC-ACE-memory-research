# dao_pang_char.py — 刂 (dāo_pāng char), 2 strokes.
# PASSed at p3_char_0036_刂 (B4). Identity alias of dao_pang radical.
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from dao_pang import draw_dao_pang  # noqa: E402


def draw_dao_pang_char(t, ox=0, oy=0, scale=1.0):
    draw_dao_pang(t, ox=ox, oy=oy, scale=scale)
