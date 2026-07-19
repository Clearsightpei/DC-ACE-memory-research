"""Render 忄 (heart radical, 3 strokes) to 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

# Stroke 1: left dot (点) - short curved stroke, tilted downward-left to right
# In GT, left dot is around x=100-115, y=170-215
def draw_left_dot():
    # A small curve going from top-right to bottom-left, then slight tail
    pts = [(118, 170), (112, 185), (108, 200), (105, 215)]
    d.line(pts, fill=BLACK, width=5)

# Stroke 2: right dot (点) - short horizontal-ish dot on the right
# In GT, right dot is around x=170-200, y=175-195
def draw_right_dot():
    pts = [(170, 180), (185, 188), (200, 195)]
    d.line(pts, fill=BLACK, width=5)

# Stroke 3: vertical (竖) - the main long vertical with slight curve at top
# GT shows curve entering from upper-left then going down straight
def draw_vertical():
    # Top curve entering from upper-left, arcing over
    top = [(140, 115), (148, 105), (156, 100), (162, 105), (164, 115)]
    d.line(top, fill=BLACK, width=5)
    # Long vertical body - straight down
    body = [(164, 115), (164, 285)]
    d.line(body, fill=BLACK, width=6)

draw_vertical()
draw_left_dot()
draw_right_dot()

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_忄.png")
img.save(out_path)
print(f"Saved: {out_path}")
