"""G1 render for 侷 (character p3_char_0472).
Revision 2: strengthen 尸 middle stroke, better proportions.
Structure: 亻(left) + 局 (尸 shell containing 丿 and 口).
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 4

def line(pts, width=LW):
    d.line(pts, fill=BLACK, width=width)

# --- 亻 (left radical, person) ---
# 撇 (long diagonal down-left)
line([(80, 60), (48, 180)])
# 竖 (vertical, joins mid of 撇)
line([(75, 110), (75, 255)])

# --- 局 (right side) ---
# Top horizontal-turn (横折) of 尸 outer shell
line([(120, 75), (225, 75)])         # top horizontal
line([(225, 75), (225, 270)])        # long right vertical (extends past bottom)

# Middle horizontal of 尸 (short, inside)
line([(135, 125), (210, 125)])

# 丿 (long slanting stroke sweeping from top-inside down-left past bottom)
line([(150, 95), (105, 275)])

# Inner 口 (mouth box, mid-right)
# top
line([(155, 175), (210, 175)])
# left vertical
line([(155, 175), (155, 225)])
# right vertical (uses outer right? keep separate for clarity)
line([(210, 175), (210, 225)])
# bottom
line([(155, 225), (210, 225)])

out = os.path.join(os.path.dirname(__file__), "01_侷.png")
img.save(out)
print("wrote", out)
