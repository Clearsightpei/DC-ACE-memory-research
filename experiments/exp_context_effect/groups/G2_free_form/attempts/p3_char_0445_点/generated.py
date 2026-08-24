"""
Render 点 (dian3) at 300x300, black ink on white.

Structure:
  Top: 占 = 卜 (short vertical + dot) + 口 (rectangle below)
    - 竖 vertical near top-center
    - 点 (dot) to the right of the vertical's mid
    - 口: 竖 left, 横折 top+right, 横 bottom
  Bottom: 灬 (four dots) spread across the width
    - leftmost dot slants left, middle two slant slightly, right dot slants right

Apply TIER-0 F 4-move: teardrop taper on all 点/撇, bezier curves,
shoulder dab at 折 joint of 口.
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

# ============ TOP: 占 ============

# 卜 vertical (竖): centered-ish, from y=35 to y=110
v_top = bez((140, 35), (140, 55), (140, 85), (140, 110), n=40)
stroke(v_top, (7, 7))

# 卜 dot (点): tucked to the right of the vertical, sloped down-right
dot_top = bez((158, 70), (170, 78), (180, 84), (188, 90), n=30)
stroke(dot_top, (4, 9))

# --- 口 rectangle: x 105..195, y 118..170 ---
# left 竖 (down stroke)
kou_left = bez((110, 118), (110, 135), (110, 155), (110, 170), n=40)
stroke(kou_left, (6, 6))

# top 横 + right 竖 (横折): horizontal then turn down
kou_top = bez((110, 118), (135, 116), (165, 116), (195, 118), n=40)
stroke(kou_top, (6, 6))
# shoulder dab at the top-right corner
dab(195, 118, 4.5)
kou_right = bez((195, 118), (195, 135), (195, 155), (195, 172), n=40)
stroke(kou_right, (6, 5))

# bottom 横 closing the rectangle
kou_bot = bez((108, 172), (135, 170), (165, 170), (197, 172), n=40)
stroke(kou_bot, (5, 5))

# ============ BOTTOM: 灬 (four dots) ============
# y baseline ~ 215, dots taper into their tails

# dot 1 (leftmost) — slants down-LEFT (撇-like)
d1 = bez((78, 215), (72, 235), (66, 250), (58, 265), n=30)
stroke(d1, (4, 9))

# dot 2 — small, slants down-slightly-right
d2 = bez((118, 220), (120, 238), (123, 252), (126, 265), n=30)
stroke(d2, (3, 8))

# dot 3 — small, slants down-slightly-right
d3 = bez((165, 220), (170, 238), (175, 252), (180, 265), n=30)
stroke(d3, (3, 8))

# dot 4 (rightmost) — slants down-RIGHT (捺-like), thicker tail
d4 = bez((210, 215), (222, 235), (232, 250), (242, 265), n=30)
stroke(d4, (3, 10))

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0445_点/01_点.png"
img.save(out)
print("saved:", out)
