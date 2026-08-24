"""G1 render of 佧 = 亻 + 卡. 卡 = 上 stacked on 下 sharing a vertical."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 4

def line(pts, w=LW):
    d.line(pts, fill="black", width=w)

# ---- Left: 亻 (person radical) ----
# piě
line([(95, 90), (72, 170)], w=LW)
# shù (vertical)
line([(92, 120), (92, 245)], w=LW)

# ---- Right: 卡 ----
# 上 part:
#   short vertical (top)
line([(195, 85), (195, 135)], w=LW)
#   top-right short horizontal (short crossbar of 上's top)
line([(195, 110), (240, 108)], w=LW)
#   long horizontal (bottom of 上, = top of 下)
line([(155, 145), (255, 143)], w=LW)

# 下 part:
#   long vertical descending through
line([(195, 145), (195, 250)], w=LW)
#   dot/piě-dian on right side of 下's vertical
line([(200, 185), (225, 205)], w=LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0354_佧/01_佧.png")
