"""木 (mù, tree) — Phase-2 radical, 4 strokes: 横 竖 撇 捺.

Rendered with PIL brush-dabs on 300x300 white canvas, black ink.
Layout: 横 crosses through upper-third; 竖 runs full vertical through
the 横's midpoint; 撇 launches from the cross-point down-and-left;
捺 launches from the cross-point down-and-right (thin->thick foot).
Strokes share the central cross joint (per shared-joint principle).
"""

from PIL import Image, ImageDraw
import math

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=400, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        omt = 1 - t
        x = omt * omt * p0[0] + 2 * omt * t * p1[0] + t * t * p2[0]
        y = omt * omt * p0[1] + 2 * omt * t * p1[1] + t * t * p2[1]
        tt = t ** ease
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)


# ---- Anchors ----
# Cross joint (center of the character body)
CX, CY = 150, 130

# ---- 1. 横 (heng): horizontal, left -> right, roughly at y=CY ----
# Slight up-tilt, uniform width, subtle endpoint press only (r+1) to
# avoid ball-tumor artifact at standalone scale.
h_x0, h_y0 = 70, 133
h_x1, h_y1 = 230, 127
r_h = 4.5
dab(h_x0, h_y0, r_h + 1)  # subtle start
line_dabs(h_x0, h_y0, h_x1, h_y1, r_h, r_h, steps=350)
dab(h_x1, h_y1, r_h + 1)  # subtle end

# ---- 2. 竖 (shu): vertical, top -> bottom, through the cross ----
# GT shows a very small top-press artifact and a plain blunt bottom.
# Use subtle endpoint radii (r+1) not r+2.
v_x0, v_y0 = 150, 55
v_x1, v_y1 = 150, 268
r_v = 5.0
dab(v_x0, v_y0, r_v + 1)  # subtle top press
line_dabs(v_x0, v_y0, v_x1, v_y1, r_v, r_v, steps=400)
dab(v_x1, v_y1, r_v)  # plain blunt bottom

# ---- 3. 撇 (pie): from cross-point down-and-left, thick->thin ----
# Gentle rightward-belly bow via quadratic bezier.
pie_p0 = (CX, CY + 2)
pie_p2 = (55, 255)
pie_p1 = (115, 205)  # control pulls into the interior/right for gentle bow
bezier_dabs(pie_p0, pie_p1, pie_p2, r0=8.5, r1=1.4, steps=420, ease=1.15)
# start dun-dab to seat at joint
dab(pie_p0[0], pie_p0[1], 9)

# ---- 4. 捺 (na): from cross-point down-and-right, thin->thick foot ----
# Slight downward-belly bow. Thin start ramping to broad terminal press.
na_p0 = (CX + 2, CY + 2)
na_p2 = (255, 255)
na_p1 = (190, 195)  # control pulls slightly below chord for gentle bow
bezier_dabs(na_p0, na_p1, na_p2, r0=2.8, r1=10.5, steps=420, ease=1.3)
# broad terminal press (flat foot)
dab(na_p2[0], na_p2[1], 11)
dab(na_p2[0] - 4, na_p2[1] + 1, 10)

out = (
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p2_radical_104_木/01_木.png"
)
img.save(out)
print(f"saved {out}")
