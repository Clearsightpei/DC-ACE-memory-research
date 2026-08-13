"""
转 = 车 (left radical) + 专 (right). 8 strokes total.
Revision: separated the two components (middle bar was spanning both — wrong),
and reshaped 专 as horizontal + horizontal + 竖折 + 竖弯钩 with hook flick UP-LEFT.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 6

def poly(points, w=LW):
    d.line(points, fill=INK, width=w, joint="curve")

# ---------------- LEFT: 车字旁 (left half x: 30-120) ----------------
# S1: top 横
poly([(38, 82), (118, 76)])
# S2: 竖折 inner (small vertical then horizontal)
poly([(58, 90), (58, 118), (108, 116)])
# S3: middle 横 (only within 车 area)
poly([(30, 148), (128, 145)])
# S4: 竖 with 提 (rising tick)
poly([(78, 55), (78, 250), (128, 220)])

# ---------------- RIGHT: 专 (right half x: 140-275) ----------------
# S1: top 横 (short)
poly([(170, 88), (245, 82)])
# S2: 横 middle-upper (longer)
poly([(150, 120), (275, 115)])
# S3: 竖折 shoulder — vertical stub then arm
poly([(200, 100), (200, 148), (255, 145)])
# S4: 竖弯钩 — sweeps down-left with hook flicking UP-LEFT at end
curve = [
    (250, 148),
    (245, 175),
    (232, 200),
    (210, 225),
    (180, 245),
    (155, 255),
    (140, 258),
    (128, 255),
    (122, 248),
    (120, 240),   # hook flicks UP-and-LEFT
]
poly(curve)

# 点 (small dot near top-right of 专)
d.ellipse([(238, 100), (250, 112)], fill=INK)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0415_转/01_转.png")
print("done")
