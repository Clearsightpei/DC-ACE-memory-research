"""Render 疡 (yang - sore/ulcer) using PIL.
Structure: 疒 radical on outer-left, 昜-simplified (勿-like) on right.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=5):
    d.line(pts, fill="black", width=width)

def curve(pts, width=5, steps=50):
    (x0, y0), (x1, y1), (x2, y2) = pts
    prev = (x0, y0)
    for i in range(1, steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t ** 2 * x2
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t ** 2 * y2
        d.line([prev, (x, y)], fill="black", width=width)
        prev = (x, y)

# --- 疒 radical (sickness) ---
# 1. Top dot 点 (small, on the top-center of the radical)
line([(115, 55), (128, 72)], width=5)

# 2. Top horizontal 横 (spans wide across whole character top)
line([(75, 90), (235, 82)], width=5)

# 3. Long left-falling stroke 撇 down to bottom-left
curve([(95, 88), (65, 180), (40, 275)], width=5)

# 4. Two small dots 冫 inside the radical (left side, middle)
line([(75, 130), (85, 148)], width=5)
line([(72, 165), (82, 183)], width=5)

# --- Right side (勿-like / simplified 昜) ---
# 5. Right vertical with turn-hook (横折钩): starts from top horizontal end
curve([(215, 85), (222, 200), (195, 230)], width=5)

# 6. Middle short horizontal inside right box
line([(140, 145), (215, 140)], width=5)

# 7. First inner 撇 (left of the two diagonals)
curve([(160, 155), (145, 220), (125, 280)], width=5)

# 8. Second inner 撇 (right, parallel)
curve([(200, 165), (180, 225), (160, 285)], width=5)

# 9. Third short 撇 (rightmost)
curve([(215, 175), (200, 230), (185, 280)], width=5)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_疡.png"))
print("saved")
