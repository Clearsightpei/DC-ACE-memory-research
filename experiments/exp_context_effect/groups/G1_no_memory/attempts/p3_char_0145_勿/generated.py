"""Render 勿 as 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5

def stroke(pts, width=LW):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=BLACK, width=width)
    for p in pts:
        d.ellipse((p[0] - width / 2, p[1] - width / 2,
                   p[0] + width / 2, p[1] + width / 2), fill=BLACK)

def smooth_curve(ctrl, steps=40, width=LW):
    """Quadratic bezier through 3 control points."""
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * ctrl[0][0] + 2 * (1 - t) * t * ctrl[1][0] + t ** 2 * ctrl[2][0]
        y = (1 - t) ** 2 * ctrl[0][1] + 2 * (1 - t) * t * ctrl[1][1] + t ** 2 * ctrl[2][1]
        pts.append((x, y))
    stroke(pts, width)

# Stroke 1: short 撇 at top-center (short diagonal from upper-right to lower-left)
smooth_curve([(140, 55), (133, 68), (122, 82)])

# Stroke 2: 横折钩 — horizontal top, turn down and curve down-left with a hook at bottom
# Top horizontal
d.line([(70, 100), (215, 95)], fill=BLACK, width=LW)
# Turn (fold) - small vertical
d.line([(215, 95), (220, 105)], fill=BLACK, width=LW)
# Long down-left curved sweep to bottom-left forming the hook
smooth_curve([(220, 105), (215, 200), (165, 265)])
# Hook - short flick back up-left at the bottom
smooth_curve([(165, 265), (152, 260), (140, 250)])

# Stroke 3: middle 撇 — from just under top-horizontal, diagonally down-left long sweep
smooth_curve([(135, 115), (105, 175), (65, 235)])

# Stroke 4: right 撇 — from upper-right area, diagonally down-left
smooth_curve([(180, 120), (145, 185), (105, 245)])

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_勿.png")
img.save(out_path)
print(f"Saved: {out_path}")
