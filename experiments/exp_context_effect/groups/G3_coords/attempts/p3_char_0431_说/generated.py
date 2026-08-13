# BANK_DEVIATION
# skipped: (no bank entry for 讠 — 讠 was TERMINAL errata; no bank entry
#   for 兑 — dui_char.py in bank is 对 (you+cun), pinyin collision only)
# reason: 说 = 讠 (2 strokes, inline per prior 话 recipe) + 兑 (7 strokes:
#   丷 splayed dots + 口 + 儿). No composite primitive fits; kou.py exists
#   but its scale/position for 兑's middle-third slot needs derivation
#   anyway, so inline the whole right column consistently in thin MMH
#   style (P12, W=5).
# fresh_component: yan_speech_inline (reused from 话), dui_inline_for_shuo

import os
from PIL import Image, ImageDraw

CANVAS = 300
W = 5
BLACK = (0, 0, 0)

img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
d = ImageDraw.Draw(img)


def stroke(p0, p1, w=W):
    d.line([p0, p1], fill=BLACK, width=w)
    r = w / 2
    for (x, y) in (p0, p1):
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


def polyline(pts, w=W):
    for i in range(len(pts) - 1):
        stroke(pts[i], pts[i + 1], w=w)


# =========================================================================
# LEFT: 讠 (yan, speech radical) — 2 strokes, column x ~ [15, 90]
# =========================================================================

# 1) 点 — small diagonal dab, top of left column, slanting down-right.
stroke((42, 78), (58, 100), w=8)

# 2) 横折提 — short heng, folds down-left as diagonal shu, ends in 提 flick.
polyline([
    (30, 148),   # left start of the short heng
    (78, 140),   # top-right corner (heng rising slightly)
    (48, 222),   # descend down-left (讠 body slants left)
    (90, 208),   # 提 flick up to the right
], w=5)


# =========================================================================
# RIGHT: 兑 (dui) — 7 strokes, column x ~ [110, 290]
# Composition: 丷 (2 splayed dots) + 口 (mouth box, 3 strokes) + 儿 (撇 + 竖弯钩)
# =========================================================================

# --- 丷 top (2 splayed dots) ---
# 3) Left dot (撇点) — starts upper-right, sweeps down-left.
stroke((165, 55), (140, 88), w=7)

# 4) Right dot (点) — starts upper-left, sweeps down-right.
stroke((240, 55), (265, 88), w=7)

# --- 口 middle (mouth box, 3 strokes) — sits x=[155, 245], y=[105, 175] ---
# 5) Left 竖:
stroke((155, 105), (155, 175), w=5)
# 6) 横折 (top heng + right vertical, one motion):
polyline([(155, 105), (250, 105), (250, 178)], w=5)
# 7) Bottom 横 (封口):
stroke((158, 175), (250, 175), w=5)

# --- 儿 bottom (撇 + 竖弯钩) — spans x=[130, 290], y=[175, 265] ---
# 8) 撇 — starts at left edge of mouth-box bottom, sweeps down-left.
polyline([(175, 175), (162, 210), (135, 265)], w=6)

# 9) 竖弯钩 — starts at right side of mouth-box bottom, drops vertically,
#    curves right along baseline, hooks up at the end.
polyline([
    (215, 175),
    (215, 235),
    (225, 258),
    (250, 268),
    (278, 260),
    (285, 240),   # hook tick upward
], w=6)


out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_说.png")
img.save(out)
print("wrote", out)
