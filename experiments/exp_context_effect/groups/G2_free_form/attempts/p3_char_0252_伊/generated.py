"""伊 — 亻 (left) + 尹 (right). 6 strokes.
- 亻: 撇 (top-down-left) + 竖 (long vertical)
- 尹: 横折 (top-right cap), 横 (middle), 横 (bottom of the two right horizontals),
  long 撇 sweeping from top down-left across all horizontals.
Simple black-on-white 300x300 PIL render.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=6):
    for i in range(len(pts)-1):
        d.line([pts[i], pts[i+1]], fill="black", width=width)
    # round caps
    for p in pts:
        r = width/2
        d.ellipse([p[0]-r, p[1]-r, p[0]+r, p[1]+r], fill="black")

# ---- 亻 (left radical) ----
# 撇: from ~ (95, 70) down-left to (55, 150)
stroke([(95, 70), (85, 95), (70, 125), (55, 155)], width=6)
# 竖: long vertical from just below the 撇 start, down to bottom
stroke([(95, 105), (95, 260)], width=6)

# ---- 尹 (right side) ----
# top-right cap: 横折 — horizontal from (135, 90) to (235, 85), then fold down to (235, 130)
stroke([(135, 90), (185, 87), (235, 85), (233, 108), (232, 132)], width=6)
# middle 横 — horizontal inside/under the fold from (145, 135) to (232, 132)
stroke([(145, 137), (188, 135), (232, 133)], width=6)
# lower 横 — a second short horizontal a bit below
stroke([(155, 175), (200, 173), (240, 172)], width=6)
# long 撇 — sweeps from top-right (225, 70) down-left through the strokes to (110, 265)
stroke([(225, 70), (200, 120), (170, 175), (140, 225), (110, 265)], width=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0252_伊/01_伊.png")
