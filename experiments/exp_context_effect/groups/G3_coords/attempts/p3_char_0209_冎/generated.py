"""p3_char_0209_冎 — direct PIL render.

冎 (gua): small top box (short 竖 + 横折) + inner short 竖 +
long middle 横 (with left-hook pie) + long 横折钩 down-right.
Bank primitives don't fit cleanly — inlining fresh per v8 guidance.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(a, b, w=6):
    d.line([a, b], fill="black", width=w)

def poly(pts, w=6):
    for i in range(len(pts) - 1):
        line(pts[i], pts[i+1], w)

# 1) top box left vertical (short 竖)
line((110, 85), (108, 140), 6)

# 2) top box: 横折 (top horizontal + right vertical)
poly([(110, 85), (195, 88), (192, 145)], 6)

# 3) inner short horizontal (bar inside the small box)
line((120, 115), (185, 117), 5)

# 4) long middle 横 (extends left of the box, forms base of top)
line((75, 165), (250, 160), 7)

# 5) 撇 dropping down-left from left of middle bar
poly([(105, 148), (85, 220), (75, 245)], 6)

# 6) 横折钩 (long stroke: horizontal from box, then hooks down-right)
poly([(195, 145), (255, 165), (245, 220), (225, 235)], 7)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0209_冎/01_冎.png")
print("saved")
