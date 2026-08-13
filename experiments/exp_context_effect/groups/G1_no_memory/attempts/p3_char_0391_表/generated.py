"""Render 表 to 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

LW = 5

def line(pts, width=LW):
    d.line(pts, fill="black", width=width, joint="curve")

# Top component 龶 (like 主 without dot)
# Small tick at top
line([(150, 55), (152, 72)], width=LW)

# First short horizontal
line([(118, 88), (188, 84)])

# Second horizontal (medium)
line([(105, 118), (200, 115)])

# Long vertical through
line([(150, 72), (150, 160)])

# Third (long) horizontal
line([(55, 162), (245, 158)])

# Bottom - 衣-like without the top strokes
# Left slanted piě from center going down-left
line([(148, 165), (50, 268)])

# Small vertical stroke slightly right of center with hook
line([(155, 180), (145, 240)])
line([(145, 240), (162, 250)])

# Small piě going down-right from around middle-right
line([(175, 195), (200, 235)])

# Right na going down-right to bottom-right
line([(180, 200), (255, 275)])

out_path = os.path.join(os.path.dirname(__file__), "01_表.png")
img.save(out_path)
print(f"Saved {out_path}")
