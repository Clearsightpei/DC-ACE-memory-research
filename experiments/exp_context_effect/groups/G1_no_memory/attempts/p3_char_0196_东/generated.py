"""Render 东 (east) as 300x300 PNG."""
import os
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 5

def line(pts, w=LW):
    d.line(pts, fill="black", width=w)

# Character 东 (simplified) — 5 strokes
# 1. Top: small 横撇 (short horizontal turning into short slash)
line([(135, 55), (170, 55)], w=5)     # short horizontal
line([(170, 55), (155, 85)], w=5)     # slash down-left

# 2. Long horizontal 横 (middle), slightly tilted up
line([(50, 135), (250, 125)], w=5)

# 3. Vertical with hook 竖钩 (center)
line([(155, 75), (155, 240)], w=5)
line([(155, 240), (138, 228)], w=5)   # hook

# 4. Left bottom short 撇 (diagonal down-left from horizontal)
line([(140, 155), (95, 235)], w=5)

# 5. Right bottom dot 点 (short diagonal down-right from horizontal)
line([(170, 155), (215, 235)], w=5)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_东.png"))
print("wrote 01_东.png")
