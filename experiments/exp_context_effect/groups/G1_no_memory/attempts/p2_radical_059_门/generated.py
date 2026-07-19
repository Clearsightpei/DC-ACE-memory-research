"""Render 门 (radical, 3 strokes) at 300x300 using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
T = 6  # stroke thickness


def stroke(points, width=T):
    d.line(points, fill=INK, width=width, joint="curve")
    for (x, y) in points:
        d.ellipse((x - width / 2, y - width / 2, x + width / 2, y + width / 2), fill=INK)


# Stroke 1: 点 — short diagonal dot in upper-left, tilted from upper-left to lower-right
# Slightly thicker to read as a dot
stroke([(78, 78), (108, 100)], width=8)

# Stroke 2: 竖 (left vertical) — starts just below the dot, extends down almost to bottom
stroke([(72, 115), (72, 258)], width=T)

# Stroke 3: 横折钩 — top horizontal starts to the right of the dot, extends across,
# turns 90° down the right side, ends with a small hook back to the left at bottom.
stroke([
    (118, 92),   # top-left of frame (right of the dot)
    (220, 88),   # top-right corner (slight upward tilt as in GT)
    (222, 100),  # small turn
    (222, 258),  # right vertical down
    (200, 268),  # hook left at the bottom
], width=T)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_门.png")
img.save(out_path)
print(f"wrote {out_path}")
