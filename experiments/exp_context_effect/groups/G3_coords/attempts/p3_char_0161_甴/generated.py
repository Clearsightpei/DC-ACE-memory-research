# p3_char_0161_甴 — main attempt
# 甴 (cockroach char): looks like a box (口-family) with a vertical
# extension out of the top (like 由/甲) and one horizontal cross-bar
# inside splitting the box in half. From the GT PNG:
#   - top vertical protruding above the box (short)
#   - box: left竖 + top横折 + bottom横
#   - one internal horizontal splitting the box
# Simple PIL rendering — 4-5 strokes total. GT ink is thin uniform,
# per P12 use ~4-5 px width, not calligraphic.

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5  # thin uniform per MMH GT convention

# Box coordinates (canvas-px, origin top-left, y grows DOWN)
# Center the box slightly high on canvas to leave room for the top tick
box_left   = 70
box_right  = 230
box_top    = 110
box_bottom = 245

# Top protruding vertical (short tick above box top-center)
tick_x = 150
tick_top_y = 55
d.line([(tick_x, tick_top_y), (tick_x, box_top)], fill=INK, width=LW)

# Left 竖 (box left side)
d.line([(box_left, box_top), (box_left, box_bottom)], fill=INK, width=LW)

# Top 横 + right 竖 (heng-zhe) — drawn as two segments
d.line([(box_left, box_top), (box_right, box_top)], fill=INK, width=LW)
d.line([(box_right, box_top), (box_right, box_bottom)], fill=INK, width=LW)

# Bottom 横
d.line([(box_left, box_bottom), (box_right, box_bottom)], fill=INK, width=LW)

# Internal middle horizontal (splits the box roughly in half — closer to bottom
# actually per GT, the internal heng sits around 60% down)
mid_y = box_top + int((box_bottom - box_top) * 0.60)
d.line([(box_left, mid_y), (box_right, mid_y)], fill=INK, width=LW)

img.save("01_甴.png")
print("wrote 01_甴.png")
