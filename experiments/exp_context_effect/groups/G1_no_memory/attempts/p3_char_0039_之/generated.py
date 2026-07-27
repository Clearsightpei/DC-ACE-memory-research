"""Render 之 (zhi) to 300x300 PNG using PIL.

之 has 3 strokes:
 1. Top dot (点) — short slanting stroke top-center.
 2. Horizontal-with-hook (横撇) — starts left-mid, goes right, hooks down-left.
 3. Bottom horizontal-pie-na (平捺) — sweeping stroke from left, curving down and out to the right.
"""

from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def line(p0, p1, width=6):
    draw.line([p0, p1], fill="black", width=width)

def polyline(pts, width=6):
    draw.line(pts, fill="black", width=width, joint="curve")

# Stroke 1: top dot (short slanted stroke) - upper area, slanting down-right (like a small curve)
polyline([(135, 60), (155, 65), (175, 85)], width=6)

# Stroke 2: 横撇 (clear horizontal top with a distinct downward-left hook)
# Horizontal part first, then sharp turn down-left as a pie
polyline([
    (75, 135),
    (100, 128),
    (170, 122),
    (195, 128),
], width=7)
# Pie portion (down-left slanting)
polyline([
    (190, 128),
    (160, 160),
    (120, 200),
    (85, 225),
], width=7)

# Stroke 3: 平捺 (long sweeping horizontal-na), starts left under stroke 2,
# dips down and sweeps out to the right with a long flat tail
polyline([
    (55, 225),
    (80, 240),
    (130, 255),
    (185, 268),
    (230, 260),
    (270, 248),
], width=8)

out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_之.png")
img.save(out_path)
print(f"Wrote {out_path}")
