"""G1 render of 将 (jiang) — 300x300, PIL. Revision 2."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 4

def line(pts, w=LW):
    d.line(pts, fill=BLACK, width=w)

# ----- LEFT: 丬 (three-stroke variant on left) -----
# top-left short slanted dot (点)
line([(45, 75), (62, 92)], w=LW)
# long vertical stroke (main spine)
line([(78, 60), (78, 260)], w=LW+1)
# short right-going tick partway down (short horizontal-ish)
line([(78, 150), (58, 165)], w=LW)
# bottom-left tick (提)
line([(78, 235), (55, 255)], w=LW)

# ----- TOP-RIGHT: 夕-like component -----
# main piě: long down-left curve from top
line([(215, 55), (135, 145)], w=LW+1)
# 橫折 short: horizontal top then turn down
line([(160, 90), (215, 90)], w=LW)
line([(215, 90), (210, 150)], w=LW)
# closing bottom stroke curving left (like bottom of 夕)
line([(160, 150), (210, 150)], w=LW)
# inner tick/dot
line([(180, 118), (195, 132)], w=LW)

# ----- BOTTOM-RIGHT: 寸 -----
# long horizontal top of 寸
line([(130, 185), (255, 182)], w=LW)
# vertical hook (straight down then curls left)
line([(195, 182), (195, 265)], w=LW+1)
line([(195, 265), (175, 258)], w=LW)
# 点 (dot) on right side of vertical
line([(210, 205), (225, 220)], w=LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0439_将/01_将.png")
