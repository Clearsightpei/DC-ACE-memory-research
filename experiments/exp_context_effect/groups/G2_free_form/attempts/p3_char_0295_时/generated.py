"""
时 (shí) = 日 (left) + 寸 (right). 6 strokes total.

Composition plan (from GT inspection + pass_index precedents 日 and 对/寸):
- Left 日: tall-narrow box, compressed to left ~38% width, vertically
  centered but sitting slightly high (matches GT where 日 top aligns
  above 寸's top and its bottom aligns roughly with 寸's 横).
  4 strokes: 竖 (left wall), 横折 (top+right), 横 (middle bar), 横 (bottom).
- Right 寸: fills right ~55% width; 竖钩 is the tallest element,
  starts above the 横 and descends past the 日's bottom baseline, hook
  flicks up-and-slightly-left. 3 strokes: 横, 竖钩, 丶.
- Small gap between 日 and 寸.

TIER-0 hook rule: 寸's 竖钩 flicks UP-and-LEFT (~-118°). Never DOWN.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    if steps is None:
        dist = math.hypot(x1 - x0, y1 - y0)
        steps = max(60, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# =========================================================================
# LEFT: 日 (tall-narrow box, compressed to left)
# =========================================================================
# Left box: LEFT..RIGHT ~ 40..115  (width 75), TOP..BOT ~ 65..225
LEFT   = 40
RIGHT  = 115
TOP    = 65
BOTTOM = 225
MID_Y  = (TOP + BOTTOM) // 2 + 3
LW     = 6

# Stroke 1: 竖 (left wall)
line_dabs(LEFT, TOP + 2, LEFT, BOTTOM, LW, LW)
dab(LEFT, TOP + 2, LW + 1)
dab(LEFT, BOTTOM, LW + 0.5)

# Stroke 2: 横折 (top 横 + right 竖)
line_dabs(LEFT - 2, TOP, RIGHT, TOP, LW, LW)
dab(LEFT - 2, TOP, LW + 1)
dab(RIGHT, TOP, LW + 1.5)  # shoulder 顿
# small shoulder step then down
line_dabs(RIGHT, TOP, RIGHT + 2, TOP + 6, LW, LW)
line_dabs(RIGHT + 2, TOP + 6, RIGHT + 2, BOTTOM, LW, LW)
dab(RIGHT + 2, BOTTOM, LW + 0.5)

# Stroke 3: 横 (internal middle cross-bar)
line_dabs(LEFT + 2, MID_Y, RIGHT - 2, MID_Y, LW - 1, LW - 1)

# Stroke 4: 横 (bottom bar closes the box)
line_dabs(LEFT - 2, BOTTOM, RIGHT + 4, BOTTOM, LW, LW)


# =========================================================================
# RIGHT: 寸 (right ~55% of canvas)
# =========================================================================
# Stroke 5: 横 — long horizontal across mid-height of right side
H_LEFT  = (145, 148)
H_RIGHT = (278, 142)
R_H = 5
dab(H_LEFT[0], H_LEFT[1], R_H + 1.5)
line_dabs(H_LEFT[0], H_LEFT[1], H_RIGHT[0], H_RIGHT[1], R_H, R_H)
dab(H_RIGHT[0], H_RIGHT[1], R_H + 2)

# Stroke 6: 竖钩 — starts above the 横 (top a bit above 日's top),
# descends past 日's bottom, hook flicks up-and-slightly-left.
V_TOP    = (218, 70)
V_BOTTOM = (218, 258)
R_V = 5.5
dab(V_TOP[0], V_TOP[1], R_V + 1.5)
line_dabs(V_TOP[0], V_TOP[1], V_BOTTOM[0], V_BOTTOM[1], R_V, R_V)

HOOK_LEN = 40
hook_angle = math.radians(-118)  # UP-and-LEFT
HX = V_BOTTOM[0] + HOOK_LEN * math.cos(hook_angle)
HY = V_BOTTOM[1] + HOOK_LEN * math.sin(hook_angle)
line_dabs(V_BOTTOM[0], V_BOTTOM[1], HX, HY, R_V, 1.0)

# Stroke 7: 丶 — small teardrop, below 横 and left of 竖钩
D_START = (168, 178)
D_END   = (188, 200)
steps = 60
for i in range(steps + 1):
    t = i / steps
    tt = t ** 1.5
    x = D_START[0] + (D_END[0] - D_START[0]) * t
    y = D_START[1] + (D_END[1] - D_START[1]) * t
    r = 1.4 + (6.0 - 1.4) * tt
    dab(x, y, r)
dab(D_END[0], D_END[1], 6.4)


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0295_时/01_时.png")
print("wrote 01_时.png")
