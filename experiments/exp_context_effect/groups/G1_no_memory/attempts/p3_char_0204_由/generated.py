"""G1 render for 由 — 300x300, black ink on white."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 6

# Character 由: box + central vertical extending above + middle horizontal
# Box: left=90, right=220, top=110, bottom=250
left, right, top, bot = 90, 220, 110, 250
mid_x = (left + right) // 2  # 155
mid_y = (top + bot) // 2     # 180

# Stroke 1: central vertical (extends above the box, through the box)
d.line([(mid_x, 45), (mid_x, bot - 5)], fill=INK, width=LW)

# Stroke 2: left vertical of box
d.line([(left, top), (left, bot)], fill=INK, width=LW)

# Stroke 3: top horizontal + right vertical (横折)
d.line([(left, top), (right, top)], fill=INK, width=LW)
d.line([(right, top), (right, bot)], fill=INK, width=LW)

# Stroke 4: middle horizontal (inside the box)
d.line([(left, mid_y), (right, mid_y)], fill=INK, width=LW)

# Stroke 5: bottom horizontal (closes the box)
d.line([(left, bot), (right, bot)], fill=INK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_由.png")
img.save(out)
print("saved", out)
