"""果 (guǒ) — 8 strokes.
Composition: 田 (top) + 木 (bottom, sharing central vertical).
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
BW = 7

def line(p1, p2, w=BW):
    d.line([p1, p2], fill=INK, width=w)

def curve(points, w=BW):
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill=INK, width=w)

# 田 box — larger and more centered horizontally
L, R = 90, 210
T, B = 45, 160
MIDX = (L + R) // 2  # 150
MIDY = (T + B) // 2  # 102

# 1. 竖 — left side of 田
line((L, T + 2), (L - 2, B), BW)

# 2. 横折 — top + right
d.line([(L - 3, T), (R + 5, T - 3)], fill=INK, width=BW)
d.line([(R + 5, T - 3), (R + 2, B + 3)], fill=INK, width=BW)

# 3. 横 — middle
line((L + 3, MIDY + 2), (R - 1, MIDY), BW)

# 4. 竖 — long central vertical
CX = MIDX
line((CX, T - 3), (CX, 288), BW + 1)

# 5. 横 — bottom of 田
line((L - 3, B), (R + 4, B + 2), BW)

# 6. 横 — long horizontal of 木, well beyond 田
HY = 200
line((28, HY + 3), (272, HY - 3), BW + 1)

# 7. 撇 — from just above HY, sweeping down-left, long
pie_pts = []
sx, sy = CX - 3, HY - 2
for t in [i/24 for i in range(25)]:
    x = sx - 95 * t - 12 * math.sin(math.pi * t * 0.7)
    y = sy + 85 * t + 5 * t * t
    pie_pts.append((x, y))
curve(pie_pts, BW)

# 8. 捺 — from center sweeping down-right, long
na_pts = []
for t in [i/24 for i in range(25)]:
    x = CX + 3 + 100 * t + 5 * math.sin(math.pi * t * 0.5)
    y = HY - 2 + 82 * t
    na_pts.append((x, y))
curve(na_pts, BW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0387_果/01_果.png")
print("wrote PNG")
