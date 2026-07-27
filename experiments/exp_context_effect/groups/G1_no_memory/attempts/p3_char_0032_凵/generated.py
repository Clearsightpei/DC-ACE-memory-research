"""Render 凵 (kǎn) using PIL. 300x300 white bg, black ink."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

ink = (0, 0, 0)
thick = 7

# 凵 has 2 strokes in MMH:
# Stroke 1: left vertical + bottom horizontal as a single "L" shape (竖折)
# Stroke 2: right vertical (竖)
# Looking at GT: shape occupies roughly middle-lower region, width ~140, height ~120

# Coordinates (PIL, y grows down)
left_x = 90
right_x = 215
top_y = 155
bot_y = 260

# Stroke 1 (竖折): left vertical going down, then horizontal right
# Left vertical
draw.line([(left_x, top_y), (left_x, bot_y)], fill=ink, width=thick)
# Bottom horizontal
draw.line([(left_x, bot_y), (right_x, bot_y)], fill=ink, width=thick)

# Stroke 2: right vertical — extends slightly past the bottom (matches GT)
draw.line([(right_x, top_y), (right_x, bot_y + 8)], fill=ink, width=thick)

out_path = os.path.join(os.path.dirname(__file__), "01_凵.png")
img.save(out_path)
print(f"Saved {out_path}")
