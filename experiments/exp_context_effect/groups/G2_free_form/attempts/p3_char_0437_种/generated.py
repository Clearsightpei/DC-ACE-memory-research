"""
Render 种 (zhong3) at 300x300, black ink on white.

Structural read from GT:
  Left: 禾 (grain radical) — 撇 (top flick) + 横 (short horizontal) +
        竖 (long vertical) + 撇 (left diagonal from mid) +
        点 (right dot, 捺→点 because on left position)
  Right: 中 — 口 box (竖 + 横折 + 横) + long center 竖 piercing through.

Applies TIER-0 calligraphic weight rules:
  - Teardrop taper on 撇 / 点
  - Bezier for curved sweeps
  - Shoulder dab at 折 joint
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

# =============== 禾 (LEFT, x ~ 20-140) ===============
# 1. 撇 at top — small flick, sits just above the 横, meets it near left
pie_top = bez((95, 55), (85, 65), (75, 72), (60, 78), n=40)
stroke(pie_top, (7, 3))

# 2. 横 — short horizontal across upper-mid area, slight rise
h1 = bez((30, 78), (60, 74), (100, 74), (140, 78), n=40)
stroke(h1, (6, 6))

# 3. 竖 — long vertical, center of 禾, from top area to bottom
v_he = bez((85, 78), (85, 140), (85, 210), (85, 265), n=80)
stroke(v_he, (7, 7))

# 4. 撇 from center — starts near intersection, sweeps down-left
pie_mid = bez((85, 110), (68, 145), (50, 180), (25, 220), n=60)
stroke(pie_mid, (8, 3))

# 5. 点 (right dot — 捺 compressed to point because 禾 is on left)
right_dot = bez((90, 125), (108, 150), (128, 180), (145, 210), n=50)
stroke(right_dot, (3, 10))

# =============== 中 (RIGHT, x ~ 160-275) ===============
# 口 box roughly (175, 100) to (255, 195)
box_left = 175
box_right = 255
box_top = 100
box_bot = 195

# 1. 竖 — left side of 口 box
v_left = bez((box_left, box_top), (box_left, box_top+35),
             (box_left, box_top+65), (box_left, box_bot), n=50)
stroke(v_left, (6, 6))

# 2. 横折 — top horizontal + right vertical (single stroke with shoulder)
h_top = bez((box_left, box_top), (box_left+25, box_top-2),
            (box_left+55, box_top-2), (box_right, box_top), n=50)
stroke(h_top, (6, 7))
# shoulder dab at corner
dab(box_right, box_top, 5)
# right vertical of 折
v_right = bez((box_right, box_top), (box_right, box_top+35),
              (box_right, box_top+65), (box_right, box_bot), n=50)
stroke(v_right, (7, 6))

# 3. 横 — bottom of 口
h_bot = bez((box_left, box_bot), (box_left+25, box_bot+1),
            (box_left+55, box_bot+1), (box_right, box_bot), n=50)
stroke(h_bot, (6, 6))

# 4. 竖 — long center vertical piercing 口, full character height
cx = (box_left + box_right) // 2  # 215
v_center = bez((cx, 40), (cx, 100), (cx, 200), (cx, 270), n=100)
stroke(v_center, (8, 8))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0437_种/01_种.png")
print("saved")
