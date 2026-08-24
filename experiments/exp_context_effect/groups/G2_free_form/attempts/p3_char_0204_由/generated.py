"""Render 由 (p3_char_0204).

由 = 5 strokes: 竖(central, protrudes above) + 竖(left side of box) +
横折(top+right of box) + 横(middle) + 横(bottom close).

Silhouette: tall narrow box, central vertical extends above box.
Aspect: roughly square box, moderate width; canvas 300x300.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
BW = 8  # brush width

# Box coords
left, right = 90, 210
top, bot = 130, 250
cx = (left + right) // 2  # 150

# 1) Central vertical (protrudes above box; goes through center)
#    Starts above the box, extends through interior.
d.line([(cx, 55), (cx, 245)], fill=INK, width=BW)

# 2) Left side vertical of box
d.line([(left, top), (left, bot)], fill=INK, width=BW)

# 3) 横折: top horizontal + right vertical
d.line([(left, top), (right, top)], fill=INK, width=BW)
d.line([(right, top), (right, bot)], fill=INK, width=BW)

# 4) Middle horizontal (inside box)
mid_y = (top + bot) // 2  # 190
d.line([(left, mid_y), (right, mid_y)], fill=INK, width=BW)

# 5) Bottom horizontal (close box)
d.line([(left, bot), (right, bot)], fill=INK, width=BW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0204_由/01_由.png")
