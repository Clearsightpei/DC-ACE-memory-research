"""G1 render of 鸭 = 甲 (left) + 鸟 (right). Revision 2."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 5

def line(pts, w=LW):
    d.line(pts, fill="black", width=w)

# ---------- LEFT: 甲 ----------
# Top horizontal
line([(40, 90), (125, 90)])
# Left vertical
line([(42, 90), (42, 175)])
# Right vertical (with slight taper — 竖折)
line([(125, 90), (125, 175)])
# Middle horizontal
line([(42, 132), (125, 132)])
# Bottom horizontal
line([(42, 175), (125, 175)])
# Central vertical extending down as tail
line([(83, 90), (83, 250)])

# ---------- RIGHT: 鸟 ----------
# 1. Top short slash (丿) - the head-top
line([(210, 55), (195, 75)])
# 2. Head: horizontal-fold-fold shape (top box)
# top horizontal
line([(195, 75), (255, 78)])
# right side going down
line([(255, 78), (255, 115)])
# bottom horizontal of head
line([(200, 115), (255, 115)])
# 3. Eye dot inside head
line([(225, 90), (235, 100)], w=6)
# 4. Left vertical of body (from head down)
line([(200, 75), (200, 200)])
# 5. Dot in the middle-body area (the 点 in 鸟)
line([(230, 145), (240, 155)], w=6)
# 6. Bottom sweep — horizontal that curls right then hooks
line([(200, 200), (275, 205)])       # bottom horizontal to the right
line([(275, 205), (270, 230)])       # slight down
line([(270, 230), (215, 235)])       # sweep back left forming the base

os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_鸭.png")
img.save(out)
print("Saved:", out)
