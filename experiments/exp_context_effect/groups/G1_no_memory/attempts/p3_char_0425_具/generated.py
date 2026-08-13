"""G1 draw of 具 (jù) — PIL, 300x300."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5

# Top rectangular box (目-like, upper portion of 具)
# Box occupies roughly x=95..205, y=45..175
left_x = 100
right_x = 200
top_y = 50
box_bot_y = 175

# Stroke 1: left vertical of the box
d.line([(left_x, top_y), (left_x, box_bot_y)], fill=BLACK, width=LW)
# Stroke 2: top horizontal + right vertical (bracket)
d.line([(left_x, top_y), (right_x, top_y)], fill=BLACK, width=LW)
d.line([(right_x, top_y), (right_x, box_bot_y)], fill=BLACK, width=LW)
# Stroke 3: inner horizontal 1
mid1_y = top_y + (box_bot_y - top_y) // 3
d.line([(left_x + 6, mid1_y), (right_x - 6, mid1_y)], fill=BLACK, width=LW)
# Stroke 4: inner horizontal 2
mid2_y = top_y + 2 * (box_bot_y - top_y) // 3
d.line([(left_x + 6, mid2_y), (right_x - 6, mid2_y)], fill=BLACK, width=LW)
# Stroke 5: bottom of box (short horizontal closing it)
d.line([(left_x, box_bot_y), (right_x, box_bot_y)], fill=BLACK, width=LW)

# Stroke 6: long horizontal base of character (wider than box), just below box
base_y = 195
d.line([(50, base_y), (250, base_y)], fill=BLACK, width=LW)

# Stroke 7: left diagonal (丿) below base
d.line([(130, 210), (105, 265)], fill=BLACK, width=LW)

# Stroke 8: right diagonal (丶/捺) below base
d.line([(170, 210), (200, 265)], fill=BLACK, width=LW)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_具.png"))
print("wrote", os.path.join(out_dir, "01_具.png"))
