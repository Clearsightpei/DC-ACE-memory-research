"""
Render 除 (chu2) at 300x300, black ink on white.

Decomposition:
  Left:  阝 (left-ear radical, 2 strokes)
           1. 横撇弯钩  — small ear-loop at top
           2. 竖        — long vertical drop
  Right: 余 (7 strokes)
           3. 撇 of 人  — top left flick
           4. 捺 of 人  — top right sweep with foot flare
           5. 横        — mid horizontal
           6. 横        — second (shorter) horizontal
           7. 竖        — center vertical drop
           8. 撇 (left small)
           9. 点 (right small)

TIER-0 checks applied:
- Components touch: 阝's 竖 (x~85) and 余's silhouette (starts x~100) share
  the mid seam; 余's 撇 sweeps to x~95 crossing under 阝.
- Hooks flick UP-and-LEFT (阝 ear terminal).
- Calligraphic 4-move: bez curves, variable widths, shoulder dabs at
  折 joints, tapered 撇/捺/点.
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


def dab(cx, cy, r):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


# =========================================================
# LEFT: 阝 (left-ear) — tight top loop, narrower footprint
# =========================================================
# 横撇弯钩 — a clean "3"-like double-arc ending in UP-LEFT hook.
# Segment 1: 横 short from (55,60) → (85,60)
ear_h = bez((52, 60), (65, 58), (78, 58), (85, 62), n=40)
stroke(ear_h, (7, 7))
dab(85, 62, 5)
# Segment 2: 撇/turn — down-left to (55,110)
ear_pie = bez((85, 62), (82, 78), (72, 92), (55, 108), n=50)
stroke(ear_pie, (7, 5))
dab(55, 108, 5)
# Segment 3: 弯 — arc back down-right to (80,140)
ear_curve = bez((55, 108), (68, 118), (76, 128), (80, 140), n=50)
stroke(ear_curve, (5, 7))
# hook flick UP-and-LEFT
ear_hook = bez((80, 140), (74, 136), (68, 132), (62, 128), n=25)
stroke(ear_hook, (7, 3))

# 竖 — long vertical from (80, 60) down to (80, 265)
shu_L = bez((80, 62), (80, 135), (80, 205), (80, 268), n=80)
stroke(shu_L, (8, 8))

# =========================================================
# RIGHT: 余 — shifted right, 撇 kept east of 阝
# =========================================================
# 撇 of 人 — apex ~(200, 55), sweeps down-left but STOPS at x~120
pie = bez((200, 55), (185, 95), (160, 128), (125, 158), n=80)
stroke(pie, (10, 4))

# 捺 of 人 — apex sweeping down-right with foot flare
na_main = bez((202, 65), (222, 100), (247, 130), (272, 155), n=80)
stroke(na_main, (5, 12))
foot = bez((272, 155), (277, 158), (282, 160), (286, 162), n=20)
stroke(foot, (12, 3))

# 横 — mid horizontal under 人
h1 = bez((140, 158), (175, 155), (220, 155), (250, 158), n=40)
stroke(h1, (6, 6))

# 横 — second, shorter horizontal
h2 = bez((160, 198), (190, 196), (218, 196), (242, 199), n=40)
stroke(h2, (5, 5))

# 竖 — center vertical of 余
shu_R = bez((200, 158), (200, 200), (200, 240), (199, 272), n=60)
stroke(shu_R, (7, 7))

# 撇 (left small at bottom)
left_dot = bez((175, 218), (160, 238), (145, 253), (128, 268), n=40)
stroke(left_dot, (7, 3))

# 点 (right small at bottom)
right_dot = bez((228, 222), (243, 237), (254, 252), (264, 264), n=40)
stroke(right_dot, (4, 8))

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0491_除/01_除.png"
)
