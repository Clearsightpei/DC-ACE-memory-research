"""Render 规 as 300x300 black-on-white PNG using PIL.
规 = 夫 (left) + 见 (right)
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 4

def line(pts, w=LW):
    d.line(pts, fill="black", width=w)

# ---- LEFT: 夫 ----
# Top horizontal (shorter, higher)
line([(45, 100), (125, 97)])
# Second horizontal (longer, main crossbar)
line([(30, 145), (135, 142)])
# Vertical descender / center stem
line([(80, 75), (80, 180)])
# 撇 (left-falling from upper stem to lower-left)
line([(80, 150), (30, 245)])
# 捺 (right-falling from upper stem to lower-right)
line([(80, 150), (140, 240)])

# ---- RIGHT: 见 ----
# Top horizontal of the box (top of 冂)
line([(165, 80), (255, 77)])
# Left vertical of box
line([(168, 80), (168, 200)])
# Right vertical of box (from top-right corner down)
line([(255, 77), (256, 200)])
# Middle horizontal inside box (eye stroke)
line([(170, 140), (256, 138)])
# 撇 (left-falling leg from bottom-left of box)
line([(168, 200), (200, 270)])
# 竖弯钩 (right leg: down then curve right, with small upward hook)
# down segment
line([(256, 200), (256, 240)])
# curve down-right
line([(256, 240), (275, 260)])
line([(275, 260), (290, 262)])
# tiny hook back up
line([(290, 262), (288, 252)])

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0407_规/01_规.png")
