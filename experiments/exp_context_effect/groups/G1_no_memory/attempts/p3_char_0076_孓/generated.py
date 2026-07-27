"""Render 孓 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 6

# Stroke 1: top horizontal-with-hook (横撇/横折) - like top of 了
# from left-upper area sweeping right, then hooking down-left
s1 = [
    (70, 90),
    (110, 80),
    (160, 78),
    (200, 82),
    (215, 95),
    (200, 110),
    (185, 118),
]
d.line(s1, fill=INK, width=LW, joint="curve")

# Stroke 2: long vertical/curved stroke with hook at bottom (弯钩)
# starts near where stroke 1 ended, curves down and slightly left, ends with small hook
s2 = [
    (175, 115),
    (170, 150),
    (162, 190),
    (150, 230),
    (135, 258),
    (115, 268),
    (100, 262),
]
d.line(s2, fill=INK, width=LW, joint="curve")

# Stroke 3: horizontal stroke crossing near middle (提 or 横)
# from lower-left rising to right
s3 = [
    (55, 210),
    (110, 205),
    (170, 200),
    (225, 195),
    (255, 190),
]
d.line(s3, fill=INK, width=LW, joint="curve")

out = os.path.join(os.path.dirname(__file__), "01_孓.png")
img.save(out)
print(out)
