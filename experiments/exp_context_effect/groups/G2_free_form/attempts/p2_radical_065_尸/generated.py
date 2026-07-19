"""Render 尸 (radical, 3 strokes) at 300x300, PIL brush-dab technique.

Stroke inventory (per label 尸 = 3画):
  1. 横折  (top): 横 rightward, shoulder, short 竖 down. Blunt end (no hook).
  2. 横    (middle): shorter horizontal inside the 尸 body, ending near the
     竖 of stroke 1 (joins the interior — creates the classic 尸 middle bar).
  3. 撇    (long left-throw): starts at the top-left corner (SAME point as
     stroke 1's start — shared joint per compound-radical rule) and sweeps
     down-and-left to the lower-left of the canvas.

Standalone-scale calibration: canvas 300x300 is standalone, so
- larger curvature on the 撇,
- smaller 顿 dabs (r=6..8) at endpoints, only r+2 at real shoulders,
- 撇 length long, tapering to a sharp tip.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(p0, p1, r0, r1, steps=None):
    x0, y0 = p0
    x1, y1 = p1
    if steps is None:
        steps = max(60, int(math.hypot(x1 - x0, y1 - y0) * 2.5))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=400):
    x0, y0 = p0
    xc, yc = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * xc + t ** 2 * x2
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * yc + t ** 2 * y2
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ---------------------------------------------------------------
# Stroke 1: 横折 (top)
#   横 from top-left corner (60, 80) rightward, slight up-tilt to (220, 72),
#   shoulder dab at (220, 72), 竖 down to (208, 165). Blunt end.
# ---------------------------------------------------------------
r_body = 5.0

TL = (60, 78)                # top-left corner (shared with 撇 start)
TR = (222, 70)               # top-right shoulder
BR = (212, 168)              # bottom-right of vertical

# subtle start seat (NOT a big 顿 ball; standalone-scale)
dab(TL[0], TL[1], r_body + 1)
# 横 rightward, slight up-tilt
line_dabs(TL, TR, r_body, r_body + 0.3)
# shoulder press (real 折 shoulder — keep r+2, moderate)
dab(TR[0], TR[1], r_body + 2)
# 竖 downward
line_dabs(TR, BR, r_body + 0.3, r_body)
# blunt terminal, small
dab(BR[0], BR[1], r_body + 0.5)


# ---------------------------------------------------------------
# Stroke 2: middle 横
#   Short horizontal inside the 尸 body. In GT it starts a bit right of
#   the 撇 shaft and runs right, joining/near the 竖 of stroke 1.
#   From ~(95, 135) to (210, 130). Blunt small terminal press.
# ---------------------------------------------------------------
M_L = (95, 138)
M_R = (208, 133)

dab(M_L[0], M_L[1], r_body + 0.5)
line_dabs(M_L, M_R, r_body - 0.3, r_body - 0.3)
dab(M_R[0], M_R[1], r_body + 0.5)


# ---------------------------------------------------------------
# Stroke 3: long 撇
#   Shares the top-left corner (TL) with stroke 1.
#   Bezier from TL down-and-left to (35, 270), with control point pulled
#   toward the interior/right of the chord for the characteristic bow.
#   Thick -> thin.
# ---------------------------------------------------------------
PIE_P0 = TL             # shared joint with stroke 1 start
PIE_P2 = (32, 275)
PIE_CTRL = (105, 205)   # bow: pulled interior/right (pronounced, standalone-scale)

# subtle joint seat (avoid balling — shared corner already has r+1 from stroke 1)
bezier_dabs(PIE_P0, PIE_CTRL, PIE_P2, r_body + 3, 1.2, steps=550)


img.save("01_尸.png")
print("saved 01_尸.png")
