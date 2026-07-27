"""
G2 attempt — p3_char_0071_口
Character: 口 (mouth) — 3 strokes, square box.

Structure (per form_catalog):
  1. 竖 as left-wall of a box: TL corner → BL corner, no hook, uniform.
  2. 横折 as top-right corner: 横 spans top → shoulder dab at TR →
     竖 descends along right wall to BR.
  3. 横 as internal / bottom bar: spans left-wall to right-wall exactly.

Layout: 300x300 canvas, square family (x~70%, y~70%).
Box: left ~65, right ~235, top ~75, bottom ~230.
Slight down-tilt on top (calligraphic feel from GT: top slightly higher on left).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 8  # stroke width

# Box corners (slight calligraphic variation — top narrows outward a touch)
TL = (65, 78)
TR = (232, 72)   # top-right slightly higher
BL = (72, 232)   # bottom-left tucked in slightly
BR = (225, 228)

def stroke(p0, p1, width=LW):
    d.line([p0, p1], fill=BLACK, width=width)
    # brush-dab endpoints (rounded)
    r = width // 2
    for (x, y) in (p0, p1):
        d.ellipse([x-r, y-r, x+r, y+r], fill=BLACK)

# Stroke 1: 竖 (left wall) — top-left to bottom-left
stroke(TL, BL)

# Stroke 2: 横折 — top 横 then shoulder then right 竖
# Top 横 (with slight up-tilt from TL to TR)
stroke(TL, TR)
# Small shoulder dab at TR (顿 pressure)
r = LW // 2 + 1
d.ellipse([TR[0]-r, TR[1]-r, TR[0]+r, TR[1]+r], fill=BLACK)
# Right 竖 down to BR
stroke(TR, BR)

# Stroke 3: 横 (bottom bar) — from BL to BR (spans full width)
stroke(BL, BR)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0071_口/01_口.png")
