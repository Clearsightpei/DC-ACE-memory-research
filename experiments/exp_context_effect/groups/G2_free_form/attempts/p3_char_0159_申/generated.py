"""申 (shen) - 5 strokes.

Structure: 田 shape (rectangular box with cross) but with the central
vertical extended both above the top and below the bottom of the box.

Stroke order (MMH):
1. 竖 — left vertical of box
2. 横折 — top horizontal + right vertical of box (one stroke, one corner)
3. 横 — middle horizontal inside the box
4. 横 — bottom horizontal closing the box
5. 丨 — long central vertical, extends above top and below bottom

Silhouette: tall vertical spine, small-ish rectangular box centered
vertically. Aspect ratio: taller than wide.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 8  # line width for a bold brush look

# Box geometry — centered horizontally, in the vertical middle band.
# GT shows box slightly wider than tall and the top spine extension
# a bit longer than the bottom one.
box_left   = 85
box_right  = 215
box_top    = 110
box_bot    = 210
box_mid_y  = (box_top + box_bot) // 2   # 160
box_mid_x  = (box_left + box_right) // 2  # 150

# Central vertical extends further above the box than below (per GT).
spine_top = 40
spine_bot = 270

# Stroke 1: 竖 — left vertical of the box.
d.line([(box_left, box_top), (box_left, box_bot)], fill=INK, width=LW)

# Stroke 2: 横折 — top horizontal then down the right side (one stroke).
d.line([(box_left, box_top), (box_right, box_top)], fill=INK, width=LW)
d.line([(box_right, box_top), (box_right, box_bot)], fill=INK, width=LW)

# Stroke 3: 横 — middle horizontal inside the box.
d.line([(box_left, box_mid_y), (box_right, box_mid_y)], fill=INK, width=LW)

# Stroke 4: 横 — bottom horizontal closing the box.
d.line([(box_left, box_bot), (box_right, box_bot)], fill=INK, width=LW)

# Stroke 5: 丨 — long central vertical spine (through the middle,
# extending above and below the box).
d.line([(box_mid_x, spine_top), (box_mid_x, spine_bot)], fill=INK, width=LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0159_申/01_申.png")
