"""
冖 (mì) — 2画 radical: 点 + 横钩.

Composition (from GT observation, image-coords, y grows DOWN, 300×300 canvas):
- Stroke 1: 点 (short teardrop dot) at upper-left, thin→thick, ~30 px.
- Stroke 2: 横钩 — long horizontal from just right of the dot, running
  rightward with slight up-tilt, then a shoulder press at the right end,
  then a downward-left hook flick (~35 px, angled ~140° in image coords).

Rendering: PIL brush-dabs.
"""

import math
import os
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def taper_line(x0, y0, x1, y1, r0, r1, steps=200, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        te = t ** ease
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * te
        dab(x, y, r)


def uniform_line(x0, y0, x1, y1, r, steps=250):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        dab(x, y, r)


# ---------------------------------------------------------------------------
# Stroke 1: 点 (dot) at upper-left.
# GT dot is more slanted like ")" — starts upper-right, tips down-left
# with a gentle curve. Slim overall.
# ---------------------------------------------------------------------------
# Slight leftward-bowed teardrop via quadratic Bezier
p0 = (95, 95)     # thin start upper-right
p2 = (78, 155)    # thick tip lower-left
p1 = (82, 118)    # control pulled to the LEFT to give ) shape
bez_steps = 200
for i in range(bez_steps + 1):
    t = i / bez_steps
    u = 1 - t
    x = u*u*p0[0] + 2*u*t*p1[0] + t*t*p2[0]
    y = u*u*p0[1] + 2*u*t*p1[1] + t*t*p2[1]
    # thin -> thick taper for a 点
    te = t ** 1.3
    r = 1.4 + (5.5 - 1.4) * te
    dab(x, y, r)
# Terminal press (small — standalone scale, per memory)
dab(p2[0], p2[1], 6.0)

# ---------------------------------------------------------------------------
# Stroke 2: 横钩 (horizontal + downward-left hook)
# Thinner overall; smaller start dab; slight up-tilt on the 横.
# ---------------------------------------------------------------------------
# 横 primary — start just right of the dot's top
h_x0, h_y0 = 108, 100
h_x1, h_y1 = 240, 92
# 顿笔 dab at start — standalone scale, keep it subtle (r+1)
dab(h_x0, h_y0, 5.5)
uniform_line(h_x0, h_y0, h_x1, h_y1, r=3.8, steps=280)

# Shoulder press at end (visible but small)
shoulder_r = 5.5
dab(h_x1, h_y1, shoulder_r)

# Hook flick: from (h_x1, h_y1) going down-and-left.
# 横钩 hook flicks down-left in image coords — angle 140° (dx<0, dy>0).
hook_len = 32.0
hook_angle_deg = 140.0
hook_angle = math.radians(hook_angle_deg)
hook_x1 = h_x1 + hook_len * math.cos(hook_angle)
hook_y1 = h_y1 + hook_len * math.sin(hook_angle)

# Taper from shoulder radius to sharp tip
taper_line(h_x1, h_y1, hook_x1, hook_y1, r0=4.5, r1=1.0, steps=180)

# ---------------------------------------------------------------------------
# Save PNG
# ---------------------------------------------------------------------------
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_冖.png")
img.save(out_path)
print(f"Saved: {out_path}")
