"""囗 (wei/enclosure radical) — a simple 3-stroke box.

Structure per form_catalog:
  1. 竖 as left-wall: top-left → bottom-left, uniform width, no hook
  2. 横折 as top+right: 横 across top, shoulder dab at top-right,
     竖 down along right wall (same length as left wall)
  3. 横 as bottom: spans left-wall to right-wall exactly

Aspect: slightly taller than wide (GT reads square-ish with a small
vertical bias). All corners touch — no gaps at top-left or bottom.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

# Box bounds — slightly taller than wide, centered
LEFT, RIGHT = 70, 225
TOP, BOTTOM = 55, 245

INK = (20, 20, 20)
STROKE_W = 10

def brush_line(p0, p1, w=STROKE_W):
    d.line([p0, p1], fill=INK, width=w)
    # round the endpoints to avoid corner gaps
    r = w // 2
    for (x, y) in (p0, p1):
        d.ellipse([x - r, y - r, x + r, y + r], fill=INK)

# 1. 竖 (left wall): top-left → bottom-left
brush_line((LEFT, TOP), (LEFT, BOTTOM))

# 2. 横折 (top + right wall):
#    横 across the top: top-left → top-right (slight shoulder dab)
brush_line((LEFT, TOP), (RIGHT, TOP))
#    small shoulder emphasis at top-right corner
d.ellipse([RIGHT - 7, TOP - 7, RIGHT + 7, TOP + 7], fill=INK)
#    竖 down along right wall
brush_line((RIGHT, TOP), (RIGHT, BOTTOM))

# 3. 横 (bottom): closes the box, wall-to-wall
brush_line((LEFT, BOTTOM), (RIGHT, BOTTOM))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0066_囗/01_囗.png")
