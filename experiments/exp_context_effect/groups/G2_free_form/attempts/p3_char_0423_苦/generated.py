"""
苦 = 艹 (top) + 古 (bottom)
古 = 十 + 口
Structure:
  - 艹: two short verticals with a horizontal crossing near top
  - 古: long horizontal, then short vertical descending through it,
        then 口 (small rectangle) at bottom
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p1, p2, width=6):
    d.line([p1, p2], fill="black", width=width)

# ---- 艹 (top radical, occupies roughly y=30..95) ----
# Two short verticals (left one slightly leans left, right one leans right)
line((100, 40), (95, 95), width=6)   # left vertical (撇 flavor)
line((205, 40), (210, 95), width=6)  # right vertical (slight lean right)
# Horizontal crossing (long, spanning ~ x=55..245)
line((55, 75), (250, 75), width=6)

# ---- 古 (bottom, occupies y=100..270) ----
# Long horizontal (the top of 古)
line((45, 125), (255, 125), width=7)
# Vertical (十's vertical, goes from the horizontal down to the top of 口)
line((150, 105), (150, 190), width=6)

# 口 (rectangle) at bottom, centered
# left vertical
line((100, 190), (100, 265), width=6)
# top horizontal (of 口)
line((100, 190), (205, 190), width=6)
# right vertical (with slight bottom hook down-right, then close)
line((205, 190), (205, 265), width=6)
# bottom horizontal
line((100, 265), (207, 265), width=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0423_苦/01_苦.png")
