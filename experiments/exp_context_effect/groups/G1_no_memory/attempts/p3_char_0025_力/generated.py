"""Render 力 (power) — 2 strokes: 横折钩 + 撇."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
TH = 5  # stroke thickness


def stroke(points, width=TH):
    """Draw a smooth polyline plus round joins."""
    d.line(points, fill=BLACK, width=width, joint="curve")
    r = width / 2
    for x, y in points:
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


# Stroke 1: 横折钩 (heng-zhe-gou)
# Short horizontal at top, sharp corner, long curving down-right vertical,
# ending with a small hook flicking up-left near the bottom.
s1 = [
    (95, 118),   # start of horizontal (extended left, slight down-slope)
    (130, 112),
    (170, 105),
    (200, 100),  # end of horizontal / top of corner
    (210, 108),  # corner
    (218, 130),
    (222, 160),
    (218, 195),
    (208, 225),
    (192, 250),  # bottom of vertical curve
    (175, 262),  # hook tip
    (160, 256),  # hook flick up-left
]
stroke(s1)

# Stroke 2: 撇 (pie) — long diagonal starting from the top of the fold corner
# curving down-left to lower-left tail.
s2 = [
    (185, 75),    # top (near horizontal's right end, slightly above)
    (170, 110),
    (150, 150),
    (125, 190),
    (100, 230),
    (72, 265),    # bottom-left tail
]
stroke(s2)

out = os.path.join(os.path.dirname(__file__), "01_力.png")
img.save(out)
print("saved", out)
