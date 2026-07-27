"""Render 山 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 6

# 山 has 3 strokes:
# 1) center vertical (tallest) with small hook at bottom-left
# 2) left short vertical with bottom horizontal that continues right
# 3) right short vertical (slightly slanted)

# Stroke 1: center vertical - tallest, from top down
# Starts around x=150, y=80 down to y=210
draw.line([(150, 80), (150, 210)], fill=INK, width=LW)

# Stroke 2: 竖折 - left vertical drops, then horizontal across the bottom
# Left vertical from (90, 130) down to (90, 220), then horizontal to (215, 220)
draw.line([(92, 130), (92, 222)], fill=INK, width=LW)
draw.line([(90, 220), (218, 220)], fill=INK, width=LW)

# Stroke 3: right short vertical - starts a bit higher up on right, slight slant
draw.line([(212, 118), (218, 218)], fill=INK, width=LW)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_山.png")
img.save(out_path)
print(f"Saved: {out_path}")
