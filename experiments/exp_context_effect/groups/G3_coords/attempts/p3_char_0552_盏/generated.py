# BANK_DEVIATION
# skipped: min_dish.py
# reason: bank 皿 is full-canvas (y=100..220); in 盏 the 皿 must compress
#   into the bottom third (~y=205..280) beneath the 戋 top. Inlining
#   a shortened 皿 with the same 5-stroke topology (3 shus + top-right
#   corner + long base heng).
# fresh_component: min_dish_bottom_for_top_stack
#
# 盏 (zhǎn) — top: 戋 (5 strokes: 一, 一, 丿-dot, 斜钩, small dot upper right)
#              bottom: 皿 (5 strokes: 3 shus + 横折 top-right + long base 一)
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 6

# ============ TOP: 戋 (jian) — occupies roughly y=25..195 ============

# Stroke 1: top 横 — wide, slightly rising
d.line([(70, 70), (225, 55)], fill=INK, width=LW)

# Stroke 2: second 横 — shorter, below the first, slightly rising
d.line([(75, 130), (185, 118)], fill=INK, width=LW)

# Stroke 3: 斜钩 (slanted hook) — starts above top-heng at mid-left,
# sweeps down-right across both hengs, ends with a small up-hook.
d.line([(130, 40), (240, 195)], fill=INK, width=LW)
# small hook tip going up-right
d.line([(240, 195), (255, 178)], fill=INK, width=LW)

# Stroke 4: small dot/pie at top right (upper right of 斜钩, near top edge)
d.line([(215, 45), (230, 70)], fill=INK, width=LW)

# Stroke 5: small dot below-left on the sweep (short pie-dot)
d.line([(110, 160), (95, 190)], fill=INK, width=LW)

# ============ BOTTOM: 皿 — occupies roughly y=210..280 ============
# Compressed from bank min_dish (which used y=100..220)

# Left vertical (slight inward slant)
d.line([(80, 215), (86, 270)], fill=INK, width=LW)

# First inner short vertical
d.line([(125, 220), (127, 270)], fill=INK, width=LW)

# Second inner short vertical
d.line([(170, 220), (170, 270)], fill=INK, width=LW)

# 横折 top-right corner (short horizontal, then down)
d.line([(110, 215), (220, 215)], fill=INK, width=LW)
d.line([(220, 215), (214, 270)], fill=INK, width=LW)

# Long bottom horizontal (extends beyond box)
d.line([(55, 282), (255, 280)], fill=INK, width=LW + 1)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0552_盏/01_盏.png")
print("saved")
