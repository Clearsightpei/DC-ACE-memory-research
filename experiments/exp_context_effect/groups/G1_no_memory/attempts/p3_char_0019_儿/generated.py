"""G1 render of 儿 (ér) — 2 strokes: 撇 (left slanting) + 竖弯钩 (vertical-bend-hook).

Revised vs clean GT: shift both stroke tops rightward and downward slightly to
match GT positioning; tops of the two strokes are at similar y; pie starts
around x=100, swg starts around x=185.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
STROKE = 8


def curve(points, width=STROKE):
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill=INK, width=width)
    for p in points:
        draw.ellipse([p[0] - width // 2, p[1] - width // 2,
                      p[0] + width // 2, p[1] + width // 2], fill=INK)


# Stroke 1: 撇 (pie) — starts upper-left, slight rightward top,
# then curves down and to the lower-left corner area.
pie_pts = [
    (108, 88),
    (105, 118),
    (98, 150),
    (88, 185),
    (74, 220),
    (60, 250),
    (48, 270),
]
curve(pie_pts, width=9)

# Stroke 2: 竖弯钩 (shu-wan-gou) — starts upper-right, drops straight down,
# curves right along the bottom, then a small upward hook.
swg_pts = [
    (188, 88),
    (188, 125),
    (188, 160),
    (190, 195),
    (196, 225),
    (210, 250),
    (232, 262),
    (252, 262),
    (258, 250),  # hook up
    (256, 235),
]
curve(swg_pts, width=9)

out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_儿.png")
img.save(out_path)
print(f"Wrote {out_path}")
