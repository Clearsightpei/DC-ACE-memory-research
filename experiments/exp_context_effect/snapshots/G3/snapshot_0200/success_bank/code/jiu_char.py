# jiu_char.py — 丩 (jiū), 2 strokes. Continuous 竖折 left + top-hook shaft right.
# PASSed at p3_char_0010_丩 (B3 pos 167).
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from _shared_helpers import to_px, tapered_bezier, tapered_line  # noqa: E402


def draw_jiu_char(draw, ox=-5, oy=0, scale=1.0):
    """Draw 丩. Math coords (+y up). Two continuous strokes."""
    s = scale
    L_top = (ox + -50 * s, oy + 45 * s)
    L_knee = (ox + -35 * s, oy + 25 * s)
    tapered_line(draw, L_top, L_knee, 5 * s, 8 * s, n=20)
    L_shaft_top = L_knee
    L_shaft_ctrl = (ox + -32 * s, oy + -25 * s)
    L_shaft_end = (ox + -28 * s, oy + -60 * s)
    tapered_bezier(draw, L_shaft_top, L_shaft_ctrl, L_shaft_end, 9 * s, 9 * s, n=32)
    L_bowl_ctrl = (ox + -15 * s, oy + -75 * s)
    L_bowl_end = (ox + 12 * s, oy + -65 * s)
    tapered_bezier(draw, L_shaft_end, L_bowl_ctrl, L_bowl_end, 9 * s, 7 * s, n=32)
    R_top = (ox + 48 * s, oy + 78 * s)
    R_ctrl = (ox + 42 * s, oy + 72 * s)
    R_shaft_top = (ox + 38 * s, oy + 55 * s)
    tapered_bezier(draw, R_top, R_ctrl, R_shaft_top, 5 * s, 9 * s, n=28)
    R_shaft_end = (ox + 36 * s, oy + -100 * s)
    tapered_line(draw, R_shaft_top, R_shaft_end, 9 * s, 7 * s, n=40)
