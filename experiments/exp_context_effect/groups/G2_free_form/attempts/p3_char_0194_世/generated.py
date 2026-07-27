"""
世 (shì) — 5 strokes.
Layout observed from GT:
  1. Long top horizontal at ~mid-upper height, spanning most of canvas.
  2. Left vertical: from top, crosses the horizontal, drops to bottom-left.
  3. Middle vertical: from top down to (or just past) the horizontal.
  4. Right vertical: from top down to (or just past) the horizontal.
  5. 竖折 / bottom U: horizontal at bottom + right-side vertical kicking up,
     joining bottom-right to horizontal line.
Silhouette: wide, blocky, comb-like top with a shallow bowl at bottom.
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
w = 8  # stroke width

# Coordinates (top-left origin, y grows down)
top_y = 70          # top of the three short verticals
mid_y = 145         # the long horizontal
bot_y = 235         # bottom horizontal
left_x = 55
mid_x = 145
right_x = 235

# 1. Top long horizontal
d.line([(40, mid_y), (265, mid_y)], fill=INK, width=w)

# 2. Left vertical: extends from top through horizontal to bottom-left area
d.line([(left_x, top_y), (left_x, bot_y)], fill=INK, width=w)

# 3. Middle vertical: from top down to horizontal (stops there — key detail)
d.line([(mid_x, top_y - 10), (mid_x, mid_y + 8)], fill=INK, width=w)

# 4. Right vertical: from top down to horizontal
d.line([(right_x, top_y + 5), (right_x, mid_y + 6)], fill=INK, width=w)

# 5. 竖折: bottom horizontal + right-side small up-kick at the end
#    Runs from bottom-left across, with slight up-hook on the far right.
d.line([(left_x, bot_y), (right_x + 20, bot_y)], fill=INK, width=w)
d.line([(right_x + 20, bot_y), (right_x + 20, bot_y - 22)], fill=INK, width=w)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0194_世/01_世.png"
)
print("saved")
