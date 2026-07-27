"""Render 皿 (bowl/vessel) — 5 strokes.

Stroke order (MMH):
  1. 竖    left outer vertical (slightly leaning inward at top)
  2. 竖折  top-horizontal + right vertical (one continuous stroke)
  3. 竖    inner-left short vertical
  4. 竖    inner-right short vertical
  5. 一    long bottom horizontal (extends beyond the box on both sides)

Layout on 300x300 canvas, ink black, background white.
The box occupies roughly x=[75,225], y=[110,220], with the bottom bar
extending to x=[40,260] at y=230.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 6  # base line width

def line(p0, p1, width=LW):
    d.line([p0, p1], fill=INK, width=width)

# Stroke 1: 竖 — left outer vertical, slight inward lean at top
line((85, 115), (78, 218), width=LW)

# Stroke 2: 竖折 — top horizontal then right vertical (one stroke)
# top horizontal from left-top corner across to right-top corner
line((85, 115), (218, 108), width=LW)
# right vertical drop, slight outward lean at bottom
line((218, 108), (225, 218), width=LW)

# Stroke 3: 竖 — inner-left short vertical
line((128, 128), (128, 218), width=LW-1)

# Stroke 4: 竖 — inner-right short vertical
line((175, 128), (178, 218), width=LW-1)

# Stroke 5: 一 — long bottom horizontal, extending beyond box on both sides
line((40, 232), (262, 228), width=LW+1)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0195_皿/01_皿.png")
print("Wrote 01_皿.png")
