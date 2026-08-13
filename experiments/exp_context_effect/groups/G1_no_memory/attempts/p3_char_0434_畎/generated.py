"""G1 render of 畎 = 田 (left) + 犬 (right)."""
import os
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 4


def line(p0, p1, w=LW):
    d.line([p0, p1], fill="black", width=w)


def poly(pts, w=LW):
    for i in range(len(pts) - 1):
        line(pts[i], pts[i + 1], w)


# =========================
# 田 on the LEFT (roughly x: 35..135, y: 120..220)
# =========================
L, R, T, B = 35, 135, 120, 220
MX = (L + R) // 2
MY = (T + B) // 2

line((L, T), (L, B))                  # left vertical
line((L, T), (R, T))                  # top horizontal
line((R, T), (R, B))                  # right vertical
line((L, B), (R, B))                  # bottom horizontal
line((MX, T), (MX, B))                # middle vertical
line((L, MY), (R, MY))                # middle horizontal

# =========================
# 犬 on the RIGHT
# Big — spans full height on the right ~x: 145..290, y: 55..270
# =========================
# 1) Heng (horizontal) with slight upward tilt
line((155, 115), (275, 105), w=LW)

# 2) Pie (long left-slanting from near center-top down to lower-left)
# Starts above the heng, crosses through it, ends bottom-left of 犬 area
poly([(220, 75), (215, 100), (208, 130), (195, 170), (175, 215), (155, 265)], w=LW)

# 3) Na (right-falling) — starts at the pie/heng crossing area, goes to bottom-right
poly([(215, 118), (235, 160), (260, 210), (285, 260)], w=LW + 1)

# 4) Dot (dian) — small stroke at top-right of 犬
poly([(258, 75), (272, 95)], w=LW + 1)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_畎.png"))
print("saved:", os.path.join(out_dir, "01_畎.png"))
