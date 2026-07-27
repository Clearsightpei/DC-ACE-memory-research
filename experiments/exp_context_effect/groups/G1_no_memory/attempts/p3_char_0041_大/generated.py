"""Render 大 (dà) — 3 strokes: horizontal, left-falling, right-falling."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

INK = "black"
W = 6  # stroke width

# Stroke 1: 横 (horizontal) — slightly rising
# spans across mid-upper area
d.line([(55, 130), (245, 122)], fill=INK, width=W)

# Stroke 2: 撇 (left-falling) — from top-middle down to lower-left
# starts above the horizontal, crosses it, curves down-left
p2 = [(155, 75), (150, 105), (140, 140), (120, 180), (95, 220), (65, 255)]
d.line(p2, fill=INK, width=W, joint="curve")

# Stroke 3: 捺 (right-falling) — from crossing point down to lower-right
p3 = [(155, 130), (170, 160), (190, 195), (215, 230), (245, 260)]
d.line(p3, fill=INK, width=W, joint="curve")

out = os.path.join(os.path.dirname(__file__), "01_大.png")
img.save(out)
print(f"wrote {out}")
