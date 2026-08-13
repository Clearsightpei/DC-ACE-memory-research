"""G1 render of 知 (zhī). PIL-based, 300x300, black ink on white."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 4  # line width

def line(p1, p2, w=LW):
    d.line([p1, p2], fill=BLACK, width=w)

def poly(pts, w=LW):
    d.line(pts, fill=BLACK, width=w, joint="curve")

# ============ Left component: 矢 (arrow) ============
# 1. 撇 (short slant): upper-left diagonal down-left
poly([(95, 70), (78, 95)], w=LW)

# 2. 横 (horizontal above): short horizontal
poly([(70, 108), (135, 100)], w=LW)

# 3. 大 top horizontal (second horizontal in 矢)
poly([(58, 155), (150, 145)], w=LW)

# 4. 撇 (long slant from top): from near top through middle down to lower-left
poly([(120, 78), (105, 130), (85, 175), (55, 225)], w=LW)

# 5. 捺 (right-falling stroke): from mid-body down-right
poly([(105, 165), (130, 205), (155, 235)], w=LW)

# ============ Right component: 口 (mouth) ============
# left vertical
poly([(180, 140), (180, 235)], w=LW)
# top horizontal + right vertical (single stroke 横折)
poly([(180, 140), (260, 145), (258, 235)], w=LW)
# bottom horizontal
poly([(180, 232), (260, 235)], w=LW)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_知.png"))
print("saved 01_知.png")
