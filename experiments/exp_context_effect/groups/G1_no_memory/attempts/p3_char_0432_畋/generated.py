"""Render 畋 (field + rap) at 300x300."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 4

def line(p1, p2, w=LW):
    d.line([p1, p2], fill="black", width=w)

# ---- Left component: 田 (field) ----
# rectangle
L, R = 40, 130
T, B = 90, 220
# outer box (top, left, right, bottom)
line((L, T), (R, T))            # top horizontal
line((L, T), (L, B))            # left vertical
line((R, T), (R, B))            # right vertical
line((L, B), (R, B))            # bottom horizontal
# inner cross
midX = (L + R) // 2
midY = (T + B) // 2
line((L, midY), (R, midY))       # horizontal
line((midX, T), (midX, B))       # vertical

# ---- Right component: 攵 ----
# Stroke 1: short slanted stroke (撇) at top-left
line((175, 90), (200, 105))
# Stroke 2: horizontal stroke
line((165, 115), (245, 115))
# Stroke 3: long diagonal 撇 (from upper right area down to lower left)
# curve implemented as polyline
pts_pie = [(215, 105), (200, 140), (175, 180), (150, 230)]
for i in range(len(pts_pie) - 1):
    line(pts_pie[i], pts_pie[i + 1])
# Stroke 4: 捺 (from mid-upper going down-right)
pts_na = [(195, 140), (220, 180), (250, 220), (275, 250)]
for i in range(len(pts_na) - 1):
    line(pts_na[i], pts_na[i + 1])

out = os.path.join(os.path.dirname(__file__), "01_畋.png")
img.save(out)
print("saved", out)
