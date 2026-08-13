# BANK_DEVIATION
# skipped: (no bank entry for 讠 — TERMINAL errata; no bank entry for 隹)
# reason: 讠 left column inlined per 话/识/证 recipe (dot + 横折提, thin MMH).
#   Right column 隹 (8 strokes) has no bank primitive; inlined fresh:
#   撇 + 竖 (left stem) + 短撇 + 4 hengs + right 竖.
# fresh_component: yan_speech_inline_for_shui, zhui_bird_inline

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


# ---- LEFT: 讠 (yan, speech radical) — x ~ [20, 85] ----

# 1) 点 — small diagonal dab at top of column.
stroke((45, 80), (60, 100), w=8)

# 2) 横折提 — short heng, folds down as diagonal shu, then 提 up-right.
polyline([
    (32, 145),   # left start of short heng
    (78, 138),   # top-right corner
    (50, 220),   # descend down-left (讠 body slants left)
    (92, 205),   # 提 flick up
], w=5)


# ---- RIGHT: 隹 (zhui, short-tailed bird) — 8 strokes, x ~ [110, 285] ----
# Layout:
#   - Left stem: 撇 (top) + 竖 (below) — forms 亻-like left side.
#   - Right side: 短撇 top, then 4 hengs stacked, with rightmost 竖 crossing them.

# 3) 撇 (long, top-left) — starts high, slants down-left.
stroke((155, 60), (118, 135), w=6)

# 4) 竖 (left vertical) — continues down from base of 撇, stops at bottom heng.
stroke((140, 130), (140, 250), w=5)

# 5) 短撇 (short pie on upper-right column) — small slant, tops the right stack.
stroke((215, 95), (192, 122), w=5)

# 6) 横 (top heng, widest) — crosses through the right column near top.
stroke((162, 132), (282, 130), w=5)

# 7) 竖 (right vertical) — descender through 4 hengs, stops at bottom heng.
stroke((242, 122), (242, 250), w=5)

# 8) 横 (2nd heng from top).
stroke((162, 168), (278, 168), w=5)

# 9) 横 (3rd heng).
stroke((162, 208), (278, 208), w=5)

# 10) 横 (bottom heng, slightly wider).
stroke((140, 250), (285, 248), w=5)


out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_谁.png")
img.save(out)
print("wrote", out)
