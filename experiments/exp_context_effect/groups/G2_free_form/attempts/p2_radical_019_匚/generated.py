"""Render 匚 (p2_radical_019_匚) to 01_匚.png.

匚 is a 2画 radical (bracket opening rightward). Stroke order per MMH:
  1) 横 (top horizontal, left→right).
  2) 竖折 (vertical descending on the left, then horizontal going right).

Per drawer_memory:
- Compound radicals share joints (no inset). The top 横 and 竖折's 竖 share
  the top-left corner.
- 折 corner has one shoulder dab (r+3) at the bottom-left joint.
- Standalone-scale: use smaller start-press (r+1 not r+2) and moderate
  curvature. Fill the canvas but leave breathing room.
- Top 横 tilts up 3-5°. Bottom 横 is roughly horizontal (slight up-tilt ok).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

def segment(x0, y0, x1, y1, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)

# Shared top-left corner
TL = (75, 80)
# Shared bottom-left corner (elbow of 竖折)
BL = (75, 240)
# Top-right endpoint (top 横 ends here) — tilt slightly up
TR = (225, 72)
# Bottom-right endpoint (bottom 横 ends here) — tilt slightly up
BR = (235, 235)

R = 5.0
R_PRESS = R + 1.0     # standalone-scale: smaller endpoint press to avoid ball artifacts
R_SHOULDER = R + 3.0  # shoulder press dab at 折 joint (real corner, keep visible)

# --- Stroke 1: top 横 (left → right, slight up-tilt) ---
dab(TL[0], TL[1], R_PRESS)                 # opening 顿
segment(TL[0], TL[1], TR[0], TR[1], R, R)
dab(TR[0], TR[1], R_PRESS)                 # terminal 顿

# --- Stroke 2: 竖折 (vertical down, shoulder, horizontal right) ---
# Vertical segment: TL → BL (shares the top-left corner with the 横)
# (Slight lean not needed — 匚's left side is essentially vertical)
dab(TL[0], TL[1], R_PRESS)                 # start 顿 (shared with 横 corner)
segment(TL[0], TL[1], BL[0], BL[1], R, R)

# Shoulder dab at the 折 joint (bottom-left)
dab(BL[0], BL[1], R_SHOULDER)

# Horizontal segment: BL → BR
segment(BL[0], BL[1], BR[0], BR[1], R, R)
dab(BR[0], BR[1], R_PRESS)                 # blunt terminal press

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_019_匚/01_匚.png")
