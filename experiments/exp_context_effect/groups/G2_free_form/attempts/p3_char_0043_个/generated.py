"""
个 (p3_char_0043) — 3 strokes.
Structure = 人-apex (撇 + 捺 meeting at single top apex) + short 竖
hanging straight down from just under the apex.

Refs:
  - form_catalog "捺 as right-leg of two-stroke apex (人, 大, 天)"
  - form_catalog sibling table: 人 = both tops at same y; 个 shares
    that 人-apex on top of a hanging 竖.
  - drawer_memory 人 retry_1 template (Bezier apex).

Notes on GT:
  - Apex high (~y=60), legs wide (spread to ~x=45 and x=250)
  - Legs stop above baseline (~y=210), i.e. NOT extending to bottom
  - Short 竖 falls from apex vicinity down to ~y=240, sitting slightly
    right of the apex point (visible in GT); it does NOT reach the bottom.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_pt(p0, p1, p2, t):
    u = 1 - t
    x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
    y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
    return x, y


def bez_deriv(p0, p1, p2, t):
    return (2 * (1 - t) * (p1[0] - p0[0]) + 2 * t * (p2[0] - p1[0]),
            2 * (1 - t) * (p1[1] - p0[1]) + 2 * t * (p2[1] - p1[1]))


APEX = (150, 62)

# ---- Stroke 1: 撇 (left leg from apex) ----
p0 = APEX
p2 = (48, 220)
ctrl = (140, 165)   # bow rightward (belly on interior)
r_start = 5.5
r_end = 1.2
dab(p0[0], p0[1], r_start)
steps = 400
for i in range(steps + 1):
    t = i / steps
    x, y = bezier_pt(p0, ctrl, p2, t)
    r = r_start + (r_end - r_start) * t
    dab(x, y, r)

# ---- Stroke 2: 捺 (right leg from apex) thin -> thick ----
q0 = APEX
q2 = (252, 215)
qctrl = (200, 165)   # slight downward bow
r0 = 1.4
r2 = 6.5
steps = 400
for i in range(steps + 1):
    t = i / steps
    x, y = bezier_pt(q0, qctrl, q2, t)
    tt = t ** 1.3
    r = r0 + (r2 - r0) * tt
    dab(x, y, r)

# broad terminal foot
dx, dy = bez_deriv(q0, qctrl, q2, 1.0)
mag = math.hypot(dx, dy)
ux, uy = dx / mag, dy / mag
foot_len = 12
foot_steps = 50
for i in range(foot_steps + 1):
    t = i / foot_steps
    x = q2[0] + ux * foot_len * t
    y = q2[1] + uy * foot_len * t
    r = 7.0 + (2.0 - 7.0) * t
    dab(x, y, r)

# ---- Stroke 3: 竖 (short vertical hanging from just under apex) ----
# In GT this drops from close to the apex and does NOT reach the bottom.
# Slight tilt/curve: starts a tad right of apex, straight vertical down.
s_x = 158              # slightly right of apex to match GT offset
s_y_top = 78           # just below apex intersection
s_y_bot = 242
s_steps = 180
r_top = 3.2
r_bot = 2.4
# tiny 顿笔 press at top
dab(s_x, s_y_top, r_top + 1.0)
for i in range(s_steps + 1):
    t = i / s_steps
    y = s_y_top + (s_y_bot - s_y_top) * t
    r = r_top + (r_bot - r_top) * t
    dab(s_x, y, r)

out_path = ("<REPO_ROOT>/experiments/"
            "exp_context_effect/groups/G2_free_form/attempts/"
            "p3_char_0043_个/01_个.png")
img.save(out_path)
print("saved", out_path)
