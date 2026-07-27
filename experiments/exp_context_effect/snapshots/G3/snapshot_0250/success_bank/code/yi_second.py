# yi_second.py — 乙 (yǐ) character. Identity alias for yi_radical.
# PASSed at p3_char_0003_乙 (B3 pos 161).
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from yi_radical import draw_yi_radical  # noqa: E402


def draw_yi_second(t, ox=0, oy=0, scale=1.0):
    draw_yi_radical(t, ox=ox, oy=oy, scale=scale)
