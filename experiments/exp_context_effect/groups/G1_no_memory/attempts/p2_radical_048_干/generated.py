"""Render 干 (radical, 3 strokes) as a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
THICK = 8

# Stroke 1: top horizontal (一) — shorter, upper part
# Slight tilt up-right like GT
draw.line([(85, 105), (215, 100)], fill=INK, width=THICK)

# Stroke 2: middle/lower horizontal (一) — longer, main横
draw.line([(55, 170), (245, 168)], fill=INK, width=THICK)

# Stroke 3: vertical (丨) — from top横 down through middle横, straight down
draw.line([(150, 100), (150, 265)], fill=INK, width=THICK)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_干.png")
img.save(out_path)
print(f"Saved: {out_path}")
