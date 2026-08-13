"""G1 render of 疔 (dīng) — 疒 radical + 丁."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5

def line(p0, p1, w=LW):
    d.line([p0, p1], fill=BLACK, width=w)

def curve(points, w=LW):
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill=BLACK, width=w)

# --- 疒 radical ---
# 1) Top dot — small slanted mark, upper-left area
line((110, 50), (125, 65))

# 2) Main horizontal — from left(~85) to right(~245), around y=90
line((85, 90), (245, 90))

# 3) Left-falling long stroke — from horizontal's left end, curving down-left
curve([(85, 90), (68, 135), (52, 185), (42, 235)])

# 4) Two dots on the left interior (冫-like, to the right of the diagonal)
# upper dot — small slanted mark
line((90, 130), (105, 148))
# lower dot — small slanted mark, lower and slightly right
line((78, 175), (95, 193))

# --- 丁 (inside, right portion under horizontal) ---
# 5) Horizontal of 丁
line((130, 155), (240, 155))

# 6) Vertical with small hook at bottom
curve([(190, 155), (190, 255), (180, 260)])

out = os.path.join(os.path.dirname(__file__), "01_疔.png")
img.save(out)
print("wrote", out)
