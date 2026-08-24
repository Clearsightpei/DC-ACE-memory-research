"""
尢 retry #1. Prior attempt saved at ../p2_radical_080_尢/01_尢.png.

Prior-attempt defects (from GT-vs-attempt comparison):
  1. The 撇 was too curved (bellied LEFT). GT's 撇 is nearly straight
     with a very subtle rightward bow — reads as an elongated, mostly
     diagonal line, not a swoop.
  2. The 竖弯钩 terminal hook was too big and angled up-and-LEFT (~-112°).
     GT's hook on 尢's 竖弯钩 is small and nearly straight UP (short
     vertical flick, closer to -95° / -100°), NOT a diagonal.
  3. Middle 横 (一) was slightly too high and short. GT has it sitting
     in the upper-middle at ~y=115, spanning roughly x=80..190.

Structure this render targets (image coords, y grows DOWN):
  Stroke 1 (一 — short 横):
    from (85, 115) to (190, 110), thin uniform width, small end presses.
  Stroke 2 (撇 — long, mostly straight, subtle right-bow):
    from (145, 60) to (55, 265). Nearly straight; Bezier control
    only pulls RIGHTWARD by a few px (belly on right, opening left).
    Thick->thin taper. 顿 press at start.
  Stroke 3 (竖弯钩):
    Beat A: 竖 near-vertical from (170, 78) descending to ~(178, 235)
    (slight rightward drift). Small 顿 at top.
    Beat B: tangent-continuous quarter-arc R=28 sweeping into rightward
    horizontal. Arc ends at (206, 263). Short rightward extension to
    (228, 263).
    Beat C: hook flick ~22 px, angle -95° (nearly straight UP with
    a tiny leftward component). Taper r=5.5 -> 1.2.
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


# --- Stroke 1: 一 (short horizontal top, slight upward tilt)
h_p0 = (82, 116)
h_p1 = (192, 108)
dab(h_p0[0], h_p0[1], 5.5)   # small 顿 at start
line_stroke(h_p0, h_p1, r_start=5.0, r_end=4.8, steps=250)
dab(h_p1[0], h_p1[1], 5.8)   # small end press


# --- Stroke 2: 撇 (long, nearly straight, subtle belly-on-right)
p0 = (148, 62)
p2 = (52, 268)
# Control pulled slightly toward the right of the straight-line midpoint,
# giving a subtle right-bow (belly-on-right, opens LEFT). Straight midpoint
# is (100, 165); shift right by ~8 px.
ctrl = (108, 165)
dab(p0[0], p0[1], 8.5)  # 顿 press at start
bezier_stroke(p0, ctrl, p2, r_start=7.0, r_end=1.2, steps=520, ease=1.15)


# --- Stroke 3: 竖弯钩
# Beat A: near-vertical 竖 (very slight rightward drift)
v_p0 = (170, 78)
v_p1 = (178, 236)
dab(v_p0[0], v_p0[1], 6.5)   # 顿 at top
bezier_stroke(v_p0, (174, 155), v_p1, r_start=5.5, r_end=5.2, steps=300)

# Beat B: tangent-continuous arc from v_p1
x0, y0 = v_p1
R = 28
arc_steps = 140
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = x0 + R * (1 - math.cos(t * math.pi / 2))
    y = y0 + R * math.sin(t * math.pi / 2)
    dab(x, y, 5.0)
arc_end = (x0 + R, y0 + R)  # (206, 264)

# Short rightward extension after the arc lands
h2_end = (230, 262)
line_stroke(arc_end, h2_end, r_start=5.0, r_end=4.7, steps=140)

# Beat C: hook flick — nearly straight UP (very slight left-lean).
# Angle -95° in image coords = mostly up, tiny leftward component.
hook_len = 24
hook_angle_deg = -95
rad = math.radians(hook_angle_deg)
hx = h2_end[0] + hook_len * math.cos(rad)
hy = h2_end[1] + hook_len * math.sin(rad)
# joining dab equal to segment radius (NOT larger — avoid stray nub)
dab(h2_end[0], h2_end[1], 5.0)
line_stroke(h2_end, (hx, hy), r_start=5.0, r_end=1.3, steps=180)


out_path = (
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_080_尢__retry_1/01_尢.png"
)
img.save(out_path)
print(f"Saved {out_path}")
