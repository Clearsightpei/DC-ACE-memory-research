"""
佣 = 亻 (left) + 用 (right)
- 亻: 撇 from upper-left going down-left, then 竖 (vertical) below the pivot
- 用: rectangular box with a hooked left-vertical extending below,
      internal horizontal bars (two), and vertical median stroke.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p0, p1, w=6):
    d.line([p0, p1], fill="black", width=w)

def bez(pts, w=6, steps=40):
    # simple polyline for a quadratic bezier
    (x0, y0), (x1, y1), (x2, y2) = pts
    prev = (x0, y0)
    for i in range(1, steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t ** 2 * x2
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t ** 2 * y2
        d.line([prev, (x, y)], fill="black", width=w)
        prev = (x, y)

# --- 亻 (left radical) ---
# 撇: from around (90, 70) sweeping down-left to (55, 175)
bez([(95, 65), (80, 130), (55, 175)], w=6)
# 竖: vertical stroke starting from pivot on 撇 (~85,115) down to (85, 250)
line((88, 115), (88, 255), w=6)

# --- 用 (right) ---
# top horizontal (short down-left slant at right into the vertical hook)
# frame:
# top horizontal from (140, 75) to (250, 68) slight rising
line((140, 78), (252, 72), w=6)

# left vertical of 用 (short - only inside 用 box): (140, 78) down to (145, 260)
# Actually 用 has: outer frame open at bottom-left? No, closed.
# Left vertical starts at top-left corner going straight down, then a slight bottom
line((142, 78), (150, 260), w=6)

# right vertical + hook at bottom (this is the 横折钩 style):
# 竖 going down from top-right (252, 72) to (245, 250), then hook up-left
line((252, 72), (247, 250), w=6)
# hook flick UP-and-LEFT
line((247, 250), (230, 235), w=6)

# Middle vertical (starts INSIDE at top horizontal, extends below the box)
line((195, 78), (195, 268), w=6)

# Two internal horizontals
line((150, 135), (250, 133), w=6)
line((150, 195), (247, 193), w=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0350_佣/01_佣.png")
