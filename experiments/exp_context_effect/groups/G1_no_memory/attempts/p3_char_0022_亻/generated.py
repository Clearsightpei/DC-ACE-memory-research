"""G1 render for p3_char_0022_亻 (radical 'person-standing')."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke(points, width=6):
    d.line(points, fill=BLACK, width=width, joint="curve")

# Stroke 1: 撇 (pie) — starts with a tiny hook/顿笔 at the top, then slants down-left.
# Small entry hook at (175, 65) -> (168, 60) -> (172, 75), then main descent.
pie = [
    (178, 68),
    (170, 62),
    (168, 72),
    (162, 95),
    (150, 125),
    (135, 160),
    (115, 195),
    (95, 225),
    (78, 245),
]
stroke(pie, width=6)

# Stroke 2: 竖 (shu) — vertical, starting from about the middle of the pie's descent,
# extending down past the pie's endpoint.
shu = [
    (152, 130),
    (152, 260),
]
stroke(shu, width=6)

out = os.path.join(os.path.dirname(__file__), "01_亻.png")
img.save(out)
print("wrote", out)
