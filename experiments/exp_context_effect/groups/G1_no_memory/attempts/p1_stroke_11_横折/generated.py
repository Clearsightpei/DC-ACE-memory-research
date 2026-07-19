"""
G1 (no memory) — p1_stroke_11_横折
Stroke: 横折 (horizontal then 90-degree turn down, like the top of 口)
Renders a 300x300 PNG with white background and black ink.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# 横折: a horizontal line that turns sharply 90 degrees down.
# Place it like the top-left+top+right-side of 口:
#   horizontal from (left, top) to (right, top)
#   then vertical from (right, top) to (right, bottom_of_hook)
#
# Small "顿笔" (pause) thickening at the corner is approximated by
# drawing a slightly thicker line and adding a small square at the joint.

INK = (0, 0, 0)
STROKE_W = 14

# horizontal segment
x1, y1 = 60, 80
x2, y2 = 240, 80
# vertical segment (drops down from the right end)
x3, y3 = 240, 240

# Draw the horizontal
draw.line([(x1, y1), (x2, y2)], fill=INK, width=STROKE_W)
# Draw the vertical
draw.line([(x2, y2), (x3, y3)], fill=INK, width=STROKE_W)

# Reinforce the corner (顿笔) with a small filled square so the 90° turn
# looks crisp rather than rounded.
r = STROKE_W // 2 + 1
draw.rectangle([(x2 - r, y2 - r), (x2 + r, y2 + r)], fill=INK)

# Rounded caps at the two free ends.
def cap(cx, cy, rr):
    draw.ellipse([(cx - rr, cy - rr), (cx + rr, cy + rr)], fill=INK)

cap(x1, y1, STROKE_W // 2)
cap(x3, y3, STROKE_W // 2)

out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p1_stroke_11_横折/01_横折.png"
img.save(out_path)
print(f"Wrote {out_path}")
