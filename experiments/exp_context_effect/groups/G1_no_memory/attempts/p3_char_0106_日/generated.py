"""Render 日 (sun) at 300x300, black ink on white, using PIL."""
from PIL import Image, ImageDraw
from pathlib import Path

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

INK = "black"
W = 5  # stroke width

# 日 is a rectangle with a horizontal bar in the middle.
# Stroke order: (1) left vertical 丨, (2) top+right 横折 (horizontal then down),
# (3) middle horizontal 一, (4) bottom horizontal 一.
# GT shows tall narrow rectangle.

# Bounding box for the character body
left, right = 95, 205
top, bottom = 55, 260
mid_y = (top + bottom) // 2 + 5  # slight below center like GT

# Stroke 1: left vertical (丨) - slight tilt like GT
d.line([(left, top + 5), (left - 3, bottom)], fill=INK, width=W)

# Stroke 2: 横折 - top horizontal then right vertical
d.line([(left - 2, top), (right, top + 3)], fill=INK, width=W)
d.line([(right, top + 3), (right - 2, bottom + 2)], fill=INK, width=W)

# Stroke 3: middle horizontal (一)
d.line([(left + 5, mid_y), (right - 8, mid_y - 2)], fill=INK, width=W)

# Stroke 4: bottom horizontal (一)
d.line([(left + 3, bottom), (right - 5, bottom + 2)], fill=INK, width=W)

out = Path(__file__).parent / "01_日.png"
img.save(out)
print(f"wrote {out}")
