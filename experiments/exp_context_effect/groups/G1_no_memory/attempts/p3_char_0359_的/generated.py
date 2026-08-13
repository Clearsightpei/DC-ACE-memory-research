"""Render 的 (de) at 300x300 using PIL. 的 = 白 (left) + 勺 (right)."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 5

def line(p1, p2, w=LW):
    d.line([p1, p2], fill="black", width=w)

def curve(pts, w=LW):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill="black", width=w)

# ---- Left: 白 (bai)  x range ~35-135, y range ~55-245  ----
# stroke 1: 撇 (top slanted stroke) — starts near top-right of frame, curves down-left
curve([(95, 55), (85, 68), (72, 85), (60, 95)])

# stroke 2: 竖 (left vertical)
line((55, 95), (55, 240))

# stroke 3: 横折 (top horizontal + right vertical, one stroke)
curve([(55, 95), (130, 92), (132, 100), (132, 240)])

# stroke 4: 横 (middle horizontal)
line((58, 165), (130, 165))

# stroke 5: 横 (bottom horizontal, closes box)
line((58, 238), (132, 238))

# ---- Right: 勺 (shao)  x range ~150-265, y range ~65-260 ----
# stroke 1: 撇 (top slanting stroke from upper-right, curves down-left through the body)
curve([(215, 65), (205, 85), (190, 115), (172, 150), (160, 175)])

# stroke 2: 横折钩 (top horizontal→right, then down-curving right side, ends with hook)
curve([
    (188, 88), (245, 85),
    (258, 92), (262, 108),
    (262, 175), (258, 210),
    (248, 235), (228, 252),
    (208, 258), (188, 250),
    (178, 240),
])

# stroke 3: 点 (dot inside the belly, short slanted stroke)
curve([(213, 178), (223, 188), (230, 200)], w=LW+2)

os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_的.png")
img.save(out)
print(out)
