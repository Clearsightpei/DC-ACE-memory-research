"""
Render radical 尢 (3 strokes) at 300x300, black ink on white.
Structure (image coords, y grows DOWN):
  Stroke 1 (撇): long throw-away. Start upper-mid ~(150, 60), curve
                 down-and-left to lower-left tip ~(70, 260). Bezier
                 with control pulled toward the interior (right).
                 Thick->thin taper. Small 顿 press at start.
  Stroke 2 (横): short horizontal, crossing the 撇. From ~(90, 138)
                 rightward to ~(200, 128), slight upward tilt.
                 Uniform width, subtle end press.
  Stroke 3 (竖弯钩): starts at top ~(178, 78), short vertical/slightly
                 curved segment descending to ~(185, 235), then a
                 smooth quarter-arc rightward to ~(238, 258), then a
                 short up-and-slightly-left hook flick ending ~(232, 232).
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_stroke(p0, p1, p2, r_start, r_end, steps=400, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        tt = t ** ease
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


def line_stroke(p0, p1, r_start, r_end, steps=300):
    for i in range(steps + 1):
        t = i / steps
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# --- Stroke 1: 撇 (long throw-away, upper-right start -> lower-left tip)
p0 = (150, 60)
p2 = (65, 262)
ctrl = (140, 150)  # pull toward interior/right for gentle bow
dab(p0[0], p0[1], 9)  # 顿 press at start
bezier_stroke(p0, ctrl, p2, r_start=7.5, r_end=1.3, steps=500, ease=1.2)

# --- Stroke 2: 横 (short, tilts slightly up), crossing the 撇
h_p0 = (88, 140)
h_p1 = (205, 128)
dab(h_p0[0], h_p0[1], 6)  # small 顿 at start
line_stroke(h_p0, h_p1, r_start=5.0, r_end=4.8, steps=250)
dab(h_p1[0], h_p1[1], 6)  # small end press

# --- Stroke 3: 竖弯钩 (vertical descending, arcs right, ends in up-left hook)
# Beat A: near-vertical/slightly slanted 竖 from top-right down.
v_p0 = (182, 78)
v_p1 = (188, 235)  # slight rightward drift as it descends
# small 顿 at top
dab(v_p0[0], v_p0[1], 6.5)
# Draw the vertical as a very gentle Bezier
bezier_stroke(v_p0, (185, 155), v_p1, r_start=5.5, r_end=5.2, steps=300)

# Beat B: tangent-continuous quarter-arc from (188, 235) sweeping into
# rightward horizontal. Uses proven KEY PRIMITIVE parametrization.
x0, y0 = v_p1
R = 26
arc_steps = 120
last = (x0, y0)
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = x0 + R * (1 - math.cos(t * math.pi / 2))
    y = y0 + R * math.sin(t * math.pi / 2)
    dab(x, y, 5.0)
    last = (x, y)
# Beat B continues: short rightward extension after the arc lands
# arc ends at (x0 + R, y0 + R) = (214, 261)
arc_end = (x0 + R, y0 + R)
h2_end = (238, 258)
line_stroke(arc_end, h2_end, r_start=5.0, r_end=4.8, steps=120)

# Beat C: hook flick (up-and-slightly-left) from h2_end
# angle roughly -110 to -120 degrees in image coords
hook_len = 32
hook_angle_deg = -112
rad = math.radians(hook_angle_deg)
hx = h2_end[0] + hook_len * math.cos(rad)
hy = h2_end[1] + hook_len * math.sin(rad)
# joining dab at base (do NOT exceed segment radius — hook joint discipline)
dab(h2_end[0], h2_end[1], 5.0)
line_stroke(h2_end, (hx, hy), r_start=5.0, r_end=1.2, steps=200)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_080_尢/01_尢.png"
)
print("Saved 01_尢.png")
