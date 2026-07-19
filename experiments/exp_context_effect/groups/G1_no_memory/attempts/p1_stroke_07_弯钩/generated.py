"""G1 no-memory attempt: 弯钩 (curved stroke with hook at end).

弯钩 = a smoothly curving stroke that starts near top, bends to the
right and then curves back left/down, ending with a small upward hook.
Rendered with PIL to a 300x300 white canvas, black ink.
"""
from PIL import Image, ImageDraw
import os
import math

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

# Build the 弯钩 body as a series of points along a curve.
# Start near top-center, curve gently to the right then sweep down-left,
# ending near lower-left. This traces the classic 弯钩 arc.
points = []
# Parameterize with t in [0, 1]
steps = 60
start = (170, 55)   # top
end = (110, 235)    # bottom before hook
# Control-ish sweep: bulge to the right around t~0.4
for i in range(steps + 1):
    t = i / steps
    # Quadratic Bezier through a control point on the right
    cx, cy = 235, 150
    x = (1 - t) ** 2 * start[0] + 2 * (1 - t) * t * cx + t ** 2 * end[0]
    y = (1 - t) ** 2 * start[1] + 2 * (1 - t) * t * cy + t ** 2 * end[1]
    points.append((x, y))

# Draw the curved body with a tapered feel by stroking multiple widths.
# Simple approach: single thick line.
for i in range(len(points) - 1):
    # Slight taper: thicker in the middle, thinner near the top
    t = i / (len(points) - 1)
    width = int(10 + 6 * math.sin(math.pi * t))
    draw.line([points[i], points[i + 1]], fill="black", width=width)

# End cap circle to smooth the joint before the hook
draw.ellipse([end[0] - 7, end[1] - 7, end[0] + 7, end[1] + 7], fill="black")

# The hook: a short upward flick going up-and-slightly-left from end point.
hook_end = (75, 200)
# Draw a curved hook via a mini bezier
hook_points = []
h_steps = 20
h_ctrl = (85, 230)
for i in range(h_steps + 1):
    t = i / h_steps
    x = (1 - t) ** 2 * end[0] + 2 * (1 - t) * t * h_ctrl[0] + t ** 2 * hook_end[0]
    y = (1 - t) ** 2 * end[1] + 2 * (1 - t) * t * h_ctrl[1] + t ** 2 * hook_end[1]
    hook_points.append((x, y))
for i in range(len(hook_points) - 1):
    t = i / (len(hook_points) - 1)
    width = max(3, int(11 - 6 * t))  # taper to a point
    draw.line([hook_points[i], hook_points[i + 1]], fill="black", width=width)

# Ensure 300x300 and save
assert img.size == (300, 300)
out_path = os.path.join(os.path.dirname(__file__), "01_弯钩.png")
img.save(out_path)
print(out_path)
