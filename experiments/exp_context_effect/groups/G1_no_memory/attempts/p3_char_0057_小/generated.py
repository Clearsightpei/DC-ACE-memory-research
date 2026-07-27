"""Render 小 (xiǎo) at 300x300 using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"

def stroke(pts, width=6):
    draw.line(pts, fill=INK, width=width, joint="curve")
    # round endcaps
    for (x, y) in pts:
        r = width / 2
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)

# Stroke 1: center vertical hook (竖钩) — starts high, comes down, hooks slightly left at bottom
center_x = 150
top_y = 90
bottom_y = 235
stroke([
    (center_x + 2, top_y),
    (center_x, top_y + 40),
    (center_x - 1, bottom_y - 20),
    (center_x - 20, bottom_y),   # hook to the left
], width=6)

# Stroke 2: left 撇 — slanting from upper-right to lower-left, wider spread
stroke([
    (115, 135),
    (95, 165),
    (70, 200),
], width=6)

# Stroke 3: right dot (点) — short slanting from upper-left to lower-right
stroke([
    (195, 145),
    (215, 170),
    (232, 195),
], width=6)

out_path = os.path.join(os.path.dirname(__file__), "01_小.png")
img.save(out_path)
print(f"Saved {out_path}")
