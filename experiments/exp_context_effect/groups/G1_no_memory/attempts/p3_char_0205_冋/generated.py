from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6

# 冋 = outer 冂 + inner 口 (small, upper area)
# Outer 冂: top horizontal + left down + right down (with slight hook)
# Left vertical (starts a bit inside top-left, angled/tapered as brush)
d.line([(70, 70), (60, 260)], fill=BLACK, width=LW)
# Top horizontal
d.line([(70, 70), (235, 75)], fill=BLACK, width=LW)
# Right vertical + hook out to right at bottom
d.line([(235, 75), (240, 250)], fill=BLACK, width=LW)
d.line([(240, 250), (260, 270)], fill=BLACK, width=LW)

# Inner 口 (roughly in upper center)
# top horizontal
d.line([(110, 140), (200, 138)], fill=BLACK, width=LW)
# left vertical
d.line([(110, 140), (115, 200)], fill=BLACK, width=LW)
# right vertical
d.line([(200, 138), (198, 200)], fill=BLACK, width=LW)
# bottom horizontal
d.line([(115, 200), (198, 200)], fill=BLACK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_冋.png")
img.save(out)
print("saved", out)
