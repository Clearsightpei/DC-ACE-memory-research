"""Render 花 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 3

def line(p1, p2, w=LW):
    d.line([p1, p2], fill=BLACK, width=w)

def curve(pts, w=LW):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill=BLACK, width=w)

# 花 = 艹 (grass top) + 化 (亻 left + 匕 right, bottom)

# === 艹 (top, spans ~y 60-110) ===
# left vertical (short, tilted slightly)
line((100, 60), (98, 110), w=LW)
# right vertical (short, tilted slightly)
line((190, 60), (193, 110), w=LW)
# long horizontal crossing both verticals (slight rise to right)
line((60, 95), (240, 88), w=LW)

# === 亻 (bottom-left person radical, spans ~y 120-260) ===
# short slanted stroke (撇) top of 亻
curve([(95, 125), (78, 150), (70, 165)], w=LW)
# long vertical of 亻
line((100, 155), (100, 265), w=LW)

# === 匕 (bottom-right, spans ~y 130-270) ===
# 撇 - a curve going from upper right down to lower left
curve([(175, 130), (160, 170), (145, 210), (135, 245)], w=LW)
# horizontal short stroke through the middle
line((160, 190), (215, 185), w=LW)
# 竖弯钩 - vertical down, curves right, hooks up
curve([(200, 155), (200, 220), (205, 250), (225, 265), (245, 260), (248, 245)], w=LW)

out_path = os.path.join(os.path.dirname(__file__), "01_花.png")
img.save(out_path)
print(f"saved {out_path}")
