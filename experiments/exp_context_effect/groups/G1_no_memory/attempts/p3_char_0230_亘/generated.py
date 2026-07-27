"""Render 亘 (p3_char_0230) as 300x300 PNG."""
from PIL import Image, ImageDraw
from pathlib import Path

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
T = 6  # stroke thickness

def line(x0, y0, x1, y1, w=T):
    d.line([(x0, y0), (x1, y1)], fill=INK, width=w)

# 亘 = top 一 + 日 (middle) + bottom 一
# Layout:
#   Top horizontal ~ y=60, spanning x=45..255
#   Middle rectangle "日" from x=80..220, y=90..210
#   Middle inner horizontal at y=150
#   Bottom horizontal ~ y=245, spanning x=30..270

# 1. Top horizontal (slightly rising)
line(45, 65, 255, 55)

# 2. Left vertical of middle box
line(85, 95, 85, 210)

# 3. Top + right (horizontal-fold-vertical)
line(85, 95, 220, 92)
line(220, 92, 218, 210)

# 4. Inner middle horizontal
line(95, 150, 210, 148)

# 5. Bottom of middle box
line(85, 210, 220, 208)

# 6. Bottom horizontal (long, slight upward at end)
line(30, 250, 270, 240)

out = Path(__file__).parent / "01_亘.png"
img.save(out)
print(f"wrote {out}")
