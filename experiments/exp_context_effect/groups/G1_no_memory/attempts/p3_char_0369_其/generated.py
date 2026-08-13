"""G1 render of 其 (p3_char_0369). Revised once."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
T = 4

def line(p1, p2, w=T):
    d.line([p1, p2], fill=INK, width=w)

# 其 - 8 strokes. Verticals actually extend ABOVE the top horizontal
# in this glyph style (little tails above), then the top horizontal
# runs across between them.

# Stroke 1: left vertical (extends from ~top down through the box)
# starts a bit above the top horizontal
line((88, 55), (78, 195), T)

# Stroke 2: right vertical (mirror), also extends above the top horizontal
line((215, 50), (222, 195), T)

# Stroke 3: top horizontal (crosses between the two verticals, slightly slanting up-right)
line((70, 78), (235, 70), T)

# Stroke 4: upper inner horizontal
line((100, 118), (208, 115), T)

# Stroke 5: lower inner horizontal
line((100, 158), (208, 155), T)

# Stroke 6: long base horizontal (extends well beyond the box)
line((40, 210), (265, 205), T + 1)

# Stroke 7: left leg 丿 (curving down-left)
line((115, 220), (85, 275), T)

# Stroke 8: right leg 丶 (down-right)
line((190, 220), (220, 275), T)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_其.png")
img.save(out_path)
print("saved", out_path)
