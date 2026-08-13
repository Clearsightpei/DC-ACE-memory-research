# ding_char.py — 丁 (dīng), 2 strokes: heng + shu_gou.
# PASSed at p3_char_0035_丁 (B4). TR1-3 composition of two bank primitives.
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from heng import draw_heng      # noqa: E402
from shu_gou import draw_shu_gou  # noqa: E402


def draw_ding_char(t, ox=0, oy=0, scale=1.0):
    # Top heng
    draw_heng(t, ox=ox + 0 * scale, oy=oy + 60 * scale, scale=0.85 * scale)
    # Central shu_gou descending from beneath heng center
    draw_shu_gou(t, ox=ox + 0 * scale, oy=oy - 10 * scale, scale=0.85 * scale)
