"""G1 render of 难 — left: 又, right: 隹."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

LW = 4

def line(pts, w=LW):
    d.line(pts, fill="black", width=w, joint="curve")

# ---------- Left: 又 (occupies ~x=25..130) ----------
# 横撇 top: short flat then diagonal down-left
line([(30, 110), (110, 115), (55, 220)], w=LW)
# 捺 diagonal down-right from junction
line([(70, 145), (140, 235)], w=LW)

# ---------- Right: 隹 (occupies ~x=150..280) ----------
# 亻 short diagonal (撇)
line([(175, 90), (160, 125)], w=LW)
# 亻 vertical
line([(170, 120), (170, 255)], w=LW)

# 丶 dot above right side
line([(215, 78), (225, 92)], w=6)

# Right vertical
line([(250, 115), (250, 245)], w=LW)

# Top horizontal (short, between top of 亻 diag and right vertical)
line([(185, 115), (250, 118)], w=LW)
# Second horizontal
line([(172, 150), (252, 148)], w=LW)
# Third horizontal
line([(172, 185), (253, 183)], w=LW)
# Bottom horizontal (base, long, extending both sides)
line([(150, 245), (275, 240)], w=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0545_难/01_难.png")
print("saved")
