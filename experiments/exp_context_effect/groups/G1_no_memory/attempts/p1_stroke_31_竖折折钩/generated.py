"""
G1 no-memory attempt: p1_stroke_31_竖折折钩
Stroke: 竖折折钩 (vertical-turn-turn-hook), as seen in 马 / 写 / 号.

Shape (rough path on a 300x300 canvas, top-left origin, y-down):
  1. Vertical segment going down (竖)
  2. First turn: right along the bottom (横 / 折)
  3. Second turn: back up (竖 / 折)
  4. Hook at the top of that second vertical, flicking up-left (钩)

I render with PIL for deterministic sizing (no turtle window overhead).
"""

from PIL import Image, ImageDraw
import os

SIZE = 300
INK = (0, 0, 0)
BG = (255, 255, 255)
STROKE = 10   # nib width, in px
HALF = STROKE // 2

img = Image.new("RGB", (SIZE, SIZE), BG)
draw = ImageDraw.Draw(img)


def seg(p0, p1, width=STROKE):
    """Draw a black line segment with rounded endcaps by adding disks."""
    draw.line([p0, p1], fill=INK, width=width)
    r = width / 2
    for (x, y) in (p0, p1):
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


# --- Anchor points (chosen to look like the enclosing stroke of 马/号) ---
# We give the shape a rectangular-ish "P without the top" silhouette:
# down the left, across the bottom, back up the right, then hook.

top_left     = ( 95,  70)   # start of the first 竖 (top)
bottom_left  = ( 95, 215)   # bottom of first 竖 / start of 横 (first 折)
bottom_right = (225, 215)   # end of 横 / start of second 竖 (second 折)
top_right    = (225,  95)   # top of second 竖 / base of the 钩
hook_tip     = (190,  75)   # 钩 flicks up-and-left

# 1) 竖 — first vertical, going down
seg(top_left, bottom_left)

# 2) 折 → 横 — turn right along the bottom
seg(bottom_left, bottom_right)

# 3) 折 → 竖 — turn back upward on the right side
seg(bottom_right, top_right)

# 4) 钩 — short hook at the top of the second vertical,
#        flicking toward the upper-left (as in 马/号)
seg(top_right, hook_tip)


out_path = os.path.join(os.path.dirname(__file__), "01_竖折折钩.png")
img.save(out_path, "PNG")
print(f"wrote {out_path} ({img.size[0]}x{img.size[1]})")
