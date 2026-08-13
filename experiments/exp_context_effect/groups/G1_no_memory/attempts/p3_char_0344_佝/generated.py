"""G1 render for 佝 (gou1) — 亻 + 句."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 5


def stroke(points, width=LW):
    d.line(points, fill=INK, width=width, joint="curve")
    r = width / 2
    for x, y in (points[0], points[-1]):
        d.ellipse((x - r, y - r, x + r, y + r), fill=INK)


# ----- Left: 亻 (person radical) -----
# Piě starting up-right, ending down-left, touching the vertical
stroke([(105, 80), (75, 135)])
# Long vertical shū (slight slant)
stroke([(88, 130), (82, 250)])

# ----- Right: 句 -----
# Top piě of 勹
stroke([(165, 85), (150, 120)])

# 勹 wrap: horizontal top, curve down right side, hook at bottom-left
wrap = [
    (150, 118),
    (240, 118),
    (240, 200),
    (225, 225),
    (210, 232),
]
stroke(wrap)

# ----- 口 inside the wrap -----
# Left vertical
stroke([(170, 155), (170, 220)])
# Top + right vertical (gong shape)
stroke([(170, 155), (222, 155), (222, 220)])
# Bottom horizontal closing 口
stroke([(170, 220), (222, 220)])

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_佝.png"))
print("wrote", os.path.join(out_dir, "01_佝.png"))
