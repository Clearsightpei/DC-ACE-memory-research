"""
改 = 己 (left) + 攵 (right)
Left 己 (3 strokes): 横折, 横, 竖弯钩
Right 攵 (4 strokes): 短撇, 横, 长撇, 捺
Layout: left ~40% width, right ~55% width. Right slightly taller/dominant.
Hook rule: 竖弯钩 flick UP-and-LEFT (~-105 to -115°) after the arc.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def line(p1, p2, width=6):
    d.line([p1, p2], fill=INK, width=width)


def poly(points, width=6):
    d.line(points, fill=INK, width=width, joint="curve")


def bezier(p0, p1, p2, steps=40, width=6):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    poly(pts, width=width)


# ============== LEFT: 己 (approx cell x:40..135, y:80..230) ==============
# Stroke 1: 横折 — horizontal then down-right turn
#   start (48, 95) -> (128, 92) [横] -> (125, 145) [折 down]
poly([(48, 95), (128, 92), (125, 145)], width=6)

# Stroke 2: 横 (middle) — from left side to right side, connects into folder
poly([(50, 145), (120, 148)], width=6)

# Stroke 3: 竖弯钩 — down from left, curve to right, then flick up-left
#   Start (50, 145) down to (52, 205), arc to (130, 220), flick up-left
# down segment
poly([(50, 148), (52, 210)], width=6)
# arc segment (bezier)
bezier((52, 210), (72, 232), (135, 222), steps=30, width=6)
# hook flick — UP-and-LEFT
# terminal at (135, 222); flick to (128, 208)
poly([(135, 222), (128, 208)], width=7)


# ============== RIGHT: 攵 (approx cell x:150..282, y:70..245) ==============
# Stroke 1: 短撇 — short flick, top area
#   from (200, 80) down-left to (178, 108)
poly([(202, 78), (178, 108)], width=6)

# Stroke 2: 横 — horizontal, crosses middle-upper
#   from (168, 118) to (258, 115)
poly([(168, 118), (258, 115)], width=6)

# Stroke 3: 长撇 — long sweeping stroke from upper-right down to lower-left
#   start ~(225, 90), curve down-left to (155, 240)
bezier((225, 92), (200, 165), (152, 245), steps=40, width=7)

# Stroke 4: 捺 — from upper-mid diagonal down-right, thickening
#   start (195, 155), curve down-right to (275, 235)
bezier((195, 155), (235, 195), (278, 238), steps=40, width=7)


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0349_改/01_改.png")
print("saved")
