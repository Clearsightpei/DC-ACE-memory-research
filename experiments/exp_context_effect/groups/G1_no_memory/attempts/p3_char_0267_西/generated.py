"""Render 西 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)
INK = "black"
LW = 4

# 西 (6 strokes):
# 1. 一   top short horizontal
# 2. 丨   left vertical of the outer frame
# 3. 横折 top of frame + right vertical (with a small hook at bottom)
# 4. ノ   inner-left short slanted stroke
# 5. 乚   inner-right curved stroke ending in hook
# 6. 一   bottom horizontal closing the frame

# Outer frame bounds
L, R = 60, 240
FRAME_TOP = 100   # top of the rectangular frame (below stroke 1)
B = 250           # bottom of frame

# Stroke 1: top horizontal (a bit wider than frame)
draw.line([(L - 10, 80), (R + 10, 80)], fill=INK, width=LW)

# Stroke 2: left vertical (starts near frame top, extends to bottom)
draw.line([(L, FRAME_TOP - 5), (L, B)], fill=INK, width=LW)

# Stroke 3: 横折 — horizontal top of frame + right vertical
draw.line([(L - 2, FRAME_TOP), (R, FRAME_TOP)], fill=INK, width=LW)
draw.line([(R, FRAME_TOP), (R, B)], fill=INK, width=LW)

# Inside the frame — two short strokes like 儿 sitting near the top
INNER_TOP = FRAME_TOP + 20
INNER_BOT = B - 40  # they don't reach the bottom line

# Stroke 4: inner left — slight slant left (ノ short)
draw.line([(L + 55, INNER_TOP), (L + 45, INNER_BOT)], fill=INK, width=LW)

# Stroke 5: inner right — vertical then hook left at bottom (乚)
draw.line([(R - 55, INNER_TOP), (R - 55, INNER_BOT - 5)], fill=INK, width=LW)
draw.line([(R - 55, INNER_BOT - 5), (R - 70, INNER_BOT)], fill=INK, width=LW)

# Stroke 6: bottom horizontal (closes the frame)
draw.line([(L, B), (R, B)], fill=INK, width=LW)

out = __file__.rsplit("/", 1)[0] + "/01_西.png"
img.save(out)
print("saved", out)
