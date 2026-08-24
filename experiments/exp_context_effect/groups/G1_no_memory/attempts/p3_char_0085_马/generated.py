"""G1 render of 马 (horse) — 3-stroke simplified form.

Strokes:
  1. 横折  (top): horizontal → down (top of the "box")
  2. 竖折折钩 (middle+right): starts as a horizontal middle bar going
     right, drops down, curves right and hooks up-left.
  3. 长横 (bottom): long horizontal base sweep.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
LW = 5

def line(pts, w=LW):
    d.line(pts, fill=INK, width=w, joint="curve")

# Stroke 1: 横折 — top horizontal then a short down segment (top-right of box)
# Top runs from (75, 85) to (185, 78); then drops to about (188, 155)
line([(75, 88), (185, 80), (190, 158)])

# Stroke 2: 竖折折钩 — middle horizontal bar extending to right, drops,
# curves right, then hook up-left at the bottom.
# horizontal middle bar (~y=150) from left of box to slightly past stroke1 down-end,
# then goes down and out to lower-right, then hooks.
line([
    (85, 150),   # left end of middle bar
    (200, 155),  # right end of middle bar, past the stroke1 down-tip
    (225, 205),  # slopes down and right (belly of horse)
    (215, 230),  # bottom of curve
    (190, 225),  # hook back up-left
])

# Stroke 3: bottom long 横 — from lower-left to lower-right
line([(50, 245), (255, 250)])

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0085_马/01_马.png")
