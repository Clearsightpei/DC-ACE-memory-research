"""
Render 俐 (li4) at 300x300, black ink on white.

Structural read: 俐 = 亻 + 利, where 利 = 禾 + 刂.
Layout is L-M-R:
  Left:   亻 (撇 + 竖) at x~30-75
  Middle: 禾 (撇, 横, 竖, 撇, 捺) at x~90-210
  Right:  刂 (短竖 + 竖钩 with UP-LEFT hook flick) at x~215-270

Uses the 4-move calligraphic-weight recipe: bezier curves + variable
width taper + shoulder at joints (implicit via overlapping strokes) +
correct UP-LEFT hook flick.
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


# ================== 亻 (left radical) ==================
# 撇: starts upper, sweeps down-left with a slight bow, taper thin at tail
pie_ren = bez((82, 55), (72, 100), (60, 135), (35, 168), n=80)
stroke(pie_ren, (10, 4))

# 竖: starts where 撇 begins (near top of the radical), straight down;
# nudged right so it approaches 禾's 横 leftmost point (rule H — touch)
shu_ren = bez((85, 105), (85, 160), (85, 210), (85, 258), n=60)
stroke(shu_ren, (8, 8))

# ================== 禾 (middle of 利) ==================
# 撇 (top short): downward-left flick at the very top
pie_top = bez((160, 45), (150, 60), (140, 72), (125, 85), n=50)
stroke(pie_top, (8, 3))

# 横: horizontal beam
heng = bez((95, 108), (130, 106), (170, 106), (210, 110), n=60)
stroke(heng, (7, 7))

# 竖: main vertical of 禾, down the middle
shu_he = bez((152, 108), (152, 160), (152, 215), (152, 265), n=70)
stroke(shu_he, (8, 8))

# 撇: crossing stroke, from just below 横 sweeping down-left
pie_he = bez((145, 140), (130, 165), (115, 190), (95, 215), n=60)
stroke(pie_he, (9, 3))

# 捺: crossing stroke, from just below 横 sweeping down-right with a foot
na_main = bez((155, 140), (175, 170), (195, 195), (210, 218), n=60)
stroke(na_main, (4, 11))
# foot flare at end of 捺
foot = bez((210, 218), (216, 220), (222, 221), (226, 222), n=15)
stroke(foot, (11, 3))

# ================== 刂 (right radical) ==================
# 短竖 (short left vertical of 刂)
shu_short = bez((225, 115), (225, 145), (225, 165), (225, 180), n=40)
stroke(shu_short, (7, 6))

# 竖钩 (tall right vertical with hook)
shu_gou = bez((262, 100), (262, 160), (262, 220), (262, 258), n=70)
stroke(shu_gou, (8, 8))
# hook flick UP-and-LEFT
hook = bez((262, 258), (256, 253), (250, 247), (244, 240), n=20)
stroke(hook, (8, 3))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0486_俐/01_俐.png")
