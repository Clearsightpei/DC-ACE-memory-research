"""G1 render of 方 (radical). 300x300 PIL, black ink on white."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def line(p0, p1, width=6):
    draw.line([p0, p1], fill="black", width=width)

def poly(points, width=6):
    for i in range(len(points) - 1):
        line(points[i], points[i + 1], width=width)

# Stroke 1: 点 (dot) at top-center, short slanted stroke ↘
poly([(150, 40), (170, 68)], width=8)

# Stroke 2: 横 (horizontal) — the middle bar, slight rise to the right
poly([(70, 108), (235, 100)], width=7)

# Stroke 3: 撇 (long slanting stroke) starting from top area near horizontal,
# sweeping down-left through the body to lower-left
poly([(125, 95), (110, 150), (85, 210), (60, 255)], width=7)

# Stroke 4: 横折钩 — starts as short horizontal on right, folds down, tiny hook left
poly([(120, 155), (205, 150), (205, 160), (195, 240)], width=7)
# small hook at bottom
poly([(195, 240), (178, 238)], width=7)

out = os.path.join(os.path.dirname(__file__), "01_方.png")
img.save(out)
print("saved", out)
