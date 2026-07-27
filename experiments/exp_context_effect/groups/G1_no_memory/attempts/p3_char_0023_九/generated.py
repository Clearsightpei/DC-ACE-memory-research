"""Render 九 (jiǔ, 'nine') as a 300x300 PNG using PIL.

Two strokes:
  1. 撇 (piě) — long left-falling stroke starting upper-middle,
     sweeping down and to the lower-left.
  2. 横折弯钩 (héng zhé wān gōu) — short horizontal, bend down,
     big belly curving to the right, ending in an upward hook.
"""

from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def stroke(points, width=6):
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill="black", width=width)
    for p in points:
        r = width / 2
        draw.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill="black")


def cubic(p0, p1, p2, p3, steps=80):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t ** 2
        b3 = t ** 3
        x = b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0]
        y = b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1]
        pts.append((x, y))
    return pts


def quad(p0, p1, p2, steps=50):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


# --- Stroke 1: 撇 (piě) ---
# Long left-falling stroke: starts around upper-mid, sweeps down-left
s1 = cubic((145, 85), (120, 150), (85, 215), (55, 275), steps=80)
stroke(s1, width=6)

# --- Stroke 2: 横折弯钩 ---
# Short horizontal top, crossing stroke1 around y=130
h1 = quad((108, 135), (150, 130), (190, 128), steps=40)
stroke(h1, width=6)

# Main belly: from top-right of horizontal, curve down and around to bottom
belly = cubic((190, 128), (225, 180), (225, 245), (180, 265), steps=100)
stroke(belly, width=6)

# Bottom sweep and up-hook (curling toward upper-right)
sweep = cubic((180, 265), (215, 270), (240, 258), (238, 220), steps=60)
stroke(sweep, width=6)

out_path = os.path.join(os.path.dirname(__file__), "01_九.png")
img.save(out_path)
print(f"Saved {out_path}")
