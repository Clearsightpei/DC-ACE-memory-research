"""Render 兀 (character) as a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 6

# 兀 has 3 strokes:
# 1) horizontal top (一)
# 2) left vertical curving to the lower-left (丿, curved leg)
# 3) right vertical with hook at bottom (乚 style)

# Stroke 1: top horizontal — slightly tilted up-right like GT
draw.line([(60, 105), (240, 100)], fill=INK, width=LW)

# Stroke 2: left leg — starts near top under the horizontal, curves down-left
# Approximate curve with polyline
left_leg = [
    (95, 108),
    (90, 140),
    (82, 175),
    (70, 210),
    (55, 245),
]
draw.line(left_leg, fill=INK, width=LW, joint="curve")

# Stroke 3: right vertical with hook to the right at bottom
right_leg = [
    (200, 108),
    (203, 160),
    (206, 220),
    (215, 250),
    (240, 258),
]
draw.line(right_leg, fill=INK, width=LW, joint="curve")

out_path = os.path.join(os.path.dirname(__file__), "01_兀.png")
img.save(out_path)
print(f"Saved: {out_path}")
