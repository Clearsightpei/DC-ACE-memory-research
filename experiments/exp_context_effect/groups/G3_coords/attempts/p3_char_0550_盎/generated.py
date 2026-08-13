# BANK_DEVIATION
# skipped: ang_char.py (that entry is for 卬, a different character, not composable)
# reason: 盎 = 央 (top) + 皿 (bottom); no bank primitive for 央, and min_dish.py
#         is a module-level script that renders at full canvas — needs
#         compression to bottom half. Inlining both fresh.
# fresh_component: yang_top_for_stack (央 compressed to top half),
#                  min_dish_bottom_stack (皿 compressed to bottom band)

"""
盎 (àng) — top-bottom compound: 央 + 皿
Approx 10 strokes total.

Layout: 央 occupies y ~30..175 (top ~50%),
        皿 occupies y ~185..280 (bottom ~35%).
"""
import os
from PIL import Image, ImageDraw

W, H = 300, 300
INK = (0, 0, 0)
LW = 5

img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def line(pts, w=LW):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=INK, width=w)


def bez(p0, p1, p2, steps=24):
    out = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        out.append((x, y))
    return out


# ===== TOP: 央 (yang) =====
# Structure: 冂-like frame at top, middle heng, then 大 (heng + pie + na)
# Actually 央 stroke order:
#  1. 竖 short vertical on left (from top going down)
#  2. 横折 top-right corner (long horizontal, then down)
#  3. 横 middle horizontal (crossing both verticals)
#  4. 撇 from top-center going down-left
#  5. 捺 from top-center going down-right

# --- Stroke 1: left 竖 (short vertical) ---
# tighter frame
line([(115, 55), (115, 110)])

# --- Stroke 2: 横折 top-right corner ---
line([(115, 55), (195, 52)])
line([(195, 52), (193, 110)])

# --- Stroke 3: middle 横 (crossing both, wider than the frame) ---
line([(80, 110), (225, 108)], w=LW)

# --- Stroke 4: 撇 (from top-center curving down-left, contained) ---
# starts ~(155, 65), ends at (70, 175) — stops above 皿
pie = bez((155, 65), (120, 130), (70, 175), 28)
line(pie)

# --- Stroke 5: 捺 (from top-center going down-right, contained) ---
na = bez((155, 65), (190, 130), (235, 175), 28)
line(na)


# ===== BOTTOM: 皿 (min dish) =====
# Compressed to y ~185..275
# Structure:
#  1. left 竖 (slightly slanted inward)
#  2. first inner 竖
#  3. second inner 竖
#  4. 横折 top-right corner
#  5. long bottom 横

TOP_Y = 190      # top of the box
BOT_Y = 260      # bottom of interior verticals
BASE_Y = 275     # long base horizontal
LEFT_X = 75
RIGHT_X = 225

# Stroke 1: left vertical (slanted inward slightly)
line([(LEFT_X, TOP_Y + 5), (LEFT_X + 8, BOT_Y)])

# Stroke 2: first inner short vertical
line([(120, TOP_Y + 12), (122, BOT_Y)])

# Stroke 3: second inner short vertical
line([(170, TOP_Y + 12), (170, BOT_Y)])

# Stroke 4: 横折 top-right (short horizontal + vertical down)
line([(105, TOP_Y + 5), (RIGHT_X, TOP_Y + 5)])
line([(RIGHT_X, TOP_Y + 5), (RIGHT_X - 8, BOT_Y)])

# Stroke 5: long bottom horizontal (extends beyond box)
line([(40, BASE_Y), (270, BASE_Y - 2)], w=LW + 1)


OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_盎.png")
img.save(OUT)
print(f"Wrote {OUT}")
