"""Render 丽 to 300x300 PNG."""
from PIL import Image, ImageDraw
from pathlib import Path

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 5

def line(p0, p1, w=LW):
    d.line([p0, p1], fill="black", width=w)

# Top horizontal 一 (slightly tilted, ends taper up)
line((45, 92), (255, 88), w=6)

# Left box (like 冂 with vertical stroke inside)
# Left box outer: top and left+bottom curve
# Top of left box
line((72, 130), (140, 130), w=5)
# Left vertical (slight lean)
line((72, 130), (68, 260), w=5)
# Right vertical of left box
line((140, 130), (140, 258), w=5)
# Small vertical stroke inside left box
line((105, 160), (103, 245), w=5)

# Right box
# Top
line((160, 130), (228, 130), w=5)
# Left vertical of right box
line((160, 130), (160, 258), w=5)
# Right vertical (with hook curl)
line((228, 130), (232, 260), w=5)
# Small vertical inside right box
line((193, 160), (191, 245), w=5)

out = Path(__file__).parent / "01_丽.png"
img.save(out)
print(f"saved {out}")
