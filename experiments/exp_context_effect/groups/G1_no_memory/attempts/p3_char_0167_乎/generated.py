"""Render 乎 to 01_乎.png (300x300, white bg, black ink).

乎 has 5 strokes:
  1. 撇 (short, top-left, slanting down-left)
  2. 点 (short slanting stroke, top-right)
  3. 横撇 (small horizontal that curls down-left) in upper middle
  4. 横 (long horizontal, middle)
  5. 竖钩 (vertical with a small hook to the left at the bottom)
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke(pts, width=6):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill=BLACK, width=width, joint="curve")

# 1. Top-left 撇: slants down-left
stroke([(135, 55), (120, 70), (105, 88)], width=6)

# 2. Top-right 点: short slant down-right
stroke([(180, 55), (195, 72), (208, 88)], width=6)

# 3. 横撇 in upper middle — small horizontal segment that hooks down-left
stroke([(115, 100), (150, 95), (180, 98), (170, 115)], width=6)

# 4. Long horizontal 一 across the middle
stroke([(45, 160), (100, 155), (170, 152), (240, 155), (260, 162)], width=7)

# 5. 竖钩: vertical going down through center, hooking left at bottom
stroke([(152, 115), (151, 160), (150, 210), (149, 240), (142, 252), (128, 254), (118, 248)], width=7)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_乎.png")
img.save(out)
print(f"Saved {out}")
