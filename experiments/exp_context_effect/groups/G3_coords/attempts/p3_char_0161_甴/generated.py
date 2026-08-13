# p3_char_0161_甴 — 甴 (yóu, cockroach)
# Composition: 由-family — box with middle horizontal bar + central 竖
# that protrudes ABOVE the box and continues DOWN into the box (touching
# the middle bar), unlike 申 which extends both above and below.
# Refined from prior attempt: tick now enters the box (由 signature).
#
# Strokes (MMH-style order):
#   1. 竖 (central vertical: from above the box down to middle bar)
#   2. 竖 (left side of box)
#   3. 横折 (top + right of box)
#   4. 横 (middle bar inside)
#   5. 横 (bottom)

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5  # thin uniform per MMH GT convention (P12)

# Box coords (canvas-px, y grows DOWN)
box_left, box_right = 70, 230
box_top, box_bottom = 110, 245

# Middle bar ~60% down
mid_y = box_top + int((box_bottom - box_top) * 0.60)

# Stroke 1: central 竖 — starts above the box top, descends through the
# top edge and INTO the box, ending near / on the middle bar.
tick_x = 150
tick_top_y = 55
d.line([(tick_x, tick_top_y), (tick_x, mid_y - 2)], fill=INK, width=LW)

# Stroke 2: left 竖
d.line([(box_left, box_top), (box_left, box_bottom)], fill=INK, width=LW)

# Stroke 3: 横折 (top + right)
d.line([(box_left, box_top), (box_right, box_top)], fill=INK, width=LW)
d.line([(box_right, box_top), (box_right, box_bottom)], fill=INK, width=LW)

# Stroke 4: middle 横
d.line([(box_left, mid_y), (box_right, mid_y)], fill=INK, width=LW)

# Stroke 5: bottom 横
d.line([(box_left, box_bottom), (box_right, box_bottom)], fill=INK, width=LW)

img.save("01_甴.png")
print("wrote 01_甴.png")
