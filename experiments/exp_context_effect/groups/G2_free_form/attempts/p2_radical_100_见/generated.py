"""
p2_radical_100_见 (jiàn) - 4-stroke radical

Analysis from GT PNG:
- Rectangular box in upper half: left 竖, top+right 横折 (forming top-left-right walls)
  plus a lower closing horizontal (bottom of the box, ~y=155)
- Below the box, two legs:
  - Left leg: 撇 curving down-and-left from inside-bottom-left of the box
  - Right leg: 竖弯钩 - short vertical from inside-bottom-right, then arcs
    smoothly rightward, hooks up-and-left at the terminal

Canonical stroke count is 4 in MMH; the visible bottom-of-box horizontal is
part of the compound geometry of the character - I'll render the box as
{竖 + 横折 + closing 横} and the two legs as separate strokes, matching the
GT silhouette closely.

Renderer: PIL brush-dabs, 300x300 white, black ink.
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(cx, cy, r):
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy)
    if steps is None:
        steps = max(int(L * 3), 30)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + dx * t
        y = y0 + dy * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=200):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# --- Box geometry ---
# Left wall x=85, right wall x=210, top y=55, bottom y=155
BOX_LEFT = 85
BOX_RIGHT = 210
BOX_TOP = 55
BOX_BOTTOM = 155
R = 5.0  # base segment radius

# Stroke 1: 竖 (left wall of box)
# top-down, from (BOX_LEFT, BOX_TOP) to (BOX_LEFT, BOX_BOTTOM)
dab(BOX_LEFT, BOX_TOP, R + 2)  # 顿 start
line_dabs(BOX_LEFT, BOX_TOP, BOX_LEFT, BOX_BOTTOM, R, R)
dab(BOX_LEFT, BOX_BOTTOM, R + 1)  # blunt end

# Stroke 2: 横折 (top horizontal + right vertical of box)
# Slight up-tilt on 横: top-left (BOX_LEFT, BOX_TOP) to (BOX_RIGHT, BOX_TOP-3)
h_start = (BOX_LEFT, BOX_TOP)
h_end = (BOX_RIGHT, BOX_TOP - 2)
dab(*h_start, R + 2)  # 顿 start
line_dabs(h_start[0], h_start[1], h_end[0], h_end[1], R, R)
dab(*h_end, R + 3)  # shoulder dab
# 竖 down the right wall to (BOX_RIGHT, BOX_BOTTOM)
line_dabs(h_end[0], h_end[1], BOX_RIGHT, BOX_BOTTOM, R, R)
dab(BOX_RIGHT, BOX_BOTTOM, R + 1)  # blunt bottom

# Closing horizontal at box bottom (part of the box's visual closure)
# From (BOX_LEFT, BOX_BOTTOM) to (BOX_RIGHT, BOX_BOTTOM - 3) slight up-tilt
line_dabs(BOX_LEFT, BOX_BOTTOM, BOX_RIGHT, BOX_BOTTOM - 2, R, R)

# --- Legs below the box ---
# Stroke 3: 撇 (left leg)
# Starts at inside-bottom-left of the box (~BOX_LEFT+5, BOX_BOTTOM), throws down-left
# with gentle rightward bow (Bezier). Ends at ~(50, 265)
pie_p0 = (BOX_LEFT + 3, BOX_BOTTOM)
pie_p2 = (35, 275)
pie_ctrl = (82, 225)  # pull toward interior/right for gentle bow
dab(pie_p0[0], pie_p0[1], R + 2)  # 顿 start (joining dab at box)
bezier_dabs(pie_p0, pie_ctrl, pie_p2, R + 1.5, 1.4, steps=300)

# Stroke 4: 竖弯钩 (right leg)
# Starts at inside-bottom-right of box (BOX_RIGHT-3, BOX_BOTTOM),
# short vertical descent, tangent-continuous quarter-arc into rightward horizontal,
# then hook flick up-and-left at ~-110 deg
sh_x0 = BOX_RIGHT - 3
sh_y0 = BOX_BOTTOM
sh_y1 = 240  # end of straight vertical portion (before arc)
dab(sh_x0, sh_y0, R + 2)  # 顿 start (joining dab)
line_dabs(sh_x0, sh_y0, sh_x0, sh_y1, R, R)

# Tangent-continuous quarter-arc: descending -> rightward
# x = x0 + R_arc*(1 - cos(t*pi/2)), y = y0 + R_arc*sin(t*pi/2)
R_arc = 25
arc_x0 = sh_x0
arc_y0 = sh_y1
arc_steps = 60
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = arc_x0 + R_arc * (1 - math.cos(t * math.pi / 2))
    y = arc_y0 + R_arc * math.sin(t * math.pi / 2)
    dab(x, y, R)
# Arc ends at (arc_x0 + R_arc, arc_y0 + R_arc) = (BOX_RIGHT-3+25, 265)
arc_end_x = arc_x0 + R_arc
arc_end_y = arc_y0 + R_arc

# Short rightward horizontal from arc-end
horiz_end_x = 248
horiz_end_y = arc_end_y - 2  # very slight lift
line_dabs(arc_end_x, arc_end_y, horiz_end_x, horiz_end_y, R, R - 0.5)

# Hook flick up-and-left, ~-110 deg from horizontal, length ~28 px
hook_len = 28
hook_angle_deg = -115  # up-and-slightly-left in math coords
# In image coords, y grows DOWN; -115 deg is up-and-left
hx1 = horiz_end_x + hook_len * math.cos(math.radians(hook_angle_deg))
hy1 = horiz_end_y + hook_len * math.sin(math.radians(hook_angle_deg))
# Joining dab at hook base = segment radius (NOT r+1, NOT r+2) per hook discipline
dab(horiz_end_x, horiz_end_y, R)
line_dabs(horiz_end_x, horiz_end_y, hx1, hy1, R, 1.0, steps=80)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_100_见/01_见.png")
print("Wrote 01_见.png")
