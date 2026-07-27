"""Render 十 (ten) to a 300x300 PNG.

十 = one horizontal stroke (一) + one vertical stroke (丨).
Structure inferred from clean GT: horizontal crosses vertical slightly
above the middle (about 45% down); vertical extends from near the top
to near the bottom.
"""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

INK = "black"
STROKE_W = 8

# Horizontal stroke (一): crossing slightly above middle
# GT: from ~x=45 to x=255, at ~y=140
draw.line([(45, 140), (255, 140)], fill=INK, width=STROKE_W)

# Vertical stroke (丨): centered horizontally, spans most of height
# GT: from ~y=55 to y=285, at x=150
draw.line([(150, 55), (150, 285)], fill=INK, width=STROKE_W)

out_path = os.path.join(os.path.dirname(__file__), "01_十.png")
img.save(out_path)
print(f"wrote {out_path}")
