# BANK_DEVIATION
# skipped: (no bank entry for 讠 — TERMINAL errata; no bank entry for simplified 卖)
# reason: Reuse the 讠 inline recipe from p3_char_0389_话 (dot + 横折提).
#   For right column 卖, inline fresh (士 top + short heng + 冖 wide + 大-style 撇捺 + dot).
#   Thin MMH style, W=5. Revision-1: tightened proportions, moved 冖 to mid, narrowed 撇捺.
# fresh_component: mai_sell_inline_for_du

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


# ---- LEFT: 讠 (yan, speech radical) — compact, offset up ----
# Column x ~ [30, 95].

# 1) 点 — small diagonal dab at top of column.
stroke((45, 95), (60, 115), w=8)

# 2) 横折提 — short heng, folds down-left as diagonal shu, then 提 up-right.
polyline([
    (35, 150),
    (78, 143),
    (55, 215),
    (92, 200),
], w=5)


# ---- RIGHT: 卖 (mài, sell) — top 士 + short heng + 冖 + 大-style + inner dot ----
# Column x ~ [110, 270].

# Top 士 (short vertical/dot + top heng + shu + shorter bottom heng)
# 3) top heng of 士
stroke((160, 75), (232, 75), w=5)
# 4) shu (vertical through both hengs)
stroke((196, 60), (196, 118), w=5)
# 5) short bottom heng of 士
stroke((172, 118), (222, 118), w=5)

# 6) middle short heng (between 士 and 冖)
stroke((165, 148), (228, 148), w=5)

# 7) 冖 — wide heng cover, narrower than full column.
stroke((125, 175), (265, 175), w=5)

# 8) 撇 — down-left diagonal from just under 冖.
stroke((195, 190), (145, 275), w=6)

# 9) 捺 — down-right diagonal, meeting 撇 near top.
stroke((198, 192), (258, 275), w=6)

# 10) 丶 — small dot inside/right of the 撇捺, upper.
stroke((215, 210), (225, 225), w=7)


out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_读.png")
img.save(out)
print("wrote", out)
