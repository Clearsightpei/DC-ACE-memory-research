"""
卂 (xùn) — 3 strokes.
From GT PNG:
  1. Top 横 — horizontal across most of the width, near the top
  2. 横折弯钩 — starts at top-right corner, short right-lean top, then
     drops as a leaning 竖, curves left across the bottom, hooks up
  3. Middle 横 — short horizontal on the left side, roughly mid-height,
     tucks into the character body (does not extend all the way right)

Revision 1 changes vs first pass:
  - Middle 横 shortened (GT shows it not reaching the right wall)
  - 横折 shoulder made more distinct
  - Bottom curve of 横折弯钩 opened up (less rounded, more 竖弯钩 shape)
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def brush_stroke(pts, w=6):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=INK, width=w)
    for x, y in pts:
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill=INK)


# -------- Stroke 1: top 横 --------
brush_stroke([(50, 95), (230, 90)], w=6)

# -------- Stroke 2: 横折弯钩 --------
# clear shoulder at top-right, then 竖 (leans slightly left),
# then curve at bottom, then short hook
pts2 = [
    (230, 82),      # start (just above end of 横 1)
    (240, 95),      # shoulder corner
    (232, 150),     # descending 竖
    (222, 205),
    (205, 240),     # begin curve left
    (170, 260),
    (130, 262),
    (105, 255),     # end of bottom curve
    (95, 240),      # hook up
    (95, 220),
]
brush_stroke(pts2, w=6)

# -------- Stroke 3: middle 横 (shorter) --------
brush_stroke([(55, 175), (195, 170)], w=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0060_卂/01_卂.png")
