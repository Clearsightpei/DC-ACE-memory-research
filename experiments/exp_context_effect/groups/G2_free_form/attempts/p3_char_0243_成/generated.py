"""
成 (Phase-3 character, 6 strokes) — revision 2

Revised for better proportions matching GT:
  - top 横 shortened and better integrated near the 斜钩 top
  - outer 撇 shortened and less steep (doesn't reach the bottom)
  - 斜钩 bowed more prominently, occupies right half + bottom-right
  - internal short 横 anchors the mid-left compact zone
  - internal small 撇 tucked in the belly
  - 丶 sits above-right of the 斜钩 origin

PIL brush-dab technique on 300x300 white canvas.
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(p0, p1, r0, r1, steps=300):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=400):
    x0, y0 = p0
    xc, yc = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        omt = 1 - t
        x = omt * omt * x0 + 2 * omt * t * xc + t * t * x2
        y = omt * omt * y0 + 2 * omt * t * yc + t * t * y2
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# 1) top short 横 (upper-left, near start of 撇 and near 斜钩 top)
h1_s = (80, 92)
h1_e = (150, 84)
dab(h1_s[0], h1_s[1], 6)
line_dabs(h1_s, h1_e, 5.0, 5.0)
dab(h1_e[0], h1_e[1], 6)

# 2) outer 撇 — shorter, less steep, ending mid-lower-left
pie1_p0 = (100, 90)
pie1_p2 = (60, 245)
pie1_c = (72, 175)
dab(pie1_p0[0], pie1_p0[1], 6)
bezier_dabs(pie1_p0, pie1_c, pie1_p2, 5.5, 1.2)

# 3) short internal 横 (crosses the 撇, mid-belt)
h2_s = (72, 158)
h2_e = (165, 152)
dab(h2_s[0], h2_s[1], 5.5)
line_dabs(h2_s, h2_e, 4.8, 4.8)
dab(h2_e[0], h2_e[1], 5.5)

# 4) 斜钩 — dominant, from upper-mid to lower-right, belly on lower-left
xg_p0 = (140, 78)
xg_p2 = (275, 250)
xg_c = (145, 220)          # belly pulled lower-left
dab(xg_p0[0], xg_p0[1], 6.5)
bezier_dabs(xg_p0, xg_c, xg_p2, 5.5, 3.5, steps=500)

# hook flick from xg_p2, up-and-slightly-left, ~ -112 deg
hook_len = 42
hook_angle_deg = -112
hx = xg_p2[0] + hook_len * math.cos(math.radians(hook_angle_deg))
hy = xg_p2[1] + hook_len * math.sin(math.radians(hook_angle_deg))
dab(xg_p2[0], xg_p2[1], 3.8)
line_dabs(xg_p2, (hx, hy), 3.8, 1.0, steps=200)

# 5) internal small 撇 — tucked in the belly, flicks down-left
pie2_p0 = (185, 175)
pie2_p2 = (140, 250)
pie2_c = (160, 215)
dab(pie2_p0[0], pie2_p0[1], 5.5)
bezier_dabs(pie2_p0, pie2_c, pie2_p2, 4.5, 1.0)

# 6) 丶 — teardrop dot at upper-right, above 斜钩 top
d0 = (210, 55)
d1 = (240, 88)
steps = 200
for i in range(steps + 1):
    t = i / steps
    tt = t ** 1.4
    x = d0[0] + (d1[0] - d0[0]) * t
    y = d0[1] + (d1[1] - d0[1]) * t
    r = 2 + (10 - 2) * tt
    dab(x, y, r)
dab(d1[0], d1[1], 10)


img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0243_成/01_成.png"
)
