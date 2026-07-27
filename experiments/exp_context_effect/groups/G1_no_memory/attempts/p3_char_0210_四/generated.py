"""G1 render of 四 (character). Simple rectangular frame with two inner strokes."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5

# Bounding box of the character (leave margins)
L, R = 55, 245
T, B = 80, 235

# 1) Left vertical (slight lean, like GT)
d.line([(L, T + 5), (L + 3, B)], fill=INK, width=LW)

# 2) Top horizontal + right vertical (one stroke: 横折)
d.line([(L - 3, T), (R, T + 8)], fill=INK, width=LW)
d.line([(R, T + 8), (R - 3, B)], fill=INK, width=LW)

# 3) Inner-left short vertical (人 left)
ix1 = L + 55
d.line([(ix1, T + 25), (ix1 - 5, B - 25)], fill=INK, width=LW)

# 4) Inner-right stroke (short 撇折 or vertical bend)
ix2 = R - 55
d.line([(ix2, T + 25), (ix2 - 3, B - 40)], fill=INK, width=LW)
# little foot bending right
d.line([(ix2 - 3, B - 40), (ix2 + 12, B - 30)], fill=INK, width=LW)

# 5) Bottom horizontal (closes the box)
d.line([(L - 2, B), (R + 2, B - 4)], fill=INK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_四.png")
img.save(out)
print(f"wrote {out}")
