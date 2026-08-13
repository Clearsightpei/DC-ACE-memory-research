"""G1 render of 疫 (character p3_char_0450)."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def line(p1, p2, w=4):
    d.line([p1, p2], fill=BLACK, width=w)


def polyline(pts, w=4):
    for a, b in zip(pts[:-1], pts[1:]):
        d.line([a, b], fill=BLACK, width=w)


# ==== 疒 radical (outer sickness frame) ====
# 1. top dot
polyline([(118, 52), (128, 62)], w=5)

# 2. top horizontal (short, slightly tilted)
polyline([(90, 88), (200, 78)], w=5)

# 3. small left tick (short slant near top-left of frame)
polyline([(80, 118), (100, 108)], w=4)

# 4. long left-down slanted sweep (the long pie 撇)
polyline([(112, 88), (95, 140), (78, 190), (58, 250)], w=5)

# ==== 殳 inside (upper 几-like cap + 又 below) ====
# upper cap: small left tick
polyline([(150, 118), (168, 108)], w=4)

# upper cap: curved top (arc-like) into right drop
polyline([(140, 132), (170, 118), (205, 120), (218, 138), (216, 168)], w=5)

# upper cap: inner horizontal base
polyline([(148, 155), (205, 155)], w=4)

# 又 lower: left slanting pie 撇 from top-center down-left
polyline([(165, 175), (145, 210), (115, 260)], w=5)

# 又 lower: cross tick near top of 又
polyline([(155, 195), (200, 190)], w=4)

# 又 lower: right捺 (down-right flare)
polyline([(170, 200), (200, 230), (235, 260)], w=5)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_疫.png"))
print("saved 01_疫.png")
