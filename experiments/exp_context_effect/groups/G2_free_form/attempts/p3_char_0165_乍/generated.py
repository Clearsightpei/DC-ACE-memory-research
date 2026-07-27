"""
乍 — 5 strokes:
  1. 撇 (pie) — upper-left diagonal flick
  2. 横 (heng) — short horizontal, top of right structure
  3. 竖 (shu) — long vertical going down through the character
  4. 横 (heng) — middle horizontal
  5. 横 (heng) — bottom horizontal

Layout: 撇 sweeps from upper-mid-right area down to lower-left.
The right/main body has a short top-横, a long 竖 going down,
and two more 横 crossing that 竖 (middle and bottom).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6  # line width


def line(x1, y1, x2, y2, w=LW):
    d.line([(x1, y1), (x2, y2)], fill=BLACK, width=w)


def bezier(pts, w=LW, steps=60):
    # simple quadratic bezier through 3 pts
    (x0, y0), (x1, y1), (x2, y2) = pts
    prev = (x0, y0)
    for i in range(1, steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * x0 + 2 * u * t * x1 + t * t * x2
        y = u * u * y0 + 2 * u * t * y1 + t * t * y2
        d.line([prev, (x, y)], fill=BLACK, width=w)
        prev = (x, y)


# Stroke 1: 撇 — starts high-right, gentle curve down-left
# Slight curve (control point pulled slightly right of straight line)
bezier([(165, 45), (120, 130), (55, 240)], w=LW)

# Stroke 2: 横 — short top horizontal, at the top of the vertical
# In 乍 this heng is short and sits at the very top of the right side
line(135, 78, 210, 74, w=LW)

# Stroke 3: 竖 — long vertical from top-横 going straight down
line(148, 78, 148, 278, w=LW)

# Stroke 4: 横 — middle horizontal (crosses vertical, extending well to the right)
line(138, 165, 235, 163, w=LW)

# Stroke 5: 横 — bottom horizontal (base of the right structure)
line(138, 235, 232, 233, w=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0165_乍/01_乍.png")
