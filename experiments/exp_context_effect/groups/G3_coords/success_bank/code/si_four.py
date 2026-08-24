# 四 (sì) — bank entry (B7 curator promotion, main PASS)
# Source: groups/G3_coords/attempts/p3_char_0210_四/generated.py
# Note: 5 (rect enclosure + 儿-like inner strokes)
# v8 signature freedom — this file preserves the drawer's original
# module-level script form; callable via `exec(open(...).read())` or
# copy the drawing block into a new function.

# p3_char_0210_四 — inline PIL rendering.
# 四 = 囗 enclosure + inner 儿-like (short 撇 + 竖弯 or similar) creating window feel.
# GT observation (300x300): rectangle spans ~55..245 horizontal, ~90..240 vertical.
# Inside: left inner stroke ~ slight pie from top toward bottom-left of interior;
# right inner stroke = short shu-like with hook curl at bottom.
# Simpler faithful rendering: rectangle box + two inner vertical strokes,
# left one a short pie, right one a shu that curls at the base.

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), (255, 255, 255))
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
w = 6

# Outer box: 囗-shape.
# Left vertical (shu):
d.line([(60, 92), (58, 240)], fill=INK, width=w)
# Top: heng — dispatched via heng_zhe: top + right vertical.
d.line([(58, 92), (245, 88)], fill=INK, width=w)
d.line([(245, 88), (243, 240)], fill=INK, width=w)
# Bottom heng closing the box.
d.line([(58, 240), (245, 240)], fill=INK, width=w)

# Inner strokes forming 儿-like inside.
# Left inner: short pie going from top inside slightly leftward-down.
d.line([(115, 120), (105, 210)], fill=INK, width=w)
# Right inner: short shu going down then a small curl right (蒸-ish).
d.line([(175, 120), (178, 195)], fill=INK, width=w)
# small hook curl at right inner stroke's bottom
d.line([(178, 195), (198, 205)], fill=INK, width=w)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0210_四/01_四.png")
