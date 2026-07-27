# yi_cross.py — 乂 (yì), 2 strokes: 撇 + 捺 crossing X.
# PASSed at p3_char_0014_乂 (B3 pos 171).
# Uses variant_pie + variant_na from _shared_helpers.
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from _shared_helpers import variant_pie, variant_na  # noqa: E402


def draw_yi_cross(draw, ox=0, oy=0, scale=1.0):
    variant_pie(draw,
                head=(ox + 45 * scale, oy + 65 * scale),
                tail=(ox + -105 * scale, oy + -110 * scale),
                bow_perp=-7.0 * scale, w_head=7.0 * scale, w_tail=1.0 * scale, n=60)
    variant_na(draw,
               head=(ox + -45 * scale, oy + 40 * scale),
               tail=(ox + 100 * scale, oy + -110 * scale),
               bow_perp=6.0 * scale, w_head=2.0 * scale,
               w_belly=10.0 * scale, w_tail=2.0 * scale, belly_u=0.65, n=70)
