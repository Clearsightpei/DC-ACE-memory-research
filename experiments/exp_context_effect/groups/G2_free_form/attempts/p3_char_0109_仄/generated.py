"""G2 first attempt for p3_char_0109_仄.

Structural read from GT PNG:
- 4 strokes total.
- Outer 厂 (top-left corner): 横 across the top + 撇 sweeping from
  top-left corner down to the lower-left. This is the "lid + left
  wall" cradle enclosing 人.
- Inner 人 nested inside the cradle: 撇 (short, from under the 横
  center) + 捺 (from same apex sweeping down-right to lower-right).

Layout (300x300 canvas):
- 厂 横: top, from ~(60,80) to ~(240,72), slight up-tilt.
- 厂 撇: starts at shared top-left corner (60,80), sweeps down and
  slightly left to about (55,265).
- 人 撇: short, starts around (155,95) (just under the 横, roughly
  under midpoint but a bit left), sweeps to lower-mid area
  (~(115,255)).
- 人 捺: shares apex with 人 撇 at (155,95), sweeps down-right to
  ~(255,265) with the classic thin→thick swell + broad foot.

Signature bits:
- The 人 inside must have shared apex (人-not-入).
- The 厂 撇 and 横 share the top-left corner.

Renderer: PIL brush-dabs at 300x300, white bg, black ink.
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(p0, p1, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_pt(p0, p1, p2, t):
    u = 1 - t
    x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
    y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
    return x, y


def bez_deriv(p0, p1, p2, t):
    return (2 * (1 - t) * (p1[0] - p0[0]) + 2 * t * (p2[0] - p1[0]),
            2 * (1 - t) * (p1[1] - p0[1]) + 2 * t * (p2[1] - p1[1]))


def bezier_dabs(p0, p1, p2, r0, r1, steps=500, taper_pow=1.0):
    for i in range(steps + 1):
        t = i / steps
        x, y = bezier_pt(p0, p1, p2, t)
        tt = t ** taper_pow
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)


# ---- 厂 outer shell ----
CORNER = (62, 80)

# Stroke 1: 横 across top, slight up-tilt to right, blunt terminal
heng_end = (238, 72)
line_dabs(CORNER, heng_end, r0=4.8, r1=3.6, steps=450)
dab(heng_end[0], heng_end[1], 4.0)
# 顿 press at shared corner
dab(CORNER[0], CORNER[1], 6.5)

# Stroke 2: 厂 撇 — from corner sweeping down and slightly left,
# belly on the right (concave-left). Thick→thin.
pie1_end = (48, 268)
pie1_ctrl = (95, 175)  # control pulled right → belly on right
bezier_dabs(CORNER, pie1_ctrl, pie1_end, r0=6.5, r1=1.2, steps=500)

# ---- Inner 人 nested in the cradle ----
# Apex sits below the 横, offset a bit left of dead center so the
# 捺 can splay to the lower-right and stay inside the frame.
APEX_INNER = (158, 100)

# Stroke 3: 人 撇 — short, shared apex, sweeps to lower-mid-left
p_end = (108, 258)
p_ctrl = (145, 185)  # slight right-belly
# 顿 press at apex
dab(APEX_INNER[0], APEX_INNER[1], 6.0)
bezier_dabs(APEX_INNER, p_ctrl, p_end, r0=6.0, r1=1.2, steps=400)

# Stroke 4: 人 捺 — same apex, thin→thick swell + broad foot
q_end = (255, 262)
q_ctrl = (208, 190)  # slight downward bow
bezier_dabs(APEX_INNER, q_ctrl, q_end, r0=1.8, r1=9.5, steps=400, taper_pow=1.3)

# Broad flat terminal foot along the tangent direction
dx, dy = bez_deriv(APEX_INNER, q_ctrl, q_end, 1.0)
mag = math.hypot(dx, dy)
ux, uy = dx / mag, dy / mag
foot_len = 18
foot_steps = 60
for i in range(foot_steps + 1):
    t = i / foot_steps
    x = q_end[0] + ux * foot_len * t
    y = q_end[1] + uy * foot_len * t
    r = 10.0 + (2.5 - 10.0) * t
    dab(x, y, r)

here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "01_仄.png")
img.save(out)
print(f"saved {out}")
