"""G1 render of 勹 (bao) — 2 strokes: 撇 + 横折钩."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5

# Stroke 1: 撇 (piě) — slanting fall from upper region down to left,
# ending at/near the start of the horizontal stroke.
d.line([(120, 65), (105, 95), (88, 125)], fill=INK, width=LW)

# Stroke 2: 横折钩 (héng zhé gōu)
# Horizontal segment: from ~(85, 128) rightward with a slight rise, to ~(215, 120).
# Then a smooth turn downward, curving to the left, ending near (160, 250).
# Finish with a small hook up-and-left.
horiz = [(80, 130), (120, 125), (170, 120), (210, 120)]
# Turn (折) point around (218, 125), then curve down-left
curve = [(218, 128), (222, 160), (218, 195), (205, 225), (180, 245), (162, 250)]
# 钩 (hook)
hook = [(162, 250), (148, 240)]

d.line(horiz + curve, fill=INK, width=LW)
d.line(hook, fill=INK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_勹.png")
img.save(out)
print("wrote", out)
