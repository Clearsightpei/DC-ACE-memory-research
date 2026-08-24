"""屮 (chè) — 3-stroke character.
Strokes (per GT):
  1) 竖折 (left): short vertical down then a horizontal that meets the center.
     In this GT it reads as: a short descending stroke on the left, then
     turning to a horizontal that runs to the central shaft.
  2) 竖 (center): full-height vertical shaft, extends above and below the crossbar.
  3) 竖 (right): short vertical, its top starts higher, dropping down to meet the horizontal.

Rendered with PIL as thin uniform black strokes on white 300x300, matching
MMH GT style (P12 in principles_stroke_family: thin uniform widths ~4px).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5  # thin uniform line width (MMH-GT style)

# Center vertical shaft — spans most of the canvas height.
cx = 150
top_y = 60
bot_y = 275
d.line([(cx, top_y), (cx, bot_y)], fill=INK, width=LW)

# Horizontal crossbar (part of the two side strokes meeting shaft).
# In 屮 the two side elements each turn into a horizontal that reaches the shaft.
# We treat it as: left 竖折 (down then right to shaft) and right stroke that
# comes down from top-right then a short horizontal to shaft (also a 竖折 mirror).
bar_y = 175

# Left stroke: 竖折 — starts high-left, comes down, turns right into the shaft.
left_top = (100, 130)
left_corner = (100, bar_y)
left_end = (cx, bar_y)
d.line([left_top, left_corner], fill=INK, width=LW)
d.line([left_corner, left_end], fill=INK, width=LW)

# Right stroke: mirror 竖折 — starts high-right, comes down, turns left into shaft.
right_top = (200, 110)
right_corner = (200, bar_y)
right_end = (cx, bar_y)
d.line([right_top, right_corner], fill=INK, width=LW)
d.line([right_corner, right_end], fill=INK, width=LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0084_屮/01_屮.png")
