"""
G1 no-memory attempt: p1_stroke_03_撇
撇 = downward-left sweep, tapered at the bottom-left tail.
Start near upper-right, curve toward lower-left, thickness tapers from
thick (top) to thin (bottom-left tail).
Renders a 300x300 white PNG with black ink using PIL.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# Control points for the pie sweep: start upper-right, end lower-left.
# We approximate a tapered brush by drawing many overlapping circles along
# a quadratic Bezier curve, with radius shrinking from thick -> thin.
p0 = (215, 70)    # start (upper right), thick
p1 = (150, 170)   # control point (mid curve, bends outward-left)
p2 = (70, 250)    # end (lower left tail), thin

STEPS = 220
r_start = 11.0
r_end = 0.8

def bezier(t, a, b, c):
    x = (1 - t) ** 2 * a[0] + 2 * (1 - t) * t * b[0] + t * t * c[0]
    y = (1 - t) ** 2 * a[1] + 2 * (1 - t) * t * b[1] + t * t * c[1]
    return x, y

for i in range(STEPS + 1):
    t = i / STEPS
    x, y = bezier(t, p0, p1, p2)
    # Ease radius: hold near-thick briefly, then taper sharply toward the tail.
    r = r_start * (1 - t) ** 1.3 + r_end * t
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p1_stroke_03_撇/01_撇.png"
img.save(out)
print(out)
