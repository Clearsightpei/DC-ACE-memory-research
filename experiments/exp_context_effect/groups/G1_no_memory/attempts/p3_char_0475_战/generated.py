"""G1 render of 战 (zhàn). Left: 占. Right: 戈."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 5

def line(p1, p2, w=LW):
    d.line([p1, p2], fill="black", width=w)

def curve(points, w=LW):
    d.line(points, fill="black", width=w, joint="curve")

# ===== LEFT component: 占 =====
# 卜 top: vertical stem
line((78, 70), (78, 155), LW)
# horizontal short tick to right of stem (the 一 of 卜)
line((78, 110), (115, 108), LW)

# 口 lower
line((45, 175), (45, 250), LW)   # left
line((45, 175), (125, 175), LW)  # top
line((125, 175), (125, 250), LW) # right
line((45, 250), (125, 250), LW)  # bottom

# ===== RIGHT component: 戈 =====
# 1) short horizontal 一 (upper)
line((150, 120), (225, 118), LW)

# 2) long 斜钩 - starts upper-right area, sweeps DOWN and slightly LEFT then curves back RIGHT with a hook up
curve([(210, 90), (220, 140), (225, 200), (240, 250), (255, 245), (262, 232)], LW)

# 3) 撇 - short diagonal from crossing horizontal, going down-left
line((175, 130), (145, 220), LW)

# 4) 点 - small dot at upper right (top of 戈)
line((255, 75), (270, 95), LW)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_战.png"))
print("saved 01_战.png")
