"""Render 礻 (示字旁, 4 strokes) to a 300x300 PNG."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke(points, width=5):
    d.line(points, fill=BLACK, width=width, joint="curve")

# Stroke 1: 点 (top dot) - short diagonal
stroke([(155, 50), (170, 75)], width=6)

# Stroke 2: 横撇 (horizontal turning into a long left-falling sweep)
# horizontal top then sweeping down-left in an arc
stroke([(90, 110), (200, 115)], width=5)
# the 撇 part - sharp turn down and left as an arc
stroke([(195, 115), (185, 135), (155, 165), (115, 195), (80, 215)], width=5)

# Stroke 3: 竖 (vertical stem going down through center)
stroke([(150, 120), (148, 275)], width=5)

# Stroke 4: 点 (right dot - short diagonal from stem toward lower-right)
stroke([(155, 165), (195, 200)], width=6)

out_path = os.path.join(os.path.dirname(__file__), "01_礻.png")
img.save(out_path)
print(f"Saved: {out_path}")
