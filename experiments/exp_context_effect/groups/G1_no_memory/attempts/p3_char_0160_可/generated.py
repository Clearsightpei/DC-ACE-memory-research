"""Render 可 as a 300x300 PNG using PIL.

Revised: move 口 (mouth) up so its top nearly touches the heng, make
mouth a bit wider, and give the vertical hook a slight curve at the
bottom.
"""
from PIL import Image, ImageDraw

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
W = 6

# 1. Top horizontal (heng) — long, spans wide, slight downward slope
d.line([(30, 92), (272, 88)], fill=INK, width=W)

# 2. Mouth (口) on the lower-left, hanging just under the heng.
# Box roughly x: 55..145, y: 100..175
# 2a. Left vertical of mouth
d.line([(60, 100), (58, 178)], fill=INK, width=W)
# 2b. Right vertical of mouth
d.line([(148, 102), (150, 176)], fill=INK, width=W)
# 2c. Bottom horizontal of mouth
d.line([(58, 176), (152, 178)], fill=INK, width=W)

# 3. Long vertical shu-gou on the right, starting from heng.
# Main vertical
d.line([(210, 90), (216, 250)], fill=INK, width=W)
# Curved hook at the bottom (two short segments approximating a curve)
d.line([(216, 250), (208, 260)], fill=INK, width=W)
d.line([(208, 260), (188, 258)], fill=INK, width=W)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G1_no_memory/attempts/p3_char_0160_可/01_可.png"
)
print("wrote 01_可.png")
