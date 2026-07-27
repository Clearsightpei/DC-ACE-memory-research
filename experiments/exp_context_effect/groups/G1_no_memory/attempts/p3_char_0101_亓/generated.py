"""Render 亓 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke(points, width=7):
    d.line(points, fill=BLACK, width=width, joint="curve")

# Stroke 1: top short horizontal (dot-like short heng)
stroke([(115, 78), (185, 72)], width=8)

# Stroke 2: long horizontal below
stroke([(55, 125), (255, 118)], width=9)

# Stroke 3: left vertical / left leg (starts at horizontal, curves left-down)
stroke([(105, 130), (100, 180), (85, 230), (65, 260)], width=8)

# Stroke 4: right vertical (straight down)
stroke([(200, 130), (200, 260)], width=8)

out_path = os.path.join(os.path.dirname(__file__), "01_亓.png")
img.save(out_path)
print(f"Saved {out_path}")
