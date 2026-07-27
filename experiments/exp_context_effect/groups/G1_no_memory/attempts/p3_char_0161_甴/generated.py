"""G1 render of 甴 — a rectangular frame with a horizontal midline,
plus a short vertical stroke sticking up from the top edge.
300x300 PNG, white background, black ink."""

from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 5  # stroke thickness

# Frame rectangle (the 日-like body, sits in lower ~65% of canvas)
left, right = 70, 230
top, bottom = 110, 265

# 1) Top vertical stroke (sticking up from top of frame)
#    From the top-center of the frame going upward
cx = (left + right) // 2
d.line([(cx, 50), (cx, top)], fill=INK, width=LW)

# 2) Frame — left vertical (竖)
d.line([(left, top), (left, bottom)], fill=INK, width=LW)

# 3) Frame — top horizontal + right vertical done as 横折 (single stroke)
d.line([(left, top), (right, top)], fill=INK, width=LW)
d.line([(right, top), (right, bottom)], fill=INK, width=LW)

# 4) Middle horizontal
mid_y = (top + bottom) // 2 + 10
d.line([(left, mid_y), (right, mid_y)], fill=INK, width=LW)

# 5) Bottom horizontal (closes the frame)
d.line([(left, bottom), (right, bottom)], fill=INK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_甴.png")
img.save(out)
print("Wrote", out)
