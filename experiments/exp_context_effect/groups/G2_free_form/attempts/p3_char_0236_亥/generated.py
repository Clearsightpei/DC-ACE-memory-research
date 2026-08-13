"""
亥 — 6 strokes, character.
Structure (top→bottom):
  1. 点 (dot) — top center-left
  2. 横 (long horizontal) — under the dot, spans most of width
  3. 撇折 (small) — starts under-left of 横, short 撇 then folds right
  4. 撇 (long) — big diagonal from upper-mid down to lower-left
  5. small 撇 — inside the belly, short flick
  6. 捺 — sweeping diagonal from mid down-right
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def stroke(points, width=5):
    for i in range(len(points) - 1):
        d.line([points[i], points[i + 1]], fill=INK, width=width)
    # dab endpoints for a slight brush feel
    for p in points:
        r = width / 2
        d.ellipse((p[0] - r, p[1] - r, p[0] + r, p[1] + r), fill=INK)


# 1. 点 — small right-leaning dot near top-center
stroke([(150, 50), (162, 65)], width=6)

# 2. 横 — long horizontal, slightly rising then dipping (calligraphic)
stroke([(55, 105), (95, 100), (160, 98), (220, 100), (250, 108)], width=5)

# 3. 撇折 — short 撇 down-left then folds right (little tucked shape below 横)
stroke([(115, 128), (100, 150), (95, 165)], width=5)   # 撇 portion
stroke([(95, 165), (120, 168), (145, 162)], width=5)   # 折 turning right

# 4. 长撇 — big diagonal from upper mid down to lower-left corner
stroke([(160, 125), (140, 160), (115, 200), (80, 240), (58, 262)], width=5)

# 5. small 撇 inside belly — short flick right-of-center, above 捺 origin
stroke([(170, 175), (158, 195), (150, 210)], width=5)

# 6. 捺 — sweeping diagonal, tapered terminal (no blob)
stroke([(175, 175), (195, 205), (220, 235), (248, 258), (268, 268)], width=5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0236_亥/01_亥.png")
