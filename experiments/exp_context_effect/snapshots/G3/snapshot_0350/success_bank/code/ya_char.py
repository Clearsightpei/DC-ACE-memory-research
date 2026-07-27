# ya_char.py — 丫 (yā), 3 strokes: left 撇 + right 短捺 + 竖 (fork shape).
# PASSed at p3_char_0040_丫 (B4). MMH-style thin uniform widths (P12).
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from _shared_helpers import variant_pie, tapered_line  # noqa: E402


def draw_ya_char(t, ox=0, oy=0, scale=1.0):
    apex = (0 + ox, 0 + oy)
    variant_pie(t, head=(-55 * scale + ox, 55 * scale + oy),
                tail=apex, bow_perp=-4.0, w_head=4.0, w_tail=2.0)
    variant_pie(t, head=(55 * scale + ox, 55 * scale + oy),
                tail=apex, bow_perp=+4.0, w_head=4.0, w_tail=2.0)
    tapered_line(t, apex, (0 + ox, -110 * scale + oy), w0=4.0, w1=4.0)
