"""
Render 疴 (ke1, 'disease') at 300x300, black ink on white.

Structural read from GT:
  疴 = 疒 (illness canopy, left/top) + 可 (right-body tucked INSIDE canopy).

  疒 canopy (5 strokes per frozen_cohort.md 疒 row):
    (1) 点 top-left of 一
    (2) 横 long top
    (3) LONG curved 撇 identity-carrier
    (4) inner 点
    (5) 提 rising short flick

  可: 一 (short) + 口 (small, under 一) + 亅 (long 竖钩, hook UP-and-LEFT)

# SIGNATURE CHECK:
# - 疒 dominates: LONG 撇 to bottom-left
# - 可 tucked bottom-right, inside 撇 sweep (TIER-0 H — touch)
# - hook flicks UP-and-LEFT (TIER-0 B)
# - inner 点+提 pair present (avoid 广 collapse per B12)
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

def line_pts(p0, p1, n=40):
    return [(p0[0] + (p1[0]-p0[0])*i/n, p0[1] + (p1[1]-p0[1])*i/n) for i in range(n+1)]

def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# =========================================================
# 疒 canopy
# =========================================================

# (1) top-left 点
dian1 = bez((72, 45), (78, 52), (84, 58), (90, 66), n=25)
stroke(dian1, (3, 7))

# (2) 横 — long top horizontal
heng_pts = bez((55, 82), (110, 78), (175, 78), (230, 82), n=60)
stroke(heng_pts, (6, 6))
dab(230, 82, 6)

# (3) LONG 撇 — from right end of 横 sweeping down to bottom-left (identity)
pie = bez((230, 82), (185, 145), (115, 205), (55, 270), n=100)
stroke(pie, (11, 3))

# (4) inner 点
dian2 = bez((88, 120), (94, 128), (100, 136), (106, 145), n=25)
stroke(dian2, (3, 7))

# (5) 提 — rising short flick
ti = bez((78, 178), (94, 172), (110, 166), (126, 158), n=30)
stroke(ti, (8, 3))

# =========================================================
# 可 — tucked bottom-right
# =========================================================

# (a) 一 short 横 of 可 (upper)
he2 = bez((140, 128), (180, 126), (215, 126), (248, 130), n=50)
stroke(he2, (5, 5))
dab(248, 130, 6)

# (b) 口 — small square, below-left of the 亅 vertical
# Use line_pts to get proper polyline rendering
KL_X, KR_X = 158, 210
KT_Y, KB_Y = 168, 218
# top 横
stroke(line_pts((KL_X, KT_Y), (KR_X, KT_Y), n=35), 5)
# left 竖
stroke(line_pts((KL_X, KT_Y), (KL_X, KB_Y), n=35), 5)
# right 竖
stroke(line_pts((KR_X, KT_Y), (KR_X, KB_Y), n=35), 5)
# bottom 横
stroke(line_pts((KL_X, KB_Y), (KR_X, KB_Y), n=35), 5)
# shoulder dabs at 口 corners
for (cx, cy) in [(KL_X, KT_Y), (KR_X, KT_Y), (KR_X, KB_Y), (KL_X, KB_Y)]:
    dab(cx, cy, 4)

# (c) 亅 竖钩 — from right end of he2, drops long, then hook UP-and-LEFT
shu = bez((246, 130), (243, 180), (241, 225), (238, 262), n=70)
stroke(shu, (7, 6))
hook = bez((238, 262), (228, 256), (216, 250), (202, 242), n=25)
stroke(hook, (7, 3))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0522_疴/01_疴.png")
