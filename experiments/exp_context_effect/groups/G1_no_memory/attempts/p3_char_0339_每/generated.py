"""Render 每 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# 每 (7 strokes): 丿 一 (top ⺈); then 母-like body: 竖折, 横折钩, 长横, 点, 点
# Overall the character is centered, roughly 220x230.

# Stroke 1: 丿 (top-right diagonal going down-left, forms top of 人-like head)
line([(170, 55), (115, 115)], width=6)

# Stroke 2: 一 (short horizontal at top, meeting the 丿)
line([(120, 100), (200, 95)], width=5)

# 母 body region
# Stroke 3: 竖折 (short vertical descending, turning right at bottom)
# left side of 母 box
line([(95, 130), (100, 205)], width=5)
line([(100, 205), (215, 210)], width=5)  # bottom of box

# Stroke 4: 横折钩 (top of box + right side down + hook)
line([(105, 130), (210, 125)], width=5)   # top horizontal
line([(210, 125), (215, 210)], width=5)   # right down

# Stroke 5: 长横 (long horizontal crossing through middle, extending beyond box)
line([(45, 175), (260, 170)], width=5)

# Stroke 6 & 7: two dots inside upper half of box
# left dot (slanting down-right)
line([(130, 150), (145, 165)], width=6)
# right dot (slanting down-right)
line([(175, 150), (190, 165)], width=6)

# Bottom hook of 母 (part of stroke 3 completion — vertical hook rising up-left)
line([(215, 210), (200, 240)], width=5)
line([(200, 240), (180, 245)], width=5)

out_path = os.path.join(os.path.dirname(__file__), "01_每.png")
img.save(out_path)
print(f"Saved {out_path}")
