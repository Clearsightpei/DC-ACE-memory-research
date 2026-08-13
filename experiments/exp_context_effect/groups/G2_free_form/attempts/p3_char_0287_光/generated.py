"""
Character 光 (6 strokes): ⺌ top + 一 middle + 儿 bottom.

Stroke order:
  1. 竖 (small vertical) — top-center, short.
  2. 撇 (short) — upper-left going down-left.
  3. 点 (short 撇/dot) — upper-right going down-right (mirrors stroke 2).
  4. 横 — long horizontal across the middle (wide, spans past top marks).
  5. 撇 — long, starts center-under-横, throws down-left to bottom-left.
  6. 竖弯钩 — starts middle-right under 横, straight down, quarter arc
     right, terminal hook flicks UP-and-slightly-LEFT (per TIER-0 hook rule).

Layout notes (from GT):
  - Top three marks are all SHORT and sit above the 横.
  - The 横 is the widest stroke — it establishes the character body.
  - Below 横: 撇 on left + 竖弯钩 on right (儿 shape), splaying outward.
  - Reuses the 儿 sub-shape geometry from p3_char_0019_儿 (PASSed reference).
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_stroke(P0, P1, P2, r_start, r_end, steps=400, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * P0[0] + 2 * u * t * P1[0] + t * t * P2[0]
        y = u * u * P0[1] + 2 * u * t * P1[1] + t * t * P2[1]
        tt = t ** ease
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


def line_stroke(P0, P1, r_start, r_end, steps=200, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        x = P0[0] + (P1[0] - P0[0]) * t
        y = P0[1] + (P1[1] - P0[1]) * t
        tt = t ** ease
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


# ---------- Stroke 1: 竖 (short vertical, top-center) ----------
dab(150, 42, 6)
line_stroke((150, 42), (150, 78), r_start=6, r_end=4.5, steps=120)

# ---------- Stroke 2: 撇 (short, upper-left) ----------
# Small flick going down-and-left from upper area
dab(102, 62, 6)
bezier_stroke((102, 62), (95, 82), (78, 108),
              r_start=6, r_end=1.5, steps=200, ease=1.2)

# ---------- Stroke 3: 点 (short right mark, mirrors stroke 2) ----------
# Small stroke going down-right from upper area
dab(198, 62, 5.5)
bezier_stroke((198, 62), (208, 82), (225, 105),
              r_start=5.5, r_end=2.0, steps=200, ease=1.2)

# ---------- Stroke 4: 横 (long horizontal across middle) ----------
dab(38, 130, 7)  # left 顿
line_stroke((38, 130), (262, 130), r_start=6.5, r_end=6.5, steps=400)
dab(262, 130, 7.5)  # right 顿 slightly heavier

# ---------- Stroke 5: 撇 (long, lower-left leg) ----------
# Starts just under middle of 横, throws down-left tapering to a tip
dab(140, 138, 7)
bezier_stroke((140, 138), (110, 210), (55, 275),
              r_start=7.5, r_end=1.2, steps=500, ease=1.15)

# ---------- Stroke 6: 竖弯钩 (right leg with hook) ----------
x_v = 178
y_top = 138
y_arc_start = 225
dab(x_v, y_top, 7)

r_v = 6.5
# vertical segment
steps_v = 250
for i in range(steps_v + 1):
    t = i / steps_v
    y = y_top + (y_arc_start - y_top) * t
    dab(x_v, y, r_v)

# quarter arc: down → right
R = 40
x0, y0 = x_v, y_arc_start
steps_arc = 300
for i in range(steps_arc + 1):
    t = i / steps_arc
    x = x0 + R * (1 - math.cos(t * math.pi / 2))
    y = y0 + R * math.sin(t * math.pi / 2)
    dab(x, y, r_v)
arc_end_x = x0 + R  # 218
arc_end_y = y0 + R  # 265

# short rightward continuation before hook
x_h_end = 240
steps_h = 100
for i in range(steps_h + 1):
    t = i / steps_h
    x = arc_end_x + (x_h_end - arc_end_x) * t
    y = arc_end_y
    dab(x, y, r_v)

# hook flick — UP and slightly LEFT (TIER-0 hook rule ~-100°)
hook_len = 30
hook_angle = math.radians(-100)
hx0, hy0 = x_h_end, arc_end_y
hx1 = hx0 + hook_len * math.cos(hook_angle)
hy1 = hy0 + hook_len * math.sin(hook_angle)
dab(hx0, hy0, r_v)
steps_hook = 200
for i in range(steps_hook + 1):
    t = i / steps_hook
    x = hx0 + (hx1 - hx0) * t
    y = hy0 + (hy1 - hy0) * t
    r = (r_v + 0.3) + (1.2 - (r_v + 0.3)) * t
    dab(x, y, r)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0287_光/01_光.png"
)
