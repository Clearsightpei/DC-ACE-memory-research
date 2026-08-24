"""
Character 儿 (2 strokes): 撇 + 竖弯钩.

Layout (from clean GT):
  - 撇 on left: starts high-center, curves down-and-left, ending at
    bottom-left. Slight leftward bow, thick→thin taper.
  - 竖弯钩 on right: starts high-right, straight vertical down, then
    smooth quarter arc curving right, ending with a short upward hook.
  - Both stroke tops sit around similar y (top of glyph).
  - Overall aspect: roughly square, centered on canvas.
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_stroke(P0, P1, P2, r_start, r_end, steps=500, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * P0[0] + 2 * u * t * P1[0] + t * t * P2[0]
        y = u * u * P0[1] + 2 * u * t * P1[1] + t * t * P2[1]
        tt = t ** ease
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


# ---------- Stroke 1: 撇 (left, curving down-and-left) ----------
# Start high, curve down and to the left, tapering to a fine tip
P0 = (120, 70)
P2 = (55, 255)
P1 = (115, 160)  # control point keeps the belly on the right side
dab(P0[0], P0[1], 7)  # subtle 顿 start dab
bezier_stroke(P0, P1, P2, r_start=8, r_end=1.2, steps=600, ease=1.15)


# ---------- Stroke 2: 竖弯钩 ----------
x_v = 185
y_top = 72
y_arc_start = 200
dab(x_v, y_top, 7)  # subtle 顿 start dab

r_v = 6.5
# vertical segment
steps_v = 300
for i in range(steps_v + 1):
    t = i / steps_v
    y = y_top + (y_arc_start - y_top) * t
    dab(x_v, y, r_v)

# tangent-continuous quarter arc: down → right
R = 42
x0, y0 = x_v, y_arc_start
steps_arc = 300
for i in range(steps_arc + 1):
    t = i / steps_arc
    x = x0 + R * (1 - math.cos(t * math.pi / 2))
    y = y0 + R * math.sin(t * math.pi / 2)
    dab(x, y, r_v)
arc_end_x = x0 + R  # 227
arc_end_y = y0 + R  # 242

# short rightward continuation before hook
x_h_end = 240
steps_h = 100
for i in range(steps_h + 1):
    t = i / steps_h
    x = arc_end_x + (x_h_end - arc_end_x) * t
    y = arc_end_y
    dab(x, y, r_v)

# hook flick — short, nearly straight up
hook_len = 32
hook_angle = math.radians(-92)
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
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0019_儿/01_儿.png"
)
