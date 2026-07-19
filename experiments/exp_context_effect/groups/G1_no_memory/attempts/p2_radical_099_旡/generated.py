"""G1 render for p2_radical_099_旡 (4 strokes).
Strokes: 1) short 横 at top, 2) longer 横 with tiny left-drop below,
3) 撇 slanting down-left from center, 4) 竖弯钩 on the right.
"""
from PIL import Image, ImageDraw
import math
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
W = 5  # stroke width


def polyline(pts, width=W):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=BLACK, width=width)


def smooth_curve(pts, width=W, steps=40):
    # simple polyline through pts (already densified)
    polyline(pts, width=width)


# Stroke 1: short 横 (top horizontal), slight upward tilt right
polyline([(120, 100), (188, 92)])

# Stroke 2: longer 横 with tiny left-down tick at left end
# Start with a small drop below the line at left end
polyline([(96, 128), (100, 138)])          # small left tail down
polyline([(100, 138), (100, 132), (215, 130)])  # main horizontal (rightward, near-flat)

# Stroke 3: 撇 — from just below the horizontal, curving down-left
pts3 = []
for t in [i/20 for i in range(21)]:
    # cubic-ish curve from (140, 140) to (85, 245)
    x = (1-t)**2 * 140 + 2*(1-t)*t * 125 + t**2 * 85
    y = (1-t)**2 * 140 + 2*(1-t)*t * 200 + t**2 * 245
    pts3.append((x, y))
polyline(pts3)

# Stroke 4: 竖弯钩 — vertical from top-right, arcs right at bottom, small up-hook at end
# Build one continuous polyline
pts4 = []
# vertical portion
pts4.append((175, 140))
pts4.append((175, 200))
# arc bending right (quarter circle center ~ (215, 200), radius 40)
cx, cy, r = 215, 200, 40
for deg in range(180, 271, 5):  # 180 -> 270
    rad = math.radians(deg)
    pts4.append((cx + r * math.cos(rad), cy + r * math.sin(rad)))
# small upward hook at end
end = pts4[-1]
pts4.append((end[0], end[1] - 12))
polyline(pts4)

out = os.path.join(os.path.dirname(__file__), "01_旡.png")
img.save(out)
print(f"wrote {out}")
