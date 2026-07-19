"""
Render 贝 (4-stroke simplified radical) to a 300x300 PNG.

Structural plan (from GT observation):
  Stroke 1: 竖 — left vertical of the box.
  Stroke 2: 横折 — top horizontal turning down into the right vertical of the box.
  Stroke 3: 撇 — long throwaway stroke from the box's bottom-left, curving
            down and to the left past the canvas midline.
  Stroke 4: 点 — short teardrop dot on the lower-right.

Image coords: y grows DOWN.
Renderer: PIL brush-dabs.
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r_start, r_end, steps=None):
    if steps is None:
        dist = math.hypot(x1 - x0, y1 - y0)
        steps = max(60, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r_start, r_end, steps=None, ease=1.0):
    if steps is None:
        steps = 400
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        tt = t ** ease
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


# --- Layout anchors ---
# Box occupies upper-middle. Left vertical at x=110, right at x=210.
# Top y=75, bottom of box y=175.
BOX_LEFT_X = 110
BOX_RIGHT_X = 205
BOX_TOP_Y = 70
BOX_BOT_Y = 175

R = 5  # base stroke radius

# Note: at standalone/radical scale, avoid visible r+2 顿-dab balls at
# plain endpoints; only use r+2 at real 折 shoulders. Use r+1 (subtle)
# at 顿笔 starts.

# --- Stroke 1: 竖 (left vertical) ---
dab(BOX_LEFT_X, BOX_TOP_Y, R + 1)  # subtle 顿 start
line_dabs(BOX_LEFT_X, BOX_TOP_Y, BOX_LEFT_X, BOX_BOT_Y, R, R)
# blunt bottom (no visible ball — this endpoint terminates plainly)

# --- Stroke 2: 横折 (top + right vertical) ---
# 横 from top-left with slight up-tilt to top-right, then shoulder,
# then straight-down 竖 that extends BELOW the box bottom to match GT.
top_x0, top_y0 = BOX_LEFT_X - 3, BOX_TOP_Y - 2
top_x1, top_y1 = BOX_RIGHT_X, BOX_TOP_Y - 5
dab(top_x0, top_y0, R + 1)  # subtle 顿 start
line_dabs(top_x0, top_y0, top_x1, top_y1, R, R)
dab(top_x1, top_y1, R + 2)  # real 折 shoulder (keep r+2 here — corner)
# right vertical drops straight down, extending WELL BELOW box bottom
right_x1, right_y1 = BOX_RIGHT_X - 2, BOX_BOT_Y + 30
line_dabs(top_x1, top_y1, right_x1, right_y1, R, R)
# plain blunt end — no ball

# --- Stroke 3: 撇 (long throwaway from box bottom-left) ---
# Starts near the bottom-left of the box, curves down and to the left.
p0 = (BOX_LEFT_X + 2, BOX_BOT_Y - 10)
p1 = (BOX_LEFT_X - 8, BOX_BOT_Y + 40)
p2 = (55, 265)
dab(p0[0], p0[1], R + 1)
bezier_dabs(p0, p1, p2, r_start=R + 1, r_end=1.2, steps=500)

# --- Stroke 4: 点 (dot on lower-right) ---
# Short 反捺 dot: thin start upper-left, thick end lower-right.
# Kept small and not overly ball-headed at the terminal.
d0 = (BOX_RIGHT_X - 8, BOX_BOT_Y + 40)
d1 = (BOX_RIGHT_X + 30, BOX_BOT_Y + 75)
STEPS = 200
for i in range(STEPS + 1):
    t = i / STEPS
    x = d0[0] + (d1[0] - d0[0]) * t
    y = d0[1] + (d1[1] - d0[1]) * t
    tt = t ** 1.5
    r = 1.5 + (7.5 - 1.5) * tt
    dab(x, y, r)
# subtle terminal press (not oversized)
dab(d1[0], d1[1], 8)

out_path = os.path.join(os.path.dirname(__file__), "01_贝.png")
img.save(out_path)
print(f"wrote {out_path}")
