"""G1 render of 伶 (líng). Left: 亻 (person radical). Right: 令."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")

# ---------- Left: 亻 (person radical) ----------
# Short slant (piě) top
stroke([(90, 75), (55, 145)], width=6)
# Vertical (shù) long
stroke([(80, 115), (80, 265)], width=6)

# ---------- Right: 令 ----------
# Top roof: 人 shape
# Left piě (long, curving)
stroke([(195, 55), (135, 145)], width=6)
# Right nà (long, straight-ish)
stroke([(195, 55), (260, 150)], width=6)

# Middle: short horizontal (representing 一 under roof)
stroke([(175, 160), (225, 160)], width=6)

# Bottom of 令: 丶 dot on left + 亅 hook on right (stylized as vertical with left hook)
# Small left dot/stroke
stroke([(170, 190), (185, 220)], width=7)
# Vertical hook - comes down center-right then hooks left at bottom
stroke([(215, 180), (215, 275)], width=6)
stroke([(215, 275), (190, 280)], width=6)

os.makedirs(os.path.dirname(__file__), exist_ok=True)
out = os.path.join(os.path.dirname(__file__), "01_伶.png")
img.save(out)
print(f"wrote {out}")
