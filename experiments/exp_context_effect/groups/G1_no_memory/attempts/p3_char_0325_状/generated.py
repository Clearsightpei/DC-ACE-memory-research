"""G1 draw of 状 (zhuang) — 爿 (left) + 犬 (right). Revision 2."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# ==== Left: 爿 (occupies roughly x=40..135, y=55..260) ====
# 1) top short pie-like slash (upper-left)
stroke([(60, 75), (95, 95)], width=5)

# 2) short horizontal near top (crossing)
stroke([(70, 118), (115, 110)], width=5)

# 3) inner short vertical (right vertical of 爿 upper box)
stroke([(112, 110), (108, 180)], width=5)

# 4) main long vertical down the left
stroke([(78, 95), (60, 265)], width=5)

# 5) bottom horizontal
stroke([(60, 248), (135, 235)], width=5)

# ==== Right: 犬 (occupies roughly x=145..275, y=70..270) ====
# 1) top horizontal (top of 大)
stroke([(150, 130), (255, 118)], width=5)

# 2) 撇 pie — from top-center down to bottom-left
stroke([(210, 108), (155, 265)], width=6)

# 3) 捺 na — from crossing near horizontal, down-right to bottom-right
stroke([(200, 148), (270, 268)], width=6)

# 4) 点 dot on upper right (犬's distinguishing dot)
stroke([(248, 95), (262, 112)], width=6)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_状.png"))
print("saved", os.path.join(out_dir, "01_状.png"))
