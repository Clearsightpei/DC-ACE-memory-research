from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

ink = "black"
w = 6

# 丫: left diagonal stroke (top-left down to center-mid)
d.line([(95, 105), (150, 165)], fill=ink, width=w)

# right diagonal stroke (top-right down to center-mid)
d.line([(210, 100), (150, 165)], fill=ink, width=w)

# vertical stroke from junction down
d.line([(150, 165), (150, 265)], fill=ink, width=w)

out = os.path.join(os.path.dirname(__file__), "01_丫.png")
img.save(out)
print("wrote", out)
