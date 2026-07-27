"""
Render 丬 (p3_char_0042_丬) at 300x300, white bg, black ink.

Structure (from GT):
- 3 strokes total.
- Stroke 1: upper 点/提 — short diagonal in upper-left area, rising
  from lower-left to upper-right (like a stubby 提).
- Stroke 2: lower 提 — short diagonal near lower-left, rising from
  lower-left to upper-right, longer than stroke 1.
- Stroke 3: long 竖 on the right side, running nearly full-height,
  with a slight lean (top slightly right of bottom / near vertical).
The right 竖 sits at about x=180 (of 300). Left short strokes cluster
around x=70-140. Vertical roughly y=40 to y=270. Upper short stroke
around y=110-140. Lower short stroke around y=200-235.
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
WIDTH = 6

def stroke(p0, p1, w=WIDTH):
    draw.line([p0, p1], fill=BLACK, width=w)
    # round caps
    r = w // 2
    for (x, y) in (p0, p1):
        draw.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)

# Stroke 1: upper short 提 (rises to the right), upper-left area.
# from (100, 140) up to (145, 115)
stroke((100, 140), (145, 115))

# Stroke 2: lower 提 (rises to the right), lower-left area, longer.
# from (75, 235) up to (155, 210)
stroke((75, 235), (155, 210))

# Stroke 3: long vertical 竖 on the right, nearly full height,
# slight lean (top a bit right of bottom).
# from (180, 45) down to (175, 275)
stroke((180, 45), (175, 275), w=7)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0042_丬/01_丬.png")
