"""G1 draw 皅 (白+巴) at 300x300."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 3

def line(x1, y1, x2, y2, w=LW):
    d.line([(x1, y1), (x2, y2)], fill=BLACK, width=w)

# ---- 白 (bai) left side ----
# 撇 top-left slash
line(80, 95, 60, 130)
# top horizontal
line(55, 128, 125, 128)
# right vertical
line(125, 128, 125, 225)
# left vertical
line(55, 128, 55, 225)
# bottom horizontal
line(55, 225, 125, 225)
# middle horizontal
line(60, 178, 120, 178)

# ---- 巴 (ba) right side ----
# Stroke 1: 横折 top and short right down
line(160, 90, 245, 90)          # top
line(245, 90, 245, 155)         # right down (upper section)
# Stroke 2: middle horizontal
line(160, 145, 245, 145)
# Stroke 3: 竖弯钩 - left vertical going down, curving right, hooking up
# left vertical
line(160, 90, 160, 235)
# curve at bottom going right
line(160, 235, 250, 235)
# right side going up a bit then hook
line(250, 235, 258, 215)
# small hook up-left
line(258, 215, 248, 210)

img.save(os.path.join(os.path.dirname(__file__), "01_皅.png"))
print("saved")
