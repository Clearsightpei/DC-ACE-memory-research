"""Render 个 as a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
THICK = 6

# Apex of the character (roof top)
apex = (150, 70)

# Stroke 1: 撇 (left-falling) from apex down-left
pie_end = (70, 220)
draw.line([apex, pie_end], fill=BLACK, width=THICK)

# Stroke 2: 捺 (right-falling) from apex down-right
# starts slightly right of apex (top of 捺 typically starts at apex/just right)
na_start = (155, 90)
na_end = (245, 210)
draw.line([na_start, na_end], fill=BLACK, width=THICK)

# Stroke 3: 丨 (vertical) below the apex, centered
shu_top = (150, 130)
shu_bot = (150, 250)
draw.line([shu_top, shu_bot], fill=BLACK, width=THICK)

out_path = os.path.join(os.path.dirname(__file__), "01_个.png")
img.save(out_path)
print(f"wrote {out_path}")
