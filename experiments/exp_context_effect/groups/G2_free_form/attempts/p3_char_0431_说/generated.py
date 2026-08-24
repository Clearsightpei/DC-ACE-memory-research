"""
说 - "speak" (9 strokes) = 讠 (left, 2 strokes) + 兑 (right, 7 strokes)
Left ~33% width, right ~60% width.

讠: 点 + 横折提
兑: 丷 (top opens outward), 口 (small), 儿 (撇 + 竖弯钩)
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("L", (W, H), 255)
d = ImageDraw.Draw(img)

def line(pts, width=6):
    d.line(pts, fill=0, width=width, joint="curve")

def taper(x0, y0, x1, y1, w0=6, w1=3, steps=28):
    for i in range(steps):
        t = i / (steps - 1)
        cx = x0 + (x1 - x0) * t
        cy = y0 + (y1 - y0) * t
        r = (w0 * (1 - t) + w1 * t) / 2
        d.ellipse((cx-r, cy-r, cx+r, cy+r), fill=0)

# ==============================
# LEFT: 讠 (~x 30-90)
# ==============================
# Top dot (点) — slanting down-right
taper(55, 70, 68, 92, w0=3, w1=7)

# 横折提: short horizontal, drop-turn, upward flick
# short horizontal
line([(40, 130), (78, 130)], width=6)
# drop straight down (short)
line([(78, 130), (60, 175)], width=6)
# 提 - rising flick to the right
taper(48, 195, 92, 170, w0=8, w1=3)

# ==============================
# RIGHT: 兑 (~x 115-265)
# ==============================
# Top 丷: opens outward
# Left dot (撇 shape - short down-left flick)
taper(160, 70, 145, 95, w0=4, w1=7)
# Right dot (点 - down-right)
taper(215, 70, 228, 95, w0=3, w1=7)

# 口 (mouth) - small, centered under 丷, ~x 140-235, y 110-155
# Left vertical stroke
line([(148, 110), (148, 155)], width=6)
# Top + right (横折)
line([(147, 110), (232, 110), (232, 155)], width=6)
# Bottom (closing horizontal)
line([(148, 155), (232, 155)], width=6)

# 儿 bottom (spans wide)
# 撇: starts from left-under of 口, sweeps down-left with taper
taper(150, 158, 108, 265, w0=8, w1=3)

# 竖弯钩: from right-under of 口, straight down, curve right, hook up-left
# vertical portion
line([(228, 158), (225, 235)], width=7)
# smooth arc turning right
line([(225, 235), (240, 258), (270, 262)], width=7)
# hook up-and-left
taper(270, 262, 276, 232, w0=8, w1=3)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0431_说/01_说.png")
print("saved")
