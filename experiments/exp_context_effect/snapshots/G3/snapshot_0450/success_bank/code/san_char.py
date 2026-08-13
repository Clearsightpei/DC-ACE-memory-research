# san_char.py — 三 (sān), 3 hengs: short top / short mid / long bottom.
# PASSed at p3_char_0055_三 (B4). draw_yi.length_px varies per stroke.
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from yi import draw_yi  # noqa: E402


def draw_san_char(t, ox=0, oy=0, scale=1.0):
    try:
        draw_yi(t, ox=ox, oy=oy + 65 * scale, scale=0.85 * scale, length_px=95)
        draw_yi(t, ox=ox, oy=oy, scale=0.80 * scale, length_px=80)
        draw_yi(t, ox=ox, oy=oy - 90 * scale, scale=1.00 * scale, length_px=180)
    except TypeError:
        # Fallback if draw_yi doesn't accept length_px.
        draw_yi(t, ox=ox, oy=oy + 65 * scale, scale=0.55 * scale)
        draw_yi(t, ox=ox, oy=oy, scale=0.45 * scale)
        draw_yi(t, ox=ox, oy=oy - 90 * scale, scale=1.00 * scale)
