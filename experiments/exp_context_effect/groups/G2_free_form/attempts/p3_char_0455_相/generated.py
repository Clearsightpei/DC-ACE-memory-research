"""
Render 相 (xiang1) at 300x300, black ink on white.

Structure: 相 = 木 (left radical) + 目 (right block).

木 as left radical (compressed):
  横 short horizontal near top
  竖 long vertical through center
  撇 bowed pie sweeping down-left from cross point
  点 (捺 becomes 点 when 木 is a left radical) — small point on right

目 (right block, tall rectangle with 3 inner horizontals — top+bottom
frames from 折 + inner 2 short 横):
  横折 forming top-and-right frame
  竖 forming left frame
  横 bottom close
  two inner short 横

# SIGNATURE CHECK (from TIER-0 D, sibling table for 木 as component):
# 木 as LEFT radical: 撇 sweeps LEFT and its tail extends past the
# 竖's foot; the right side is a small 点 (NOT full 捺). 横 sits above
# the halfway point. 竖 is dominant vertical.
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

def shoulder_dab(x, y, r=5):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# ============================================================
# LEFT: 木 (compressed as left radical), roughly x=30..140
# ============================================================

# 横 — short horizontal, slight upslope
heng = bez((35, 105), (65, 102), (100, 100), (135, 98), n=50)
stroke(heng, (6, 6))

# 竖 — long vertical, centered in 木's box
shu = bez((88, 75), (88, 145), (88, 210), (88, 265), n=80)
stroke(shu, (8, 8))

# 撇 — bowed pie from just above cross-point, sweeping down-left, tapered
pie = bez((88, 118), (75, 155), (55, 200), (32, 250), n=80)
stroke(pie, (9, 3))

# 点 (right side of 木 as left radical — a small dot, NOT a full 捺)
dian = bez((92, 135), (108, 155), (122, 175), (135, 200), n=40)
stroke(dian, (3, 9))

# ============================================================
# RIGHT: 目, roughly x=170..265, y=55..275
# ============================================================

L, R = 170, 265
T, B = 55, 275

# 竖 (left frame)
left_v = bez((L, T + 3), (L, T + 80), (L, T + 150), (L, B), n=80)
stroke(left_v, (8, 8))

# 横折 (top and right frame) — top horizontal then 折 down to bottom
top_h = bez((L - 3, T), (L + 25, T - 2), (L + 60, T - 2), (R, T), n=60)
stroke(top_h, (7, 7))
# shoulder dab at the fold corner
shoulder_dab(R, T + 2, r=5)
# right vertical (from fold going down)
right_v = bez((R, T + 2), (R + 1, T + 80), (R + 1, T + 150), (R, B - 2), n=80)
stroke(right_v, (7, 7))

# bottom 横 (close of the box)
bottom_h = bez((L - 3, B), (L + 25, B + 1), (L + 60, B + 1), (R + 3, B), n=60)
stroke(bottom_h, (7, 7))

# inner 横 upper (about 1/3 down)
inner1 = bez((L + 6, T + 75), (L + 30, T + 74), (L + 55, T + 74), (R - 4, T + 76), n=50)
stroke(inner1, (5, 5))

# inner 横 lower (about 2/3 down)
inner2 = bez((L + 6, T + 150), (L + 30, T + 149), (L + 55, T + 149), (R - 4, T + 151), n=50)
stroke(inner2, (5, 5))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0455_相/01_相.png")
