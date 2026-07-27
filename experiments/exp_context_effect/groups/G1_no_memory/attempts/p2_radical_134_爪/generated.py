"""Render 爪 (claw radical, 4 strokes) at 300x300."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke(points, width=6):
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill=BLACK, width=width)
    r = width // 2
    for x, y in points:
        draw.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)

# Stroke 1: short 撇 top-left tick
s1 = [(140, 110), (132, 122), (127, 135)]
stroke(s1, width=6)

# Stroke 2: horizontal top stroke going right with slight downward slope, small hook end
s2 = [(148, 105), (175, 100), (200, 103), (205, 112)]
stroke(s2, width=6)

# Stroke 3: middle short vertical/撇 going down from top-center
s3 = [(158, 122), (156, 150), (155, 180)]
stroke(s3, width=6)

# Stroke 4: long left 撇 — curves outward (leftward bow) then down to bottom-left
s4 = [(128, 140), (118, 165), (108, 195), (100, 225), (95, 255), (92, 275)]
stroke(s4, width=6)

# Stroke 5: long 捺 — from mid-upper area sweeping down-right to bottom-right
s5 = [(160, 145), (185, 175), (215, 205), (245, 235), (265, 258)]
stroke(s5, width=6)

out = os.path.join(os.path.dirname(__file__), "01_爪.png")
img.save(out)
print(f"Saved: {out}")
