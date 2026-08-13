"""G1 render of 信 — person radical (亻) + speech (言)."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 4

def line(p1, p2, w=LW):
    d.line([p1, p2], fill="black", width=w)

# ---- 亻 (person radical, left side) ----
# 撇 (diagonal from upper right to lower left)
line((85, 70), (50, 175), w=LW)
# 竖 (vertical, attached at mid of 撇, going down)
line((72, 130), (72, 265), w=LW)

# ---- 言 (speech, right side) ----
# top 点 (small diagonal dot above)
line((175, 55), (188, 78), w=LW)

# top long 横 (horizontal)
line((110, 95), (255, 92), w=LW)

# second 横
line((130, 130), (240, 128), w=LW)
# third 横
line((130, 165), (240, 163), w=LW)

# 口 at bottom
# left vertical
line((140, 195), (140, 258), w=LW)
# top horizontal + right vertical (as a hooked shape 横折)
line((140, 195), (238, 193), w=LW)
line((238, 193), (238, 258), w=LW)
# bottom horizontal (closing)
line((140, 258), (238, 258), w=LW)

out_path = os.path.join(os.path.dirname(__file__), "01_信.png")
img.save(out_path)
print("wrote", out_path)
