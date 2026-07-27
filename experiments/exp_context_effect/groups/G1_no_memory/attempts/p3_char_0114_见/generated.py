"""Render 见 to 300x300 PNG. G1 no-memory attempt (revision 1)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 5

def line(p1, p2, width=LW):
    d.line([p1, p2], fill=INK, width=width)

def curve(points, width=LW):
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill=INK, width=width)

# 见: 4 strokes
# 1) 竖 (left) - long, curving left as it descends
# 2) 横折 (top horizontal + right vertical down)
# 3) 撇 - inside slant from upper interior down to lower-left
# 4) 竖弯钩 - inside vertical, curves right at bottom, hooks up

# GT bbox roughly: x 55..230, y 55..285

# Stroke 1: left vertical, starts high, curves outward (leftward) toward bottom
s1 = [(95, 60), (92, 130), (85, 200), (72, 250), (55, 280)]
curve(s1)

# Stroke 2: 横折 - top horizontal
line((95, 60), (225, 65))
# then right vertical straight down
line((225, 65), (222, 260))

# Stroke 3: 撇 - inside, from top area going down-left
pie = [(150, 90), (140, 150), (125, 210), (105, 255), (85, 280)]
curve(pie)

# Stroke 4: 竖弯钩 - starts from top interior, straight down, curves right, hook up
hook = [(180, 90), (182, 180), (185, 240), (200, 265), (225, 268), (232, 258), (232, 248)]
curve(hook)

out = os.path.join(os.path.dirname(__file__), "01_见.png")
img.save(out)
print(f"Saved: {out}")
