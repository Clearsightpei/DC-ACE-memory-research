"""G1 render for 主 (5 strokes: dot, short heng, vertical, medium heng, long heng)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
T = 6  # stroke thickness

# 1) Top dot (点) - short diagonal from upper-left to lower-right, around top-center
d.line([(148, 40), (162, 60)], fill=INK, width=T)

# 2) Short top heng (短横) - just below dot
d.line([(110, 90), (195, 88)], fill=INK, width=T)

# 3) Medium middle heng (中横)
d.line([(90, 155), (215, 152)], fill=INK, width=T)

# 4) Vertical (竖) - through the two upper hengs down to the bottom heng
d.line([(152, 90), (152, 235)], fill=INK, width=T)

# 5) Long bottom heng (长横) - widest, slight upward curve at ends
d.line([(55, 238), (250, 235)], fill=INK, width=T)

out = os.path.join(os.path.dirname(__file__), "01_主.png")
img.save(out)
print(f"wrote {out}")
