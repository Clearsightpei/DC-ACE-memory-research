"""
Render 疝 (shan) - illness radical 疒 enclosing 山.

Structure:
- 疒 (illness/sickness radical): 点 top, 横 across top of 疒, 撇 long
  sweep down-left, then two 点 dots on the interior-left of the sweep.
- 山 (mountain): sits inside/to the lower-right of the 疒 enclosure.
  Three vertical strokes with a base horizontal.

Following G2 memory: no sibling-risk components here. Simple PIL
brush-dab strokes at 300x300.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=7):
    d.line(pts, fill="black", width=width, joint="curve")
    for x, y in pts:
        d.ellipse((x - width/2, y - width/2, x + width/2, y + width/2), fill="black")

# --- 疒 radical ---
# 1. Top dot (点) - short slanting dot at top
stroke([(120, 45), (135, 60)], width=6)

# 2. Top horizontal (横) - short, slight upward slant right
stroke([(90, 85), (200, 78)], width=6)

# 3. Long left sweep (撇) - from right end of top horizontal down-left,
#    a long curving diagonal down to bottom-left corner
stroke([(155, 78), (140, 130), (110, 180), (70, 260)], width=7)

# 4. Two inner dots (两点) on the left interior of the sweep
# upper 点
stroke([(95, 130), (110, 140)], width=6)
# lower 点
stroke([(80, 175), (100, 180)], width=6)

# --- 山 (mountain) inside lower-right of 疒 ---
# Center vertical (tallest)
stroke([(180, 155), (180, 260)], width=7)
# Bottom horizontal (base)
stroke([(140, 260), (240, 258)], width=7)
# Left short vertical rising from base
stroke([(145, 260), (145, 200)], width=7)
# Right vertical rising from base
stroke([(235, 258), (240, 175)], width=7)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0378_疝/01_疝.png")
