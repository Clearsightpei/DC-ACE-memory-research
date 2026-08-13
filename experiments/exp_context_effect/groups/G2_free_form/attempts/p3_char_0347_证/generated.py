"""
证 = 讠 (left, yan radical, 2 strokes) + 正 (right, zheng, 5 strokes)

Total 7 strokes. Left ~30% width, right ~55% width.

讠 (left):
  1. 点 (top dot) — short slash top-left of radical
  2. 横折提 — short horizontal, fold down-left, then up-right lift

正 (right, 5 strokes):
  1. 横 (top horizontal, short)
  2. 竖 (left vertical, from below the top horizontal)
  3. 横 (middle horizontal, medium)
  4. 竖 (right vertical, short)
  5. 横 (bottom horizontal, longest)
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(pts, width=7):
    d.line(pts, fill=BLACK, width=width, joint="curve")


# ---- 讠 (left) — center around x=75, occupies roughly x=45..105, y=75..245 ----

# stroke 1: 点 (top dot) — short down-right slash, upper area
stroke([(70, 75), (90, 100)], width=8)

# stroke 2: 横折提 — short horizontal top, fold down (long vertical-ish curve), then lift up-right
# horizontal top
stroke([(55, 135), (105, 130)], width=7)
# fold down and slight left curve (goes from (105,130) down-left to (55,225))
stroke([(105, 130), (95, 175), (55, 225)], width=7)
# lift up-right (提)
stroke([(55, 225), (110, 210)], width=7)

# ---- 正 (right) — occupies roughly x=135..280, y=100..245 ----
# Strategy: keep the components clearly SEPARATED so it doesn't read as a
# closed box (like 巳). Middle horizontal must PROTRUDE LEFT past the
# left vertical (like 止), and the bottom must be widest on both sides.

# stroke 1: top horizontal (medium)
stroke([(180, 110), (250, 108)], width=7)

# stroke 2: left short vertical — drops from just under the top horizontal,
# stops around middle horizontal height (does NOT reach bottom)
stroke([(195, 115), (192, 180)], width=7)

# stroke 3: middle horizontal — extends LEFT past the left vertical
# (this is the 止-signature that breaks the box illusion)
stroke([(165, 180), (245, 178)], width=7)

# stroke 4: right vertical — from top horizontal's right end down to bottom
stroke([(245, 115), (250, 240)], width=7)

# stroke 5: bottom horizontal — widest, extends past both sides
stroke([(140, 245), (280, 240)], width=9)

out_path = (
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0347_证/01_证.png"
)
img.save(out_path)
print("wrote", out_path)
