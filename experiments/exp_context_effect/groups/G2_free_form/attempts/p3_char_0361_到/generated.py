"""
到 = 至 (left, ~65% width) + 刂 (right, ~30% width)
至 has 6 strokes: 一 (top), 厶 (撇折+点), 土 (横竖横, bottom wider)
刂 has 2 strokes: 竖 (short, left) + 竖钩 (long, right, hook flicks UP-LEFT)

Hook flick rule from memory: 竖钩 terminal flicks UP-and-LEFT (~-100°).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
WIDE = 6
NARROW = 5


def line(pts, w=WIDE):
    d.line(pts, fill=INK, width=w, joint="curve")


# ============ LEFT SIDE: 至 (bounded ~x=40..185, y=45..255) ============

# Stroke 1: 一 (top horizontal, short)
line([(70, 65), (155, 68)], WIDE)

# Stroke 2 & 3: 厶 shape (撇折 + 点) — closed triangle under top 一
# 撇折: starts near top-center, goes down-left, then turns right along baseline
line([(120, 75), (80, 118), (135, 122)], WIDE)
# 点: short diagonal from upper-right down toward baseline meeting point
line([(140, 92), (150, 122)], WIDE)

# Stroke 4: 横 (middle horizontal of 土)
line([(75, 155), (165, 158)], WIDE)

# Stroke 5: 竖 (vertical of 土)
line([(118, 158), (118, 235)], WIDE)

# Stroke 6: 横 (bottom horizontal of 土, wider)
line([(55, 235), (185, 238)], WIDE + 1)


# ============ RIGHT SIDE: 刂 (bounded ~x=205..270, y=60..250) ============

# Stroke 7: 竖 (short vertical on left of 刂)
line([(215, 90), (215, 175)], WIDE)

# Stroke 8: 竖钩 (long vertical with hook flicking UP-LEFT)
line([(258, 65), (258, 235)], WIDE)
# hook: flick from bottom of 竖 up and to the LEFT
line([(258, 235), (238, 220)], WIDE)


img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0361_到/01_到.png"
)
print("saved 01_到.png")
