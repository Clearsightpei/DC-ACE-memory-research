"""
仡 = 亻 (left) + 乞 (right)
Revision 1: cleaner continuous strokes, more pronounced hook flick UP-LEFT.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=7):
    d.line(pts, fill="black", width=width, joint="curve")
    # round caps at endpoints only
    x0, y0 = pts[0]; x1, y1 = pts[-1]
    d.ellipse((x0-width/2, y0-width/2, x0+width/2, y0+width/2), fill="black")
    d.ellipse((x1-width/2, y1-width/2, x1+width/2, y1+width/2), fill="black")

# ---- Left 亻 (occupies roughly x=60-120) ----
# 撇: top-right down to bottom-left
stroke([(105, 65), (98, 95), (88, 130), (75, 165)], width=7)
# 竖: from crook of 撇 straight down
stroke([(97, 105), (98, 175), (99, 245), (100, 275)], width=7)

# ---- Right 乞 (occupies roughly x=140-270) ----
# 短撇 top
stroke([(190, 65), (178, 85), (163, 105)], width=7)
# 横 middle (single smooth stroke)
stroke([(148, 135), (185, 133), (225, 132), (250, 130)], width=7)
# 横折弯钩: horizontal → sharp turn down → sweep across bottom → flick UP-LEFT
hzwg = [
    (150, 180), (190, 180), (230, 181), (252, 183),   # top horizontal
    (250, 205), (240, 225), (225, 245),               # turn & curve down-left
    (218, 260), (225, 270),                            # bottom curve
    (250, 273), (275, 270),                            # sweep to the right
    (263, 258), (255, 250),                            # flick UP-LEFT (hook)
]
stroke(hzwg, width=7)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0187_仡/01_仡.png")
