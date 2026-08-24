"""
Render 速 (sù) at 300x300, black ink on white.

Structural read from GT:
  Left/bottom: 辶 (walking radical)
    - small 点 top-left (~55,55)
    - short 横撇 below the dot (a curly hook, ~50-90, y~90-115)
    - long 平捺 sweep — starts left, dips, sweeps right ending with foot flare
  Upper-right: 束 (bundle)
    - top 横 (short horizontal, ~y=45)
    - 口 box roughly x=125-215, y=55-130
    - 竖 through center (x=170, y=25-215)
    - 撇 sweeps down-left from mid-vertical (~y=140 to bottom-left)
    - 捺 sweeps down-right from mid-vertical (~y=140 to bottom-right)

Apply calligraphic 4-move: teardrop tapers, shoulder dabs at 折,
Bezier sweeps for 撇/捺, hook flick UP-LEFT.
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


# ====== 束 upper-right ======

# 1. top 横 (short) — x=125..215, y=48
top_h = bez((125, 48), (155, 46), (185, 46), (215, 50), n=40)
stroke(top_h, (5, 6))

# 2. 竖 through center (x=170, y=25..215) — long central vertical
v_center = bez((170, 25), (170, 90), (170, 160), (170, 215), n=80)
stroke(v_center, (6, 6))

# 3. 口 box — left vertical
box_l = bez((128, 58), (128, 85), (128, 110), (128, 135), n=40)
stroke(box_l, (5, 5))

# 4. 口 box — right vertical + hook at bottom (implied via折)
box_r_top = bez((213, 58), (213, 75), (213, 95), (213, 115), n=40)
stroke(box_r_top, (5, 5))
# shoulder dab at box top-right折 corner
dab(213, 58, 4)

# 5. 口 box — top horizontal (short, connects box_l top to box_r top)
box_top = bez((128, 58), (155, 56), (185, 56), (213, 58), n=40)
stroke(box_top, (4, 4))

# 6. 口 box — bottom 横 (middle of 束)
box_bot = bez((125, 135), (155, 133), (185, 133), (217, 137), n=40)
stroke(box_bot, (5, 6))

# 7. 撇 — sweep from ~ (170,140) down-left to ~ (108, 215)
pie = bez((170, 145), (155, 165), (135, 190), (108, 215), n=80)
stroke(pie, (9, 4))

# 8. 捺 — sweep from ~ (170,140) down-right to ~ (240, 210), with foot flare
na = bez((170, 145), (188, 168), (215, 188), (238, 208), n=80)
stroke(na, (5, 12))
# foot flare
foot = bez((238, 208), (246, 210), (253, 212), (258, 213), n=20)
stroke(foot, (12, 3))

# ====== 辶 walking radical (bottom-left wrap) ======

# 9. 点 top-left dot
d1 = bez((55, 52), (60, 60), (63, 68), (66, 76), n=30)
stroke(d1, (4, 9))

# 10. 横撇 — the 3-fold curly bit under the dot
#    a small horizontal then bends down-left
hp1 = bez((45, 100), (60, 96), (75, 96), (88, 100), n=40)
stroke(hp1, (4, 5))
# shoulder dab at fold
dab(88, 100, 5)
# then swings down-left
hp2 = bez((88, 100), (75, 118), (60, 135), (48, 152), n=50)
stroke(hp2, (5, 4))

# 11. 平捺 — the long bottom sweep of 辶
#     starts around (48, 152), dips low, sweeps up-right to (270, 255), foot flare
pna_a = bez((48, 152), (55, 190), (75, 235), (130, 262), n=80)
stroke(pna_a, (5, 10))
pna_b = bez((130, 262), (180, 268), (225, 260), (265, 250), n=80)
stroke(pna_b, (10, 13))
# foot flare at right end
foot2 = bez((265, 250), (272, 251), (278, 252), (282, 253), n=20)
stroke(foot2, (13, 3))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0531_速/01_速.png")
