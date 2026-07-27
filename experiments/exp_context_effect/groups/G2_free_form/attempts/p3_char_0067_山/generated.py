"""Render 山 (mountain) to a 300x300 PNG.

Stroke order (3 strokes):
  1) 竖折: left short vertical down, then horizontal bottom across to right.
  2) 竖:   center tall vertical (the tallest of the three).
  3) 竖:   right vertical, medium height, slight rightward tilt at top.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

ink = (0, 0, 0)
w = 8  # brush width

# 1) 竖折 (left vertical + horizontal bottom)
# Left short vertical from (~70, 130) down to (~70, 235)
d.line([(72, 130), (70, 235)], fill=ink, width=w)
# Horizontal bottom from (70,235) across to right side (~235, 232)
d.line([(70, 235), (238, 232)], fill=ink, width=w)

# 2) Center tall vertical: from top (~150, 80) down to bottom (~150, 225)
d.line([(150, 78), (150, 225)], fill=ink, width=w)

# 3) Right vertical: from (~228, 120) down to (~238, 232) — slight outward slope
d.line([(228, 118), (238, 232)], fill=ink, width=w)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0067_山/01_山.png")
