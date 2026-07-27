"""
p3_char_0150_引 — G2 free-form attempt.

Composition: 弓 (left) + 丨 (right).
弓 = 3 folds forming a stacked "E" open-to-left: 横折 + 横 + 横折钩.
    All three fold on the RIGHT edge. Bottom stroke hooks up-and-left.
丨 = tall vertical on the right, slightly taller than the 弓 unit.

Layout in 300x300 canvas:
- 弓 occupies left ~55%, vertically centered.
- 丨 sits at right ~65-70% x, taller — starts higher, ends lower.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
INK = 0
BG = 255
img = Image.new("L", (W, H), BG)
d = ImageDraw.Draw(img)

def stroke(pts, width=10):
    d.line(pts, fill=INK, width=width, joint="curve")
    # round terminals
    r = width // 2
    for (x, y) in [pts[0], pts[-1]]:
        d.ellipse([x - r, y - r, x + r, y + r], fill=INK)

# ---- 弓 (left component) ----
# Right edge for the three folds:
xR = 135          # right shoulder x
xL_top = 45       # top-left start
xL_mid = 50
xL_bot = 45

# Stroke 1: 横折 (top) — horizontal then down (short down segment)
y1 = 70
stroke([(xL_top, y1), (xR, y1), (xR + 2, y1 + 28)], width=10)

# Stroke 2: 横 (middle) — short horizontal, connected on the right
y2 = 118
stroke([(xL_mid + 8, y2), (xR + 2, y2)], width=10)

# Stroke 3: 横折钩 (bottom) — horizontal, down, then hook up-and-left
y3 = 158
xR3 = xR + 4
p1 = (xL_bot, y3)
p2 = (xR3, y3)
# down and slightly right-leaning
p3 = (xR3 + 2, y3 + 78)
# hook flick UP-and-LEFT (per TIER-0 rule B)
p4 = (xR3 - 45, y3 + 55)
stroke([p1, p2, p3, p4], width=10)

# ---- 丨 (right component) — tall vertical, taller than 弓 ----
xV = 215
stroke([(xV, 55), (xV + 2, 270)], width=11)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0150_引/01_引.png")
print("saved")
