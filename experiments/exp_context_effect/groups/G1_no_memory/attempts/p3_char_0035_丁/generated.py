"""Render 丁 (dīng) — 2 strokes: horizontal top + vertical hook."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
STROKE = 8

# Stroke 1: horizontal top (一) — spans most of the width, roughly at y ~ 95
# Slight upward curve at ends per the GT
draw.line([(45, 100), (255, 95)], fill=INK, width=STROKE)

# Stroke 2: vertical hook (亅) — starts near top-center, goes down, hooks left
# Vertical part
draw.line([(155, 95), (155, 235)], fill=INK, width=STROKE)
# Hook at bottom, curving to the left
draw.line([(155, 235), (125, 250)], fill=INK, width=STROKE)

# Save
out_path = os.path.join(os.path.dirname(__file__), "01_丁.png")
img.save(out_path)
print(f"Saved {out_path}")
