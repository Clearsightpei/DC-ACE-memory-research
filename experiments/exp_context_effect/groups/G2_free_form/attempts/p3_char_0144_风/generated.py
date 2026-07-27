"""
风 (feng, wind) — p3_char_0144
Structure (per errata guidance for the FROZEN 风 case):
  1. Outer LEFT: 撇 — curved sweep from top-right area down to bottom-left.
     Must be a FULL curved sweep (Bezier control pulled right of chord midpoint),
     NOT a straight diagonal or vertical wall (that reads as 冈).
  2. Outer RIGHT+TOP: 横折弯钩 — short 横 across the top, shoulder,
     then 竖弯钩 sweeping right at the bottom and terminal hook
     flicking UP-and-LEFT.
  3. Interior: small 乂 (short 撇 + short 点/small 捺) — splayed like a V,
     not tightly overlapping.
Renderer: PIL brush-dabs and short line segments along Bezier samples.
300x300 white canvas, black ink.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier2(p0, p1, p2, t):
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
    return x, y


def taper_bezier(p0, p1, p2, r_start, r_end, steps=400):
    """Draw a quadratic Bezier as brush-dabs with linearly tapering radius."""
    for i in range(steps + 1):
        t = i / steps
        x, y = bezier2(p0, p1, p2, t)
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def taper_line(p0, p1, r_start, r_end, steps=300):
    for i in range(steps + 1):
        t = i / steps
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# ---------------------------------------------------------------
# STROKE 1: outer LEFT 撇 — curved sweep from upper-right to lower-left.
# 顿 dab at the start (top), Bezier control pulled to the RIGHT of the
# chord midpoint to make the outer wall bow (concave toward upper-right).
# ---------------------------------------------------------------
p0_pie = (110, 55)    # top start (just left of center)
p2_pie = (55, 265)    # bottom-left endpoint
ctrl_pie = (135, 175)  # control pulled RIGHT/down of chord midpoint (curved sweep)
dab(p0_pie[0], p0_pie[1], 6)  # 顿 press
taper_bezier(p0_pie, ctrl_pie, p2_pie, r_start=4.5, r_end=1.2, steps=500)

# ---------------------------------------------------------------
# STROKE 2: 横折弯钩 — the outer right/top/bottom sweep.
#   a) short 横 across the top
#   b) shoulder 顿 dab
#   c) 竖 slightly right (going down along the right side)
#   d) arc curving right-then-hook (弯钩)
#   e) hook flicks UP-and-LEFT
# ---------------------------------------------------------------
# (a) top 横: from just right of the 撇's top down to the top-right corner.
heng_start = (108, 60)
heng_end = (235, 55)
taper_line(heng_start, heng_end, r_start=4, r_end=4, steps=200)
dab(heng_end[0], heng_end[1], 5.5)  # shoulder 顿

# (b+c+d) 竖 -> 弯 (Bezier arc) sweeping down and out then curving right at bottom
# Start at heng_end, come straight down along the right side, then arc out
# rightward and end at the bottom-right — this is the classic 竖弯 sweep.
p0_arc = (235, 55)
p1_arc = (260, 230)   # bows the vertical outward (right)
p2_arc = (255, 265)   # bottom of the belly (near bottom-right)
taper_bezier(p0_arc, p1_arc, p2_arc, r_start=4.5, r_end=3.8, steps=500)

# (e) hook flick UP-and-LEFT from the end of the belly (~-125°)
hook_start = (255, 265)
hook_len = 34
hook_angle_deg = -120  # image coords: up-and-left
hx = hook_start[0] + hook_len * math.cos(math.radians(hook_angle_deg))
hy = hook_start[1] + hook_len * math.sin(math.radians(hook_angle_deg))
taper_line(hook_start, (hx, hy), r_start=3.8, r_end=1.0, steps=200)

# ---------------------------------------------------------------
# STROKE 3 & 4: interior 乂 (small 撇 + 点)
#   The interior sits in the middle-lower of the frame, splayed like a V,
#   NOT a tight X. Left leg = 撇 (curves down-left), right leg = 点/short 捺.
# ---------------------------------------------------------------
# Interior 乂: two legs that CROSS in the middle (X-shape), not a V.
# Left leg = 撇 (from upper-right down to lower-left)
# Right leg = 点/捺 (from upper-left down to lower-right)
# Their upper endpoints are SEPARATE and they cross around y~185.

# Left leg (撇): start upper-right, end lower-left
in_pie_p0 = (185, 130)
in_pie_p2 = (110, 240)
in_pie_c = (165, 195)
dab(in_pie_p0[0], in_pie_p0[1], 4.5)
taper_bezier(in_pie_p0, in_pie_c, in_pie_p2, r_start=3.5, r_end=1.0, steps=350)

# Right leg (点/短捺): start upper-left, end lower-right — crosses the 撇
in_dot_p0 = (135, 130)
in_dot_p2 = (215, 240)
in_dot_c = (155, 195)  # slight bow so it curves down-right
dab(in_dot_p0[0], in_dot_p0[1], 3.5)
taper_bezier(in_dot_p0, in_dot_c, in_dot_p2, r_start=2.5, r_end=3.8, steps=350)
dab(in_dot_p2[0], in_dot_p2[1], 4)  # small foot

# ---------------------------------------------------------------
img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0144_风/01_风.png")
print("Saved 01_风.png")
