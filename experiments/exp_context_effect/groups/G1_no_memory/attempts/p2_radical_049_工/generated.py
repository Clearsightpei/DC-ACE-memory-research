"""G1 render of 工 (radical). 300x300 PNG."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
TH = 7  # stroke thickness

# Based on GT: top horizontal (short), middle vertical, bottom horizontal (wider)
# Top horizontal — around y=105, from x=95 to x=205
d.line([(95, 108), (205, 100)], fill=INK, width=TH)

# Middle vertical — from just under top horizontal to just above bottom horizontal
d.line([(150, 108), (148, 215)], fill=INK, width=TH)

# Bottom horizontal — wider, slightly wavy, around y=225
d.line([(60, 230), (240, 225)], fill=INK, width=TH)

out_path = os.path.join(os.path.dirname(__file__), "01_工.png")
img.save(out_path)
print(f"Wrote {out_path}")
