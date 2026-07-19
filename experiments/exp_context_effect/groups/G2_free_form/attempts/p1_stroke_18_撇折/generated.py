"""
p1_stroke_18_撇折 — 撇折 (pie-zhe): 撇 then折转向右横
Rendering: PIL brush-dab technique from drawer_memory.md.

Structure (per memory notes on 撇点/撇折 family):
- Primary 撇: upper-right start → lower-left tip, thick→thin, gentle
  rightward bow (quadratic Bezier).
- 顿笔 dab at start of 撇.
- Second segment attaches at the tip of the 撇 — for 撇折 the second
  beat is a SHORT 横 turning rightward (per label description
  "撇然后转向右横"). NOTE: while the memory's 撇折 entry describes a
  提-like tail, the official target_description explicitly says
  "转向右横" (turn to a horizontal), so this attempt renders a short
  横 as the second beat with a 折 shoulder dab at the joint, then a
  small terminal press at the horizontal's right endpoint.
- 折 shoulder: one slightly-larger dab at the corner.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_quad(p0, p1, p2, t):
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
    return x, y


# ------------------------------------------------------------
# Primary 撇 — upper-right → lower-left, gentle rightward bow.
# Start P0 upper-right (about 1/3 from top, right-of-center).
# End  P2 lower-left, roughly at horizontal midline.
# Control P1 pulled slightly to the RIGHT/interior of the chord
# so the belly of the 撇 bows outward on the right side.
# ------------------------------------------------------------
P0 = (210, 60)   # upper-right start
P2 = (95, 175)   # lower-left tip (joint with second segment)
P1 = (185, 130)  # control — pulls the arc slightly right of chord

# 顿笔 press at start
dab(P0[0], P0[1], 8)

N_pie = 400
r_start = 7.5
r_end = 1.5
for i in range(N_pie + 1):
    t = i / N_pie
    x, y = bezier_quad(P0, P1, P2, t)
    r = r_start + (r_end - r_start) * t
    dab(x, y, r)

# ------------------------------------------------------------
# 折 shoulder dab at joint (the tip of the 撇 = start of 横).
# Slightly larger than local radius to visualise the 顿 press.
# ------------------------------------------------------------
joint_x, joint_y = P2
dab(joint_x, joint_y, 6)

# ------------------------------------------------------------
# Second beat — short 横 rightward from the joint.
# Per 折 rules: nearly uniform width, slight terminal press.
# Give it a tiny 3–5° upward tilt (standalone 横 convention).
# ------------------------------------------------------------
Hstart = (joint_x, joint_y)
Hend = (215, joint_y - 8)   # right and slightly upward

N_h = 300
r_h = 5.0
for i in range(N_h + 1):
    t = i / N_h
    x = Hstart[0] + (Hend[0] - Hstart[0]) * t
    y = Hstart[1] + (Hend[1] - Hstart[1]) * t
    dab(x, y, r_h)

# Terminal press at end of 横 (blunt round end for 折 second beat)
dab(Hend[0], Hend[1], 7)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p1_stroke_18_撇折/01_撇折.png"
)
print("wrote 01_撇折.png (300x300)")
