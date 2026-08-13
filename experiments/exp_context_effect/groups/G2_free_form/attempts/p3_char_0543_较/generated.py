"""
Render 较 (jiao4) at 300x300, black ink on white.

Left = 车 radical (5 stroke encoding):
  1) 横 top (spans left..right of radical width)
  2) 横折 forming the top+right of the small middle box
  3) 横 middle (bottom of the box)
  4) 竖 long vertical piercing through the top 横, box, and continuing down
  5) 提 bottom rising stroke (up-and-right flick)
Right = 交 (6 strokes):
  1) 点 top center
  2) 横 long horizontal
  3) 撇 short top-left of 父
  4) 点 top-right of 父
  5) 撇 long down-left
  6) 捺 long down-right (crosses 撇)

TIER-0: components TOUCH (车's right edge nearly touches 交's leftmost point);
tapered 撇/捺/点/提; hook-free radical.
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


# =========================================================
# LEFT: 车 radical  (x range ~35..130)
# =========================================================

# 1) 横 top
h_top = bez((40, 85), (65, 82), (100, 82), (128, 85), n=45)
stroke(h_top, (6, 6))

# 2) 横折: horizontal from left, then folds down (top and right side of the small box)
#    horizontal segment
fold_h = bez((55, 115), (75, 113), (100, 113), (120, 115), n=35)
stroke(fold_h, (6, 6))
#    shoulder dab at corner
d.ellipse((115, 111, 125, 121), fill="black")
#    vertical segment (short) down from the corner
fold_v = bez((120, 115), (120, 128), (120, 142), (120, 155), n=30)
stroke(fold_v, (6, 6))

# 3) 横 middle (bottom of small box)
h_mid = bez((55, 155), (80, 153), (105, 153), (125, 155), n=40)
stroke(h_mid, (6, 6))

# 4) 竖 long vertical (from above top 横 down through the box, ending mid-body)
sh = bez((85, 68), (85, 130), (85, 180), (85, 220), n=70)
stroke(sh, (7, 7))

# 5) 提 bottom rising, up-and-right
ti = bez((42, 210), (65, 202), (95, 190), (130, 175), n=45)
stroke(ti, (10, 3))


# =========================================================
# RIGHT: 交  (x range ~140..280)
# =========================================================

# 1) 点 top center dot
dot_top = bez((198, 45), (200, 52), (202, 60), (204, 68), n=20)
stroke(dot_top, (4, 10))

# 2) 横 long horizontal
h_long = bez((148, 90), (185, 87), (225, 87), (275, 92), n=55)
stroke(h_long, (7, 7))

# 3) 撇 short top-left of 父 (starts just below the 横 on the left)
pie_tl = bez((180, 105), (170, 122), (162, 135), (152, 148), n=45)
stroke(pie_tl, (7, 3))

# 4) 点 top-right of 父
dot_tr = bez((238, 108), (243, 120), (248, 133), (253, 145), n=30)
stroke(dot_tr, (3, 9))

# 5) 撇 long: from mid-upper-right down to lower-left
pie_long = bez((220, 145), (198, 178), (172, 212), (145, 252), n=90)
stroke(pie_long, (10, 4))

# 6) 捺 long: from mid-upper-left down to lower-right (crosses the 撇)
na_main = bez((182, 150), (208, 182), (240, 215), (275, 250), n=90)
stroke(na_main, (5, 12))
# foot flare
foot = bez((275, 250), (280, 252), (284, 253), (288, 254), n=15)
stroke(foot, (12, 4))


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0543_较/01_较.png")
