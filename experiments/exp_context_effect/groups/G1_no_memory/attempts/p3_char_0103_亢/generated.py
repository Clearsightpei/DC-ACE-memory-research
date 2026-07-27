"""Render 亢 (kang) — 4 strokes: dot, horizontal, left curve, right vertical-hook."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6

# Stroke 1: 点 (dot / short stroke) — small tick top-center-left area
# In 亢 the top dot is a short diagonal stroke going down-right
d.line([(140, 55), (165, 80)], fill=BLACK, width=LW)

# Stroke 2: 横 (horizontal) — long horizontal, slightly rising
d.line([(55, 110), (250, 105)], fill=BLACK, width=LW+1)

# Stroke 3: 撇 (left downward curve) — starts inside top, curves down-left
# Approximated by connected line segments forming a curve
curve_left = [
    (115, 120),
    (110, 145),
    (100, 175),
    (85, 205),
    (70, 235),
    (55, 260),
]
d.line(curve_left, fill=BLACK, width=LW, joint="curve")

# Stroke 4: 竖弯钩 (vertical-bend-hook) — from top-right area, goes down, curves and hooks
# In 亢 the right stroke is a vertical with a small hook at bottom (横折弯钩 style)
# Starts high near horizontal, goes down, ends with small upward hook
right_stroke = [
    (200, 120),
    (200, 200),
    (200, 240),
    (205, 258),
    (220, 262),
    (235, 258),
]
d.line(right_stroke, fill=BLACK, width=LW, joint="curve")

out_path = os.path.join(os.path.dirname(__file__), "01_亢.png")
img.save(out_path)
print(f"Saved: {out_path}")
