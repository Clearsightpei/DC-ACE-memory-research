"""
Render 疰 (zhu4) at 300x300, black ink on white.

疒 canopy (5 strokes):
  (1) 点 at top-left of 一
  (2) 横 long top spanning canopy width
  (3) LONG curved 撇 from right end of 横 down to bottom-left (identity)
  (4) inner 点 below 横, right of 撇
  (5) 提 short rising flick BELOW inner 点

Body 主 tucked bottom-right INSIDE the canopy sweep (5 strokes):
  top 点, upper 横, middle 横, 竖 (long vertical), bottom 横.

TIER-0 rules applied: components touch (body tucked under 撇 sweep),
teardrop tapers, bezier curves for 撇, shoulder dab at 折 corners.
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

# ===== 疒 canopy =====

# (1) top-left 点 (short diagonal dot)
p1 = bez((85, 45), (82, 55), (80, 65), (78, 75), n=25)
stroke(p1, (3, 7))

# (2) 横 long top — starts inside/right of the 点, spans to right edge
h_top = bez((70, 78), (130, 74), (200, 74), (245, 78), n=50)
stroke(h_top, (6, 6))

# (3) LONG 撇 — from right end of 横 (or just left of it) curving down-left
pie = bez((100, 78), (85, 130), (70, 190), (45, 275), n=90)
stroke(pie, (10, 4))

# (4) inner 点 — small dot just below 横, right of the 撇
inner_dot = bez((92, 105), (88, 118), (85, 128), (82, 135), n=25)
stroke(inner_dot, (4, 8))

# (5) 提 rising flick — short, from lower-left rising up-right, below inner 点
ti = bez((70, 165), (85, 158), (100, 152), (115, 148), n=30)
stroke(ti, (8, 3))

# ===== 主 body — tucked bottom-right inside canopy =====

# top 点 (slanted dot above top 横 of 主)
zdot = bez((175, 100), (180, 108), (185, 115), (188, 122), n=25)
stroke(zdot, (3, 8))

# upper 横 (short)
zh1 = bez((150, 138), (185, 135), (220, 135), (245, 139), n=40)
stroke(zh1, (5, 5))

# middle 横 (a bit longer)
zh2 = bez((135, 185), (180, 182), (225, 182), (255, 186), n=40)
stroke(zh2, (5, 5))

# 竖 (long vertical passing through all horizontals)
zshu = bez((195, 135), (196, 190), (197, 240), (197, 275), n=60)
stroke(zshu, (8, 7))

# bottom 横 (longest, base — extends fully across body)
zh3 = bez((120, 273), (175, 270), (235, 270), (275, 275), n=50)
stroke(zh3, (6, 7))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0516_疰/01_疰.png")
