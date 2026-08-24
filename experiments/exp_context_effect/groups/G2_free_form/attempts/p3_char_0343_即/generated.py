"""Render 即 (jí) — left 艮/皀 component + right 卩 component.

Layout: left-right compound. Left occupies ~45%, right ~55%.
Left component: small box with 2 internal horizontal strokes, then a
竖提 base stroke ending with an upward flick to the right.
Right component 卩: 横折钩 (top box) + long 竖 hanging down.

Hook flicks UP-and-LEFT (TIER-0 rule).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5  # main line width

def line(pts, w=LW):
    d.line(pts, fill=BLACK, width=w, joint="curve")

# ---------- LEFT: 艮/皀-like component (top日-box + 匕-style base) ----------
# Top box: roughly x in [42, 118], y in [45, 155]
# Stroke 1: 竖 (left vertical of box)
line([(45, 50), (48, 155)], w=LW)

# Stroke 2: 横折 (top + right side)
line([(45, 50), (118, 48), (120, 155)], w=LW)

# Stroke 3: upper-middle 横
line([(50, 88), (118, 90)], w=LW)

# Stroke 4: lower-middle 横
line([(50, 122), (118, 124)], w=LW)

# Stroke 5: bottom 横 closing the box
line([(50, 155), (120, 155)], w=LW)

# Stroke 6: 匕-style base — a 撇 from top-right of base area down to lower-left,
# then a 竖弯钩-like sweep across the bottom with UP-LEFT flick at the right end.
# 撇: from around (95, 160) down-left to (50, 260)
line([(95, 160), (55, 260)], w=LW)
# 竖弯钩: from (60, 200) down and curving right to (130, 265), flick UP-and-LEFT
line([(60, 200), (60, 255), (90, 268), (130, 265), (128, 245)], w=LW)

# ---------- RIGHT: 卩 component ----------
# 横折钩 top box: horizontal from (170,70) to (230,68), fold down to (232,175), hook flicks UP-LEFT
line([(170, 70), (232, 68), (230, 175), (210, 170)], w=LW)  # hook UP-and-LEFT

# 竖 hanging: long vertical from around (185,70) down to (185,275)
line([(185, 72), (188, 275)], w=LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0343_即/01_即.png")
print("saved")
