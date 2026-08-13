"""
Render 侯 (hóu, marquis) at 300x300, black ink on white.

Structure (9 strokes):
  Left: 亻 — 撇 + 竖 (person radical, left column x=35-95)
  Right (x=100-275):
    Top: 𠂉-hood — short 撇 + long 一 (across the top of right block)
    Middle: short 一 (under the hood)
    Bottom: 矢-like — 一 + big 大 shape (vertical 竖 with 撇 and 捺
            diverging from mid-vertical)

Uses TIER-0 F recipe: bez() + stroke() with variable widths, teardrop
taper on 撇/捺, shoulder dab at 折 joints.
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


# ---------------- 亻 (left) ----------------
# 1. 撇 — from ~(80, 55) sweep down-left, teardrop taper
pie_ren = bez((80, 55), (72, 100), (62, 145), (42, 195), n=70)
stroke(pie_ren, (10, 4))

# 2. 竖 — vertical from mid of 撇 (~(78, 95)) straight down
shu_ren = bez((78, 95), (78, 155), (78, 215), (78, 265), n=60)
stroke(shu_ren, (7, 7))

# ---------------- Right block ----------------
# 3. Short 撇 top-left of right block (part of 𠂉 hood)
pie_top = bez((150, 45), (142, 55), (135, 65), (128, 78), n=40)
stroke(pie_top, (7, 3))

# 4. Long 一 — hood horizontal, from end of the short 撇 across to the right
# small shoulder dab at the joint
dab(130, 76, 5)
h_top = bez((128, 76), (170, 74), (215, 74), (265, 78), n=60)
stroke(h_top, (7, 7))
# slight thickening at right end (typical 一 ending)
dab(263, 78, 5.5)

# 5. Middle short 一 (under the hood)
h_mid = bez((150, 128), (185, 126), (220, 126), (250, 130), n=50)
stroke(h_mid, (6, 6))
dab(249, 130, 5)

# 6. 矢 top 一 (short, above the 大 part)
h_bot = bez((140, 175), (175, 173), (215, 173), (255, 176), n=50)
stroke(h_bot, (6, 6))
dab(253, 176, 5)

# 7. 竖 — vertical of the 大, from top of 矢 area down through
shu_mid = bez((195, 130), (195, 175), (195, 210), (195, 232), n=50)
stroke(shu_mid, (7, 7))

# 8. 撇 — from mid-vertical sweep down-left (part of 大 bottom)
pie_da = bez((195, 205), (170, 225), (145, 245), (115, 268), n=70)
stroke(pie_da, (9, 3))

# 9. 捺 — from same origin sweep down-right, thickening to a foot
na = bez((195, 205), (220, 225), (245, 250), (272, 272), n=70)
stroke(na, (4, 12))
# foot flare
foot = bez((272, 272), (275, 272), (278, 272), (280, 272), n=15)
stroke(foot, (12, 4))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0464_侯/01_侯.png")
