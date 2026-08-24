"""
Render 痈 at 300x300, black ink on white.

痈 = 疒 (canopy radical, FROZEN COHORT — 14x failed B12-B13) + 用 (interior).

# SIGNATURE CHECK (疒 frozen-radical, from memory_index.md TIER-0.G):
#   1) 5-stroke decomposition: 点 / 横 / 长撇 / inner 点 / 提
#   2) Inner 点+提 MUST sit VISIBLY INSIDE canopy's upper triangle
#      (bounded by 横 above, 撇 to the left). NOT dangling on 撇 stem.
#   3) Interior body (用) shrunk ~20% and tucked FULLY under 撇's belly.
#   4) Components MUST TOUCH (TIER-0.H): 用 must overlap 撇 sweep, no gap.
# CALLIGRAPHIC 4-MOVE (TIER-0.F):
#   - Teardrop taper on every 撇/捺/点 via stroke(widths=(a,b))
#   - Shoulder dab at every 折 joint (用's 横折钩)
#   - Bezier for curved sweeps (长撇, 横折钩's arc)
#   - Hook flick UP-and-LEFT (用's 竖钩 terminal + inner 提)

用 = 5 strokes: 撇 / 横折钩 / 横 / 横 / 竖 (中).
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def bez(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0]
        y = u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]
        pts.append((x, y))
    return pts


def stroke(pts, widths):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(n - 1, 1)
        if isinstance(widths, tuple):
            w = widths[0] + (widths[1] - widths[0]) * t
        else:
            w = widths
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ==============================================================
# 疒 canopy — 5 strokes
# ==============================================================

# (1) 点 — top-left dot (start of canopy)
dot1 = bez((115, 40), (112, 48), (110, 55), (108, 62), n=20)
stroke(dot1, (4, 8))

# (2) 横 — short-ish horizontal at top, slight rightward tilt down
h_top = bez((120, 68), (155, 66), (195, 66), (225, 70), n=50)
stroke(h_top, (6, 5))
# shoulder dab at right end for shoulder-hint (小 dab)
dab(225, 70, 4)

# (3) 长撇 — LONG sweeping 撇 down-left from just under 横 left end
#     This defines the canopy wedge. Bowed, taper thick->thin.
pie_long = bez((128, 60), (110, 130), (85, 190), (45, 265), n=90)
stroke(pie_long, (11, 4))

# (4) inner 点 — MUST sit INSIDE canopy triangle (between 横 and 撇)
#     Placed at roughly (108, 108) — clearly inside the wedge.
inner_dot = bez((105, 100), (108, 108), (112, 118), (115, 126), n=20)
stroke(inner_dot, (4, 8))

# (5) 提 — rising stroke inside canopy, from lower-left to upper-right,
#     terminating still INSIDE the wedge.
ti = bez((90, 148), (108, 143), (128, 138), (145, 132), n=40)
stroke(ti, (8, 3))


# ==============================================================
# 用 interior body — 5 strokes, tucked under 撇's belly, shrunk ~20%
# Positioned so its LEFT edge overlaps the 撇 stem (no gap).
# Body bounds approx: x=140..235, y=95..270
# ==============================================================

# (a) 撇 of 用 — short left descending stroke from top-left of frame
pie_yong = bez((155, 100), (150, 155), (145, 210), (140, 260), n=70)
stroke(pie_yong, (9, 5))

# (b) 横折钩 — the frame: top horizontal + right vertical + hook
#     top horizontal: (160, 105) to (235, 105)
htop_yong = bez((160, 105), (185, 103), (215, 103), (235, 106), n=50)
stroke(htop_yong, (7, 7))
# shoulder dab at 折 corner
dab(235, 106, 6)
# right vertical down
rv = bez((235, 108), (235, 155), (235, 210), (233, 260), n=70)
stroke(rv, (8, 7))
# hook flick UP-and-LEFT at bottom (~-115°)
hook = bez((233, 260), (228, 254), (222, 248), (215, 242), n=25)
stroke(hook, (8, 3))

# (c) middle 横 — first internal horizontal
h_mid1 = bez((155, 160), (185, 158), (215, 158), (233, 160), n=40)
stroke(h_mid1, (5, 5))

# (d) middle 横 — second internal horizontal (bottom of 日-like inner)
h_mid2 = bez((150, 215), (185, 213), (215, 213), (233, 215), n=40)
stroke(h_mid2, (5, 5))

# (e) center 竖 — vertical from top horizontal down through body
v_center = bez((193, 105), (192, 155), (191, 215), (190, 265), n=70)
stroke(v_center, (6, 6))


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0540_痈/01_痈.png")
