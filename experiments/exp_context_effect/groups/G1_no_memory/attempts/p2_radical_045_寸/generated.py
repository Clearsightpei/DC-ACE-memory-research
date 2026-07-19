"""Render 寸 (radical, 3 strokes) at 300x300 with PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
STROKE = 5

# Stroke 1: 横 (horizontal) — long horizontal across the middle
# GT shows it slightly tilted upward, spanning most of width
draw.line([(55, 145), (245, 135)], fill=BLACK, width=STROKE)

# Stroke 2: 竖钩 (vertical hook) — vertical line down from just right of center,
# with hook at bottom pointing left
draw.line([(163, 85), (163, 240)], fill=BLACK, width=STROKE)
# Hook curling left at the bottom
draw.line([(163, 240), (138, 228)], fill=BLACK, width=STROKE)

# Stroke 3: 点 (dot) — short curved stroke on lower-left, direction upper-right to lower-left
# GT shows a slight arc going from ~(125,165) down-left to ~(105,190)
draw.line([(128, 165), (108, 192)], fill=BLACK, width=STROKE)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_寸.png")
img.save(out_path)
print(f"Saved {out_path}")
