"""
Render 结 (jie2) at 300x300, black ink on white.

Structure: 纟 (left, ~1/3 width) + 吉 (right, ~2/3 width)

FROZEN-RADICAL alarm (TIER-0 G): 纟 attested 2+ fails.
Fix hypothesis: 纟 = 撇折 + 撇折 + 提 — 3 middle segments share joint pixels.
Render as connected polylines, not detached loops.

吉 = 士 (十横 + 竖 + 短横) on top + 口 (box) on bottom.
士 sibling row: TOP horizontal is the LONG one, bottom horizontal SHORTER.

Calligraphic 4-move: bezier + variable-width stroke + shoulder dab + hook flick.
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


# ============ LEFT: 纟 (silk radical) ============
# 撇折 #1 (top): diagonal down-left flick, then short折 turn right-down
p1 = bez((85, 55), (75, 70), (65, 82), (55, 92), n=40)
stroke(p1, (5, 3))
dab(55, 92, 3.5)  # shoulder
p1b = bez((55, 92), (62, 100), (70, 108), (78, 115), n=30)
stroke(p1b, (3, 4))

# 撇折 #2 (middle): similar shape below
p2 = bez((78, 115), (68, 128), (58, 140), (50, 150), n=40)
stroke(p2, (4, 3))
dab(50, 150, 3.5)  # shoulder
p2b = bez((50, 150), (58, 158), (68, 166), (78, 172), n=30)
stroke(p2b, (3, 4))

# 提 (rising stroke) at bottom - starts low-left, rises up-right
ti = bez((40, 235), (60, 225), (80, 215), (110, 200), n=50)
stroke(ti, (7, 2))


# ============ RIGHT: 吉 ============
# 士 top: long horizontal, vertical, shorter horizontal

# Top LONG horizontal (士 top stroke - the wide one)
h_top = bez((130, 75), (170, 72), (210, 72), (255, 76), n=50)
stroke(h_top, (5, 6))

# Central vertical 竖 — extends slightly ABOVE top horizontal (士 signature)
v = bez((193, 65), (192, 95), (192, 125), (192, 150), n=40)
stroke(v, (7, 7))

# Shorter horizontal below (士 bottom stroke — shorter than top)
h_mid = bez((160, 150), (185, 148), (210, 148), (228, 152), n=40)
stroke(h_mid, (5, 5))

# 口 bottom box — tighter than before
box_top_l = (155, 185)
box_top_r = (230, 185)
box_bot_l = (160, 255)
box_bot_r = (225, 253)

# left vertical (竖)
lv = bez(box_top_l, (145, 205), (147, 230), box_bot_l, n=40)
stroke(lv, (6, 6))

# top + right of 口 as 横折 (one connected)
top_h = bez(box_top_l, (175, 178), (210, 178), box_top_r, n=40)
stroke(top_h, (5, 6))
dab(240, 180, 4)  # shoulder dab at 折 corner
right_v = bez(box_top_r, (238, 205), (235, 232), box_bot_r, n=40)
stroke(right_v, (6, 6))

# bottom horizontal (closing 口)
bot_h = bez(box_bot_l, (180, 260), (210, 260), box_bot_r, n=40)
stroke(bot_h, (5, 6))


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0467_结/01_结.png")
