from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 6

# Stroke 1: short horizontal (top), slight upward tilt to the right
d.line([(105, 80), (200, 72)], fill=INK, width=LW)

# Stroke 2: long horizontal (middle) across the character
d.line([(55, 150), (250, 145)], fill=INK, width=LW)

# Stroke 3: vertical descending from middle-right, with a small hook (piě/gōu at end)
# Vertical portion
d.line([(165, 150), (165, 240)], fill=INK, width=LW)
# Hook going left-down
d.line([(165, 240), (140, 250)], fill=INK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_亍.png")
img.save(out)
print(f"Wrote {out}")
