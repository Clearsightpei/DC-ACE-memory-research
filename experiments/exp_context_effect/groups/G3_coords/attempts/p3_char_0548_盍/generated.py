# BANK_DEVIATION
# skipped: min_dish.py (called via reference only; reformatted inline for compressed bottom half)
# reason: 皿 needs to fit in bottom 40% of canvas under 去; original min_dish is full-canvas
# fresh_component: min_dish_compressed_for_top_stack (皿 compressed vertically, wider base)

"""
盍 (hé, "lid/cover") — top-bottom stack: 去 (top) + 皿 (bottom).
去 decomposes as 土 (top-3-strokes) + 厶 (bottom-2-strokes).
GT shows a tall 去 above a shallow wide 皿.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5

# =========== TOP: 去 (approx y = 25..165) ===========

# --- 土 top part ---
# Stroke 1: top short heng
d.line([(115, 45), (195, 40)], fill=INK, width=LW)
# Stroke 2: vertical shu through
d.line([(153, 32), (150, 100)], fill=INK, width=LW)
# Stroke 3: wider bottom heng (of 土)
d.line([(85, 100), (220, 98)], fill=INK, width=LW+1)

# --- 厶 bottom part of 去 ---
# Stroke 4: 撇折 — starts as a leftward pie, then folds into a rising heng
# Pie segment: from (155, 115) down-left to (115, 155)
d.line([(155, 115), (115, 155)], fill=INK, width=LW)
# Folded heng segment: from (115, 155) up-right to (170, 152)
d.line([(115, 155), (170, 150)], fill=INK, width=LW)
# Stroke 5: small 点 (dot) at the right end
d.line([(170, 150), (185, 168)], fill=INK, width=LW+1)

# =========== BOTTOM: 皿 (approx y = 185..270) ===========
# Compressed version of min_dish, wider base

# Left vertical (slight inward slant)
d.line([(80, 190), (85, 255)], fill=INK, width=LW)

# Inner short vertical 1
d.line([(125, 200), (127, 255)], fill=INK, width=LW)

# Inner short vertical 2
d.line([(170, 200), (170, 255)], fill=INK, width=LW)

# Top-right corner 横折: short horizontal then vertical down
d.line([(112, 190), (222, 190)], fill=INK, width=LW)
d.line([(222, 190), (215, 255)], fill=INK, width=LW)

# Long base horizontal (extends beyond)
d.line([(45, 272), (265, 268)], fill=INK, width=LW+1)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0548_盍/01_盍.png")
print("saved")
