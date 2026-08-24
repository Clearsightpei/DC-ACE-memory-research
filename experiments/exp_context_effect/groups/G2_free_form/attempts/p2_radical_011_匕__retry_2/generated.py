"""
G2 retry_2 for p2_radical_011_匕 (2画).

Target: 匕 = 撇 + 竖弯钩.

Errata fixes applied for this retry (from retry_1 diagnosis):
  1. Hook was ABSENT in retry_1 — must draw the terminal 钩 flick as
     an explicit final step. ~30–35 px @ ~-105° from the bottom of the
     L (up-and-slightly-left).
  2. 撇 started too high, tip crossed the vertical near y≈5% depth.
     Start 撇 higher (upper-right around y=55) and land tip lower so
     it crosses the 竖 at ~30% depth of the vertical.

Standalone-scale principles honored: gentle bow on 撇, hook length ~1/3
of terminal beat, endpoint 顿-dabs kept modest (r+1 not r+2).
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_stroke(p0, p1, p2, r_start, r_end, steps=420, ease=1.0):
    """Sample a quadratic Bezier as brush-dabs with linear radius taper."""
    for i in range(steps + 1):
        t = i / steps
        tt = t ** ease
        mt = 1 - t
        x = mt * mt * p0[0] + 2 * mt * t * p1[0] + t * t * p2[0]
        y = mt * mt * p0[1] + 2 * mt * t * p1[1] + t * t * p2[1]
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


# =========================================================================
# Stroke 1: 竖弯钩 (vertical → smooth rightward arc → up-and-left hook)
# =========================================================================
# Vertical descends from around (95, 90) to (95, 210). Then smooth arc
# (KEY PRIMITIVE) into a rightward horizontal, landing near (200, 245).
# Terminal hook flicks up-and-slightly-left from the arc's rightmost end.

# --- 竖 body (top to bottom, straight vertical) ---
vx = 95
v_top = 90
v_bot = 210
r_body = 6.5

# 顿 press at start (modest, r+1 for standalone)
dab(vx, v_top, r_body + 1.5)

steps_v = 220
for i in range(steps_v + 1):
    t = i / steps_v
    y = v_top + (v_bot - v_top) * t
    dab(vx, y, r_body)

# --- tangent-continuous quarter-arc (vertical → rightward horizontal) ---
# Start tangent (0, +) at (vx, v_bot); end tangent (+, 0) after R.
R = 42
arc_steps = 180
arc_end_x = vx + R
arc_end_y = v_bot + R  # end of arc = start of horizontal segment
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = vx + R * (1 - math.cos(t * math.pi / 2))
    y = v_bot + R * math.sin(t * math.pi / 2)
    dab(x, y, r_body)

# --- rightward 横 running from arc end onward ---
h_end_x = 210
h_y = arc_end_y  # same y — chain from arc endpoint
steps_h = 200
for i in range(steps_h + 1):
    t = i / steps_h
    x = arc_end_x + (h_end_x - arc_end_x) * t
    dab(x, h_y, r_body)

# --- terminal 钩 (mandatory final step — the key retry fix) ---
# Flick up-and-slightly-left from (h_end_x, h_y). Length ~34 px,
# angle ~-105° in image coords (i.e. mostly up, slightly leftward).
hook_len = 34
hook_angle_deg = -105  # image coords: 0=right, -90=up, -180=left
hook_angle = math.radians(hook_angle_deg)
hook_end_x = h_end_x + hook_len * math.cos(hook_angle)
hook_end_y = h_y + hook_len * math.sin(hook_angle)

# joining dab at hook base equal to segment radius (principle 5 corollary)
dab(h_end_x, h_y, r_body)

hook_steps = 140
for i in range(hook_steps + 1):
    t = i / hook_steps
    x = h_end_x + (hook_end_x - h_end_x) * t
    y = h_y + (hook_end_y - h_y) * t
    r = r_body + (1.2 - r_body) * t  # taper thick → sharp
    dab(x, y, r)

# =========================================================================
# Stroke 2: 撇 (upper-right → lower-left, gentle rightward bow)
# =========================================================================
# Per errata: start higher so tip crosses 竖 at ~30% depth.
# Vertical spans y=90..210 (Δ=120). 30% depth ≈ y=126. Tip should land
# to the LEFT of the 竖 (vx=95). So P2 ≈ (55, 155) — clearly past the
# vertical, tip below the 30%-depth crossing.
p0 = (175, 55)   # upper-right start (higher than retry_1)
p1 = (150, 105)  # control pulled toward interior for gentle bow
p2 = (55, 155)   # lower-left tip, past the 竖

# 顿笔 at start (modest for standalone — r=8)
dab(p0[0], p0[1], 8)

bezier_stroke(p0, p1, p2, r_start=9.5, r_end=1.4, steps=440, ease=1.1)

# =========================================================================
img.save(
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p2_radical_011_匕__retry_2/01_匕.png"
)
