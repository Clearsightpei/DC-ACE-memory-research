"""p3_char_0196_东 — G3 fresh inline render.

5 strokes (simplified 东):
  1. small top stroke (short pie/折-like top)
  2. long horizontal 一
  3. vertical hook 亅 (with left hook)
  4. lower-left 撇 (pie)
  5. lower-right 点 (dot)

Under v8 signature freedom, inlining with PIL for clean 300x300 output.
GT-driven proportions, not bank-derived.
"""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLK = (0, 0, 0)

def line(pts, w=6):
    d.line(pts, fill=BLK, width=w, joint="curve")

def curve(pts, w=6, steps=40):
    # cubic bezier through 4 control points
    (x0, y0), (x1, y1), (x2, y2), (x3, y3) = pts
    prev = (x0, y0)
    for i in range(1, steps + 1):
        t = i / steps
        u = 1 - t
        x = u**3 * x0 + 3 * u**2 * t * x1 + 3 * u * t**2 * x2 + t**3 * x3
        y = u**3 * y0 + 3 * u**2 * t * y1 + 3 * u * t**2 * y2 + t**3 * y3
        d.line([prev, (x, y)], fill=BLK, width=w)
        prev = (x, y)

# 1. small top stroke — short diagonal hook at top-center
#    from ~ (148, 55) down-right ending near (168, 90)
line([(148, 55), (170, 92)], w=6)

# 2. long horizontal 一 — slight upward tilt on right (calligraphic)
line([(55, 138), (245, 130)], w=6)

# 3. vertical hook — vertical shaft through center, small hook to left at bottom
line([(150, 92), (150, 235)], w=7)
# hook (curving left)
curve([(150, 235), (146, 245), (138, 250), (128, 246)], w=6)

# 4. lower-left 撇 (pie) — from just below crossing, going down-left
curve([(130, 165), (115, 200), (95, 235), (65, 262)], w=6)

# 5. lower-right 点 (dot / na-like) — from just below crossing, going down-right
curve([(175, 168), (200, 200), (225, 235), (248, 262)], w=6)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_东.png"))
