"""G1 no-memory attempt: p1_stroke_16_斜钩 (xie gou).

斜钩: a diagonal stroke from upper-left to lower-right that ends with
a short hook flicking up (as in 我, 成). Rendered with PIL onto a
300x300 white canvas in black ink.
"""

from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# Main diagonal body: from upper-left area down to lower-right.
# Start slightly thin, thicken toward the middle, then taper before the hook.
# Approximate the tapered slash with a series of line segments of
# varying thickness along the diagonal.

# Anchor points for the main body (upper-left to lower-right, slightly curved).
# A 斜钩 has a gentle bow — bulges slightly toward lower-left.
# We interpolate control points along a quadratic bezier.
def bezier(p0, p1, p2, t):
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
    return (x, y)

p0 = (85, 55)     # top-left start
p1 = (130, 175)   # control point — biases the curve to bulge lower-left
p2 = (235, 240)   # bottom-right end (just before the hook)

# Draw the body as many short segments with variable width to give
# a brush-like taper: thin at start, thickest in middle, thin at end.
N = 120
prev = None
for i in range(N + 1):
    t = i / N
    pt = bezier(p0, p1, p2, t)
    # thickness: 3 at ends, ~10 at midbody
    w = 3 + 7 * (1 - abs(2 * t - 1))
    if prev is not None:
        draw.line([prev, pt], fill="black", width=int(round(w)))
    prev = pt

# Small round cap at the start for a 顿笔 (initial press).
draw.ellipse([p0[0] - 5, p0[1] - 5, p0[0] + 5, p0[1] + 5], fill="black")

# The hook (钩): from the end of the body, flick upward and slightly left.
# Short, sharp, curving up.
hook_start = p2
hook_ctrl = (238, 218)
hook_end = (225, 200)

Nh = 40
prev = None
for i in range(Nh + 1):
    t = i / Nh
    pt = bezier(hook_start, hook_ctrl, hook_end, t)
    # hook tapers to a point
    w = 8 - 6 * t
    if prev is not None:
        draw.line([prev, pt], fill="black", width=max(1, int(round(w))))
    prev = pt

out = os.path.join(os.path.dirname(__file__), "01_斜钩.png")
img.save(out)
print(out)
