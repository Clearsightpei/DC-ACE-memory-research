"""
G2 retry_3 for p2_radical_011_匕 (2画).

Target: 匕 = 撇 + 竖弯钩.

Retry_2 FAIL diagnosis: 撇 endpoint was too far left (x=55) but its body
did NOT visibly CROSS THROUGH the 竖. Result read as 七 (top-flick
floating above/around the vertical, not passing through it).

Retry_3 fixes (per errata + form_catalog "撇 as body-crossing diagonal"):
  1. 撇 must be LONG (~150-170 px). Start UPPER-RIGHT well above the
     top of the 竖, end LOWER-LEFT well past the 竖 body.
  2. 撇 BODY must physically overlap the 竖 line — the crossing point
     lies in the UPPER THIRD of the vertical (around y=115).
  3. Top pixel of 撇 must be visibly ABOVE the top of the 竖.
  4. Terminal 钩 hook of 竖弯钩 must be present (up-and-slightly-left).

HARD RULE (memory_index): 匕 vs 七 sibling bit — 匕's top is a 撇
(upper-right → lower-left diagonal), NOT a 横. Render the canonical
sibling-table form; do not talk myself out of it.
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_stroke(p0, p1, p2, r_start, r_end, steps=440, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        tt = t ** ease
        mt = 1 - t
        x = mt * mt * p0[0] + 2 * mt * t * p1[0] + t * t * p2[0]
        y = mt * mt * p0[1] + 2 * mt * t * p1[1] + t * t * p2[1]
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


# =========================================================================
# Stroke 1: 竖弯钩 — vertical → smooth rightward arc → up-left hook
# =========================================================================
vx = 100                # vertical x-position
v_top = 100             # top of vertical (below the 撇's start y)
v_bot = 210             # bottom of vertical before arc begins
r_body = 6.5

# 顿 press at top
dab(vx, v_top, r_body + 1.5)

# Vertical body
for i in range(220 + 1):
    t = i / 220
    y = v_top + (v_bot - v_top) * t
    dab(vx, y, r_body)

# Quarter arc (tangent-continuous): vertical → rightward horizontal
R = 42
arc_end_x = vx + R
arc_end_y = v_bot + R
for i in range(180 + 1):
    t = i / 180
    x = vx + R * (1 - math.cos(t * math.pi / 2))
    y = v_bot + R * math.sin(t * math.pi / 2)
    dab(x, y, r_body)

# Rightward 横 continuation
h_end_x = 215
h_y = arc_end_y
for i in range(200 + 1):
    t = i / 200
    x = arc_end_x + (h_end_x - arc_end_x) * t
    dab(x, h_y, r_body)

# Terminal 钩 hook — up-and-slightly-left, mandatory
hook_len = 34
hook_angle = math.radians(-105)   # image coords: -90=up
hook_end_x = h_end_x + hook_len * math.cos(hook_angle)
hook_end_y = h_y + hook_len * math.sin(hook_angle)

dab(h_end_x, h_y, r_body)         # join dab

for i in range(140 + 1):
    t = i / 140
    x = h_end_x + (hook_end_x - h_end_x) * t
    y = h_y + (hook_end_y - h_y) * t
    r = r_body + (1.2 - r_body) * t
    dab(x, y, r)


# =========================================================================
# Stroke 2: 撇 — LONG body-crossing diagonal (upper-right → lower-left)
# =========================================================================
# form_catalog "撇 as body-crossing diagonal":
#   LONG (~150-180 px), moderate slope, MUST cross through the 竖 with
#   BODY overlapping and top pixel ABOVE the crossed line.
#
# 竖 spans y=100..210 at x=100.
# Start upper-right at y≈60 (visibly ABOVE v_top=100).
# End lower-left at y≈180, x≈45 (well past x=100 leftward).
# Crossing of vx=100 happens around y≈115 (upper-third of 竖 — matches
# "upper-third crossing" spec from B1 retry note).
p0 = (200, 60)    # upper-right start — ABOVE the vertical's top
p1 = (140, 110)   # control near the crossing point for a natural bow
p2 = (45, 175)    # lower-left endpoint — well past the 竖

# 顿笔 press at start
dab(p0[0], p0[1], 9)

bezier_stroke(p0, p1, p2, r_start=10.0, r_end=1.4, steps=460, ease=1.15)

# =========================================================================
img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p2_radical_011_匕__retry_3/01_匕.png"
)
