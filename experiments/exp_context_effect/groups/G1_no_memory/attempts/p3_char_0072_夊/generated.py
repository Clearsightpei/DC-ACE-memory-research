"""Render 夊 (zhǐ) to 300x300 PNG."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")

# Stroke 1: short 撇 near top-left
stroke([(140, 70), (132, 88), (120, 108)], width=5)

# Stroke 2: main 撇 — long diagonal from mid-upper to lower-left
stroke([(158, 115), (140, 145), (115, 180), (80, 215), (55, 245)], width=6)

# Stroke 3: 横 + 捺 combined — horizontal top from x~115 to x~180 at y~120,
# then curves down-right into a long 捺 ending at lower-right
stroke([(115, 122), (150, 118), (180, 125), (200, 160), (225, 205), (255, 250)], width=6)

out = os.path.join(os.path.dirname(__file__), "01_夊.png")
img.save(out)
print(f"Saved {out}")
