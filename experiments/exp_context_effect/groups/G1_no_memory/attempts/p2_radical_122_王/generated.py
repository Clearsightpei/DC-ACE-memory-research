"""G1 render for 王 (radical 122). PIL, 300x300, white bg, black ink."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
W_STROKE = 6

# 王 has 4 strokes: top horizontal, middle horizontal, vertical, bottom horizontal.
# GT shows a slightly narrower top, narrow middle, wider bottom, and a vertical spine.

# Top horizontal (略窄): from (~95, 95) to (~215, 92)
d.line([(95, 96), (215, 92)], fill=INK, width=W_STROKE)

# Middle horizontal (shortest): from (~110, 155) to (~195, 152)
d.line([(110, 156), (195, 152)], fill=INK, width=W_STROKE)

# Vertical spine: from (~150, 95) to (~150, 220)
d.line([(150, 95), (150, 220)], fill=INK, width=W_STROKE)

# Bottom horizontal (widest): from (~75, 222) to (~230, 218)
d.line([(75, 222), (230, 218)], fill=INK, width=W_STROKE)

out = os.path.join(os.path.dirname(__file__), "01_王.png")
img.save(out)
print("wrote", out)
