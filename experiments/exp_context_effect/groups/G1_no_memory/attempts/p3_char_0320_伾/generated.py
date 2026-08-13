"""Render 伾 (亻 + 丕) to 01_伾.png at 300x300."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLK = (0, 0, 0)

def line(p1, p2, width=5):
    d.line([p1, p2], fill=BLK, width=width)

# 亻 (person radical) on the left
# 撇 (slanted down-left)
line((105, 55), (60, 200), width=6)
# 竖 (long vertical)
line((105, 115), (105, 275), width=5)

# 丕 on the right (~ x range 135..275)
# top 一 (long horizontal, slightly rising to right)
line((140, 85), (275, 78), width=6)
# short 撇 (down-left slant)
line((190, 90), (170, 175), width=5)
# short 竖 (vertical center)
line((215, 92), (215, 175), width=5)
# short 点/捺 (down-right slant)
line((240, 92), (255, 165), width=5)
# bottom 一 (long horizontal)
line((135, 245), (285, 240), width=7)

out = os.path.join(os.path.dirname(__file__), "01_伾.png")
img.save(out)
print("saved", out)
