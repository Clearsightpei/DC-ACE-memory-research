"""力 (li) — 2-stroke character (Phase 3).

Redraw against clean GT. GT shows thinner brush lines with:
  Stroke 1 — 横折钩: short slight-upward 横 across upper canvas,
             hard 折 shoulder at upper right, gently right-bowing 竖
             ending in a small hook flicking up-left.
  Stroke 2 — 撇: starts from near the top of the 横 (slightly above),
             sweeps down-and-left in a long moderate curve to lower-
             left. Crosses the 横 near its left third.
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


def bezier_dabs(p0, p1, p2, r0, r1, steps=500, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        tt = t ** ease
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)


# ---- Stroke 1: 横折钩 ----
# Top 横 — short, slight up-tilt. Thinner than prior attempt.
h_start = (110, 115)
h_end = (215, 105)
r_h = 3.2
dab(h_start[0], h_start[1], r_h + 1.5)          # small 顿笔 at start
line_dabs(h_start[0], h_start[1], h_end[0], h_end[1], r_h, r_h, steps=300)
# 折 shoulder dab at corner
shoulder = h_end
dab(shoulder[0], shoulder[1], r_h + 2.0)

# Curving 竖 — belly on the RIGHT (bows out slightly right).
v_start = shoulder
v_end = (180, 250)
v_ctrl = (230, 175)
bezier_dabs(v_start, v_ctrl, v_end, r0=r_h + 0.5, r1=r_h, steps=400)

# Terminal 钩 — small flick up-and-left.
hook_len = 22
hook_angle = math.radians(-155)
hx = v_end[0] + hook_len * math.cos(hook_angle)
hy = v_end[1] + hook_len * math.sin(hook_angle)
dab(v_end[0], v_end[1], r_h)
line_dabs(v_end[0], v_end[1], hx, hy, r0=r_h, r1=0.8, steps=200)


# ---- Stroke 2: 撇 (body-crossing diagonal) ----
# In GT: 撇 starts near/just above the top 横's left portion, curls
# down-and-left in a long moderate arc.
pie_p0 = (150, 85)      # start just above the 横 line
pie_p2 = (55, 265)      # end lower-left
pie_ctrl = (125, 165)   # gentle rightward bow (concave to left)
dab(pie_p0[0], pie_p0[1], 5.5)  # small 顿笔
bezier_dabs(pie_p0, pie_ctrl, pie_p2, r0=5.0, r1=1.2, steps=700, ease=1.0)


img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0025_力/01_力.png"
)
