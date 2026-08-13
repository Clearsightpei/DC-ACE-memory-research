"""Render 留 to 01_留.png (300x300, white bg, black ink)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)
LW = 4

def line(p1, p2, w=LW):
    d.line([p1, p2], fill=BLACK, width=w)

def poly(pts, w=LW):
    d.line(pts, fill=BLACK, width=w, joint="curve")

# ============ TOP-LEFT: 卯-left (looks like ㄣ / small angled shape) ============
# 撇 stroke going down-left then a hook
poly([(85, 60), (65, 95), (60, 135), (95, 155)], w=LW)
# small internal horizontal-hook (橫折) inside
poly([(80, 95), (105, 95), (105, 118)], w=LW)

# ============ TOP-RIGHT: 卯-right (刀-shape) ============
# Top horizontal + right vertical with hook (橫折鉤)
poly([(130, 60), (230, 60), (230, 155), (215, 165)], w=LW)
# 丿 descending stroke inside (from top curving down-left)
poly([(155, 75), (140, 120), (135, 165)], w=LW)

# ============ BOTTOM: 田 ============
box_l, box_t, box_r, box_b = 90, 180, 230, 275
# left vertical (drawn first)
line((box_l, box_t), (box_l, box_b))
# top + right + hook (横折)
poly([(box_l, box_t), (box_r, box_t), (box_r, box_b)], w=LW)
# middle vertical
mx = (box_l + box_r) // 2
line((mx, box_t), (mx, box_b))
# middle horizontal
my = (box_t + box_b) // 2
line((box_l, my), (box_r, my))
# bottom horizontal
line((box_l, box_b), (box_r, box_b))

out = os.path.join(os.path.dirname(__file__), "01_留.png")
img.save(out)
print("saved", out)
