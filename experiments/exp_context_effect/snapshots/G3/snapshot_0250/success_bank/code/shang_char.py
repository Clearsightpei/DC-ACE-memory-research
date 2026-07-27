# shang_char.py — 上 (shàng), 3 strokes: 竖 + short-横 + long-横.
# PASSed at p3_char_0045_上 (B4).
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from shu import draw_shu    # noqa: E402
from heng import draw_heng  # noqa: E402


def draw_shang_char(t, ox=0, oy=0, scale=1.0):
    # Bottom long heng
    draw_heng(t, ox=ox + 0 * scale, oy=oy - 80 * scale, scale=1.05 * scale)
    # Vertical shu, slightly left of center
    draw_shu(t, ox=ox - 20 * scale, oy=oy + 5 * scale, scale=0.75 * scale)
    # Short mid heng, shifted right
    draw_heng(t, ox=ox + 20 * scale, oy=oy - 8 * scale, scale=0.55 * scale)
