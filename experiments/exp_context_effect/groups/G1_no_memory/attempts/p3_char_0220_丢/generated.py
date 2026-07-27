from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 5

# 丢 = 丿 (short falling) + 三-like (top short horiz, mid horiz, small vertical) + 厶 at bottom
# stroke order approx:
# 1. short 丿 near top (falling stroke on top)
# 2. short horizontal (top)
# 3. longer horizontal (middle)
# 4. short vertical descender
# 5. 厶 bottom (small 撇折 + 点)

# 1. Top short 丿 (falling stroke)
d.line([(155, 50), (110, 80)], fill="black", width=LW)

# 2. Top short horizontal
d.line([(95, 95), (180, 90)], fill="black", width=LW)

# 3. Middle horizontal (longest of upper part)
d.line([(80, 135), (210, 130)], fill="black", width=LW)

# 4. Vertical descender crossing the middle horizontal
d.line([(140, 95), (140, 165)], fill="black", width=LW)

# 5. Long horizontal (bottom horizontal, longest — this is actually part of 丢: the bottom of 云 style)
d.line([(50, 195), (255, 190)], fill="black", width=LW)

# 6. 厶 bottom-left: 撇折 (falls down-left then turns right)
# 撇 part
d.line([(140, 215), (110, 265)], fill="black", width=LW)
# 折 (bottom horizontal of 厶)
d.line([(110, 265), (175, 260)], fill="black", width=LW)

# 7. 点 top-right of 厶 (small dot/stroke)
d.line([(180, 235), (200, 265)], fill="black", width=LW)

out = os.path.join(os.path.dirname(__file__), "01_丢.png")
img.save(out)
print("saved", out)
