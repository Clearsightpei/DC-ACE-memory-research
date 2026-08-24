"""
Render 疥 (jie4) at 300x300, black ink on white.

Structural read from GT:
  疒 (sickness radical, 5 strokes) wrapping top-left:
    1. 点 top-left
    2. 横 running right along the top
    3. 撇 long, sweeping from near top-right down to lower-left
    4. 点 inside upper-left (below the 横, right of the 撇)
    5. 提 inside lower-left (rising tick)
  介 (4 strokes) nestled inside the wrap:
    6. 撇 apex down-left
    7. 捺 apex down-right (with foot)
    8. 竖撇 left inner
    9. 竖 right inner
Applies calligraphic-weight 4-move: teardrop tapers, shoulder dabs,
bezier sweeps, UP-and-LEFT hook flicks (none here).
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


# ============ 疒 (sickness radical) ============

# 1. 点 top-left (short down-right teardrop)
p1 = bez((65, 30), (70, 42), (76, 52), (82, 60), n=25)
stroke(p1, (3, 9))

# 2. 横 top horizontal — from near the top dot area sweeping right
h_top = bez((80, 72), (135, 66), (190, 64), (245, 62), n=60)
stroke(h_top, (6, 6))
# shoulder dab at right end where the horizontal meets the 撇 origin
dab(245, 64, 5)

# 3. 撇 long left-sweep from near right end of 横 down to lower-left
pie_long = bez((110, 65), (90, 140), (60, 210), (25, 280), n=100)
stroke(pie_long, (10, 4))

# 4. 点 inside upper (below horizontal, right of long 撇)
p4 = bez((80, 120), (86, 130), (92, 140), (98, 150), n=25)
stroke(p4, (3, 8))

# 5. 提 inside lower (rising tick from lower-left up to right)
ti = bez((60, 195), (72, 190), (85, 182), (100, 172), n=30)
stroke(ti, (8, 3))

# ============ 介 (nestled inside/below the wrap) ============

# 6. 撇 apex — from top center-right sweeping down-left (stops mid, doesn't cross 疒 撇)
jie_pie = bez((185, 100), (170, 145), (155, 185), (135, 230), n=80)
stroke(jie_pie, (10, 4))

# 7. 捺 apex — from same apex sweeping down-right with foot
jie_na = bez((185, 110), (210, 150), (230, 195), (250, 240), n=80)
stroke(jie_na, (4, 12))
foot = bez((250, 240), (255, 243), (260, 245), (263, 247), n=15)
stroke(foot, (12, 3))

# 8. 竖撇 inner-left — slightly curved down-left
jie_left = bez((175, 175), (170, 210), (165, 245), (158, 278), n=60)
stroke(jie_left, (7, 4))

# 9. 竖 inner-right — straight down
jie_right = bez((215, 175), (215, 210), (215, 245), (215, 278), n=60)
stroke(jie_right, (7, 7))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0448_疥/01_疥.png")
