"""G1 render for p3_char_0372_疌 (revision).

疌 = 聿-like top (three horizontals + vertical spine) stacked over 疋-like bottom.
"""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 3

def line(x1, y1, x2, y2, w=LW):
    d.line([(x1, y1), (x2, y2)], fill=BLACK, width=w)

def poly(pts, w=LW):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=BLACK, width=w)

# ===== TOP: 聿 -like component (occupies y ~ 45..170) =====
# Central vertical spine (extending slightly down past bottom horizontal)
line(150, 55, 150, 175, LW)

# Three horizontals inside a rectangular frame + one long crossbar
# Top horizontal (short)
line(110, 70, 190, 68, LW)
# Right descending side (short)
line(190, 68, 190, 130, LW)
# Middle horizontal
line(110, 100, 190, 98, LW)
# Third horizontal (inner)
line(110, 130, 190, 128, LW)
# Long crossbar (spans wider)
line(80, 160, 220, 158, LW)

# ===== BOTTOM: 疋-like component (occupies y ~ 170..270) =====
# Small horizontal top of 疋
line(125, 185, 175, 183, LW)
# Central short vertical
line(150, 175, 150, 220, LW)
# Left downward piě (long slant to lower-left)
poly([(140, 210), (110, 240), (85, 275)], LW)
# Right small vertical / hook
line(175, 205, 175, 235, LW)
# Bottom horizontal sweep (long na base)
poly([(150, 235), (185, 260), (240, 268)], LW)

# Save
out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_疌.png"))
print("wrote", os.path.join(out_dir, "01_疌.png"))
