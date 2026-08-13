"""Render 亚 to a 300x300 PNG."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)
W = 6  # stroke width

# 亚 structure:
# 1) top horizontal (medium width, near top)
# 2) left short vertical stroke (going down slightly left)
# 3) short horizontal (middle-left dash)
# 4) short horizontal (middle-right dash)
# 5) right short vertical stroke
# 6) bottom long horizontal (wider than top)
# Actually stroke order for 亚 (6 strokes): 一 丨 丨 一 一
# top horizontal, left vertical, middle-left short horizontal, middle-right short horizontal, right vertical, bottom horizontal
# Wait 亚 has 7 strokes typically: horiz, vertical, horiz-short, vert, horiz-short, ... Let me use 6-stroke variant.

# Top horizontal
d.line([(70, 90), (230, 85)], fill="black", width=W)

# Left "vertical" (slightly slanted left)
d.line([(90, 95), (75, 175)], fill="black", width=W)

# Middle-left short horizontal
d.line([(95, 155), (135, 150)], fill="black", width=W)

# Center vertical (through middle)
d.line([(150, 90), (150, 220)], fill="black", width=W)

# Middle-right short horizontal
d.line([(165, 150), (210, 155)], fill="black", width=W)

# Right vertical (slightly slanted right)
d.line([(215, 95), (230, 180)], fill="black", width=W)

# Bottom long horizontal
d.line([(45, 240), (260, 235)], fill="black", width=W)

out = os.path.join(os.path.dirname(__file__), "01_亚.png")
img.save(out)
print("saved", out)
