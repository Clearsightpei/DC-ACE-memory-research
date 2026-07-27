from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 4

# 册 - two vertical rectangle-like frames joined by a horizontal bar
# Left frame
# top-left short horizontal (top of left frame)
d.line([(60, 90), (135, 85)], fill=INK, width=LW)
# left vertical of left frame (curving down-left)
d.line([(65, 90), (55, 250)], fill=INK, width=LW)
# right vertical of left frame (drops down)
d.line([(133, 85), (128, 210)], fill=INK, width=LW)
# hook at bottom of left inner vertical (curves left)
d.line([(128, 210), (100, 245)], fill=INK, width=LW)

# Right frame
# top short horizontal
d.line([(150, 80), (235, 85)], fill=INK, width=LW)
# left vertical of right frame
d.line([(152, 80), (148, 210)], fill=INK, width=LW)
# hook at bottom of left inner vertical of right frame
d.line([(148, 210), (120, 245)], fill=INK, width=LW)
# right vertical of right frame (drops down and slight curve)
d.line([(233, 85), (245, 260)], fill=INK, width=LW)

# The middle horizontal bar crossing both frames
d.line([(45, 175), (255, 172)], fill=INK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_册.png")
img.save(out)
print("wrote", out)
