"""
Render 些 (p3_char_0383).

Structure: 此 (top) + 二 (bottom)
  此 = 止 (top-left) + 匕 (top-right)
  二 = two horizontals below (lower one longer)

# SIGNATURE CHECK (from sibling_signature_checklist.md):
#   匕: top stroke is a 撇 (upper-right -> lower-left);
#       terminal hook flicks UP-and-LEFT.
# Compound-component rule: apply row inside the sub-glyph.
"""

from PIL import Image, ImageDraw

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

W = 10  # ink width


def line(x1, y1, x2, y2, w=W):
    d.line([(x1, y1), (x2, y2)], fill="black", width=w)


def polyline(pts, w=W):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill="black", width=w)


# ---- Top half: 此 (approx rows 30..170) ----

# LEFT sub-glyph: 止
# 止 has: short vertical (top-left area), short horizontal (middle-left),
#        long horizontal base, left descending "foot" (short 竖 down-left).
# Approximate 米字格 quadrant TL.

# 止 = 竖 (left tall) + 一 (mid short) + 竖 (right short) + 一 (base)
# left tall 竖
line(70, 50, 70, 155)
# mid short 横 (right side of left 竖)
line(70, 100, 115, 100)
# right short 竖 (top of the mid 横 upward-ish? actually short 竖 going down from 横 area to base)
line(115, 75, 115, 155)
# base 横 (longer)
line(45, 155, 140, 155)

# RIGHT sub-glyph: 匕
# 匕 has: top 撇 (upper-right -> lower-left), then 竖弯钩 (down-right,
# arc, up-left hook).
# Approximate right side (TR quadrant).

# top 撇: starts upper-right, goes lower-left
polyline([(215, 55), (200, 75), (180, 105), (160, 130)])
# 竖弯钩 body: start upper (near where 撇 crosses), go down, arc right, hook up-left
polyline([
    (190, 60),   # start upper
    (190, 100),
    (192, 130),
    (200, 150),
    (225, 158),
    (250, 155),  # arc bottom rightmost
    (255, 148),  # hook flicks UP and slightly LEFT
    (250, 135),
])

# ---- Bottom half: 二 (rows 195..270) ----
# short upper 横
line(105, 210, 195, 210)
# long lower 横
line(60, 265, 245, 265)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0383_些/01_些.png")
print("saved")
