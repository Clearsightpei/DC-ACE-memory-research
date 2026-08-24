"""
p2_radical_100_见 (jiàn) - 4-stroke radical - RETRY 2

# SIGNATURE CHECK (verbatim from sibling_signature_checklist.md):
# | 见 | 冂 + ONE 横 + 撇+竖弯钩 legs | sibling: 贝 (冂 + TWO 横 + legs) |

Prior retry (p2_radical_100_见) failed: I drew a CLOSED BOX (top+left+right
+ a bottom closing 横), leaving the interior empty. Result read as 凡 / 冂-box
with legs. Missing the diagnostic INTERIOR 横.

Errata fix:
- 冂-box: open at bottom (no closing horizontal at box bottom).
- ONE interior 横 sits inside the box near its lower third (~y=115).
- Legs 撇 + 竖弯钩 hang from box bottom-left and bottom-right.
- 竖弯钩's tail sweeps rightward and hooks UP-and-LEFT (~-110 deg).

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


# --- Box geometry: OPEN AT BOTTOM ---
BOX_LEFT = 80
BOX_RIGHT = 215
BOX_TOP = 55
BOX_BOTTOM = 160  # bottom of left/right walls (no closing horizontal here)
R = 5.0

# Stroke 1: 竖 (left wall of box) - straight vertical
dab(BOX_LEFT, BOX_TOP, R + 2)
line_dabs(BOX_LEFT, BOX_TOP, BOX_LEFT, BOX_BOTTOM, R, R)
dab(BOX_LEFT, BOX_BOTTOM, R + 1)

# Stroke 2: 横折钩 (top horizontal + right vertical, forming top+right walls)
# 横: slight up-tilt, from top-left to top-right corner
h_start = (BOX_LEFT, BOX_TOP)
h_end = (BOX_RIGHT, BOX_TOP - 2)
dab(*h_start, R + 2)
line_dabs(h_start[0], h_start[1], h_end[0], h_end[1], R, R)
dab(*h_end, R + 3)  # shoulder dab
# 竖 down the right wall
line_dabs(h_end[0], h_end[1], BOX_RIGHT, BOX_BOTTOM, R, R)
dab(BOX_RIGHT, BOX_BOTTOM, R + 1)

# Stroke 3: INSIDE 横 (the diagnostic bit — 见 has ONE, 贝 has TWO)
# Sits clearly INSIDE the box (well above the box bottom) so it doesn't
# read as a closing bottom horizontal. Bar spans wall-to-wall.
IN_H_Y = 105  # comfortably inside the box (top=55, bottom=160)
IN_H_LEFT = BOX_LEFT + 4
IN_H_RIGHT = BOX_RIGHT - 4
dab(IN_H_LEFT, IN_H_Y, R + 1)
line_dabs(IN_H_LEFT, IN_H_Y, IN_H_RIGHT, IN_H_Y - 2, R, R)
dab(IN_H_RIGHT, IN_H_Y - 2, R + 1)

# --- Legs below the box ---
# Stroke 4: 撇 (left leg) - starts at box bottom-left, throws down-and-left
pie_p0 = (BOX_LEFT + 2, BOX_BOTTOM)
pie_p2 = (30, 275)
pie_ctrl = (72, 225)
dab(pie_p0[0], pie_p0[1], R + 2)
bezier_dabs(pie_p0, pie_ctrl, pie_p2, R + 1.5, 1.2, steps=300)

# Stroke 5: 竖弯钩 (right leg) - starts at box bottom-right, short vertical,
# tangent quarter-arc rightward, then hook flick up-and-left.
sh_x0 = BOX_RIGHT - 2
sh_y0 = BOX_BOTTOM
sh_y1 = 235
dab(sh_x0, sh_y0, R + 2)
line_dabs(sh_x0, sh_y0, sh_x0, sh_y1, R, R)

# Tangent quarter-arc: descending -> rightward
R_arc = 30
arc_x0 = sh_x0
arc_y0 = sh_y1
arc_steps = 70
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = arc_x0 + R_arc * (1 - math.cos(t * math.pi / 2))
    y = arc_y0 + R_arc * math.sin(t * math.pi / 2)
    dab(x, y, R)
arc_end_x = arc_x0 + R_arc
arc_end_y = arc_y0 + R_arc

# Short rightward run from arc-end
horiz_end_x = 265
horiz_end_y = arc_end_y - 2
line_dabs(arc_end_x, arc_end_y, horiz_end_x, horiz_end_y, R, R - 0.5)

# Hook flick UP-and-LEFT — 见's identity bit for the terminal 钩
hook_len = 30
hook_angle_deg = -115  # up-and-slightly-left
hx1 = horiz_end_x + hook_len * math.cos(math.radians(hook_angle_deg))
hy1 = horiz_end_y + hook_len * math.sin(math.radians(hook_angle_deg))
dab(horiz_end_x, horiz_end_y, R)  # joining dab = segment radius
line_dabs(horiz_end_x, horiz_end_y, hx1, hy1, R, 1.0, steps=80)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_100_见__retry_2/01_见.png")
print("Wrote 01_见.png")
