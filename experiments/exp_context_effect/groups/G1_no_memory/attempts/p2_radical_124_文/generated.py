"""Render 文 (4-stroke radical) to 300x300 PNG.

Structure of 文:
  1. 点 (dot) — small slanted dot at top center
  2. 横 (horizontal) — long horizontal stroke below dot
  3. 撇 (left-falling) — starts above the horizontal, at right-of-center,
     sweeps down-left, CROSSING through the horizontal and continuing
     down to lower-left. Wait — actually in 文, 撇 starts from ON the
     horizontal (center) and sweeps down-left.
  4. 捺 (right-falling) — starts on the horizontal near where 撇 begins,
     sweeps down-right, CROSSING the 撇 to form an X below the 横.
"""
from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def line(p1, p2, width=8):
    draw.line([p1, p2], fill=BLACK, width=width)
    for p in (p1, p2):
        r = width // 2
        draw.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=BLACK)


def stroke(points, width=8):
    for i in range(len(points) - 1):
        line(points[i], points[i + 1], width=width)


# 1. 点 (dot) — small slanted stroke, upper center, slanting down-right
line((148, 55), (162, 78), width=10)

# 2. 横 (horizontal) — long, slightly rising left-to-right
line((60, 118), (240, 112), width=9)

# 3. 撇 (left-falling) — starts on the horizontal at center-right,
#    sweeps down-left with a curve, ending at lower-left
pts_pie = []
for t in [i / 30 for i in range(31)]:
    # start at (160, 118), end at (65, 260)
    x = 160 - 95 * t
    # add subtle S-curve: start steep, then flatten
    y = 118 + 142 * t + 8 * math.sin(math.pi * t)
    pts_pie.append((x, y))
stroke(pts_pie, width=8)

# 4. 捺 (right-falling) — starts on horizontal at center-left area,
#    sweeps down-right crossing 撇 to form X shape below 横
pts_na = []
for t in [i / 30 for i in range(31)]:
    # start at (130, 118), end at (245, 255)
    x = 130 + 115 * t
    y = 118 + 137 * t
    pts_na.append((x, y))
# draw with slight taper: thicker near the end for 捺 aesthetic
for i in range(len(pts_na) - 1):
    w = 8 + int(2 * (i / len(pts_na)))
    line(pts_na[i], pts_na[i + 1], width=w)

out_path = os.path.join(os.path.dirname(__file__), "01_文.png")
img.save(out_path)
print(f"Wrote {out_path}")
