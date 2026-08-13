"""Render 准 to 01_准.png (300x300, white bg, black ink)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# 冫 — two dots on the left (upper and lower)
# upper dot 点 (a short 撇/dot)
stroke([(55, 90), (75, 115)], width=6)
# lower dot 提 (rising)
stroke([(55, 165), (80, 155)], width=6)

# 隹 (right side)
# top short 撇 (slanted from upper area)
stroke([(160, 75), (135, 100)], width=5)

# 亻 vertical stroke (left side of 隹)
stroke([(135, 100), (130, 260)], width=6)

# top-right 点 of 隹 (a small 点)
stroke([(200, 90), (215, 110)], width=5)

# main vertical of 主-like body inside 隹
stroke([(180, 115), (180, 270)], width=6)

# three horizontal strokes crossing the vertical
# top horizontal (short)
stroke([(150, 130), (215, 128)], width=5)
# middle horizontal
stroke([(148, 175), (220, 173)], width=5)
# bottom horizontal (longest)
stroke([(120, 240), (240, 238)], width=6)

out_path = os.path.join(os.path.dirname(__file__), "01_准.png")
img.save(out_path)
print("wrote", out_path)
