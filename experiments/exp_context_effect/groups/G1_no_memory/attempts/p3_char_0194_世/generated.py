"""Render 世 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6

# 世 — 5 strokes:
# Layout: three vertical stubs sticking up above a long horizontal bar,
# then a 竖折 (down-then-right) forming the bottom pocket, plus a
# leftmost vertical that runs from top to bottom crossing everything.

# 1. Left vertical — long, from above horizontal down to bottom
d.line([(72, 90), (78, 245)], fill=BLACK, width=LW)

# 2. Middle short vertical — from top down to just past the horizontal
d.line([(140, 82), (140, 195)], fill=BLACK, width=LW)

# 3. Right vertical — slightly slanted, from top down to bottom pocket
d.line([(215, 78), (225, 205)], fill=BLACK, width=LW)

# 4. Long horizontal bar (中间的长横)
d.line([(40, 132), (270, 122)], fill=BLACK, width=LW)

# 5. Bottom stroke: horizontal from left-bottom rightward, then a short hook up
d.line([(78, 245), (255, 250)], fill=BLACK, width=LW)
d.line([(255, 250), (252, 200)], fill=BLACK, width=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0194_世/01_世.png")
