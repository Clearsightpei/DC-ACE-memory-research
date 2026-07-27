"""世 (shi) — 5 strokes.
GT posture: thin uniform lines (MMH). 5 strokes:
  1. 横 top horizontal (long, slight down-tilt right-side)
  2. 竖 left vertical (crosses top horizontal, descends past middle)
  3. 竖 middle vertical (crosses top horizontal, descends to bottom row)
  4. 竖 right-inner stub (short vertical above top horizontal near right)
  5. 竖折 right side + bottom close — down right side, across bottom to meet left vertical
Under v8: bank primitives are REFERENCE ONLY; here we hand-render thin lines
directly with PIL to match the thin-uniform MMH GT posture (P12).
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 5  # thin uniform width per MMH GT posture

def line(p0, p1, w=LW):
    d.line([p0, p1], fill=INK, width=w)
    # rounded end caps
    r = w // 2
    for (x, y) in (p0, p1):
        d.ellipse([x - r, y - r, x + r, y + r], fill=INK)

# 1. Top 横 — long horizontal, slight tilt down toward right
line((38, 108), (270, 100))

# 2. Left 竖 — crosses top horizontal, extends toward bottom-left corner
line((72, 70), (68, 250))

# 3. Middle 竖 — crosses top horizontal, extends down inside the enclosure
line((152, 75), (150, 220))

# 4. Right-inner stub — short vertical above top horizontal
line((210, 72), (208, 115))

# 5. 竖折 — down the right side, across the bottom to meet the left vertical
#    (drawn as two connected segments)
line((258, 92), (255, 245))
line((255, 245), (68, 250))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0194_世/01_世.png")
