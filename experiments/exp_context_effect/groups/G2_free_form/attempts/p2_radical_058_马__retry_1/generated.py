"""
p2_radical_058_马 (3画) — G2 retry_1.

Retry fix idea (from errata + new principle 8):
  The prior attempt drew a bottom 横 that FLOATED separately from the body.
  Canonical 马 has the bottom 横 originating at the LEFT edge (aligned with
  stroke-2's left wall) and running rightward THROUGH the terminal hook,
  visually terminating the zig-zag body. It must connect to the body — not
  float underneath it.

3-stroke decomposition (MMH-standard):
  1. 横折 — top box top edge + short right vertical.
  2. 竖折折钩 — left wall of top box, folds into middle 横, folds down into
     a 竖 ending with a small 钩 flick up-and-left.
  3. 一 (long 横) — starts at the LEFT edge aligned with stroke-2's left
     wall, runs rightward THROUGH the terminal hook of stroke 2.

Style: PIL brush-dabs, uniform ~5-6 px radius, shoulder-dabs at 折 corners.
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
    L = math.hypot(x1 - x0, y1 - y0)
    if steps is None:
        steps = max(int(L * 2.5), 8)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ----------------------------------------------------------------------
# Layout — top box occupies upper-middle; body descends to middle; the
# final 横 sits at ~y=210 and starts at the LEFT wall of the body so it
# CONNECTS to the body (not floating below).
# ----------------------------------------------------------------------

# Top box (stroke 1 = 横折 = top edge + short right vertical)
TL = (90, 75)     # top-left corner
TR = (210, 65)    # top-right corner (top 横 tilts up slightly)
BR = (218, 118)   # bottom-right of top box (after short 竖 down from TR)

# Stroke 2 beats (竖折折钩)
S2_TOP = (95, 78)   # start of stroke 2's 竖 (just under TL)
BL     = (100, 122) # end of beat A (bottom of top box, left)
MID_R  = (200, 128) # end of beat B (bottom of top box, right)
HK_BOT = (175, 225) # bottom of beat C (leans slightly left, ends near bottom 横)
HK_TIP = (120, 195) # hook flick tip (up-and-left, ~-140°)

# Stroke 3: final 一 — starts at LEFT edge aligned with body's left wall
# (x≈45, slightly left of BL) and runs THROUGH the hook base area, ending
# past the right edge of the body. Positioned so the hook of stroke 2
# ends near/at this 横 level (visual THROUGH connection).
H_L = (45, 240)
H_R = (275, 235)

R = 5.5
R_SHOULDER = R + 2.5

# ----------------------------------------------------------------------
# Stroke 1: 横折
# ----------------------------------------------------------------------
dab(TL[0], TL[1], R + 1.5)
line_dabs(TL[0], TL[1], TR[0], TR[1], R, R + 0.5)
dab(TR[0], TR[1], R_SHOULDER)
line_dabs(TR[0], TR[1], BR[0], BR[1], R, R)
dab(BR[0], BR[1], R + 1)

# ----------------------------------------------------------------------
# Stroke 2: 竖折折钩
# ----------------------------------------------------------------------
dab(S2_TOP[0], S2_TOP[1], R + 1.5)
# beat A: 竖 down (left wall of top box)
line_dabs(S2_TOP[0], S2_TOP[1], BL[0], BL[1], R, R)
# shoulder at BL
dab(BL[0], BL[1], R_SHOULDER)
# beat B: 横 rightward (middle 横 / bottom of top box)
line_dabs(BL[0], BL[1], MID_R[0], MID_R[1], R, R)
# shoulder at MID_R
dab(MID_R[0], MID_R[1], R_SHOULDER)
# beat C: 竖 down (leans slightly left)
line_dabs(MID_R[0], MID_R[1], HK_BOT[0], HK_BOT[1], R, R)
# hook flick — up-and-left @ ~-140°
line_dabs(HK_BOT[0], HK_BOT[1], HK_TIP[0], HK_TIP[1], R + 0.5, 1.2, steps=80)

# ----------------------------------------------------------------------
# Stroke 3: final 一 (long 横) — CONNECTS to body: starts at left edge
# aligned with body's left wall, runs through/past the terminal hook area.
# ----------------------------------------------------------------------
dab(H_L[0], H_L[1], R + 2)
line_dabs(H_L[0], H_L[1], H_R[0], H_R[1], R, R + 0.5)
dab(H_R[0], H_R[1], R + 2)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_058_马__retry_1/01_马.png")
