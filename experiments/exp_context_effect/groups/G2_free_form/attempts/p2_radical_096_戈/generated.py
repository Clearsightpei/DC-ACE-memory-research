"""
戈 (radical, 4 strokes)
Composition:
  1) 横 (heng) — mid-upper horizontal, slight up-tilt
  2) 斜钩 (xie-gou) — dominant long diagonal from upper-mid to lower-right,
     belly-on-lower-left curvature, ending in up-and-slightly-left hook flick
  3) 撇 (pie) — from upper-mid area going down-and-left, crosses the 横
  4) 丶 (dian) — small teardrop dot at upper-right, above the 斜钩

Uses PIL brush-dab technique on 300x300 white canvas.
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(p0, p1, r0, r1, steps=400):
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


# --------------------------------------------------------------------------
# 1) 横 (heng): mid-upper horizontal, slight up-tilt
#    Positioned so the 斜钩 starts just above/left of its left endpoint
#    and the 撇 crosses through it near its left.
# --------------------------------------------------------------------------
heng_start = (55, 122)
heng_end = (215, 110)     # slight up-tilt
dab(heng_start[0], heng_start[1], 6)              # smaller 顿 (standalone)
line_dabs(heng_start, heng_end, 5.0, 5.0, steps=300)
dab(heng_end[0], heng_end[1], 5.5)                 # small terminal press

# --------------------------------------------------------------------------
# 2) 斜钩 (xie-gou): dominant diagonal, belly on lower-left
#    Proven params scaled/positioned for 戈 layout:
#    - P0 near upper area, above and slightly right of the 横's left half
#    - P2 lower-right
#    - control pulled to lower-left => belly on lower-left (concave up-right)
#    Then hook flick from P2 going up-and-slightly-left ~ -110 deg
# --------------------------------------------------------------------------
xg_p0 = (110, 68)
xg_p2 = (265, 235)
xg_ctrl = (125, 215)          # pulled MORE toward lower-left => pronounced belly
dab(xg_p0[0], xg_p0[1], 6.5)  # smaller start dab
bezier_dabs(xg_p0, xg_ctrl, xg_p2, 5.5, 3.5, steps=500)

# hook flick from xg_p2 at ~ -110 deg, length ~ 42 px, taper
hook_len = 42
hook_angle_deg = -112
hx = xg_p2[0] + hook_len * math.cos(math.radians(hook_angle_deg))
hy = xg_p2[1] + hook_len * math.sin(math.radians(hook_angle_deg))
dab(xg_p2[0], xg_p2[1], 3.8)  # small joining dab (NOT r+2 per corollary)
line_dabs(xg_p2, (hx, hy), 3.8, 1.0, steps=200)

# --------------------------------------------------------------------------
# 3) 撇 (pie): from upper area (starting inside/right of the 斜钩 P0 region)
#    throwing down-and-left, crossing THROUGH the 横.
#    Must start above/right of the 横 and end below/left of it — visible crossing.
# --------------------------------------------------------------------------
pie_p0 = (145, 95)
pie_p2 = (35, 265)            # extend much further down-left
pie_ctrl = (115, 195)         # gentle rightward bow
dab(pie_p0[0], pie_p0[1], 6.5)  # smaller 顿 start (standalone)
bezier_dabs(pie_p0, pie_ctrl, pie_p2, 5.5, 1.2, steps=500)

# --------------------------------------------------------------------------
# 4) 丶 (dian): small teardrop at upper-right, above/right of the 斜钩 top
# --------------------------------------------------------------------------
d0 = (218, 55)
d1 = (248, 92)
steps = 200
for i in range(steps + 1):
    t = i / steps
    tt = t ** 1.4
    x = d0[0] + (d1[0] - d0[0]) * t
    y = d0[1] + (d1[1] - d0[1]) * t
    r = 2 + (10 - 2) * tt
    dab(x, y, r)
dab(d1[0], d1[1], 11)  # terminal press


img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_096_戈/01_戈.png"
)
