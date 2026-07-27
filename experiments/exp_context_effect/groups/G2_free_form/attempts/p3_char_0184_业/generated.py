"""
业 — 5 strokes:
  1. left 丿 (short flick, top-left of body)
  2. left 丨 (short vertical, inner-left)
  3. right 丨 (short vertical, inner-right, slightly taller)
  4. right 丶 (short flick, top-right of body)
  5. bottom 一 (long horizontal base spanning body)

Not on sibling-risk list. Simple derivation from GT.
Layout: base horizontal near y=230; verticals rise from base to y~120;
dots angle outward at top (~y 130-160).
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
ink = (0, 0, 0)
LW = 9

# Body: two long verticals (spread apart), bottom 横 spans wide,
# top has two OUTER ticks angling toward the vertical tops.
base_y = 240
left_v_x = 118
right_v_x = 188

# Stroke 1: left outer tick 丶 (from upper-outer down-right toward verticals)
d.line([(65, 130), (108, 175)], fill=ink, width=LW)

# Stroke 2: left inner vertical (from near top down to baseline)
d.line([(left_v_x, 110), (left_v_x, base_y - 3)], fill=ink, width=LW)

# Stroke 3: right inner vertical (parallel, similar height)
d.line([(right_v_x, 105), (right_v_x, base_y - 3)], fill=ink, width=LW)

# Stroke 4: right outer tick 丶 (from upper-outer down-left toward verticals)
d.line([(240, 130), (198, 175)], fill=ink, width=LW)

# Stroke 5: bottom long horizontal (spans wider than the verticals)
d.line([(40, base_y), (262, base_y)], fill=ink, width=LW + 2)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0184_业/01_业.png")
