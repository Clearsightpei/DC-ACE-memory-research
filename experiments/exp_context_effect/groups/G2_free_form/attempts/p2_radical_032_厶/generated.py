"""
p2_radical_032_厶 (2画 radical)

Two strokes:
  1. 撇折 — 撇 throws from upper-right down to lower-left,
     then a 折 shoulder into a short 横 going rightward.
     Together this forms the open-bottom triangular top of 厶.
  2. 点 — a teardrop dot at the lower-right, going down-and-right.

Renderer: PIL brush-dabs (drawer_memory principle).
Canvas: 300x300, white bg, black ink.

Coords: image-coords (y grows DOWN).

Notes vs memory:
  * Standalone radical → curvature more pronounced, smaller 顿 dabs
    at endpoints (r+1, not r+2, per "no visible balls" rule).
  * 撇折: primary 撇 gently bowed (Bezier), joining shoulder dab at
    tip, then short 横 with slight up-tilt.
  * 点: teardrop thin→thick, easing tt=t**1.4.
  * The 撇折's shape is the classic ㄥ-like top; the 点 sits at the
    open bottom-right.
"""

import math
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_stroke(p0, p1, p2, r_start, r_end, steps=400):
    """Quadratic Bezier sampled as brush-dabs with linear radius ramp."""
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def teardrop(p0, p1, r_start, r_end, steps=200, ease=1.4):
    """Straight-line teardrop dot with eased thin→thick radius."""
    for i in range(steps + 1):
        t = i / steps
        tt = t ** ease
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


def line_taper(p0, p1, r_start, r_end, steps=200):
    for i in range(steps + 1):
        t = i / steps
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# --- Stroke 1: 撇折 ---
# Primary 撇: starts upper-right with a small rightward-curling tip
# (like the GT's small hook at the top), then throws down-and-left,
# then folds via shoulder into a rightward 横 with slight up-tilt.
# Fill the canvas more — standalone radical scale-up discipline.

# Tiny opening curl: a short segment going right-down before the main 撇 body
curl_start = (170, 85)
curl_end = (188, 95)
line_taper(curl_start, curl_end, r_start=4.5, r_end=5.5, steps=100)
dab(curl_end[0], curl_end[1], 5.5)

# Primary 撇 body: from the curl end down-and-left to the joint,
# gentle rightward bow (belly on the right).
pie_p0 = curl_end
pie_p2 = (75, 220)       # lower-left tip (the joint)
pie_ctrl = (155, 140)    # control pulled toward interior/right for a bow

bezier_stroke(pie_p0, pie_ctrl, pie_p2, r_start=5.5, r_end=1.8, steps=400)

# 折 shoulder dab at the joint (small — no visible ball rule for standalones)
JOINT = pie_p2
dab(JOINT[0], JOINT[1], 6)

# Longer 横 going rightward with slight up-tilt from the joint.
heng_end = (215, 208)    # extends further right to fill the canvas
line_taper(JOINT, heng_end, r_start=5.5, r_end=4.8, steps=200)
# Terminal blunt press (subtle)
dab(heng_end[0], heng_end[1], 5.5)

# --- Stroke 2: 点 (反捺-like slash) ---
# Positioned at the lower-right, going down-and-right.
# In GT this reads more like a short slash than a fat teardrop.
dot_p0 = (200, 215)
dot_p1 = (255, 260)
teardrop(dot_p0, dot_p1, r_start=2.0, r_end=7.5, steps=250, ease=1.3)
# Terminal press for the broad foot
dab(dot_p1[0], dot_p1[1], 8)


img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_032_厶/01_厶.png"
)
