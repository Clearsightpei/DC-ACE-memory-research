"""G1 render of 一 (horizontal stroke character)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# 一 is a single horizontal stroke (heng).
# Referencing GT: stroke is in lower-middle area, slightly wavy/tapered ends.
# Left endpoint slightly lower, right endpoint has a small "dun" (press) hook down.

# Main body: a horizontal stroke with slight curvature and tapered ends.
# We'll draw it as a filled polygon approximating brush shape.

# Anchor points along the stroke (x, y) - y grows down in PIL
# Stroke center-line: from ~x=60 to ~x=240, at y ~ 190
left_x, right_x = 55, 245
y_center = 190

# Slightly bow upward in middle (concave from below), like a shallow arc
# Also the right end dips slightly (dun bi ending)
def stroke_y(x):
    t = (x - left_x) / (right_x - left_x)
    # gentle arch: middle slightly higher (smaller y)
    arc = -3 * (1 - (2*t - 1)**2)  # up to -3 pixels at middle
    # right end has a small downward dun
    dun = 0
    if t > 0.9:
        dun = 6 * ((t - 0.9) / 0.1)
    return y_center + arc + dun

# Draw thick tapered brush stroke by stacking ellipses along path
n_steps = 200
prev = None
for i in range(n_steps + 1):
    t = i / n_steps
    x = left_x + t * (right_x - left_x)
    y = stroke_y(x)
    # Thickness: taper at very ends, thicker at right end (dun bi)
    if t < 0.06:
        # left entry (qi bi) - starts thin, quickly thickens
        thick = 4 + 6 * (t / 0.06)
    elif t > 0.92:
        # right end - press then lift (dun bi) - thicker bulge
        u = (t - 0.92) / 0.08
        thick = 10 + 4 * (1 - abs(2*u - 1))
    else:
        thick = 10
    r = thick / 2
    draw.ellipse([x - r, y - r, x + r, y + r], fill="black")

out_path = os.path.join(os.path.dirname(__file__), "01_一.png")
img.save(out_path)
print("Wrote", out_path)
