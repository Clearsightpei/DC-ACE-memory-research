# jiu_long_char.py — 久 (jiǔ), 3 strokes: top 撇 + 横撇 + long 捺.
# PASSed at p3_char_0046_久 (B4). Uses variant helpers.
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from _shared_helpers import variant_pie, variant_na, tapered_line, to_px  # noqa: E402


def draw_jiu_long_char(t, ox=0, oy=0, scale=1.0):
    def P(x, y):
        return (ox + x * scale, oy + y * scale)
    variant_pie(t, head=P(+5, +105), tail=P(-70, +10),
                bow_perp=-8, w_head=9, w_tail=1)
    tapered_line(t, P(-25, +40), P(+40, +45), w0=5, w1=8)
    cx, cy = to_px(*P(+40, +45))
    r = 5
    t.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))
    variant_pie(t, head=P(+38, +43), tail=P(-70, -50),
                bow_perp=-10, w_head=8, w_tail=1)
    variant_na(t, head=P(-10, -20), tail=P(+105, -125),
               bow_perp=+10, w_head=2, w_belly=14, w_tail=2, belly_u=0.72)
