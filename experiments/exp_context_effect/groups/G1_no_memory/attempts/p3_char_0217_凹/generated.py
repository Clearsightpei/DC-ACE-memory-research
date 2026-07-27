"""G1 render of 凹 (concave). No memory, PIL-based, 300x300."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLK = (0, 0, 0)
LW = 6

# Character 凹 — 5 strokes. Layout based on GT observation:
# Top edge sits ~y=95, bottom ~y=245. Left edge ~x=55, right ~x=245.
# Central notch: top ~y=95, bottom of notch ~y=155, notch width ~x=120..180.

# Stroke 1: left vertical (short, going down from top-left)
# The left "shoulder" — goes from top-left down a bit
d.line([(60, 100), (60, 245)], fill=BLK, width=LW)  # left long vertical

# Stroke 2: top-left horizontal then down into notch
# horizontal segment from (60,100) to (120,105) then down to (120,155)
d.line([(60, 100), (125, 105)], fill=BLK, width=LW)
d.line([(125, 105), (122, 158)], fill=BLK, width=LW)

# Stroke 3: bottom of notch — horizontal across notch then up on right side of notch
d.line([(122, 158), (180, 155)], fill=BLK, width=LW)
d.line([(180, 155), (178, 100)], fill=BLK, width=LW)

# Stroke 4: top-right horizontal then down (right shoulder + right vertical)
d.line([(178, 100), (243, 105)], fill=BLK, width=LW)
d.line([(243, 105), (243, 245)], fill=BLK, width=LW)

# Stroke 5: bottom horizontal closing
d.line([(60, 245), (243, 245)], fill=BLK, width=LW)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_凹.png"))
print("wrote", os.path.join(out_dir, "01_凹.png"))
