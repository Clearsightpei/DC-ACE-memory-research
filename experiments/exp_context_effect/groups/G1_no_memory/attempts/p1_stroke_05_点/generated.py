"""G1 no-memory attempt: 点 (dot) — short diagonal dot, upper-left to lower-right."""
from PIL import Image, ImageDraw

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

# 点画: a short diagonal teardrop-like dot going from upper-left to lower-right.
# Roughly centered in the 米字格. We draw a tapered diagonal shape by stacking
# short line segments with increasing width — thin at the top-left, thicker at
# the bottom-right (typical brush 点).
x0, y0 = 140, 120   # upper-left start
x1, y1 = 175, 170   # lower-right end
steps = 40
for i in range(steps):
    t0 = i / steps
    t1 = (i + 1) / steps
    xa = x0 + (x1 - x0) * t0
    ya = y0 + (y1 - y0) * t0
    xb = x0 + (x1 - x0) * t1
    yb = y0 + (y1 - y0) * t1
    # width grows from ~3 at the top to ~14 near the bottom, then tapers
    # slightly at the very end for the 顿笔 tail.
    if t1 < 0.85:
        w = 3 + int(11 * t1)
    else:
        w = 3 + int(11 * 0.85) - int((t1 - 0.85) * 20)
    draw.line([(xa, ya), (xb, yb)], fill="black", width=max(1, w))

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p1_stroke_05_点/01_点.png"
img.save(out)
print(out)
