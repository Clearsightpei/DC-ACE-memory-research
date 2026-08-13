"""G1 render of 乖 (character p3_char_0368)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
LW = 4

# Stroke 1: short horizontal at top (the 撇-like short top)
d.line([(120, 60), (180, 55)], fill=INK, width=LW)

# Stroke 2: long horizontal (upper crossbar of 千-like center)
d.line([(60, 105), (240, 100)], fill=INK, width=LW)

# Stroke 3: long central vertical (through the character)
d.line([(150, 70), (150, 265)], fill=INK, width=LW)

# Left "北"-like element: two short horizontals + a vertical hook on left side
# left vertical
d.line([(70, 140), (70, 215)], fill=INK, width=LW)
# left upper short horizontal (like 一)
d.line([(70, 140), (110, 138)], fill=INK, width=LW)
# left lower short horizontal
d.line([(70, 180), (115, 178)], fill=INK, width=LW)
# left bottom hook stroke (small pickup)
d.line([(70, 215), (115, 210)], fill=INK, width=LW)

# Right side: mirrors like 匕 / small hook shape
# right small horizontal top
d.line([(190, 140), (230, 138)], fill=INK, width=LW)
# right vertical hook (comes down and curls left)
d.line([(230, 138), (230, 210)], fill=INK, width=LW)
d.line([(230, 210), (200, 220)], fill=INK, width=LW)
# right small stroke inside (little slash)
d.line([(195, 155), (215, 175)], fill=INK, width=LW)

out_path = os.path.join(os.path.dirname(__file__), "01_乖.png")
img.save(out_path)
print(f"Wrote {out_path}")
