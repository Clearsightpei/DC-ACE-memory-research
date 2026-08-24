"""Render 事 (p3_char_0367) — 8 strokes.

Structure:
  1. Top short 横 (near the top)
  2. Long horizontal below top
  3. Small 口/日-like box in upper-middle (横折 + 横 + closing 横)
     Actually 事 = 一 + 口 + 二 + long-vertical-hook piercing all,
     with a final horizontal near the bottom that the vertical hook crosses.
  4-6. Middle stack of horizontals
  7. Bottom long 横 (with slight tilt)
  8. Central vertical 竖钩 piercing top-to-bottom, hooks up-and-LEFT at bottom.

Following G2 memory: hook flick UP-and-LEFT (~-105°).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6  # main line width


def line(p0, p1, w=LW):
    d.line([p0, p1], fill=BLACK, width=w)


def poly(points, w=LW):
    d.line(points, fill=BLACK, width=w, joint="curve")


# --- Layout on 300x300 canvas ---
# 事 is a narrow-tall character; center is around x=150.

# 1. Top small 横 (short, high) -- like a small tick at top
line((135, 42), (172, 42), w=6)

# 2. Long upper horizontal (spans wide, slight tilt down-right)
line((50, 82), (250, 78), w=6)

# 3. Small 口 box (upper-middle):
#    left vertical
line((95, 90), (95, 145), w=5)
#    top horizontal (already covered by long horizontal, but small closing top inside)
line((95, 90), (205, 90), w=5)
#    right vertical
line((205, 90), (205, 145), w=5)
#    middle horizontal (bottom of the 口)
line((95, 145), (205, 145), w=5)
#    inner horizontal inside the box (the 曰 middle bar)
line((105, 118), (195, 118), w=4)

# 4. Middle horizontal (below the box)
line((60, 178), (240, 175), w=6)

# 5. Lower-middle horizontal
line((70, 215), (235, 212), w=6)

# 6. Bottom long horizontal (the widest, with tilt)
line((45, 250), (255, 245), w=6)

# 7. Central vertical 竖钩 (piercing everything, ending with hook UP-and-LEFT)
poly([(150, 40), (150, 268)], w=7)
# hook: from bottom, flick up-and-LEFT
poly([(150, 268), (128, 254)], w=7)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0367_事/01_事.png"
)
print("wrote 01_事.png")
