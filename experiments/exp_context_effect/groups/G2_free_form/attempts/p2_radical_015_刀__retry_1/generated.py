"""刀 (dao) — 2-stroke radical. RETRY 1.

Fixes from errata:
- Stroke 1 (横折钩): keep top 横 short (~120 px), shoulder, curving 竖
  with belly on RIGHT (concave-left). Hook flick around -140° with
  joining dab RADIUS equal to segment radius (not r+1) to avoid stray
  nub artifact below body.
- Stroke 2 (撇): start ABOVE the 横 (y ~70), cross THROUGH the 横 at
  ~x=140, continue down-left to (~55, 260). Top of 撇 must poke UP
  above the 横 line.

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


# ---- Stroke 1: 横折钩 (short top-横 + shoulder + curving 竖 + hook) ----
# Top 横: short (~120 px), slight up-tilt.
h_start = (110, 100)
h_end = (230, 92)
r_h = 5.0
dab(h_start[0], h_start[1], r_h + 2)  # 顿笔 at start
line_dabs(h_start[0], h_start[1], h_end[0], h_end[1], r_h, r_h, steps=300)
# Shoulder dab at corner
shoulder = h_end
dab(shoulder[0], shoulder[1], r_h + 3)

# Curving 竖 with belly on RIGHT (concave toward left), tail flicks up-left.
v_start = shoulder
v_end = (180, 255)
v_ctrl = (240, 175)  # control to the right → left-concave belly
bezier_dabs(v_start, v_end, v_ctrl, r0=r_h + 1, r1=r_h + 0.3, steps=400)

# Hook flick from v_end going up-and-left (~ -140°), taper thick→thin.
# Joining dab radius == segment radius (fix: was r+1, caused stray nub).
hook_len = 34
hook_angle = math.radians(-140)  # image coords: -140° = up-left
hx = v_end[0] + hook_len * math.cos(hook_angle)
hy = v_end[1] + hook_len * math.sin(hook_angle)
dab(v_end[0], v_end[1], r_h + 0.3)  # joining dab matches segment radius
line_dabs(v_end[0], v_end[1], hx, hy, r0=r_h + 0.3, r1=1.1, steps=200)


# ---- Stroke 2: 撇 — starts ABOVE the top-横, crosses THROUGH it ----
# Revision: move start closer to left end of 横 (~x=135, above 横 at y=72),
# so the top of 撇 pokes up just left-of-center like the GT.
# Bezier bows gently, thick→thin, ending near lower-left.
pie_p0 = (138, 72)     # ABOVE 横 near its left third (top of 撇 pokes up here)
pie_p2 = (55, 258)     # lower-left tip
pie_ctrl = (110, 190)  # control for gentle rightward bow
# 顿笔 dab at start — smaller so it doesn't read as a separate dot
dab(pie_p0[0], pie_p0[1], 7)
bezier_dabs(pie_p0, pie_p2, pie_ctrl, r0=6.5, r1=1.2, steps=500, ease=1.15)


img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_015_刀__retry_1/01_刀.png"
)
