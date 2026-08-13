from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 5

def line(x1, y1, x2, y2, w=LW):
    d.line([(x1, y1), (x2, y2)], fill="black", width=w)

# 果 = 田 (top) + 木 (bottom)
# Top 田: rectangle with cross
# rectangle roughly x 90..210, y 45..165
L, R, T, B = 90, 210, 45, 165
# Top horizontal
line(L, T, R, T)
# Left vertical (slight lean)
line(L, T, L - 5, B)
# Right vertical (slanted piegou)
line(R, T, R + 5, B)
# Bottom of 田
line(L - 5, B, R + 5, B)
# Vertical middle
line((L + R) // 2, T, (L + R) // 2, B)
# Horizontal middle
line(L - 2, (T + B) // 2, R + 2, (T + B) // 2)

# 木 bottom:
# Long horizontal across the character
line(30, 180, 270, 180)
# Vertical stem
line(150, 155, 150, 285)
# Left downstroke (撇)
for i in range(6):
    d.line([(145 - i*0.5, 195 + i*2), (60 + i, 275 - i*0.5)], fill="black", width=LW)
# Right downstroke (捺)
for i in range(6):
    d.line([(155 + i*0.5, 195 + i*2), (250 - i, 275 - i*0.5)], fill="black", width=LW)

out = os.path.join(os.path.dirname(__file__), "01_果.png")
img.save(out)
print(out)
