"""G1 render for 即 (p3_char_0343). Revision 2."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=3):
    d.line(pts, fill="black", width=width)

# LEFT COMPONENT: 艮 (looks like 白 + long horizontal + na)
# Small diagonal on top-left (the 丿 above the box)
line([(52, 80), (72, 62)], width=3)

# Box (like 白/日) top-horizontal
line([(55, 90), (125, 90)], width=3)
# Left vertical of the box
line([(55, 90), (60, 165)], width=3)
# Right vertical of the box (with slight hook)
line([(125, 90), (128, 165)], width=3)
# Middle horizontal divider inside box
line([(60, 128), (127, 128)], width=3)
# Bottom horizontal (closing the 日/白 shape)
line([(60, 165), (128, 165)], width=3)

# Long bottom horizontal of 艮 (extends further)
line([(40, 210), (145, 205)], width=3)
# 捺 (falling right stroke) - the bottom right of 艮
line([(110, 205), (150, 245)], width=3)

# RIGHT COMPONENT: 卩
# Top horizontal-turn stroke: horizontal then down (top part of 卩's box)
line([(170, 85), (222, 82)], width=3)
line([(222, 82), (222, 155)], width=3)
# Hook bottom of the small box (curving in)
line([(222, 155), (195, 162)], width=3)
line([(195, 162), (188, 155)], width=3)
# Left vertical of top box
line([(178, 90), (180, 145)], width=3)

# Long vertical descender with slight sway (the 竖 of 卩)
line([(188, 90), (188, 280)], width=3)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_即.png"))
print("saved")
