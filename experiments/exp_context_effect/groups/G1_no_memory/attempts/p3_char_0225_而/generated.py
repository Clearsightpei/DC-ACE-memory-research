from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 4

# 而: 6 strokes
# 1. top short horizontal (一)
d.line([(115, 70), (185, 70)], fill="black", width=LW)

# 2. long horizontal below it
d.line([(60, 115), (240, 115)], fill="black", width=LW)

# 3. left vertical curving to lower-left (leftmost downstroke of the frame)
d.line([(75, 115), (70, 230)], fill="black", width=LW)

# 4. inner-left short vertical
d.line([(115, 145), (115, 220)], fill="black", width=LW)

# 5. inner-right short vertical
d.line([(170, 145), (170, 220)], fill="black", width=LW)

# 6. right frame: vertical hook down then curve
d.line([(225, 115), (225, 210)], fill="black", width=LW)
# hook curving to the right/down
d.line([(225, 210), (240, 235)], fill="black", width=LW)

out = os.path.join(os.path.dirname(__file__), "01_而.png")
img.save(out)
print("saved", out)
