"""Render 下 as a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
STROKE = 8

# Stroke 1: horizontal top stroke (一) — slightly bowed, ends flick down a bit
# Draw a smooth curve using multiple segments to give slight character
d.line([(45, 95), (255, 100)], fill=INK, width=STROKE)
# small end flicks (subtle)
d.line([(45, 95), (40, 105)], fill=INK, width=STROKE)
d.line([(255, 100), (258, 118)], fill=INK, width=STROKE)

# Stroke 2: vertical stroke (丨) down from center of horizontal
d.line([(150, 100), (150, 260)], fill=INK, width=STROKE)

# Stroke 3: small dot / short diagonal (丶) to the right of vertical, upper part
d.line([(155, 140), (185, 175)], fill=INK, width=STROKE)

out = os.path.join(os.path.dirname(__file__), "01_下.png")
img.save(out)
print("wrote", out)
