"""
册 (ce4) — 5 strokes.
Structure: two vertical "frame" shapes side by side, each a 竖 + 横折钩,
plus a long horizontal bar through the middle connecting both frames.

Layout (300x300 canvas):
- Left frame: left竖 at x~70, right竖(hook) at x~130; top~60, bottom~250
- Right frame: left竖 at x~170, right竖(hook) at x~230; top~60, bottom~250
- Middle horizontal spans across ~x=45 to x=255 at y~155
- Left frame's right vertical hooks left at the bottom (册 hooks inward
  but conventionally the outer hook flicks toward the interior body).
- Right frame's right vertical also hooks left/inward.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6

def line(a, b, w=LW):
    d.line([a, b], fill=BLACK, width=w)

# --- Left frame ---
# Stroke 1: left 竖 of left frame — slight slant, slightly shorter than right
line((72, 80), (66, 260), w=LW)

# Stroke 2: 横折钩 — top horizontal + right vertical + hook flick up-left
# top horizontal
line((72, 70), (140, 68), w=LW)
# right vertical down
line((140, 68), (138, 250), w=LW)
# hook flick UP-and-LEFT (per hook family rule)
line((138, 250), (122, 236), w=LW)

# --- Right frame ---
# Stroke 3: left 竖 of right frame
line((170, 80), (166, 260), w=LW)

# Stroke 4: 横折钩 — top + right vertical + hook
line((170, 70), (238, 68), w=LW)
line((238, 68), (236, 250), w=LW)
# hook flick UP-and-LEFT
line((236, 250), (220, 236), w=LW)

# --- Stroke 5: the long horizontal 一 through the middle, connecting both frames ---
# The bar is slightly angled up-right (calligraphic 横)
line((40, 162), (260, 152), w=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0207_册/01_册.png")
print("wrote 01_册.png")
