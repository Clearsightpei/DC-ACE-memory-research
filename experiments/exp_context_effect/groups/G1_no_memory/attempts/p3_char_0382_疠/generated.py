"""G1 render for 疠 (p3_char_0382). 300x300 PNG, PIL."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 4

def line(p1, p2, w=LW):
    d.line([p1, p2], fill=BLACK, width=w)

def curve(points, w=LW):
    for i in range(len(points) - 1):
        d.line([points[i], points[i + 1]], fill=BLACK, width=w)

# 疠 = 疒 (sickness radical, top-left wrap, 5 strokes) + 万 (inside, 3 strokes)
# Compose within roughly x:60-260, y:50-260

# --- 疒 radical ---
# 1) top dot (点)
line((115, 60), (128, 78))

# 2) horizontal top stroke (横)
line((95, 100), (220, 95))

# 3) long left descending 撇
curve([(128, 100), (115, 135), (100, 175), (80, 220), (60, 260)])

# 4) small left dot upper (两点 on radical)
line((90, 130), (102, 140))

# 5) small left dot lower
line((78, 165), (90, 175))

# --- 万 (inside lower-right region roughly x:130-235, y:130-250) ---
# horizontal (short)
line((140, 155), (225, 150))

# right vertical/hook: goes down then hooks left (横折钩)
curve([(218, 155), (218, 195), (215, 225), (205, 245), (185, 250)])

# left slash (撇) from middle of 横 down-left
curve([(165, 160), (155, 195), (145, 225), (135, 250)])

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_疠.png"))
print("saved 01_疠.png")
