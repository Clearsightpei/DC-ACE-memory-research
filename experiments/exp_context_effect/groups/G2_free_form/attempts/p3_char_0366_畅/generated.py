"""畅 (chàng) — left-right compound: 申 (left) + 昜 (right, ~9 strokes total right).

Following GT observation:
- Left half (~1/3 canvas width): compressed 申 — narrow box with cross,
  central vertical extending above and below.
- Right half (~2/3 canvas width): 昜-like structure. GT shows:
    * top: short horizontal (~ or 日 collapsed)
    * middle-below: 勿-style wrap (横折钩 + interior 撇 x2)

Hook rule: 横折钩 flick UP-and-LEFT.

Reuses geometry from prior PASS 申 (p3_char_0159) and 勿 (p3_char_0145),
scaled/positioned for left-right composition.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(points, width=6):
    d.line(points, fill=BLACK, width=width, joint="curve")
    for (x, y) in [points[0], points[-1]]:
        r = width / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


def bezier(p0, p1, p2, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


LW = 6

# ============================================================
# LEFT HALF: 申 — compressed narrow, occupies x in [30, 120]
# ============================================================
box_left  = 45
box_right = 110
box_top   = 100
box_bot   = 210
box_mid_y = (box_top + box_bot) // 2
box_mid_x = (box_left + box_right) // 2

spine_top = 60
spine_bot = 250

# S1: left vertical
stroke([(box_left, box_top), (box_left, box_bot)], width=LW)
# S2: 横折 top+right
stroke([(box_left, box_top), (box_right, box_top)], width=LW)
stroke([(box_right, box_top), (box_right, box_bot)], width=LW)
# S3: middle horizontal
stroke([(box_left, box_mid_y), (box_right, box_mid_y)], width=LW)
# S4: bottom horizontal
stroke([(box_left, box_bot), (box_right, box_bot)], width=LW)
# S5: central spine
stroke([(box_mid_x, spine_top), (box_mid_x, spine_bot)], width=LW)

# ============================================================
# RIGHT HALF: 昜-like — occupies x in [140, 285]
# Top: a short horizontal (representing simplified top of 昜)
# Middle: another horizontal below
# Below: 勿-shape wrap
# ============================================================

# Top short horizontal (~ 一)
stroke([(155, 80), (275, 80)], width=LW)

# Second short horizontal below it (representing 曰/日 flattened to just a mark)
# From GT: there's a small horizontal around y~115 on the right side
stroke([(155, 118), (245, 118)], width=LW)

# Below that: 勿-shape wrap. Position anchored to right half.
# Shoulder 撇 (top-left short)
s_shoulder = bezier((180, 135), (168, 158), (150, 185))
stroke(s_shoulder, width=LW)

# 横折钩: top horizontal + long descending curve + hook up-left
stroke([(178, 155), (270, 148)], width=LW)
descend = bezier((270, 148), (265, 220), (215, 275))
stroke(descend, width=LW)
# hook flick UP-and-LEFT
stroke([(215, 275), (196, 258)], width=LW)

# Interior 撇 #1 (upper)
s_int1 = bezier((215, 175), (200, 200), (175, 230))
stroke(s_int1, width=LW)

# Interior 撇 #2 (lower, longer)
s_int2 = bezier((248, 195), (215, 240), (165, 285))
stroke(s_int2, width=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0366_畅/01_畅.png")
