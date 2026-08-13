"""Render 神 (shen) at 300x300, black on white."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 4

def line(pts, w=LW):
    d.line(pts, fill=INK, width=w)

# 神 = 礻(left radical) + 申(right)
# Left radical 礻 (approx cols 40..115)
# Stroke 1: dot (点) top
line([(70, 55), (85, 75)], w=5)
# Stroke 2: horizontal (short 横 / actually a slant into hook) - top curve
line([(55, 100), (110, 90)])
# Stroke 3: vertical descender (long, slight curve)
line([(90, 90), (85, 250)])
# Stroke 4: left downward stroke (撇) crossing the vertical
line([(90, 140), (45, 260)])
# Stroke 5: right dot on radical
line([(90, 155), (115, 175)], w=5)

# Right component 申 (approx cols 140..260)
# Top short vertical (top of 田/申)
# Left vertical of the box
line([(160, 90), (160, 230)])
# Top horizontal
line([(160, 90), (250, 95)])
# Right vertical
line([(250, 95), (250, 230)])
# Bottom horizontal
line([(160, 230), (250, 230)])
# Middle horizontal (inside the box)
line([(160, 160), (250, 160)])
# Central long vertical extending above and below
line([(205, 55), (205, 285)])

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0463_神/01_神.png")
