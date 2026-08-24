# p3_char_0367_事 — attempt 1
#
# 事 (shì, "matter") — 8 strokes. Layout (from GT):
#   1) short 一 at top
#   2) 横折 (heng+vertical) forming top-right of small 曰-like box
#   3) small 一 closing bottom of top box
#   4) long 一 middle (widest of the stack — belt)
#   5) short 一 above middle inside box
#   6) short 一 between middle and bottom
#   7) long 一 near bottom (second widest)
#   8) long 竖钩 spine through everything, hook flicks up-left at base
#
# Inline PIL render — the character's spine + belt geometry is uncommon;
# no bank primitive matches cleanly enough to justify a call. Widths kept
# in the 4-6 px band per drawer_memory.md's "trust GT thin lines" guidance.

from PIL import Image, ImageDraw

CANVAS = 300
BG = (255, 255, 255)
INK = (0, 0, 0)

img = Image.new("RGB", (CANVAS, CANVAS), BG)
t = ImageDraw.Draw(img)

W_THIN = 4
W_MED = 5
W_SPINE = 6


def h(y, x0, x1, w=W_MED):
    t.line([(x0, y), (x1, y)], fill=INK, width=w)


def v(x, y0, y1, w=W_MED):
    t.line([(x, y0), (x, y1)], fill=INK, width=w)


# Center-x of the character's spine
cx = 150

# Stroke 1 — top short 一 (across the top of the box)
h(70, 92, 210, W_MED)

# Stroke 2 — top box: right vertical (from top-right down to close box)
v(210, 70, 138, W_THIN)

# Stroke 3 — left short vertical (inside top box, forms 曰 left side)
v(105, 78, 140, W_THIN)

# Stroke 4 — bottom of the top box (small 一)
h(138, 105, 210, W_THIN)

# Stroke 5 — a small crossbar inside the box (曰 middle)
h(108, 108, 208, W_THIN)

# Stroke 6 — MIDDLE BELT (widest horizontal, spans full char)
h(178, 45, 258, W_MED)

# Stroke 7 — lower short heng (between belt and bottom)
h(210, 78, 224, W_THIN)

# Stroke 8 — bottom wide heng (second widest)
h(248, 55, 250, W_MED)

# Stroke 9 — long spine 竖钩 (from just above top box down through belt & bottom,
# hooking up-left at the bottom)
spine_x = 152
spine_top = 62
spine_bot = 268
t.line([(spine_x, spine_top), (spine_x, spine_bot)], fill=INK, width=W_SPINE)
# hook: from (spine_x, spine_bot) flick up-and-left, taper
hook_pts = [
    (spine_x, spine_bot),
    (spine_x - 8, spine_bot - 6),
    (spine_x - 18, spine_bot - 14),
    (spine_x - 28, spine_bot - 24),
]
for i in range(len(hook_pts) - 1):
    w = max(1, W_SPINE - i - 1)
    t.line([hook_pts[i], hook_pts[i + 1]], fill=INK, width=w)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0367_事/01_事.png")
