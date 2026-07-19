"""G1 render of radical 肀 (4 strokes)."""
import os
from PIL import Image, ImageDraw

SIZE = 300
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_肀.png")

img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
W = 6

# 肀: like top of 聿. Three horizontals stacked closely, long vertical
# through them (no bottom hook). Top stroke is a short 横折 (horizontal
# then turn down).
#
# GT observations (from gt/phase2/肀.png):
#  - top short 横折 sits just above the upper of two closely spaced horizontals
#  - middle & bottom horizontals span wide, roughly equal length
#  - long vertical extends well below the bottom horizontal
#  - overall the character sits slightly left of center-vertical? Actually
#    horizontals extend a bit further right than left of the vertical.

CX = 150

# Stroke 1: top short 横折 — short horizontal, then turns down
# Sits above the middle horizontal, right of the vertical
d.line([(148, 95), (185, 100)], fill=BLACK, width=W)     # short horizontal top
d.line([(185, 100), (180, 130)], fill=BLACK, width=W)    # turn down (折)

# Stroke 2: upper long horizontal
d.line([(70, 140), (240, 138)], fill=BLACK, width=W)

# Stroke 3: lower long horizontal
d.line([(80, 185), (235, 183)], fill=BLACK, width=W)

# Stroke 4: long central vertical (no hook)
d.line([(CX, 105), (CX, 275)], fill=BLACK, width=W)

img.save(OUT)
print(f"Saved {OUT}")
