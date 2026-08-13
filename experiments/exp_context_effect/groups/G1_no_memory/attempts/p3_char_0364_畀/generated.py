from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 5

# 畀 = 田 (top) + 丌 (bottom)
# Top 田: roughly rows 45..145, cols 95..205
L, R, T, B = 95, 205, 45, 145
MX = (L + R) // 2  # 150
MY = (T + B) // 2  # 95

# 田 strokes:
# 1) left vertical
d.line([(L, T), (L, B)], fill="black", width=LW)
# 2) top horizontal + right vertical (横折)
d.line([(L, T), (R, T)], fill="black", width=LW)
d.line([(R, T), (R, B)], fill="black", width=LW)
# 3) middle horizontal
d.line([(L, MY), (R, MY)], fill="black", width=LW)
# 4) middle vertical
d.line([(MX, T), (MX, B)], fill="black", width=LW)
# 5) bottom horizontal
d.line([(L, B), (R, B)], fill="black", width=LW)

# Bottom 丌:
# 6) long horizontal below 田
HY = 175
d.line([(50, HY), (250, HY)], fill="black", width=LW)
# 7) left down-stroke (short, slightly leftward)
d.line([(110, HY), (95, 265)], fill="black", width=LW)
# 8) right vertical (straight down)
d.line([(190, HY), (190, 265)], fill="black", width=LW)

out = os.path.join(os.path.dirname(__file__), "01_畀.png")
img.save(out)
print("saved", out)
