"""Render 从 (cong) — two 人 side by side. Left smaller/higher, right larger/lower."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
W = 5

def curve(pts, width=W):
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i+1]], fill=INK, width=width)
    for (x, y) in pts:
        draw.ellipse((x - width/2, y - width/2, x + width/2, y + width/2), fill=INK)

# LEFT 人 — smaller, positioned upper-left
# 撇 (pie): starts top, curves down-left
left_pie = [
    (80, 90), (76, 110), (70, 135), (62, 160), (52, 185), (42, 210)
]
# 捺 (na, here more like a small dian/short stroke): from mid of pie going down-right
left_na = [
    (72, 130), (82, 150), (92, 170), (100, 185)
]

# RIGHT 人 — larger, positioned lower-right, taller
# 撇: starts top, longer curve down-left
right_pie = [
    (185, 75), (180, 100), (172, 130), (162, 160), (148, 195), (132, 230), (118, 260)
]
# 捺: from near top going down-right, long
right_na = [
    (192, 105), (208, 140), (225, 180), (245, 220), (262, 258)
]

for stroke in (left_pie, left_na, right_pie, right_na):
    curve(stroke)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_从.png")
img.save(out)
print("wrote", out)
