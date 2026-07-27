"""Render 凸 (p3_char_0215) — G2 free-form.

Not a sibling-risk target; no hooks. Rely on silhouette:
- Upper narrow rectangle centered horizontally, ~1/3 width.
- Lower wide rectangle spanning ~5/6 width, open top under the upper block's mouth.
- Two vertical struts drop from upper corners down to the lower rectangle's top.
- Bottom is a full-width horizontal.
Stroke count: 5 canonical (竖, 横折, 竖, 横折折折, 横).
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
LW = 8

# Layout: 米字格 mental grid on 300x300, ink-safe padding ~30.
# Upper block: x in [115, 185], y in [55, 165]
# Lower block: x in [40, 260],  y in [165, 245]
# Bottom horizontal at y=245.

# Stroke 1: upper-left short 竖 (top-left of raised part down)
d.line([(115, 55), (115, 165)], fill=INK, width=LW)

# Stroke 2: 横折 — top horizontal of raised, then down right side to shelf
d.line([(115, 55), (185, 60)], fill=INK, width=LW)      # top
d.line([(185, 60), (185, 165)], fill=INK, width=LW)     # right drop

# Stroke 3 & 4 combined body: the lower rectangle's left drop + bottom-left
# left down from shelf
d.line([(115, 165), (40, 170)], fill=INK, width=LW)     # left shelf (top of base, left half)
d.line([(40, 170), (40, 245)], fill=INK, width=LW)      # left vertical of base

# right shelf (top of base, right half) + right vertical of base
d.line([(185, 165), (260, 170)], fill=INK, width=LW)    # right shelf
d.line([(260, 170), (260, 245)], fill=INK, width=LW)    # right vertical

# Stroke 5: bottom long 横
d.line([(40, 245), (260, 245)], fill=INK, width=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0215_凸/01_凸.png")
