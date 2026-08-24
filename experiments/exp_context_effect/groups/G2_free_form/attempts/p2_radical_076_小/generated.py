"""
p2_radical_076_小  —  G2 free-form drawer

小 = 3 strokes:
  1) 竖钩 (center) — vertical descending with a hook flick up-and-left at
     the bottom. Runs roughly from mid-top through mid-bottom.
  2) 撇 (left)  — short throw from upper-right to lower-left, gentle bow.
  3) 点 (right) — short teardrop dot (thin->thick), leans down-and-right,
     but here in 小 it is more of a short curved dot going down-and-right
     from upper-left to lower-right on the right side.

GT observation (gt/phase2/小.png):
  - Center 竖钩: starts near (150, 80), descends to about (150, 220),
    then flicks up-and-left to about (128, 205). Slight curve at the hook
    junction (a small round bend rather than a sharp corner).
  - Left stroke: a downward-left small stroke from about (110, 155) to
    about (75, 220). Slight bow.
  - Right stroke: a curved dot from about (200, 155) to (225, 205) — arcs
    with belly down-left.

Renderer: PIL brush-dabs (per drawer_memory). 300x300 white bg, black ink.
Standalone-scale: use smaller start-press (r=6) and pronounced curvature.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_taper(x0, y0, x1, y1, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_taper(p0, p1, p2, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# --------------------------------------------------------------------
# Stroke 1: 竖钩 (center) — the dominant central spine
# --------------------------------------------------------------------
# Start 顿-dab at top (subtle for standalone — r=6, not r+2 large ball)
sx, sy = 152, 78
ex, ey = 150, 218
dab(sx, sy, 7)  # small start press
# uniform vertical, r=5.5 (slight taper toward hook base)
line_taper(sx, sy, ex, ey, 5.8, 5.8, steps=300)
# joining dab at hook base — per memory, EQUAL to segment radius (not r+1/+2)
dab(ex, ey, 5.8)
# hook flick: up-and-slightly-left, angle ~-115° in image coords,
# length ~32 px (standalone-scale — long enough to read as a sweep)
hook_len = 32
hook_ang = math.radians(-115)  # image coords (y grows DOWN)
hx = ex + hook_len * math.cos(hook_ang)
hy = ey + hook_len * math.sin(hook_ang)
line_taper(ex, ey, hx, hy, 5.8, 1.2, steps=200)

# --------------------------------------------------------------------
# Stroke 2: 撇 (left) — short throw upper-right → lower-left, gentle bow
# --------------------------------------------------------------------
# Start higher-right of the left-side region, throw down-and-left
p0 = (112, 148)
p2 = (68, 218)
p1 = (100, 178)  # control pulled slightly toward the interior for gentle bow
# 顿-dab at start (small for standalone)
dab(p0[0], p0[1], 7)
bezier_taper(p0, p1, p2, r0=7.5, r1=1.3, steps=350)

# --------------------------------------------------------------------
# Stroke 3: 点 (right) — short dot going down-and-right, thin→thick
# --------------------------------------------------------------------
# In 小, the right stroke is a 反捺-style 点: starts thin at upper-left,
# thickens toward lower-right, terminal press.
q0 = (198, 148)
q2 = (232, 210)
q1 = (210, 185)  # slight bow, belly down-left
bezier_taper(q0, q1, q2, r0=2.0, r1=8.5, steps=300)
# terminal press for a broad foot
dab(q2[0], q2[1], 9)

# --------------------------------------------------------------------
img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_076_小/01_小.png")
print("wrote 01_小.png")
