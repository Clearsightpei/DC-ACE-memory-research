"""G1 render for radical 己 (3 strokes)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 7

def line(pts, width=LW):
    d.line(pts, fill=INK, width=width, joint="curve")

# Stroke 1: 横折 (top) — horizontal from left to right, then short vertical down
# Top horizontal (slight upward curve like GT)
line([(80, 100), (210, 92)])
# Turn: short vertical down (the fold)
line([(210, 92), (215, 135)])

# Stroke 2: 横 (middle) — shorter horizontal, joins the left vertical, ends mid-width
line([(80, 155), (175, 152)])

# Stroke 3: 竖弯钩 (bottom) — vertical down from left, curve right along bottom, up-hook
# Vertical down
line([(80, 155), (85, 225)])
# Bottom curve to the right
line([(85, 225), (225, 230)])
# Clearer up-hook at the end
line([(225, 230), (232, 200)])

out = os.path.join(os.path.dirname(__file__), "01_己.png")
img.save(out)
print("wrote", out)
