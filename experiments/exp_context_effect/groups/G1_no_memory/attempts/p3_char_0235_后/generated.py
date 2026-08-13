"""Render 后 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke(points, width=4):
    d.line(points, fill=BLACK, width=width, joint="curve")

# 后 - 6 strokes

# 1. Top short 撇 (small diagonal, top-left area)
stroke([(135, 45), (110, 75)], width=4)

# 2. Top horizontal extending right from the 撇 area
stroke([(115, 78), (215, 70)], width=4)

# 3. Long 撇 - starts near top-left of body, sweeps down and slightly left
stroke([(115, 78), (95, 140), (75, 210), (60, 265)], width=4)

# 4. Middle horizontal (upper edge of the 口 sub-shape, sits inside body)
stroke([(105, 150), (225, 148)], width=4)

# 5. 横折 (top-right of 口): horizontal then hook down forming right side
stroke([(110, 195), (228, 192), (228, 258)], width=4)

# 6. Bottom horizontal closing 口 (left to right)
stroke([(112, 258), (230, 258)], width=4)

out_path = os.path.join(os.path.dirname(__file__), "01_后.png")
img.save(out_path)
print(f"Saved {out_path}")
