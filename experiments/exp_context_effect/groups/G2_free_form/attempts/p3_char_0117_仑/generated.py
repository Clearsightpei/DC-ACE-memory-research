"""
G2 first attempt for p3_char_0117_仑 (4-stroke character).

Decomposition (from GT viewing):
  仑 = 人-lid (撇 + 捺 sharing apex, wide splay) on top
       + 匕 body (撇 + 竖弯钩) below, tucked under the lid.

# SIGNATURE CHECK:
#   人-lid (from sibling_signature_checklist row 人):
#     apex SHARED at same y; both strokes throw outward; 捺 has thick foot.
#   匕 (from sibling_signature_checklist row 匕):
#     top stroke is a 撇 (upper-right→lower-left); terminal hook flicks
#     UP-and-LEFT.
#
# HARD RULE (memory_index v7.1): render the canonical sibling-table form.
# For the 人-lid on top: shared apex, symmetric splay, thick 捺 foot.
# For the 匕 body: 撇 first, then 竖弯钩 whose 撇 crosses the 竖 body.

Layout on 300x300:
  APEX of 人-lid at (150, 45) — wide splay reaching outer canvas.
  匕 sits in lower-middle: vertical body around x=145, y=170..235,
  arc to right ending around x=215, hook up-left. 撇 crosses the
  vertical in its upper third.
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_stroke(p0, p1, p2, r_start, r_end, steps=440, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        tt = t ** ease
        mt = 1 - t
        x = mt * mt * p0[0] + 2 * mt * t * p1[0] + t * t * p2[0]
        y = mt * mt * p0[1] + 2 * mt * t * p1[1] + t * t * p2[1]
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


def bez_deriv(p0, p1, p2, t):
    return (2 * (1 - t) * (p1[0] - p0[0]) + 2 * t * (p2[0] - p1[0]),
            2 * (1 - t) * (p1[1] - p0[1]) + 2 * t * (p2[1] - p1[1]))


# ============================================================
# Part A — 人-lid on top: SHARED APEX at (150, 45)
# ============================================================
APEX = (150, 45)

# Stroke 1: 撇 (left leg of lid) — thick→thin, gentle rightward bow
p0 = APEX
ctrl1 = (120, 90)
p2 = (30, 180)
dab(p0[0], p0[1], 5)
bezier_stroke(p0, ctrl1, p2, r_start=5.5, r_end=1.2, steps=420, ease=1.05)

# Stroke 2: 捺 (right leg of lid) — thin→moderately thick with modest foot
q0 = APEX
qctrl = (200, 100)
q2 = (270, 190)
bezier_stroke(q0, qctrl, q2, r_start=1.6, r_end=6.5, steps=420, ease=1.3)

# Modest flat terminal foot on 捺 (along tangent direction)
dx, dy = bez_deriv(q0, qctrl, q2, 1.0)
mag = math.hypot(dx, dy)
ux, uy = dx / mag, dy / mag
foot_len = 14
for i in range(50 + 1):
    t = i / 50
    x = q2[0] + ux * foot_len * t
    y = q2[1] + uy * foot_len * t
    r = 7.0 + (2.0 - 7.0) * t
    dab(x, y, r)


# ============================================================
# Part B — 匕 body underneath, tucked under the 人-lid
# ============================================================
# 竖弯钩 (vertical → rightward arc → up-left hook)
vx = 150
v_top = 160
v_bot = 220
r_body = 4.0

# 顿 press at top
dab(vx, v_top, r_body + 1.5)

# Vertical body
for i in range(180 + 1):
    t = i / 180
    y = v_top + (v_bot - v_top) * t
    dab(vx, y, r_body)

# Quarter arc: vertical → rightward horizontal
R = 32
arc_end_x = vx + R
arc_end_y = v_bot + R
for i in range(160 + 1):
    t = i / 160
    x = vx + R * (1 - math.cos(t * math.pi / 2))
    y = v_bot + R * math.sin(t * math.pi / 2)
    dab(x, y, r_body)

# Rightward 横 continuation
h_end_x = 225
h_y = arc_end_y
for i in range(180 + 1):
    t = i / 180
    x = arc_end_x + (h_end_x - arc_end_x) * t
    dab(x, h_y, r_body)

# Terminal 钩 up-and-slightly-LEFT (匕 signature)
hook_len = 26
hook_angle = math.radians(-108)
hook_end_x = h_end_x + hook_len * math.cos(hook_angle)
hook_end_y = h_y + hook_len * math.sin(hook_angle)
dab(h_end_x, h_y, r_body)
for i in range(120 + 1):
    t = i / 120
    x = h_end_x + (hook_end_x - h_end_x) * t
    y = h_y + (hook_end_y - h_y) * t
    r = r_body + (1.2 - r_body) * t
    dab(x, y, r)


# Stroke 4: 撇 of 匕 — LONG body-crossing diagonal
# Starts upper-right ABOVE v_top, ends lower-left past the vertical.
# Crossing lands in the upper-third of the 竖.
sp0 = (215, 150)    # upper-right start, above v_top=160
sp1 = (175, 175)    # near crossing point
sp2 = (100, 215)    # lower-left endpoint, past x=150
dab(sp0[0], sp0[1], 5)
bezier_stroke(sp0, sp1, sp2, r_start=5.0, r_end=1.2, steps=380, ease=1.1)


img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p3_char_0117_仑/01_仑.png"
)
print("saved")
