"""
Render 俳 (fei2) at 300x300, black ink on white.

Structure: 亻 (left) + 非 (right)
  亻 : 撇 (down-left curve from top) + 竖 (straight down from mid-撇)
  非 : left vertical + 3 short horizontals extending RIGHT from it (toward center)
       right vertical + 3 short horizontals extending RIGHT from it (outward)

TIER-0 notes:
- No hook in this character (no 钩).
- 亻 竖 must TOUCH/overlap the 非 body horizontally (H rule): 亻 竖 sits
  around x=90 and 非 leftmost stroke starts around x=115, close enough
  that the horizontal ticks from 非's left vertical begin near x=125.
- Compound: apply calligraphic 4-move (taper on 撇, bezier curves,
  shoulder dabs unnecessary here since no 折 joints).
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

# ============ 亻 (person radical, left) ============
# 撇: top around (105, 55), sweeps down-left with taper thick→thin
pie = bez((108, 55), (95, 100), (78, 135), (55, 175), n=80)
stroke(pie, (10, 4))

# 竖: from mid-撇 (around x=88, y=115) straight down
shu = bez((88, 115), (88, 175), (88, 235), (88, 275), n=60)
stroke(shu, (8, 7))

# ============ 非 (right) ============
# Left vertical of 非
lv = bez((140, 65), (140, 130), (140, 200), (140, 275), n=60)
stroke(lv, (8, 7))

# 3 horizontals extending RIGHT from left vertical (like flags going right toward middle)
h1L = bez((140, 100), (160, 100), (180, 100), (198, 100), n=30)
stroke(h1L, (6, 5))
h2L = bez((140, 155), (160, 155), (180, 155), (200, 155), n=30)
stroke(h2L, (6, 5))
h3L = bez((140, 210), (160, 210), (180, 210), (200, 210), n=30)
stroke(h3L, (6, 5))

# Right vertical of 非
rv = bez((225, 65), (225, 130), (225, 200), (225, 275), n=60)
stroke(rv, (8, 7))

# 3 horizontals extending RIGHT from right vertical (outward, past the vertical)
h1R = bez((225, 100), (245, 100), (263, 100), (280, 100), n=30)
stroke(h1R, (6, 5))
h2R = bez((225, 155), (245, 155), (263, 155), (280, 155), n=30)
stroke(h2R, (6, 5))
h3R = bez((225, 210), (245, 210), (263, 210), (280, 210), n=30)
stroke(h3R, (6, 5))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0558_俳/01_俳.png")
