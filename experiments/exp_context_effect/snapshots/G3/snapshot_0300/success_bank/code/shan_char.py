# shan_char.py — 山 (shān), 3 strokes. Identity alias of shan radical.
# PASSed at p3_char_0067_山 (B4).
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from shan import draw_shan  # noqa: E402


def draw_shan_char(t, ox=0, oy=0, scale=1.0):
    draw_shan(t, ox=ox, oy=oy, scale=scale)
