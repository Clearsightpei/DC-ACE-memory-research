"""G1 render for 並 (p3_char_0360)."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

W = 4

def line(x1, y1, x2, y2, w=W):
    d.line([(x1, y1), (x2, y2)], fill="black", width=w)

# 並 = two 立 merged side-by-side, sharing a bottom horizontal.
# Strokes (approx 8):
#   1. left dot (short slant \)
#   2. right dot (short slant /)  -> 丷 on top
#   3. upper horizontal (short, spans both tops)
#   4. left vertical (from upper horizontal down)
#   5. right vertical (from upper horizontal down)
#   6. middle horizontal (short, connects the two verticals mid-way)
#   7. inner-left short vertical hook
#   8. inner-right short vertical hook
#   9. bottom long horizontal (widest)

# Top dots 丷 (left leans down-right, right leans down-left)
line(120, 55, 132, 92)
line(190, 55, 178, 92)

# Upper horizontal (short, roughly under the dots)
line(110, 108, 200, 105)

# Left vertical (from left end of upper horizontal, straight down through middle)
line(120, 108, 118, 240)

# Right vertical (from right end of upper horizontal, straight down)
line(195, 105, 200, 240)

# Middle horizontal (shorter, connects the two verticals about mid-body)
line(125, 170, 195, 168)

# Inner two short verticals (小-like, sitting between middle-h and bottom)
line(148, 175, 150, 235)
line(172, 175, 175, 235)

# Bottom long horizontal (widest — foundation stroke)
line(50, 258, 265, 252)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_並.png"))
print("saved")
