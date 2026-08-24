"""
Render 高 (gao1) at 300x300, black ink on white.

Structural read from GT (top -> bottom):
  1. Small 丶 dot at top-center.
  2. Long 横 spanning most of the width just below the dot.
  3. Small 口 (3 strokes) in the upper-middle: left 竖, 横折, bottom 横.
  4. 冖 cover-wider-than-口: opens with a small tick/dot on the left,
     then a long 横折 that tucks down at the right corner.
  5. Bottom body: a taller 冂 (left 竖, top-plus-right 横折) with a
     smaller inner 口 (3 strokes) tucked inside.

Recipe followed:
  - Bezier for any sweep, dab shoulder at every 折 corner,
    variable-width stroke via ellipse-sampling, hook flicks UP-and-LEFT.
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


def shoulder(x, y, r=5):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ---------- 1. top 丶 dot ----------
top_dot = bez((148, 22), (150, 26), (153, 32), (156, 40), n=25)
stroke(top_dot, (3, 8))

# ---------- 2. long 横 under the dot ----------
h_top = bez((45, 60), (110, 57), (190, 57), (255, 62), n=60)
stroke(h_top, (6, 7))

# ---------- 3. upper 口 (3 strokes) ----------
# 3a. left 竖
sq1_v = bez((115, 82), (115, 95), (115, 108), (115, 122), n=30)
stroke(sq1_v, (6, 6))
# 3b. top + right (横折)
sq1_top = bez((113, 82), (140, 80), (170, 80), (188, 82), n=30)
stroke(sq1_top, (6, 6))
shoulder(188, 82, r=5)
sq1_right = bez((188, 82), (188, 95), (188, 108), (188, 122), n=30)
stroke(sq1_right, (6, 6))
# 3c. bottom 横
sq1_bot = bez((115, 122), (140, 122), (170, 122), (188, 122), n=30)
stroke(sq1_bot, (6, 6))

# ---------- 4. 冖 cover ----------
# 4a. left tick (small 点)
cap_tick = bez((45, 138), (48, 143), (52, 148), (55, 152), n=20)
stroke(cap_tick, (3, 7))
# 4b. long 横折
cap_top = bez((55, 148), (120, 145), (200, 145), (252, 148), n=60)
stroke(cap_top, (5, 6))
shoulder(252, 148, r=5)
cap_right = bez((252, 148), (252, 158), (252, 165), (250, 170), n=20)
stroke(cap_right, (6, 5))

# ---------- 5. bottom body ----------
# 5a. left 竖 (tall)
body_left = bez((62, 172), (62, 210), (62, 245), (62, 275), n=50)
stroke(body_left, (7, 7))
# 5b. top 横 + right 竖 (横折)
body_top = bez((62, 172), (130, 170), (210, 170), (238, 172), n=60)
stroke(body_top, (6, 7))
shoulder(238, 172, r=5)
body_right = bez((238, 172), (238, 210), (238, 245), (238, 275), n=50)
stroke(body_right, (7, 7))

# ---------- 6. inner 口 inside the bottom body ----------
# 6a. left 竖
i_v = bez((105, 210), (105, 225), (105, 240), (105, 252), n=30)
stroke(i_v, (5, 5))
# 6b. top 横 + right (横折)
i_top = bez((103, 210), (135, 208), (170, 208), (195, 210), n=30)
stroke(i_top, (5, 5))
shoulder(195, 210, r=4)
i_right = bez((195, 210), (195, 225), (195, 240), (195, 252), n=30)
stroke(i_right, (5, 5))
# 6c. bottom 横
i_bot = bez((105, 252), (135, 252), (170, 252), (195, 252), n=30)
stroke(i_bot, (5, 5))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0507_高/01_高.png")
