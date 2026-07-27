"""Render 廾 (character p3_char_0092) to a 300x300 PNG.

Structure (3 strokes):
  1. Left stroke: short vertical/slight-diagonal down that curves out to
     lower-left with a slight hook (like piě-style).
  2. Long horizontal crossing near the upper-middle spanning both verticals.
  3. Right stroke: vertical (slight lean), slightly to right of center.
"""

from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
T = 6  # stroke thickness


def stroke(points, width=T):
    d.line(points, fill=INK, width=width, joint="curve")


# Stroke 1: left descending stroke — starts high-left of center,
# comes down mostly vertical, curves out to the lower-left.
# Roughly from (110, 120) down to about (85, 235) with a curve.
left_stroke = [
    (118, 118),
    (115, 150),
    (110, 185),
    (100, 215),
    (82, 240),
]
stroke(left_stroke)

# Stroke 3: right vertical stroke — nearly straight down,
# from (180, 130) to (185, 245).
right_stroke = [
    (182, 128),
    (183, 165),
    (184, 205),
    (186, 245),
]
stroke(right_stroke)

# Stroke 2: long horizontal crossing near upper-middle,
# from (55, 165) to (245, 160) — slight rise to the right (typical of héng).
horizontal = [
    (55, 168),
    (100, 165),
    (150, 162),
    (200, 160),
    (245, 160),
]
stroke(horizontal)

out_path = os.path.join(os.path.dirname(__file__), "01_廾.png")
img.save(out_path)
print(f"Saved {out_path}")
