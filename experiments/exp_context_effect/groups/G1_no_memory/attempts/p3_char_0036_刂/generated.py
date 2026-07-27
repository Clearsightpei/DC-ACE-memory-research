from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5

# Left short vertical stroke (短竖) - starts high with slight top tick, goes down
# GT shows a small tick then a vertical
d.line([(120, 105), (130, 120)], fill=INK, width=LW)  # small top tick
d.line([(130, 120), (128, 195)], fill=INK, width=LW)  # short vertical

# Right vertical + long hook (竖钩)
# Long vertical from higher up
d.line([(200, 80), (200, 245)], fill=INK, width=LW)
# Hook at the bottom - going left more significantly
d.line([(200, 245), (160, 240)], fill=INK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_刂.png")
img.save(out)
print(out)
