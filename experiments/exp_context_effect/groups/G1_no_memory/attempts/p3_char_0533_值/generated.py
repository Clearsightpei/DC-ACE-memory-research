"""Render 值 (zhí) as 300x300 PNG using PIL.
值 = 亻 (left) + 直 (right)
"""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLK = (0, 0, 0)
LW = 4

def line(p1, p2, w=LW):
    d.line([p1, p2], fill=BLK, width=w)

# ---------- 亻 (person radical, left side) ----------
# Left slanted stroke (撇) - starts high right, slants down-left
line((95, 65), (55, 180), w=5)
# Vertical stroke - touches the slant near its midpoint
line((80, 130), (80, 250), w=5)

# ---------- 直 (right side) ----------
# Short vertical on top of 直
line((195, 60), (195, 85), w=5)
# Top horizontal of 直 (long, spans wider than 目)
line((140, 85), (275, 85), w=5)
# Second horizontal (top of 目 box)
line((150, 105), (260, 105), w=4)

# 目 box - left vertical
line((155, 105), (155, 235), w=4)
# 目 box - right vertical
line((255, 105), (255, 235), w=4)
# Middle horizontals of 目
line((155, 145), (255, 145), w=3)
line((155, 185), (255, 185), w=3)
# Bottom of 目
line((155, 235), (255, 235), w=4)

# Bottom horizontal (extends beyond 目 - the bottom 一 of 直)
line((135, 255), (280, 255), w=5)

out = os.path.join(os.path.dirname(__file__), "01_值.png")
img.save(out)
print(f"saved {out}")
