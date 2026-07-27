"""Render 为 (wei) as 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5

def curve(points, width=LW):
    # Draw a polyline as a smooth curve (line segments between many pts)
    d.line(points, fill=BLACK, width=width, joint="curve")

# Stroke 1: top-left short slanted stroke (short pie)
curve([(115, 80), (128, 110), (140, 130)], width=LW)

# Stroke 2: top-right short dot/tick
curve([(190, 60), (200, 78), (192, 95)], width=LW)

# Stroke 3: long horizontal curved stroke (横 across middle), slight arc
curve([(60, 158), (100, 150), (150, 148), (200, 150), (230, 156)], width=LW)

# Stroke 4: interior small dot (inside, below horizontal on right side)
curve([(150, 195), (163, 208), (175, 213)], width=LW)

# Stroke 5: right vertical curve with hook at bottom (横折弯钩 right side)
right_curve = [
    (225, 152), (232, 180), (235, 210), (228, 235), (212, 253), (192, 260), (180, 253)
]
curve(right_curve, width=LW)

# Stroke 6: long sweeping left pie from top-mid down to bottom-left
pie = [
    (155, 130), (138, 165), (115, 205), (88, 240), (65, 268), (50, 280)
]
curve(pie, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_为.png")
img.save(out)
print("wrote", out)
