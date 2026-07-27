"""p3_char_0010_丩 (jiū) — G3 coord-bank attempt (revision 1).

Rev-1 diagnosis vs GT:
  - Left stroke should be ONE continuous form starting from a small
    down-right entry tick then flowing as a smooth vertical that hooks
    right at the bottom (竖折). My first attempt's entry segment read
    as a separate stroke — merge it into the bezier so the shape is
    one continuous "J" with the tick at the top-left.
  - Right stroke: the top nub should read as a small down-turning
    hook (like the top of a 竖钩 reversed) — needs slightly more
    horizontal extent so it doesn't look like an accidental dot.
  - Overall: left stroke needs to be TALLER (top starts higher),
    matching GT proportions.
"""

import sys, os
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)
from _shared_helpers import to_px, tapered_bezier, tapered_line  # noqa

CANVAS = 300

img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
draw = ImageDraw.Draw(img)


def draw_jiu(draw, ox=0, oy=0, scale=1.0):
    """Draw 丩 centered at (ox, oy) with given scale.

    Math coords (center origin, +y up). Widths in px.

    Two-stroke composition:
      1. LEFT stroke: 竖折 as ONE bezier — top nub curls down-right
         from upper-left tip, becomes vertical, then hooks right at
         bottom forming the bowl.
      2. RIGHT stroke: small down-turning 横撇-style hook at top,
         then long vertical descending to bottom.
    """
    s = scale

    # ---- LEFT STROKE (single continuous 竖折 as two bezier segments) ----
    # Top: small entry tick (upper-left) blending into the vertical.
    L_top = (ox + -50 * s, oy + 45 * s)      # upper-left start
    L_knee = (ox + -35 * s, oy + 25 * s)     # tick lands into shaft
    tapered_line(draw, L_top, L_knee, 5 * s, 8 * s, n=20)

    # Vertical descent as bezier with slight rightward curve.
    L_shaft_top = L_knee
    L_shaft_ctrl = (ox + -32 * s, oy + -25 * s)
    L_shaft_end = (ox + -28 * s, oy + -60 * s)
    tapered_bezier(draw, L_shaft_top, L_shaft_ctrl, L_shaft_end,
                   9 * s, 9 * s, n=32)

    # Bottom hook: bowl of the 折 — curves right and slightly up.
    L_bowl_ctrl = (ox + -15 * s, oy + -75 * s)
    L_bowl_end = (ox + 12 * s, oy + -65 * s)
    tapered_bezier(draw, L_shaft_end, L_bowl_ctrl, L_bowl_end,
                   9 * s, 7 * s, n=32)

    # ---- RIGHT STROKE: top down-turn hook + long vertical ----
    # Top hook: starts upper-right, curves down-and-left into the
    # top of the vertical shaft.
    R_top = (ox + 48 * s, oy + 78 * s)       # upper-right tip
    R_ctrl = (ox + 42 * s, oy + 72 * s)      # curve knee
    R_shaft_top = (ox + 38 * s, oy + 55 * s) # top of vertical
    tapered_bezier(draw, R_top, R_ctrl, R_shaft_top,
                   5 * s, 9 * s, n=28)

    # Long vertical shaft — descends well below the left stroke's
    # bottom, ending near lower canvas.
    R_shaft_end = (ox + 36 * s, oy + -100 * s)
    tapered_line(draw, R_shaft_top, R_shaft_end, 9 * s, 7 * s, n=40)


# Slightly left of canvas center to match GT bias.
draw_jiu(draw, ox=-5, oy=0, scale=1.0)

out_path = os.path.join(_HERE, "01_丩.png")
img.save(out_path)
print(f"Saved: {out_path}")
