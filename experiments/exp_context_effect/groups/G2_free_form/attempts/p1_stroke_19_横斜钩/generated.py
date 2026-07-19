"""
横斜钩 (heng-xie-gou) — horizontal + slanted arc + upward hook.

Shape (image coords, y grows DOWN, 300x300):
  1. Short 横: left-to-right near the top, slight 3-5 deg upward tilt.
     Starts with 顿笔 (initial press). Ends with a shoulder press dab.
  2. 斜钩-style curve: from the shoulder, a long bowed arc going
     down-and-right. Belly on the LOWER-LEFT (concave toward upper-
     right), per drawer_memory rule for 斜钩. Sampled as a quadratic
     Bezier. Uniform-ish width, gently tapering near the hook base.
  3. Hook flick: from the curve's endpoint, a short stroke going
     up-and-left (~ -100 deg in image coords), tapering to sharp tip.

Rendered via PIL brush-dabs (small filled ellipses along the path).
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(cx, cy, r):
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


def line_dabs(x0, y0, x1, y1, r_start, r_end, steps=None):
    dist = math.hypot(x1 - x0, y1 - y0)
    if steps is None:
        steps = max(60, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r_start, r_end, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# --- 1. 横 segment (short horizontal near top) ---
heng_x0, heng_y0 = 55, 70          # left start (upper-left area)
heng_x1, heng_y1 = 155, 62         # right end (slight upward tilt)
R_MAIN = 6.5                        # main stroke radius

# 顿笔 initial press
dab(heng_x0, heng_y0, R_MAIN + 2.5)

# uniform 横 body, ramping slightly UP toward the shoulder press
line_dabs(heng_x0, heng_y0, heng_x1, heng_y1,
          r_start=R_MAIN, r_end=R_MAIN + 1.5)

# --- Shoulder press dab at the joint (横 -> 斜钩 corner) ---
SHOULDER_R = R_MAIN + 3.0
dab(heng_x1, heng_y1, SHOULDER_R)

# --- 2. 斜钩-style curved body ---
# From the shoulder (upper area) down-and-right to the hook base.
# Belly on lower-left: control point pulled toward lower-left of the
# straight P0->P2 chord.
p0 = (heng_x1, heng_y1)              # (155, 62)
p2 = (255, 240)                       # lower-right tip / hook base
# chord midpoint ~ (205, 151). Pull control down-left of that.
p1 = (170, 200)                       # belly toward lower-left
bezier_dabs(p0, p1, p2,
            r_start=SHOULDER_R,       # match shoulder
            r_end=R_MAIN - 1.0,       # slight taper near hook base
            steps=450)

# --- 3. Hook flick (up-and-left from p2) ---
# ~ -100 to -110 deg in image coords => up and slightly left.
hook_len = 40
hook_angle_deg = -110  # image coords: -90 = straight up, more negative = leftward
rad = math.radians(hook_angle_deg)
hx1 = p2[0] + hook_len * math.cos(rad)
hy1 = p2[1] + hook_len * math.sin(rad)
line_dabs(p2[0], p2[1], hx1, hy1,
          r_start=R_MAIN - 0.5,
          r_end=1.0,                  # sharp tip
          steps=180)

# --- Save ---
out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_横斜钩.png"))
print("saved 01_横斜钩.png")
