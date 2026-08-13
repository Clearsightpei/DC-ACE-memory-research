"""
Render 便 (biàn) at 300x300, black ink on white.

Structural read from GT:
  Left: 亻 (person radical) — a short down-left 撇 at top-right of radical,
        then a tall 竖 dropping from near where the 撇 begins.
  Right: 更
    - top 横 (horizontal)
    - 曰-like box: left 竖, top-right corner 横折, middle 横 crossbar,
      bottom 横 closes the box
    - long 横 crossing under the box (the second 横 of 更 body)
    - 撇 sweeping down-left from center of box (through the crossbar area)
    - 捺 sweeping down-right (S-curve) meeting 撇 near center

Applies the 4-move calligraphic weight recipe (TIER-0 F):
  1. teardrop-taper on 撇/捺/点
  2. shoulder dabs at 折 corners
  3. bezier for curved sweeps
  4. no hooks in this character (便 has no 钩)
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


def dab(x, y, r=6):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ---------------- 亻 (left radical, ~x 40-95) ----------------
# 撇: short slash starting near top of radical, sweeping down-left
pie_r = bez((85, 55), (72, 90), (60, 115), (45, 140), n=60)
stroke(pie_r, (10, 4))

# 竖: tall vertical from just below the 撇's start, dropping to lower area
shu_r = bez((80, 90), (80, 150), (80, 210), (80, 265), n=60)
stroke(shu_r, (7, 6))

# ---------------- 更 (right side, ~x 110-270) ----------------
# top 横 (horizontal)
h_top = bez((120, 65), (160, 63), (220, 63), (260, 65), n=40)
stroke(h_top, (6, 6))

# left 竖 of the 曰 box
shu_L = bez((135, 80), (135, 115), (135, 145), (135, 170), n=40)
stroke(shu_L, (6, 6))

# top-right corner: 横折 — horizontal then folds down (right side of box)
hz_top = bez((135, 82), (170, 80), (215, 80), (245, 82), n=40)
stroke(hz_top, (6, 6))
dab(245, 82, r=5)  # shoulder dab at 折 corner
hz_side = bez((245, 82), (245, 110), (245, 140), (245, 170), n=40)
stroke(hz_side, (6, 5))

# middle 横 (crossbar inside box)
h_mid = bez((138, 125), (170, 124), (215, 124), (243, 125), n=40)
stroke(h_mid, (5, 5))

# bottom 横 closing the box (this is also the long crossing 横 of 更)
h_bot = bez((105, 175), (160, 173), (230, 173), (270, 175), n=40)
stroke(h_bot, (6, 7))

# 撇 of 更: sweeps down-left starting from just under the crossbar
pie_body = bez((175, 155), (160, 195), (130, 235), (95, 278), n=80)
stroke(pie_body, (10, 3))

# 捺 of 更: S-curve down-right, starts near crossbar center, meets 撇 region
na_body = bez((180, 175), (205, 210), (235, 245), (275, 272), n=80)
stroke(na_body, (4, 13))
# 捺 foot flare
foot = bez((270, 272), (275, 273), (280, 274), (283, 274), n=15)
stroke(foot, (12, 4))


img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0469_便/01_便.png"
)
