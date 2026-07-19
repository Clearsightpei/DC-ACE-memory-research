"""
p2_radical_023_卩 (jié) — 2-stroke radical.

Structure (from GT):
  Stroke 1: 横折钩 — small 横 at upper-right, shoulder, curved 竖 down,
            tucking with a small inward hook. Forms the "P-loop" on the
            upper right.
  Stroke 2: 竖 — long straight vertical on the left, extending down
            below the loop to the bottom of the canvas.

Renderer: PIL brush-dabs at 300x300.
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(p0, p1, r0, r1, steps=None):
    x0, y0 = p0
    x1, y1 = p1
    dist = math.hypot(x1 - x0, y1 - y0)
    if steps is None:
        steps = max(int(dist * 3), 20)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=300):
    x0, y0 = p0
    xc, yc = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        omt = 1 - t
        x = omt * omt * x0 + 2 * omt * t * xc + t * t * x2
        y = omt * omt * y0 + 2 * omt * t * yc + t * t * y2
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ---------------------------------------------------------------
# Stroke 2 FIRST (draw the long 竖 spine so it sits behind the loop
# in overlap regions). Actually order doesn't matter visually in
# black ink, but conventionally 卩's 竖 is stroke 2.
# ---------------------------------------------------------------
# Long straight vertical on the LEFT side of the character.
# GT shows the vertical starting roughly where the loop's top is
# (a bit lower than loop top) and dropping to near the bottom.
r_shu = 5.5
shu_top = (128, 100)
shu_bot = (128, 278)
# subtle 顿 (r+1) — standalone scale rule: r+2 becomes a visible ball
dab(shu_top[0], shu_top[1], r_shu + 1)
line_dabs(shu_top, shu_bot, r_shu, r_shu)
# blunt end at bottom, subtle
dab(shu_bot[0], shu_bot[1], r_shu + 1)


# ---------------------------------------------------------------
# Stroke 1: 横折钩 forming the upper-right "P loop".
# Anchors (image coords y down):
#   - 横 starts at ~(135, 82) small 顿 press, goes right to (200, 78)
#   - shoulder dab at (200, 78)
#   - curved 竖 descending from (200, 78) down and slightly curving
#     left, ending at ~(178, 175)
#   - hook flicks up-and-left, terminating around (150, 160)
# ---------------------------------------------------------------
r_main = 5.0

# 横 top: short horizontal with slight up-tilt
heng_start = (138, 90)
heng_end = (208, 82)
dab(heng_start[0], heng_start[1], r_main + 1.5)  # 顿 press
line_dabs(heng_start, heng_end, r_main, r_main + 0.5)

# Shoulder dab at corner (顿) — real 折 shoulder, keep prominent
shoulder = (210, 82)
dab(shoulder[0], shoulder[1], r_main + 2.5)

# Curved 竖 descending — this is the "belly" of the P (round loop).
# Quadratic Bezier bowing RIGHT (belly on right), then tucking left.
b_p0 = (210, 85)
b_p1 = (232, 138)  # push control further right for rounder belly
b_p2 = (168, 180)
bezier_dabs(b_p0, b_p1, b_p2, r_main + 0.5, r_main, steps=280)

# Joining dab at hook base
dab(b_p2[0], b_p2[1], r_main + 1.5)

# Hook flick — up and to the left (tucking inward toward the 竖)
hook_end = (145, 158)
# taper thick->thin along hook
steps = 60
for i in range(steps + 1):
    t = i / steps
    x = b_p2[0] + (hook_end[0] - b_p2[0]) * t
    y = b_p2[1] + (hook_end[1] - b_p2[1]) * t
    r = (r_main + 0.5) + (1.2 - (r_main + 0.5)) * t
    dab(x, y, r)


# ---------------------------------------------------------------
out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_023_卩/01_卩.png"
img.save(out)
print("saved", out)
