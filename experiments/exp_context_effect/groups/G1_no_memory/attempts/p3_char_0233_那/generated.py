"""G1 render for 那 (p3_char_0233) — revision 1."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# Left component (尹-like of 那): three horizontals stacked, a short vertical
# joining top-two, and a long 撇 sweeping from upper-right down to lower-left.

# Top horizontal (slight upward slant right)
line([(45, 100), (150, 92)], width=5)
# Middle horizontal
line([(55, 145), (145, 140)], width=5)
# Bottom horizontal (slightly longer, extending past midline right)
line([(35, 200), (160, 190)], width=5)
# Short vertical connecting top and middle horizontals (left side)
line([(80, 92), (78, 148)], width=5)
# Long 撇: from top-right of left component sweeping to bottom-left
line([(150, 100), (60, 275)], width=6)

# Right component 阝 (right ear radical):
# Small D-shaped loop at top, then long vertical descending
# Loop top-right corner + curve
line([(195, 105), (240, 105)], width=5)                # top of loop
line([(240, 105), (245, 145), (215, 155)], width=5)    # right/bottom curve
line([(215, 155), (195, 155)], width=5)                # bottom of loop back
# Long vertical descending (with slight left tail at bottom)
line([(200, 100), (200, 270)], width=6)

out = os.path.join(os.path.dirname(__file__), "01_那.png")
img.save(out)
print("saved", out)
