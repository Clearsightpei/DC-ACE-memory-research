"""G1 draw 疸 = 疒 (illness radical) + 旦 inside."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p1, p2, w=4):
    d.line([p1, p2], fill="black", width=w)

def polyline(pts, w=4):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill="black", width=w)

# ---- 疒 radical ----
# 1) top dot (short slash) sitting above the horizontal
polyline([(115, 40), (135, 58)], w=5)

# 2) top horizontal stroke of 疒 (spans across top)
polyline([(70, 78), (240, 72)], w=5)

# 3) long left-falling stroke from left end of horizontal down to lower-left
polyline([(78, 80), (68, 130), (52, 190), (35, 265)], w=5)

# 4) two dots on the inside-left of 疒 (below horizontal, left of 旦)
polyline([(85, 120), (100, 138)], w=5)   # upper dot (dian toward lower-right)
polyline([(72, 160), (88, 178)], w=5)    # lower dot

# ---- 旦 inside (positioned in right pocket of 疒) ----
# 日 (rectangle with middle bar) - narrower to leave room, closer to top-right
L, R = 130, 232
T, B = 110, 195
MID = 155
# top
line((L, T), (R, T), w=4)
# right vertical
line((R, T), (R, B), w=4)
# left vertical
line((L, T), (L, B), w=4)
# middle horizontal
line((L, MID), (R, MID), w=4)
# bottom horizontal of 日
line((L, B), (R, B), w=4)

# 旦's bottom 一 (long horizontal below 日) — extends well past on both sides
line((105, 232), (270, 232), w=5)

out_path = os.path.join(os.path.dirname(__file__), "01_疸.png")
img.save(out_path)
print("wrote", out_path)
