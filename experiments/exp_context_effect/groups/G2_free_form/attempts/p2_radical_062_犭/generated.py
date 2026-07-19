"""犭 (dog-radical, 3 strokes). PIL brush-dab render, 300x300.

Revision pass. Composition (image coords, y grows DOWN):
  Stroke 1 (top 撇): upper-right → lower-left, CROSSING the spine near
           its top. Endpoints on opposite sides of spine.
  Stroke 2 (弯钩 spine): main long curve, belly-on-right, from upper-left
           down to lower-mid ending with an up-left hook flick.
  Stroke 3 (middle 撇): starts on the RIGHT of the spine at mid-height,
           throws down-left, ending on the LEFT of the spine (visible
           crossing signature per drawer_memory rule #3).

Standalone-scale discipline: canvas filled generously, curvature
pronounced, no oversized 顿-ball at endpoints.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_taper(p0, p1, r0, r1, steps=400):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_taper(p0, p1, p2, r0, r1, steps=400):
    x0, y0 = p0
    xc, yc = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * x0 + 2 * u * t * xc + t * t * x2
        y = u * u * y0 + 2 * u * t * yc + t * t * y2
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# --- Stroke 2: 弯钩 spine (draw first so overlaps look natural on top) ---
# Spine goes from upper area (around y=70) down to lower-mid (y=245),
# belly-on-right (control x well to the right of chord midline).
sp_start = (155, 68)
sp_ctrl = (215, 175)
sp_end = (168, 250)
dab(sp_start[0], sp_start[1], 6)
bezier_taper(sp_start, sp_ctrl, sp_end, r0=5.5, r1=4.8, steps=500)

# Hook flick from bottom endpoint, up-and-left (~-115°)
hook_len = 32
hook_angle = math.radians(-115)
hx = sp_end[0] + hook_len * math.cos(hook_angle)
hy = sp_end[1] + hook_len * math.sin(hook_angle)
line_taper(sp_end, (hx, hy), r0=4.8, r1=1.2, steps=200)

# --- Stroke 1: top 撇 crossing the spine near the top ---
# Starts upper-right of spine top (~y=55, right of spine),
# throws down-and-left, ending LEFT of spine (~x<spine at that y).
# Spine at y≈95 is approximately x=175 (right-bulging). We want stroke 1
# to cross the spine around y=88 and end at lower-left.
s1_p0 = (200, 50)
s1_ctrl = (180, 78)
s1_p2 = (120, 118)
dab(s1_p0[0], s1_p0[1], 7)
bezier_taper(s1_p0, s1_ctrl, s1_p2, r0=6.5, r1=1.4, steps=350)

# --- Stroke 3: middle 撇 crossing through spine ---
# Starts on RIGHT of spine at mid-height (spine at y≈155 is around x=200),
# throws down-left ending on LEFT of spine at lower area.
s3_p0 = (215, 138)
s3_ctrl = (170, 175)
s3_p2 = (85, 230)
dab(s3_p0[0], s3_p0[1], 7)
bezier_taper(s3_p0, s3_ctrl, s3_p2, r0=6.5, r1=1.5, steps=400)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_062_犭/01_犭.png"
)
