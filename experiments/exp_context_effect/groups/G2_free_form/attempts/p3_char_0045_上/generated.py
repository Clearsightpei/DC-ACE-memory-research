"""
Render 上 (p3_char_0045) — 3 strokes:
  1) 竖 (vertical) — starts upper-middle, moderate length
  2) 短横 (short horizontal) — from the vertical's midpoint, extending right
  3) 长横 (long horizontal, the base) — LONGER than the top strokes
Rule from form_catalog: 上 vs 下 — the LONGER 横 sits at the base of the glyph.
Rendered with PIL at 300x300, white bg, black ink.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
WIDTH = 8

# Stroke 1: 竖 (vertical), starts upper-middle
# Top around (150, 70) down to (150, 210)
v_top = (150, 70)
v_bot = (150, 210)
draw.line([v_top, v_bot], fill=INK, width=WIDTH)

# Small 顿 dab at top of vertical
draw.ellipse([v_top[0]-5, v_top[1]-3, v_top[0]+5, v_top[1]+5], fill=INK)

# Stroke 2: 短横 (short horizontal to the right of vertical, mid-height)
# From ~ (150, 150) to (215, 145) — slight up-tilt, short
h2_left = (150, 152)
h2_right = (218, 145)
draw.line([h2_left, h2_right], fill=INK, width=WIDTH)
# Small terminal dab
draw.ellipse([h2_right[0]-5, h2_right[1]-5, h2_right[0]+5, h2_right[1]+5], fill=INK)

# Stroke 3: 长横 (long horizontal base) — LONGER, spans wide
# Slight up-tilt, sits at the bottom
h3_left = (55, 235)
h3_right = (250, 225)
draw.line([h3_left, h3_right], fill=INK, width=WIDTH)
# Terminal dabs
draw.ellipse([h3_left[0]-4, h3_left[1]-4, h3_left[0]+6, h3_left[1]+6], fill=INK)
draw.ellipse([h3_right[0]-6, h3_right[1]-6, h3_right[0]+4, h3_right[1]+6], fill=INK)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0045_上/01_上.png")
