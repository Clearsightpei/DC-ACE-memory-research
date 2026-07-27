# xia_char.py — 下 (xià), 3 strokes: 横 + 竖 + 点.
# PASSed at p3_char_0053_下 (B4). Pure bank primitive composition.
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from heng import draw_heng   # noqa: E402
from shu import draw_shu     # noqa: E402
from dian import draw_dian   # noqa: E402


def draw_xia_char(t, ox=0, oy=0, scale=1.0):
    draw_heng(t, ox=ox, oy=oy + 60 * scale, scale=1.05 * scale)
    draw_shu(t, ox=ox - 2 * scale, oy=oy - 30 * scale, scale=0.90 * scale)
    draw_dian(t, ox=ox + 40 * scale, oy=oy + 15 * scale, scale=0.85 * scale)
