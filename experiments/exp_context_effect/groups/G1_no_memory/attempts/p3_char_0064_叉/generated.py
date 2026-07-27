"""Render 叉 to 01_叉.png using PIL. 300x300 white background, black ink."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

W = 8  # stroke width

# 叉 has 3 strokes:
# 1) 横撇 (heng-pie): horizontal top then sharp diagonal down-left
# 2) 捺 (na): diagonal down-right crossing the pie
# 3) 点 (dian): short dot inside the upper-left area

# Stroke 1: 横撇 (top horizontal into a downward-left diagonal)
# Horizontal from ~ (95,100) to (200,95), then turn and slash down-left to (75, 240)
heng = [(95, 105), (205, 98)]
d.line(heng, fill="black", width=W)
# The pie portion after the corner
pie = [(205, 98), (170, 150), (120, 200), (75, 245)]
for i in range(len(pie)-1):
    d.line([pie[i], pie[i+1]], fill="black", width=W)

# Stroke 2: 捺 (na) — from upper-left area diagonally down to lower right
# Starts around (85, 150), sweeps down-right past center to (260, 255)
na = [(85, 150), (135, 190), (190, 225), (260, 255)]
for i in range(len(na)-1):
    d.line([na[i], na[i+1]], fill="black", width=W)

# Stroke 3: 点 (small short diagonal stroke) in the upper-left inner region
dot = [(110, 140), (145, 158)]
d.line(dot, fill="black", width=W)

out = os.path.join(os.path.dirname(__file__), "01_叉.png")
img.save(out)
print("Wrote", out)
