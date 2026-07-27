"""Render 子 (child) to 300x300 PNG."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 6

# Stroke 1: top horizontal-hook (横撇/横钩) — starts upper-left, goes right, hooks down
# Roughly: (80, 90) -> (200, 85) -> hook down to (195, 110)
draw.line([(80, 92), (135, 82), (195, 85)], fill=INK, width=LW)
draw.line([(195, 85), (200, 100), (185, 115)], fill=INK, width=LW)

# Stroke 2: vertical hook (竖钩) — from top center down through, ending with a small hook
# Starts near where stroke 1 ended (~(160, 100)) going down to bottom, hook left
draw.line([(160, 100), (155, 170), (145, 240)], fill=INK, width=LW)
# hook at bottom curving left
draw.line([(145, 240), (130, 250), (110, 245)], fill=INK, width=LW)

# Stroke 3: horizontal stroke through the middle (一)
draw.line([(65, 165), (155, 160), (240, 168)], fill=INK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_子.png")
img.save(out)
print(f"saved {out}")
