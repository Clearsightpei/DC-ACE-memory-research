"""Render 说 (shuo) to a 300x300 PNG using PIL.

Revised once after comparing to GT.
Structure:
- Left radical 讠 (speech): short slanted dot on top, then a
  short down-right stroke that hooks up-right (simplified 讠 with hook).
- Right side 兑:
  - 丷 : two slanted dots on top (\\ and /)
  - 口 : small square
  - 儿 : left 撇 curving down-left, right 竖弯钩 going down then right and up.
"""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)
INK = (0, 0, 0)


def line(pts, width=5):
    draw.line(pts, fill=INK, width=width, joint="curve")


# ---- Left radical 讠 ----
# Top dot: short slanted stroke like a comma
line([(55, 55), (75, 78)], width=6)

# Speech-radical body: horizontal-turn-hook (simplified 讠)
# A short down-slant, then a longer stroke curving down and hooking up-right
line([(50, 130), (75, 150), (65, 240), (105, 250), (95, 235)], width=5)

# ---- Right side 兑 ----
# Top 丷 : left dot (slanting down-left, i.e. 撇), right dot (slanting down-right, i.e. 点)
line([(155, 55), (140, 82)], width=6)   # left slanted 撇
line([(210, 55), (225, 82)], width=6)   # right slanted 点

# 口 (mouth box)
# Left vertical
line([(155, 100), (155, 150)], width=5)
# Top horizontal + right vertical
line([(155, 100), (220, 100), (220, 150)], width=5)
# Bottom horizontal (small closing stroke)
line([(155, 150), (220, 150)], width=5)

# 儿 (legs)
# Left leg: 撇 - starts near top of 口 area, curves down and to the left
line([(160, 160), (145, 210), (120, 260)], width=5)
# Right leg: 竖弯钩 - straight down, curves right, hooks up
line([(210, 160), (210, 230), (240, 260), (260, 255), (255, 240)], width=5)


out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_说.png"))
print("wrote", os.path.join(out_dir, "01_说.png"))
