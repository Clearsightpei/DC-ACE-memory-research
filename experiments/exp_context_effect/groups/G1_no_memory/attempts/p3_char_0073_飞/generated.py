"""Render 飞 (fēi) at 300x300 using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6

# 飞 has 3 strokes:
# 1) 横折 — a horizontal that turns sharply down (top-left area)
# 2) short 点/撇 in the middle-right (inside the "pocket")
# 3) 竖弯钩 or long curved sweep — the big body curve on the right

# Stroke 1: 横折 — horizontal then sharp turn down
# Horizontal from left to right (slightly rising), then folds down
h1 = [
    (45, 115),
    (75, 110),
    (110, 105),
    (145, 100),
    (170, 98),
]
d.line(h1, fill=BLACK, width=LW, joint="curve")
# Fold: turn down from end of horizontal
fold = [
    (170, 98),
    (168, 115),
    (162, 135),
    (155, 150),
]
d.line(fold, fill=BLACK, width=LW, joint="curve")

# Stroke 2: short 撇/点 inside the pocket (short diagonal stroke)
dot_stroke = [
    (175, 140),
    (188, 158),
    (200, 172),
]
d.line(dot_stroke, fill=BLACK, width=LW, joint="curve")

# Stroke 3: the big sweeping curve — starts near where stroke 1 ended area
# but is a separate stroke: goes down and curves to the right, ending with a small hook up
big_curve = [
    (160, 145),
    (165, 175),
    (175, 205),
    (192, 230),
    (212, 245),
    (225, 245),
    (232, 235),
    (232, 220),
]
d.line(big_curve, fill=BLACK, width=LW, joint="curve")

out_path = os.path.join(os.path.dirname(__file__), "01_飞.png")
img.save(out_path)
print(f"Saved {out_path}")
