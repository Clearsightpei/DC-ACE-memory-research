# pie_char.py — 丿 character, 2 strokes (thin uniform lines).
# PASSed at p3_char_0005_丿 (B3 pos 163).
# GT was MMH-median-style: thin uniform ~3-4 px, not brush profile.
# Uses variant_pie for both strokes at thin widths.
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from _shared_helpers import variant_pie  # noqa: E402


def draw_pie_char(draw, ox=0, oy=0, scale=1.0):
    variant_pie(draw,
                head=(ox + 5 * scale, oy + 70 * scale),
                tail=(ox + -65 * scale, oy + -115 * scale),
                bow_perp=-10.0 * scale, w_head=4.0 * scale, w_tail=2.0 * scale, n=60)
    variant_pie(draw,
                head=(ox + 30 * scale, oy + 50 * scale),
                tail=(ox + 65 * scale, oy + -20 * scale),
                bow_perp=-2.0 * scale, w_head=4.0 * scale, w_tail=2.0 * scale, n=36)
