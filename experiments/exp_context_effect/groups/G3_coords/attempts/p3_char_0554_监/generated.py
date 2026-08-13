# BANK_DEVIATION
# skipped: min_dish.py
# reason: 皿 needs to be compressed into the bottom third of the canvas as a base radical; bank version fills the whole canvas.
# fresh_component: min_dish_compressed_bottom_for_监

"""
监 (jiān) — top half: 臣-like left cluster + 卜-like right cluster + middle 一,
bottom half: 皿 (compressed).

Inlining fresh via PIL — from GT visual decomposition.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5

# =================================================================
# TOP-LEFT cluster (compressed 臣): ~x 50–130, y 45–150
# Two-stroke shape: slanted upper stroke + tall vertical
# =================================================================
# Slanted upper stroke (like a 撇 leaning right-down but short)
d.line([(58, 55), (110, 100)], fill=INK, width=LW)
# Tall vertical (a bit tilted)
d.line([(72, 65), (82, 155)], fill=INK, width=LW)
# Small horizontal cross bar mid-left (part of compressed 臣)
d.line([(80, 115), (118, 115)], fill=INK, width=LW)

# =================================================================
# TOP-RIGHT cluster (like 卜 / short shu + slanted): ~x 140–260, y 50–150
# =================================================================
# Vertical stroke (tall shu)
d.line([(178, 55), (172, 155)], fill=INK, width=LW)
# Short horizontal cap up top going right
d.line([(178, 62), (245, 80)], fill=INK, width=LW)
# Slanted stroke (na-like) going down-right
d.line([(190, 95), (250, 150)], fill=INK, width=LW)

# =================================================================
# MIDDLE HORIZONTAL (一 spanning under top clusters): ~y 165, x 50-270
# =================================================================
d.line([(50, 168), (275, 165)], fill=INK, width=LW + 1)

# =================================================================
# BOTTOM 皿 (compressed dish): x 55–260, y 180–275
# =================================================================
# Left vertical (slight inward slant)
d.line([(75, 185), (82, 260)], fill=INK, width=LW)
# First inner vertical
d.line([(125, 190), (127, 260)], fill=INK, width=LW)
# Second inner vertical
d.line([(175, 190), (175, 260)], fill=INK, width=LW)
# Top-right corner 横折
d.line([(105, 185), (230, 185)], fill=INK, width=LW)
d.line([(230, 185), (222, 260)], fill=INK, width=LW)
# Bottom long horizontal (extends beyond box)
d.line([(40, 273), (275, 271)], fill=INK, width=LW + 1)

out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0554_监/01_监.png"
img.save(out_path)
print(f"saved {out_path}")
