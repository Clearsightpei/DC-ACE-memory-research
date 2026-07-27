"""G1 fresh render of 女 (nǚ, woman). 3 strokes."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

W = 6  # ink width

def stroke(points, width=W):
    draw.line(points, fill="black", width=width, joint="curve")

# Stroke 1: 撇点 (piědiǎn) - a curved stroke going down-left then down-right.
# Starts upper-mid-left, sweeps down-left, then hooks down-right to form the base.
s1 = [
    (135, 75),   # start upper
    (130, 100),
    (120, 130),
    (105, 160),
    (95, 185),
    (95, 200),   # bottom of the pie
    (110, 210),  # turn (fold)
    (145, 225),  # dian extending down-right
    (175, 240),
]
stroke(s1)

# Stroke 2: 撇 (piě) - long diagonal from upper-right to lower-left, crossing stroke 1.
s2 = [
    (215, 95),
    (200, 130),
    (180, 165),
    (155, 200),
    (125, 235),
    (95, 260),
    (75, 275),
]
stroke(s2)

# Stroke 3: 横 (héng) - long horizontal across the middle.
s3 = [
    (45, 175),
    (90, 172),
    (150, 170),
    (210, 172),
    (255, 175),
]
stroke(s3)

out_path = os.path.join(os.path.dirname(__file__), "01_女.png")
img.save(out_path)
print(f"Saved: {out_path}")
