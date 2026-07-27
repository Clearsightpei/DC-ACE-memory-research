from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
TH = 5

# 与 (3 strokes):
# 1. 横折 - little down-tick then long horizontal to the right, then long slant down
# 2. 横 - short horizontal in the middle (slight slant)
# 3. 一 (bottom horizontal that extends wider) with hook going down at the right end
#
# Looking at GT: the top compound stroke goes down-right diagonal to the bottom-right,
# then a small hook. Bottom horizontal spans wider than top.

# Stroke 1: top compound - short vertical tick, then top horizontal, then down-slope, then hook down-left
s1 = [
    (110, 70),   # top of initial tick
    (105, 105),  # tick down
    (210, 95),   # top horizontal to right
    (225, 260),  # long down-right slope to bottom
    (200, 275),  # hook down-left
]
d.line(s1, fill=INK, width=TH, joint="curve")

# Stroke 2: middle short horizontal (slight downward slant)
s2 = [(125, 150), (200, 145)]
d.line(s2, fill=INK, width=TH, joint="curve")

# Stroke 3: bottom horizontal (spans wider, slightly slanted up-right)
s3 = [(55, 225), (210, 218)]
d.line(s3, fill=INK, width=TH, joint="curve")

out = os.path.join(os.path.dirname(__file__), "01_与.png")
img.save(out)
print("Saved", out)
