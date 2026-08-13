# BANK_DEVIATION
# skipped: (no bank entry for 讠 — TERMINAL errata; no direct 舌 bank entry —
#   she_char.py is 社, not 舌)
# reason: Left column 讠 (2 strokes) inlined fresh per prior 识/证 recipe.
#   Right column 舌 = 千-like top (pie + heng + shu) + 口 bottom (6 strokes
#   total). Inline fresh — kou.py exists but slotting it into 舌 requires
#   position/scale from GT anyway, so inline both halves consistently in
#   thin MMH style (P12, W=5).
# fresh_component: yan_speech_inline_for_hua, she_tongue_inline

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


# ---- LEFT: 讠 (yan, speech radical) ----
# Column occupies x ~ [20, 85]. Two strokes: dot + 横折提.

# 1) 点 — small diagonal dab at top of column, slanting down-right.
stroke((42, 80), (58, 100), w=8)

# 2) 横折提 — short heng, folds down-left as diagonal shu, then 提 up-right.
polyline([
    (30, 145),   # left start of the short heng
    (78, 138),   # top-right corner (heng slightly rising)
    (48, 220),   # descend down-left (讠 body slants left)
    (90, 205),   # 提 flick up to the right
], w=5)


# ---- RIGHT: 舌 (she, tongue) — 6 strokes ----
# Column occupies x ~ [110, 285]. Composition: 千-like top (3 strokes) + 口 bottom.

# 3) 撇 (pie) — short flick at top, from upper-right to lower-left.
stroke((215, 55), (175, 105), w=6)

# 4) 一 (long heng) — wide horizontal across the top of the character,
#    the widest stroke of 舌.
stroke((115, 118), (285, 115), w=5)

# 5) 丨 (shu) — vertical from just above the long heng, passing through it,
#    down to the top of 口.
stroke((198, 95), (198, 180), w=5)

# 6) 口 — mouth box, 3 strokes. Wider than tall, sits under the shu.
#    (a) left 竖:
stroke((155, 180), (155, 250), w=5)
#    (b) 横折 top + right vertical (single polyline):
polyline([(155, 180), (258, 180), (258, 250)], w=5)
#    (c) bottom 横:
stroke((155, 248), (260, 248), w=5)


out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_话.png")
img.save(out)
print("wrote", out)
