"""
Render 神 (shen2) at 300x300, black ink on white.

Structural read from GT:
  Left: 礻 (示 as left radical, 4 strokes)
    1. 点  — top-left dot, angled down-right
    2. 横撇 — short horizontal then sharp sweep down-left
    3. 竖  — vertical crossing the horizontal
    4. 点  — right-side dot below the horizontal
  Right: 申 (5 strokes)
    - box (竖 left, 横折 top+right, 横 bottom)
    - 横 middle
    - 竖 long central vertical extending above and below the box
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

# =========================================================
# LEFT: 礻 radical (4 strokes)
# =========================================================

# 1) 点 — top-left small dot, slanting down-right
dot1 = bez((50, 60), (56, 68), (62, 76), (68, 82), n=30)
stroke(dot1, (4, 9))

# 2) 横撇 — short horizontal, then a sharp sweep down-left
#    Horizontal portion (a slight down-slope)
heng = bez((30, 108), (55, 106), (85, 106), (108, 110), n=50)
stroke(heng, (7, 8))
# shoulder dab at the 折 joint
dab(108, 110, 6)
# 撇 sweep after the shoulder
pie = bez((108, 110), (95, 140), (75, 180), (32, 230), n=70)
stroke(pie, (9, 4))

# 3) 竖 — vertical crossing the horizontal
shu_left = bez((72, 85), (72, 140), (72, 200), (72, 260), n=60)
stroke(shu_left, (8, 8))

# 4) 点 — right-side dot below the horizontal
dot2 = bez((92, 155), (100, 165), (108, 175), (115, 188), n=30)
stroke(dot2, (4, 10))

# =========================================================
# RIGHT: 申 (5 strokes)
# =========================================================
# Box: x=175..258, y=95..238
BX0, BX1 = 175, 258
BY0, BY1 = 95, 238
MID_Y = 168
CX = (BX0 + BX1) // 2  # central vertical x

# 1) 竖 (left side of box)
shu_l = bez((BX0, BY0), (BX0, (BY0+BY1)//2), (BX0, BY1-10), (BX0, BY1), n=60)
stroke(shu_l, (7, 7))

# 2) 横折 — top horizontal + right vertical (single stroke)
top = bez((BX0, BY0), ((BX0+BX1)//2, BY0-2), (BX1-15, BY0-2), (BX1, BY0+2), n=50)
stroke(top, (7, 8))
# shoulder dab
dab(BX1, BY0+2, 6)
right_side = bez((BX1, BY0+2), (BX1, (BY0+BY1)//2), (BX1, BY1-10), (BX1, BY1), n=60)
stroke(right_side, (8, 7))

# 3) 横 middle
mid = bez((BX0, MID_Y), ((BX0+BX1)//2, MID_Y-1), ((BX0+BX1)//2+15, MID_Y-1), (BX1, MID_Y+1), n=50)
stroke(mid, (6, 7))

# 4) 横 bottom
bot = bez((BX0-2, BY1), ((BX0+BX1)//2, BY1-1), ((BX0+BX1)//2+15, BY1-1), (BX1+2, BY1+1), n=50)
stroke(bot, (7, 8))

# 5) 竖 long central — extends above and below the box
central = bez((CX, 55), (CX, 130), (CX, 210), (CX, 278), n=90)
stroke(central, (9, 9))

# save
img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0463_神/01_神.png")
