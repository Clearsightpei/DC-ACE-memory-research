"""Render 上 (character) to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 6

# 上 = three strokes:
# 1) vertical (shu) — long vertical down the middle
# 2) short horizontal (heng) — small tick to the right of middle
# 3) long bottom horizontal (heng) — baseline

# Stroke 1: vertical, slightly off-center-left, from upper-mid down to lower baseline
# Starts around (145, 80), ends around (145, 235)
draw.line([(148, 78), (146, 235)], fill=INK, width=LW)
# small hook/pen-lift at top-right
draw.line([(148, 78), (160, 88)], fill=INK, width=LW)

# Stroke 2: short horizontal to the right of vertical
# From about (155, 155) to (210, 148) — slight upward slope
draw.line([(158, 158), (215, 148)], fill=INK, width=LW)

# Stroke 3: long horizontal baseline; GT shows endpoints angled upward
# (shallow inverted-V / wide-flat shape). Middle sits lower than the ends.
pts = [(45, 260), (95, 245), (150, 240), (205, 245), (260, 258)]
draw.line(pts, fill=INK, width=LW, joint="curve")

out_path = os.path.join(os.path.dirname(__file__), "01_上.png")
img.save(out_path)
print(f"Wrote {out_path}")
