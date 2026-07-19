"""Render 乛 (radical) — horizontal then curved/tapered downward-right tail.

Interpretation from GT: a shallow 横 running left→right in the upper-middle
of the canvas, then a smooth arc turning down-and-right that tapers to a
sharp tip. Similar family to 横钩 but the tail runs down-right (not up-left).
Rendered PIL brush-dabs, 300×300 white, black ink.
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# --- 横 (horizontal), slight up-tilt, in upper-middle band ---
# Start with a small 顿 press, uniform body, end into the turn point.
x_h0, y_h0 = 70, 152
x_h1, y_h1 = 195, 145   # slight upward tilt (y decreases as we go right)
r_body = 4.5
dab(x_h0, y_h0, r_body + 1.5)          # start press (subtle, standalone-scale)
line_dabs(x_h0, y_h0, x_h1, y_h1, r_body, r_body, steps=360)

# --- Turn / joint dab ---
dab(x_h1, y_h1, r_body + 1.5)

# --- Smooth arc turning down-and-right into a tapered tail ---
# Tangent-continuous: at t=0 tangent is (+x, 0) matching 横 rightward motion.
# At t=1 tangent points down-and-right.  Use quarter-arc parametrization:
#   x = cx + R * sin(t*pi/2), y = cy - R * cos(t*pi/2)  gives entry tangent (+x,0)
# with cx = x_h1, cy = y_h1 + R.  End tangent is (0,+y).  We'll then extend
# a short down-right tapered segment to give the tail its calligraphic drop.
R = 26
cx, cy = x_h1, y_h1 + R
arc_end_x, arc_end_y = None, None
arc_steps = 90
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = cx + R * math.sin(t * math.pi / 2)
    y = cy - R * math.cos(t * math.pi / 2)
    # gently taper through the arc from body-radius to a slightly thinner value
    r = r_body - 0.8 * t
    dab(x, y, r)
    arc_end_x, arc_end_y = x, y

# --- Tapered tail continuing down-and-slightly-right to a sharp tip ---
# From the arc end (tangent pointing straight down) blend into a down-right
# taper — Bezier for smoothness.
P0 = (arc_end_x, arc_end_y)
P2 = (215, 215)          # tip lower-right
P1 = (arc_end_x + 2, (arc_end_y + P2[1]) / 2 - 3)   # control just below arc end
r_start_tail = r_body - 0.8
r_end_tail = 1.0
tail_steps = 220
for i in range(tail_steps + 1):
    t = i / tail_steps
    x = (1 - t) * (1 - t) * P0[0] + 2 * (1 - t) * t * P1[0] + t * t * P2[0]
    y = (1 - t) * (1 - t) * P0[1] + 2 * (1 - t) * t * P1[1] + t * t * P2[1]
    r = r_start_tail + (r_end_tail - r_start_tail) * t
    dab(x, y, r)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_004_乛/01_乛.png")
