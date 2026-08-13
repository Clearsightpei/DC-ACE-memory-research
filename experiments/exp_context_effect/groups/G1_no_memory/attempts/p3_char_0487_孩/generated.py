"""G1 render of 孩 (child). Left: 子 radical, Right: 亥.
PIL, 300x300, white bg, black ink.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

def curve(pts, width=5, steps=30):
    (x0,y0),(x1,y1),(x2,y2) = pts
    prev = (x0,y0)
    for i in range(1, steps+1):
        t = i/steps
        x = (1-t)*(1-t)*x0 + 2*(1-t)*t*x1 + t*t*x2
        y = (1-t)*(1-t)*y0 + 2*(1-t)*t*y1 + t*t*y2
        d.line([prev, (x,y)], fill="black", width=width)
        prev = (x,y)

# ====== LEFT: 子 (child radical) ======
# stroke 1: 横撇弯钩 (top: short horizontal then sharp turn down-left)
line([(30, 60), (110, 55)], width=5)
line([(110, 55), (55, 110)], width=5)
# stroke 2: 竖钩 (vertical hook, long, ends with small left-flick hook)
curve([(85, 60), (80, 170), (60, 235)], width=5)
line([(60, 235), (90, 220)], width=5)  # hook
# stroke 3: 横 (horizontal crossbar through middle)
line([(20, 150), (120, 143)], width=5)

# ====== RIGHT: 亥 ======
# stroke 1: 点 top dot
line([(180, 40), (192, 58)], width=6)
# stroke 2: 一 horizontal across
line([(140, 78), (285, 72)], width=5)
# stroke 3: 撇 (left-descending from under 一, upper part)
curve([(175, 90), (155, 130), (135, 165)], width=5)
# stroke 4: 撇折 (small: down-left then flick right)
line([(180, 125), (165, 150)], width=5)
line([(165, 150), (200, 148)], width=5)
# stroke 5: another small 撇 in middle
line([(210, 130), (195, 155)], width=5)
# stroke 6: 一 short mid horizontal (bottom of middle chunk)
line([(170, 175), (250, 172)], width=5)
# stroke 7: 撇 long sweeping down to bottom-left
curve([(200, 180), (170, 220), (125, 280)], width=5)
# stroke 8: 捺 long sweeping down to bottom-right
curve([(215, 180), (245, 230), (285, 280)], width=5)

os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_孩.png")
img.save(out)
print("wrote", out)
