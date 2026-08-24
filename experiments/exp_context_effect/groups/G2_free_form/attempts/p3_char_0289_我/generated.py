"""
我 (Phase-3 character, 7 strokes)

# SIGNATURE CHECK: 我 contains 戈 as right-side component. 戈 = 横+斜钩+撇+点.
# The 斜钩 must sweep down-right with UP-and-LEFT hook flick (~-110°),
# NOT a plain diagonal. See TIER-0/B: hook flicks UP-and-LEFT always.
# Left half: 撇 (top-left tick) + 横 short + 竖钩 (drops down with up-left hook) +
# 提 (rising stroke from mid-left).
# Adapted from p3_char_0243_成 template — same right side (斜钩+撇+点),
# left side upgraded from single 撇 to (short 撇 + 短横 + 竖钩 + 提).

Stroke order:
  1) 撇   top-left tick (small)
  2) 横   short horizontal (left half, mid-upper)
  3) 竖钩 vertical dropping through the 横, hooks up-left at bottom
  4) 提   rising stroke, from mid-left low
  5) 斜钩 dominant diagonal from upper-mid to bottom-right, hook up-left
  6) 撇   short 撇 crossing the 斜钩 in upper belly
  7) 丶   dot upper-right, above the 斜钩 top
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


# 1) top-left 撇 tick — short, from ~(90,60) flicking down-left
pie0_p0 = (95, 55)
pie0_p2 = (65, 105)
pie0_c = (78, 75)
dab(pie0_p0[0], pie0_p0[1], 6)
bezier_dabs(pie0_p0, pie0_c, pie0_p2, 5.5, 1.5)

# 2) short 横 (mid-upper, left half) — from left of 撇-tip across to below 斜钩 origin
h1_s = (55, 115)
h1_e = (155, 108)
dab(h1_s[0], h1_s[1], 6)
line_dabs(h1_s, h1_e, 5.0, 5.0)
dab(h1_e[0], h1_e[1], 6)

# 3) 竖钩 — from top of 横 down, hooks up-and-left at bottom
sg_top = (105, 108)
sg_bot = (105, 230)
dab(sg_top[0], sg_top[1], 6)
line_dabs(sg_top, sg_bot, 5.5, 5.5)
# hook flick up-and-left ~-155°
hook_len = 32
hook_angle = math.radians(-155)
hx = sg_bot[0] + hook_len * math.cos(hook_angle)
hy = sg_bot[1] + hook_len * math.sin(hook_angle)
dab(sg_bot[0], sg_bot[1], 5.5)
line_dabs(sg_bot, (hx, hy), 5.5, 1.2, steps=200)

# 4) 提 — rising stroke from mid-left (below the 横), rising to upper-right
ti_s = (55, 195)
ti_e = (140, 165)
line_dabs(ti_s, ti_e, 5.5, 1.2, steps=250)
dab(ti_s[0], ti_s[1], 6)

# 5) 斜钩 — dominant, from upper-mid to lower-right, belly on lower-left
xg_p0 = (150, 78)
xg_p2 = (275, 250)
xg_c = (155, 220)  # belly pulled lower-left
dab(xg_p0[0], xg_p0[1], 6.5)
bezier_dabs(xg_p0, xg_c, xg_p2, 5.5, 3.5, steps=500)
# hook flick UP-and-LEFT (~-112°)
hook_len2 = 42
hook_angle2 = math.radians(-112)
hx2 = xg_p2[0] + hook_len2 * math.cos(hook_angle2)
hy2 = xg_p2[1] + hook_len2 * math.sin(hook_angle2)
dab(xg_p2[0], xg_p2[1], 3.8)
line_dabs(xg_p2, (hx2, hy2), 3.8, 1.0, steps=200)

# 6) internal short 撇 — crosses upper belly of 斜钩, flicks down-left
pie2_p0 = (200, 155)
pie2_p2 = (150, 220)
pie2_c = (170, 195)
dab(pie2_p0[0], pie2_p0[1], 5.5)
bezier_dabs(pie2_p0, pie2_c, pie2_p2, 4.5, 1.0)

# 7) 丶 — teardrop dot at upper-right, above 斜钩 top
d0 = (215, 55)
d1 = (245, 88)
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
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0289_我/01_我.png"
)
