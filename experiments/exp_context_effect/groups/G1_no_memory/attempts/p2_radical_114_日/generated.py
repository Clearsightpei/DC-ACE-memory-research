"""G1 render of 日 (radical 114). 300x300 PIL, black ink on white."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

# 日 is a tall narrow rectangle with a horizontal bar through the middle.
# 4 strokes:
#   1) 竖 (left vertical)
#   2) 横折 (top horizontal + right vertical, one stroke)
#   3) 横 (middle horizontal, slightly shorter than top/bottom)
#   4) 横 (bottom horizontal, closes the box)
# Match GT proportions: tall/narrow, roughly x in [95, 205], y in [70, 240].

INK = "black"
LW = 6  # brush width

left_x = 105
right_x = 195
top_y = 55
mid_y = 150
bot_y = 250

# Stroke 1: 竖 (left vertical) — usually starts slightly higher than the top-horizontal
d.line([(left_x, top_y - 2), (left_x, bot_y)], fill=INK, width=LW)

# Stroke 2: 横折 (top horizontal then turns down on the right)
# Horizontal top
d.line([(left_x - 2, top_y), (right_x, top_y)], fill=INK, width=LW)
# Right vertical (part of the 横折)
d.line([(right_x, top_y), (right_x, bot_y)], fill=INK, width=LW)

# Stroke 3: middle 横 — slightly inset from the sides
d.line([(left_x + 4, mid_y), (right_x - 4, mid_y)], fill=INK, width=LW)

# Stroke 4: bottom 横 — closes the box
d.line([(left_x, bot_y), (right_x, bot_y)], fill=INK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_日.png")
img.save(out)
print(f"wrote {out}")
