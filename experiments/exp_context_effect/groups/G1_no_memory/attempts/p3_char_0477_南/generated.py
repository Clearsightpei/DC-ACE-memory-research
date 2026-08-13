"""G1 render of 南 (south) at 300x300."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

W = 6  # stroke width

def line(p1, p2, w=W):
    d.line([p1, p2], fill="black", width=w)

# Top "十" crown: horizontal + vertical piercing it
line((90, 60), (215, 60), W)     # top horizontal
line((150, 35), (150, 100), W)   # vertical through it (extends below into box top area)

# Outer 冂 frame:
# top horizontal of the box
line((70, 105), (230, 105), W)
# left vertical (straight down)
line((70, 105), (70, 265), W)
# right vertical + small left hook (亅)
line((230, 105), (230, 255), W)
line((230, 255), (212, 270), W)

# Inner element: upper horizontal
line((100, 145), (200, 145), W)

# Inner Ц (U-shape open at top): two short verticals + bottom horizontal
line((115, 165), (115, 225), W)  # left inner vertical
line((185, 165), (185, 225), W)  # right inner vertical
line((115, 225), (185, 225), W)  # bottom of Ц

# Inner 十 inside the Ц
line((130, 195), (170, 195), W)  # small horizontal
line((150, 170), (150, 220), W)  # small vertical

out = os.path.join(os.path.dirname(__file__), "01_南.png")
img.save(out)
print("saved", out)
