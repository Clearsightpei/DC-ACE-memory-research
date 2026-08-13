"""伎 — 亻 (left) + 支 (right). 6 strokes total.

Left 亻 (2 strokes):
  1. 撇 from upper-left down-left
  2. long 竖 from below-撇 down to bottom

Right 支 (4 strokes) — 十 above + 又 below:
  3. 横 across upper-right (top horizontal)
  4. short 竖 dropping from horizontal middle down
  5. 横撇 (short horizontal that flicks into a 撇 going down-left to bottom)
  6. 捺 long diagonal down-right meeting the 撇

300x300 PIL render, black ink, white bg.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=6):
    for i in range(len(pts)-1):
        d.line([pts[i], pts[i+1]], fill="black", width=width)
    for p in pts:
        r = width/2
        d.ellipse([p[0]-r, p[1]-r, p[0]+r, p[1]+r], fill="black")

# ---- 亻 (left radical) ----
# 撇: from ~ (95, 65) down-left to (55, 155)
stroke([(95, 65), (85, 90), (70, 125), (55, 160)], width=6)
# 竖: long vertical from just below the 撇 start, down to bottom
stroke([(90, 105), (90, 265)], width=6)

# ---- 支 (right side) ----
# top 横: horizontal across upper right
stroke([(140, 90), (185, 88), (245, 85)], width=6)
# short 竖: drops from horizontal middle down through where 横撇 will cross
stroke([(190, 88), (190, 170)], width=6)
# 横撇: a short horizontal starting from left, then curves/flicks down-left to bottom
stroke([(145, 165), (185, 163), (210, 163),
        (195, 190), (170, 230), (140, 275)], width=6)
# 捺: long diagonal from ~(190, 170) down-right to (270, 275)
stroke([(190, 170), (215, 210), (245, 245), (272, 275)], width=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0254_伎/01_伎.png")
