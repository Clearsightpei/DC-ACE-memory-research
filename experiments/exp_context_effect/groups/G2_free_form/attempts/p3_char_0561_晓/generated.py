"""
Render 晓 (xiao3) at 300x300, black ink on white.

# SIGNATURE CHECK:
# 晓 = 日 (left, narrow tall) + 尧 (right)
# 尧 = top (戈-like slash + 2 short horizontals stacked with tiny vertical)
#      + 兀 (横 + 撇 + 竖弯钩, hook flick UP-and-LEFT)
# TIER-0 H: components MUST touch — 日 right edge nearly meets 尧 left strokes.
# TIER-0 B: 竖弯钩 hook flicks UP-and-LEFT into character body.
# TIER-0 F: use bez() + stroke() with taper on 撇/捺, shoulder dab at 折 joints.
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


def dab(x, y, r=4.5):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# =============== LEFT: 日 (narrow tall rectangle w/ middle bar) ===============
# columns: x_left=45, x_right=105  rows: y_top=80, y_mid=150, y_bot=220
# 1. 竖 (left vertical)
stroke(bez((48, 82), (48, 130), (48, 180), (48, 222), n=50), (7, 6))
# 2. 横折 (top horizontal + right descending vertical)
stroke(bez((48, 82), (72, 80), (95, 80), (105, 82), n=40), (6, 6))
dab(105, 82, 5)  # shoulder dab
stroke(bez((105, 82), (105, 130), (105, 180), (105, 222), n=50), (6, 6))
# 3. 横 (middle bar)
stroke(bez((52, 152), (72, 151), (92, 151), (102, 152), n=30), (5, 5))
# 4. 横 (bottom, closes rectangle)
stroke(bez((48, 222), (72, 221), (92, 221), (105, 222), n=30), (6, 6))


# =============== RIGHT UPPER: 尧 top = 戈-like slash + stacked shorts ===============
# Long down-right diagonal (looks like a 撇/丿 that curves from upper right to mid-left)
# From GT: a strong slash starts near top-right around (245, 55) descending left to (160, 155)
stroke(bez((240, 55), (218, 90), (192, 125), (162, 158), n=80), (10, 5))

# Upper short horizontal (near top, left of the slash)
stroke(bez((140, 95), (165, 93), (188, 93), (205, 96), n=40), (6, 5))
# Tiny vertical/dot connecting the two horizontals (small tick)
stroke(bez((172, 96), (172, 108), (172, 120), (172, 130), n=25), (5, 5))
# Middle short horizontal (a bit lower and shifted)
stroke(bez((138, 135), (162, 134), (188, 134), (210, 136), n=40), (6, 5))


# =============== RIGHT LOWER: 兀 (横 + 撇 + 竖弯钩) ===============
# 一 (top horizontal of 兀, long, spans right side)
stroke(bez((130, 178), (170, 176), (215, 176), (260, 180), n=50), (7, 6))
dab(258, 180, 5)

# 丿 (left leg — 撇, curves down-left)
stroke(bez((160, 180), (152, 210), (142, 240), (128, 268), n=70), (7, 4))

# 竖弯钩 (right leg — vertical, curves right, then hook UP-and-LEFT)
# vertical segment
stroke(bez((220, 180), (220, 210), (222, 235), (228, 252), n=50), (7, 6))
dab(228, 253, 6)  # shoulder dab at fold
# horizontal sweep to the right
stroke(bez((228, 253), (245, 258), (260, 261), (275, 263), n=50), (6, 7))
# hook flick UP-and-LEFT (TIER-0 B)
stroke(bez((275, 263), (272, 255), (268, 247), (263, 240), n=25), (7, 3))


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0561_晓/01_晓.png")
