"""
空 (kōng) - 8 strokes.
Composition: 穴 (top, 5 strokes: dot, horizontal-hook, left-dot, right-flick+dot)
           + 工 (bottom, 3 strokes: horizontal, vertical, horizontal)
穴字头 breakdown (matching GT):
  1. Top center dot
  2. 宀-like horizontal turn (small hook right)
  3. Left short flick 撇
  4. Middle-lower small flick
  5. Right dot
工 breakdown:
  6. Short top horizontal
  7. Short vertical
  8. Long bottom horizontal (wider than the 穴 above)
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=6):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill="black", width=width)
    for p in pts:
        d.ellipse([p[0] - width/2, p[1] - width/2, p[0] + width/2, p[1] + width/2], fill="black")

# 1. Top dot (center of 宀)
stroke([(150, 45), (158, 60)], width=7)

# 2. Horizontal-turn (宀 top): starts left, goes right, small down-hook at right
stroke([(85, 90), (215, 90), (218, 105)], width=6)

# 3. Left 撇 of 穴 (下方 left short flick)
stroke([(105, 105), (85, 135)], width=6)

# 4. Middle small flick (right of center inside 穴)
stroke([(150, 110), (140, 130)], width=6)

# 5. Right dot of 穴
stroke([(180, 115), (195, 135)], width=6)

# 6. Top horizontal of 工
stroke([(115, 175), (185, 175)], width=6)

# 7. Vertical of 工
stroke([(150, 178), (150, 235)], width=7)

# 8. Bottom long horizontal of 工
stroke([(65, 240), (240, 238)], width=7)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0397_空/01_空.png"
img.save(out)
print("saved", out)
