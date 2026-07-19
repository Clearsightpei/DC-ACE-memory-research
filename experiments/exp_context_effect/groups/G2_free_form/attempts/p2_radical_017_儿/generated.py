"""
Radical 儿 (2 strokes): 撇 + 竖弯钩
Layout on 300x300:
  Stroke 1: 撇 — top around (110, 85), curves down-left to (75, 235). Gentle bow.
  Stroke 2: 竖弯钩 — starts upper (175, 85), descends as 竖 to (175, 190),
            smooth quarter-arc curving right to (230, 245), then hook flicks
            up (short vertical-ish flick) ending near (225, 205).
Rendered with PIL brush-dabs.
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


# ---------- Stroke 1: 撇 (left, curved throw-away) ----------
# Upper-right start → lower-left tip, thick→thin, more pronounced rightward
# bow (belly on right, concave-left). Standalone-scale: extend length &
# curvature; shrink start 顿 dab to r=6 (per standalone rule).
P0 = (120, 70)
P2 = (55, 250)
# Pull control point ~50 px off the chord midpoint toward the interior (right)
P1 = (115, 145)
# subtle start 顿 dab (standalone scale — no balloon)
dab(P0[0], P0[1], 6.5)
bezier_stroke(P0, P1, P2, r_start=8, r_end=1.2, steps=550, ease=1.15)


# ---------- Stroke 2: 竖弯钩 ----------
# Vertical 竖 segment
x_v = 180
y_top = 75
y_arc_start = 195  # where vertical ends and arc begins
# subtle 顿 dab at top (standalone scale)
dab(x_v, y_top, 6.5)
# straight vertical, uniform width, slight taper going into arc
steps_v = 300
r_v = 6.5
for i in range(steps_v + 1):
    t = i / steps_v
    y = y_top + (y_arc_start - y_top) * t
    dab(x_v, y, r_v)

# Smooth tangent-continuous quarter arc: vertical → rightward horizontal
# x = x0 + R*(1 - cos(t*pi/2)), y = y0 + R*sin(t*pi/2)
R = 45
x0, y0 = x_v, y_arc_start
steps_arc = 300
for i in range(steps_arc + 1):
    t = i / steps_arc
    x = x0 + R * (1 - math.cos(t * math.pi / 2))
    y = y0 + R * math.sin(t * math.pi / 2)
    dab(x, y, r_v)
arc_end_x = x0 + R  # 220
arc_end_y = y0 + R  # 240

# Short rightward horizontal continuation to give the 弯 body some length
x_h_end = 235
steps_h = 120
for i in range(steps_h + 1):
    t = i / steps_h
    x = arc_end_x + (x_h_end - arc_end_x) * t
    y = arc_end_y
    dab(x, y, r_v)

# Hook flick: from (x_h_end, arc_end_y) flicking upward (mostly vertical,
# slight left lean) — this is the 钩 of 竖弯钩. Longer flick for standalone.
hook_len = 55
hook_angle = math.radians(-95)  # nearly straight up, tiny left lean
hx0, hy0 = x_h_end, arc_end_y
hx1 = hx0 + hook_len * math.cos(hook_angle)
hy1 = hy0 + hook_len * math.sin(hook_angle)
# joining dab at hook start
dab(hx0, hy0, r_v + 2)
steps_hook = 250
for i in range(steps_hook + 1):
    t = i / steps_hook
    x = hx0 + (hx1 - hx0) * t
    y = hy0 + (hy1 - hy0) * t
    r = (r_v + 0.5) + (1.3 - (r_v + 0.5)) * t
    dab(x, y, r)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_017_儿/01_儿.png"
)
