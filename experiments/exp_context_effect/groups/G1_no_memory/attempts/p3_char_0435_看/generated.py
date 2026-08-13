"""G1 render of 看 (look) — 手 on top + 目 on bottom-right."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
T = 4


def line(p0, p1, width=T):
    d.line([p0, p1], fill=INK, width=width)


def curve(points, width=T, steps=80):
    (x0, y0), (x1, y1), (x2, y2) = points
    prev = (x0, y0)
    for i in range(1, steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t ** 2 * x2
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t ** 2 * y2
        d.line([prev, (x, y)], fill=INK, width=width)
        prev = (x, y)


# ---- Top part: 手 ----
# Stroke 1: short 丿 top-left (little diagonal descending left)
curve([(135, 45), (120, 55), (105, 68)], width=T)

# Stroke 2: short horizontal near top
line((110, 78), (185, 72), width=T)

# Stroke 3: middle horizontal (a bit longer)
line((85, 108), (215, 102), width=T)

# Stroke 4: long horizontal — the wide 一 of 手 (spans nearly full width)
line((45, 152), (280, 142), width=T)

# Stroke 5: long 撇 sweeping from upper-right down to lower-left
curve([(180, 55), (125, 175), (55, 285)], width=T)

# ---- Bottom part: 目 (tucked to the right of the 撇) ----
LX, RX = 155, 235
TY, BY = 172, 285
# Left vertical
line((LX, TY), (LX, BY), width=T)
# Top horizontal
line((LX, TY), (RX, TY), width=T)
# Right vertical
line((RX, TY), (RX, BY), width=T)
# Bottom horizontal
line((LX, BY), (RX, BY), width=T)
# Two middle horizontals inside 目
line((LX, TY + 38), (RX, TY + 37), width=T)
line((LX, TY + 76), (RX, TY + 75), width=T)

out = os.path.join(os.path.dirname(__file__), "01_看.png")
img.save(out)
print("wrote", out)
