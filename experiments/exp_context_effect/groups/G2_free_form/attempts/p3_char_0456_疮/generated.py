"""
Render 疮 (chuang1) at 300x300, black ink on white.

Structural read from GT:
  疒 (sickness radical, left+top wrap):
    - 点 top-center
    - 横 short horizontal from top-left → right
    - Long 撇 sweeping down-left from top-right of the 横 to bottom-left
    - Two 点 stacked on the mid-left (like 冫 tucked inside 疒 body)
  仓 (right-bottom, tucked inside the 疒 wrap):
    - 人 top (撇 + 捺)
    - Short 横 middle
    - 巳 bottom (横折 + curve with UP-LEFT hook flick)
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

def line(p0, p1, w):
    pts = bez(p0, (p0[0]*0.66+p1[0]*0.34, p0[1]*0.66+p1[1]*0.34),
              (p0[0]*0.34+p1[0]*0.66, p0[1]*0.34+p1[1]*0.66), p1, n=40)
    stroke(pts, w if isinstance(w, tuple) else (w, w))

# ============ 疒 radical (wraps top+left) ============
# 1. 点 at top center of radical
dot1 = bez((115, 30), (120, 38), (124, 46), (128, 55), n=25)
stroke(dot1, (3, 8))

# 2. 横 short horizontal (top of the wrap), slight down-slant
h_top = bez((80, 70), (115, 68), (155, 68), (190, 72), n=50)
stroke(h_top, (5, 6))
# shoulder dab at right end (where 横 turns into 撇 tail direction)
d.ellipse((186, 68, 196, 78), fill="black")

# 3. Long 撇 sweeping down-left, from top-right end of 横 down to bottom-left
pie_long = bez((190, 72), (155, 130), (100, 190), (35, 275), n=100)
stroke(pie_long, (10, 3))

# 4. Two 点 on the left, tucked inside the 疒 wrap
dot_l1 = bez((78, 130), (73, 138), (70, 145), (66, 155), n=25)
stroke(dot_l1, (3, 7))
dot_l2 = bez((66, 165), (63, 175), (60, 185), (58, 195), n=25)
stroke(dot_l2, (3, 7))

# ============ 仓 inside (right/lower-right, tucked in the wrap) ============
# 1. 撇 of 人 top
pie_ren = bez((205, 90), (185, 115), (165, 135), (145, 155), n=60)
stroke(pie_ren, (9, 3))

# 2. 捺 of 人 top - S curve with foot flare
na_ren = bez((205, 95), (220, 120), (240, 140), (265, 160), n=60)
stroke(na_ren, (4, 11))
# foot flare
foot = bez((265, 160), (270, 162), (275, 163), (278, 164), n=15)
stroke(foot, (11, 3))

# 3. Short 横 middle (below 人)
h_mid = bez((165, 180), (195, 178), (225, 178), (255, 180), n=40)
stroke(h_mid, (5, 5))

# 4. 巳 bottom - 横折 then curve with hook
# 横 top of 巳
h_ba = bez((170, 205), (200, 203), (225, 203), (245, 205), n=40)
stroke(h_ba, (5, 5))
# shoulder dab
d.ellipse((241, 201, 251, 211), fill="black")
# 折 down (vertical right side)
v_ba = bez((245, 205), (245, 225), (245, 245), (243, 265), n=50)
stroke(v_ba, (6, 5))
# curve to left along bottom
bottom_curve = bez((243, 265), (225, 275), (200, 275), (180, 270), n=40)
stroke(bottom_curve, (5, 5))
# hook flick UP and LEFT (into character body)
hook = bez((180, 270), (175, 263), (172, 255), (168, 245), n=25)
stroke(hook, (5, 3))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0456_疮/01_疮.png")
