"""G1 render of 疹 (chen3 — rash). 300x300, PIL. Revision 2."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
LW = 4

def line(p0, p1, w=LW):
    d.line([p0, p1], fill=INK, width=w)

def curve(pts, w=LW):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill=INK, width=w)

# ===== Left: 疒 radical (occupies left half, descends full height) =====
# 1) top dot / short tick above horizontal
curve([(80, 40), (95, 60)])

# 2) horizontal stroke of 疒 (wide, slight upward tilt to right end)
line((45, 78), (175, 72))

# 3) long left-curving descender starting from left end of horizontal,
#    sweeping down and curving out to bottom-left
curve([(58, 78), (52, 120), (46, 160), (38, 200), (25, 245), (18, 275)])

# 4) two small interior strokes (short diagonals inside 疒)
curve([(70, 118), (90, 135)])   # upper
curve([(65, 155), (88, 175)])   # lower

# ===== Right: 㐱 =====
# 5) left diagonal of top ^
curve([(185, 55), (160, 90)])
# 6) right diagonal of top ^ + long extension to the right
curve([(185, 55), (210, 78), (260, 90), (285, 95)])

# 7-9) three 彡 strokes going down-right
curve([(150, 130), (170, 148), (200, 168)])
curve([(140, 165), (170, 190), (200, 210)])
curve([(130, 210), (165, 240), (195, 265)])

os.makedirs(os.path.dirname(__file__), exist_ok=True)
out = os.path.join(os.path.dirname(__file__), "01_疹.png")
img.save(out)
print(out)
