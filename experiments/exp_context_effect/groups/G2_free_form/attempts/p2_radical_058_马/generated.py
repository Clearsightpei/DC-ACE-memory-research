"""
p2_radical_058_马 (3画) — G2 attempt.

3-stroke decomposition (MMH-standard):
  1. 横折 — top rectangle's top edge + right side (short 横 then 折 to short 竖).
  2. 竖折折钩 — left vertical of top box, folding into middle 横 (bottom of top
     box), then folding down into a 竖 that ends with a 钩 flick up-left.
  3. 一 (long 横) — the long horizontal crossing through the bottom.

Style: PIL brush-dabs, uniform ~5-6 px radius, shoulder-dabs at 折 corners.
Standalone-scale on 300×300 → dabs modest (r+1 at plain ends, r+2 at 折
corners and stroke-starts).

Image coords (y grows DOWN).
"""

import math
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    """Straight line as brush-dabs with linear radius ramp."""
    L = math.hypot(x1 - x0, y1 - y0)
    if steps is None:
        steps = max(int(L * 2.5), 8)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=140):
    """Quadratic Bezier as short line segments with per-segment width."""
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)
        pts.append((x, y, r))
    return pts


# ----------------------------------------------------------------------
# Layout — target roughly matches the GT: top box occupies upper-middle,
# hook extends to lower-middle, final 横 sits at ~y=245 spanning wide.
# ----------------------------------------------------------------------

# Top box corners  (stroke 1 = 横折 forms top + right side of upper box)
TL = (85, 75)     # top-left corner
TR = (205, 65)    # top-right corner (top 横 tilts up slightly)
BR = (215, 120)   # bottom-right of top box (after short 竖 down from TR)

# Stroke 2's beats (竖折折钩)
S2_TOP = (90, 82)   # just under TL — start of stroke 2's 竖
BL     = (95, 125)  # bottom-left of top box (end of beat A)
MID_R  = (200, 130) # right end of middle 横 (end of beat B)
HK_BOT = (190, 210) # bottom of the descending 竖 with hook
HK_TIP = (140, 178) # hook flick end (up-and-left, longer flick)

# Final 一 (long 横)
H_L = (50, 245)
H_R = (275, 240)

R = 5.5   # base stroke radius
R_SHOULDER = R + 2.5

# ----------------------------------------------------------------------
# Stroke 1: 横折 — short top 横 (TL → TR) then 折 into short 竖 (TR → BR)
# ----------------------------------------------------------------------

# Top 横 with 顿-dab at start
dab(TL[0], TL[1], R + 1.5)
line_dabs(TL[0], TL[1], TR[0], TR[1], R, R + 0.5)
# Shoulder dab at TR
dab(TR[0], TR[1], R_SHOULDER)
# Short 竖 down to BR
line_dabs(TR[0], TR[1], BR[0], BR[1], R, R)
# Blunt terminal press
dab(BR[0], BR[1], R + 1)

# ----------------------------------------------------------------------
# Stroke 2: 竖折折钩
#   beat A: 竖  TL2 → BL         (left side of top box)
#   beat B: 横  BL → BR2         (bottom of top box, the middle 横)
#   beat C: 竖  BR2 → HK_BOT     (drop down)
#   flick : hook HK_BOT → HK_TIP  (up-and-left)
# ----------------------------------------------------------------------

# 顿-dab at start (top of left vertical)
dab(S2_TOP[0], S2_TOP[1], R + 1.5)
# beat A: 竖 down (left side of top box)
line_dabs(S2_TOP[0], S2_TOP[1], BL[0], BL[1], R, R)
# shoulder at BL
dab(BL[0], BL[1], R_SHOULDER)
# beat B: 横 rightward across bottom of top box, ends past BR to make a
# clear second belly (this middle 横 is the visual signature of 马)
line_dabs(BL[0], BL[1], MID_R[0], MID_R[1], R, R)
# shoulder at MID_R
dab(MID_R[0], MID_R[1], R_SHOULDER)
# beat C: drop down — slight leftward lean into vertical to HK_BOT
line_dabs(MID_R[0], MID_R[1], HK_BOT[0], HK_BOT[1], R, R)
# hook flick — longer, angled ~-140° (up-and-left), sharp taper
line_dabs(HK_BOT[0], HK_BOT[1], HK_TIP[0], HK_TIP[1], R + 0.5, 1.2, steps=80)

# ----------------------------------------------------------------------
# Stroke 3: final 一 (long 横) — spans wide with slight up-tilt.
# ----------------------------------------------------------------------

dab(H_L[0], H_L[1], R + 2)   # 顿-dab at start
line_dabs(H_L[0], H_L[1], H_R[0], H_R[1], R, R + 0.5)
dab(H_R[0], H_R[1], R + 2)   # terminal press

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_058_马/01_马.png")
