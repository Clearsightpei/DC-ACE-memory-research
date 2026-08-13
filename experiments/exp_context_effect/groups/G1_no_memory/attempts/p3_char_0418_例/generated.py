"""Render 例 to 300x300 PNG with PIL. Revised for better structure."""
import os
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5

def line(p1, p2, w=LW):
    d.line([p1, p2], fill=BLACK, width=w)

def curve(points, w=LW):
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill=BLACK, width=w)

# 例 = 亻 (person radical, left) + 列 (right = 歹 + 刂)

# --- 亻 radical ---
# 撇 (slanted stroke from upper right to lower left)
curve([(75, 85), (65, 110), (55, 140), (48, 165)], w=LW)
# 竖 (vertical down from top of pie)
line((72, 115), (72, 255), w=LW)

# --- 歹 (middle-right) ---
# top short 横 (horizontal)
line((115, 100), (170, 98), w=LW)
# 撇 short - diagonal down-left from left end of top horizontal
curve([(130, 90), (118, 115), (108, 135)], w=LW)
# middle 横 - longer horizontal
line((105, 140), (185, 138), w=LW)
# 横折 - horizontal then hook down forming the ㇇ under middle 横
# Actually 歹 has 撇 going through, and a dot
# long 撇 from top-middle going bottom-left through the middle 横
curve([(160, 105), (145, 145), (125, 190), (108, 240)], w=LW)
# 点 (dot) on right side inside
curve([(163, 165), (175, 190)], w=LW)

# --- 刂 (knife radical, right) ---
# short vertical on left (short 竖)
line((215, 110), (215, 210), w=LW)
# long vertical with hook on right (竖钩)
curve([(255, 95), (255, 230), (250, 255), (238, 268)], w=LW)

out = os.path.join(os.path.dirname(__file__), "01_例.png")
img.save(out)
print("Wrote", out)
