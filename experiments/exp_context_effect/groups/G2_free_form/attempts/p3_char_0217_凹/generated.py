"""
Item: p3_char_0217_凹 (concave)
5 strokes:
  1. 竖 — left outer vertical (top-left going down)
  2. 横折折 — from top of stroke 1 rightward, down (into notch left wall), rightward across notch bottom
  3. 竖折 (short) — up from notch bottom's right end, then continuation not right; here stroke 3 is
     the middle-top short vertical going up-then-right (forming right wall of notch and its top)
  4. 横折 — top of the right side: rightward across then down the right outer vertical
  5. 横 — bottom horizontal closing the shape

Silhouette: wide near-square outer U-cup with a rectangular notch bitten out
of the top-center. Overall aspect ~1:1, filling ~65% of canvas.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 8

def polyline(points, width=LW):
    d.line(points, fill=BLACK, width=width, joint="curve")
    # round the endpoints
    r = width // 2
    for (x, y) in [points[0], points[-1]]:
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)

# outer bounding box of the character body
L, R = 55, 245        # left / right outer edges
T, B = 70, 250        # top / bottom outer edges
# notch (top center) — a rectangular bite taken out from the top
NL, NR = 115, 195     # notch left / right x
NB = 135              # notch bottom y (how deep the notch goes)
# The two shoulders (top edges either side of the notch)
SL_TOP = T + 5        # top-of-left-shoulder
SR_TOP = T + 5        # top-of-right-shoulder

# Stroke 1: 竖 — left outer vertical (goes from top-left down to just above bottom)
polyline([(L, SL_TOP), (L + 2, B - 5)])

# Stroke 2: 横折折 — from top of left wall, across to notch's left edge,
# then DOWN into the notch, then RIGHT across the notch's floor.
polyline([(L, SL_TOP), (NL, SL_TOP + 2),        # top horizontal (left shoulder)
          (NL + 2, NB),                          # down into the notch
          (NR - 2, NB + 4)])                     # across notch floor rightward

# Stroke 3: middle right wall of the notch going UP then RIGHT across the right shoulder
# This is drawn as a short vertical (up out of the notch) plus the right shoulder top.
polyline([(NR, NB + 4), (NR - 2, SR_TOP + 2),   # up out of notch
          (R, SR_TOP)])                          # across right shoulder rightward

# Stroke 4: 竖 — right outer vertical (goes from right-shoulder down to bottom)
polyline([(R, SR_TOP), (R - 2, B - 5)])

# Stroke 5: 横 — bottom horizontal closing the cup
polyline([(L - 2, B), (R + 2, B - 2)])

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0217_凹/01_凹.png"
img.save(out)
print("saved", out)
