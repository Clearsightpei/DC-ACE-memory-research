"""
Render 俏 (qiao4) at 300x300, black ink on white.

Structure: 亻 (left) + 肖 (right).
  亻: 撇 sweeping down-left from top, 竖 straight down starting mid-撇.
  肖 top: 小-shape — center short 竖, left 点/撇, right 点.
  肖 bottom (月-like): left 撇 curving down-left, right 横折钩 (top-right
    corner, down-right side, hook flicks UP-LEFT at bottom), two short
    inner horizontals.

# SIGNATURE CHECK: components MUST TOUCH — 亻 竖 tail extends near
# baseline of 月; 肖-top strokes connect visually to 月 top edge.
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

# ============ 亻 (left) ============
# 撇: from top-center-left, curving down-left, teardrop taper
pie_ren = bez((92, 55), (85, 100), (70, 140), (48, 190), n=80)
stroke(pie_ren, (10, 4))

# 竖: from middle of 撇 straight down
shu_ren = bez((88, 110), (88, 160), (88, 210), (88, 250), n=60)
stroke(shu_ren, (8, 7))

# ============ 肖 top (小-shape) ============
# center short 竖 (top dot-stroke)
top_center = bez((198, 45), (198, 60), (198, 75), (198, 88), n=30)
stroke(top_center, (7, 6))

# left 点/撇 of 小 — short flick down-left
top_left = bez((178, 55), (170, 68), (162, 78), (155, 90), n=30)
stroke(top_left, (7, 3))

# right 点 of 小 — short flick down-right
top_right = bez((218, 55), (228, 68), (236, 78), (244, 90), n=30)
stroke(top_right, (3, 8))

# ============ 月 body (bottom of 肖) ============
# left 撇 — top-left of 月, curves gently down-left, teardrop tail
yue_left = bez((160, 105), (155, 155), (150, 205), (140, 258), n=80)
stroke(yue_left, (9, 5))
# shoulder dab at top of 月
dab(160, 105, 5.5)

# 横折钩 — top horizontal, corner, right vertical, hook UP-LEFT
# top horizontal
yue_top = bez((160, 105), (185, 103), (215, 103), (245, 106), n=50)
stroke(yue_top, (7, 7))
# shoulder dab at top-right corner
dab(245, 108, 6.5)
# right vertical (slight inward curve)
yue_right = bez((245, 108), (243, 160), (240, 210), (236, 255), n=70)
stroke(yue_right, (8, 7))
# hook flick UP-and-LEFT
hook = bez((236, 255), (230, 250), (222, 244), (214, 238), n=25)
stroke(hook, (7, 3))

# ============ two inner horizontals of 月 ============
inner1 = bez((165, 155), (190, 154), (215, 154), (238, 156), n=40)
stroke(inner1, (5, 5))

inner2 = bez((165, 200), (190, 199), (215, 199), (238, 201), n=40)
stroke(inner2, (5, 5))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0484_俏/01_俏.png")
