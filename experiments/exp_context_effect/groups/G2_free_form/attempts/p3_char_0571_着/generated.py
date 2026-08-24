"""
Render 着 at 300x300, black ink on white.

# SIGNATURE CHECK:
# 着 = 丷 (two slant dots) + three 横 + long 撇 crossing + 目 (bottom body)
# 11 strokes total (羊-top variant + 目).
# Top zone: y=25..135 (dots + 3 horizontals).
# 撇 sweeps from top-right area (near x=175,y=55) down through the horizontals
# to bottom-left (~x=45,y=245), passing THROUGH the horizontals.
# 目 sits bottom-right, tucked to right side under the 撇 belly.
# Applies calligraphic-weight 4-move: teardrop taper on 撇/点, shoulder dab
# at 折 joint of 目, bezier sweep on 撇, no hooks here so hook rule N/A.
# Components MUST touch: 撇 crosses horizontals; 目 top touches bottom 横.
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


def shoulder_dab(x, y, r=5.5):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# --- Top: 丷 (two slant dots/short 撇 pair) ---
# left dot: short stroke going down-LEFT (like 点/撇)
left_dot = bez((125, 30), (118, 40), (110, 52), (100, 62), n=30)
stroke(left_dot, (4, 8))

# right dot: short stroke going down-RIGHT (mirror)
right_dot = bez((180, 30), (188, 42), (196, 54), (205, 65), n=30)
stroke(right_dot, (4, 8))

# --- Three horizontals of the top (羊-like) ---
# horizontal 1 (upper) — spans mid width, slight up-right tilt
h1 = bez((95, 78), (140, 76), (185, 76), (215, 78), n=40)
stroke(h1, (6, 6))

# horizontal 2 (middle)
h2 = bez((90, 108), (140, 106), (190, 106), (220, 108), n=40)
stroke(h2, (6, 6))

# --- Long 撇 sweeping down-left across, teardrop taper thick->thin ---
pie = bez((175, 55), (150, 115), (110, 170), (48, 250), n=100)
stroke(pie, (12, 4))

# horizontal 3 (bottom of top / above 目) — this is the long 横
h3 = bez((75, 148), (135, 146), (195, 146), (238, 149), n=50)
stroke(h3, (7, 7))

# --- 目 body (bottom-right) ---
# left vertical (竖)
mu_left = bez((133, 158), (133, 200), (133, 240), (133, 278), n=50)
stroke(mu_left, (6, 6))

# top-right 横折: horizontal + shoulder dab + vertical
mu_top = bez((133, 158), (170, 157), (210, 157), (235, 158), n=40)
stroke(mu_top, (6, 6))
shoulder_dab(233, 159, r=5.5)
mu_right = bez((233, 158), (232, 198), (231, 238), (230, 278), n=50)
stroke(mu_right, (6, 6))

# inner 横 (upper interior)
mu_i1 = bez((140, 195), (170, 194), (200, 194), (223, 195), n=30)
stroke(mu_i1, (5, 5))

# inner 横 (lower interior)
mu_i2 = bez((140, 235), (170, 234), (200, 234), (223, 235), n=30)
stroke(mu_i2, (5, 5))

# bottom 横 of 目 — connect left to right
mu_bot = bez((133, 278), (170, 277), (200, 277), (230, 278), n=40)
stroke(mu_bot, (6, 6))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0571_着/01_着.png")
