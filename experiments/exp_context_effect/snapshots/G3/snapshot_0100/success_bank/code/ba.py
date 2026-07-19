# ba.py — 八 (ba) radical, 2 strokes (pie + na, splayed with a V-notch gap).
# Bootstrap batch (position 41) — human PASSed.
#
# Composed from bank primitives pie and na, each at scale 0.65 with
# deliberate horizontal separation to create the V-notch gap at the top.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from pie import draw_pie  # noqa: E402
from na import draw_na    # noqa: E402


def draw_ba(t, ox=0.0, oy=0.0, scale=1.0):
    """八 radical: splayed 撇 + 捺 with a small V-notch gap at the top."""
    draw_pie(t, ox=ox + (-40) * scale, oy=oy + 5 * scale, scale=0.65 * scale)
    draw_na(t,  ox=ox + 65 * scale,   oy=oy + (-5) * scale, scale=0.65 * scale)
