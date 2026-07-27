"""G1 render of 仔 = 亻 (person radical) + 子 (child)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
TH = 7


def line(pts, width=TH):
    d.line(pts, fill=INK, width=width, joint="curve")


def curve(pts, width=TH, steps=32):
    (x0, y0), (x1, y1), (x2, y2) = pts
    prev = (x0, y0)
    for i in range(1, steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t ** 2 * x2
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t ** 2 * y2
        d.line([prev, (x, y)], fill=INK, width=width)
        prev = (x, y)


# ============== 亻 (person radical, left) ==============
# Stroke 1: 撇 (falls from upper right down to lower left)
curve([(100, 80), (85, 140), (55, 215)], width=TH)

# Stroke 2: 竖 (vertical, starts where 撇 bends, goes straight down)
line([(92, 150), (92, 255)], width=TH)

# ============== 子 (child, right) ==============
# Stroke 1 of 子: 横撇 (a horizontal stroke that then turns sharply down-left)
# Horizontal top segment
line([(150, 95), (240, 95)], width=TH)
# Sharp turn: short downward-left tail from the right end of the horizontal
curve([(240, 95), (232, 120), (210, 140)], width=TH)

# Stroke 2 of 子: 竖钩 (vertical hook - the main spine)
# It starts near the middle of the horizontal top and goes down
line([(190, 95), (190, 235)], width=TH)
# hook curling left at the bottom
curve([(190, 235), (180, 248), (160, 248)], width=TH)

# Stroke 3 of 子: 横 (the horizontal middle crossbar, wider)
line([(130, 180), (255, 180)], width=TH)

out = os.path.join(os.path.dirname(__file__), "01_仔.png")
img.save(out)
print(f"wrote {out}")
