"""力 (li) — 2-stroke radical.

Stroke 1: 横折钩 — short slightly-up-tilted 横 across the top, hard 折 shoulder,
          then a long 竖 that CURVES leftward as it descends (belly on the right),
          ending in an up-left hook flick. Body traces the right half.
Stroke 2: 撇 — throw from top-横 area (starting on/near the top-横 line),
          sweeping down-and-left through the character interior,
          thick→thin, gentle rightward bow. Ends in lower-left region.

Difference from 刀: in 力, the 撇 starts AT/BELOW the top-横 (does not cross
above it), and the 撇 does not extend as far to the lower-left as in 刀 —
it stays inside the character's bounding box.

Rendered at 300x300, PIL brush-dabs.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=400, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        tt = t ** ease
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)


# ---- Stroke 1: 横折钩 ----
# Top 横: short, slight up-tilt. Positioned upper-center-right.
h_start = (100, 95)
h_end = (225, 85)
r_h = 5.0
dab(h_start[0], h_start[1], r_h + 2)  # 顿笔 at start
line_dabs(h_start[0], h_start[1], h_end[0], h_end[1], r_h, r_h, steps=300)
# Shoulder dab at corner
shoulder = h_end
dab(shoulder[0], shoulder[1], r_h + 3)

# Curving 竖 with belly on the RIGHT (concave toward left).
# Bezier: start at shoulder, end low, control pulled to the RIGHT.
v_start = shoulder
v_end = (170, 250)
v_ctrl = (240, 175)  # control point to the right → left-concave belly
bezier_dabs(v_start, v_end, v_ctrl, r0=r_h + 1, r1=r_h + 0.5, steps=400)

# Hook flick from v_end going up-and-left (~ -150°), taper thick→thin
hook_len = 34
hook_angle = math.radians(-150)  # image coords: -150° = up-left
hx = v_end[0] + hook_len * math.cos(hook_angle)
hy = v_end[1] + hook_len * math.sin(hook_angle)
# joining dab
dab(v_end[0], v_end[1], r_h + 1)
line_dabs(v_end[0], v_end[1], hx, hy, r0=r_h + 0.5, r1=1.2, steps=200)


# ---- Stroke 2: 撇 — throw from LEFT END of top-横 sweeping down-and-left ----
# For 力: 撇 starts at/near the LEFT END of the top-横 (just above the 横's
# left endpoint), and sweeps down-and-left all the way to the lower-left,
# passing THROUGH the top-横 area. Gentle rightward bow (concave up-right).
pie_p0 = (110, 90)     # start point at/just above the top 横's left end
pie_p2 = (50, 265)     # lower-left tip — reaches lower-left region
pie_ctrl = (80, 200)   # control point for gentle rightward bow
# 顿笔 dab at start
dab(pie_p0[0], pie_p0[1], 9)
bezier_dabs(pie_p0, pie_p2, pie_ctrl, r0=8.5, r1=1.3, steps=500, ease=1.15)


img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_025_力/01_力.png"
)
