from PIL import Image, ImageDraw
import os

OUT = os.path.join(os.path.dirname(__file__), "01_畐.png")

img = Image.new("RGB", (300, 300), "white")
d = ImageDraw.Draw(img)
W = 6  # stroke width

# Character 畐: 一 on top, then 口 (small box), then 田 (grid box)
# Rough vertical layout centered horizontally around x=150

# --- Top horizontal 一 ---
d.line([(90, 55), (215, 60)], fill="black", width=W)

# --- Middle 口 (small box) ---
# Left vertical
d.line([(115, 90), (110, 140)], fill="black", width=W)
# Top horizontal + right hook (横折)
d.line([(115, 90), (190, 92)], fill="black", width=W)
d.line([(190, 92), (188, 140)], fill="black", width=W)
# Bottom horizontal closing 口
d.line([(110, 140), (188, 140)], fill="black", width=W)

# --- Bottom 田 ---
# Left vertical
d.line([(85, 160), (82, 250)], fill="black", width=W)
# Top horizontal + right vertical (横折)
d.line([(85, 160), (215, 162)], fill="black", width=W)
d.line([(215, 162), (213, 250)], fill="black", width=W)
# Middle horizontal
d.line([(85, 205), (213, 205)], fill="black", width=W)
# Middle vertical
d.line([(148, 162), (148, 250)], fill="black", width=W)
# Bottom horizontal closing 田
d.line([(82, 250), (213, 250)], fill="black", width=W)

img.save(OUT)
print("saved", OUT)
