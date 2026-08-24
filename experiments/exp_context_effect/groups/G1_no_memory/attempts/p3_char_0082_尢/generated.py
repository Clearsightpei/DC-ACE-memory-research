"""G1 render of 尢 (3 strokes: 横, 撇, 横折弯钩)."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 6

def line(pts, width=LW):
    d.line(pts, fill=INK, width=width, joint="curve")

# Stroke 1: short horizontal top-left
line([(65, 108), (150, 100)])

# Stroke 2: long 撇 — starts upper-right area, sweeps down-left
pts_pie = [
    (170, 70),
    (155, 105),
    (135, 145),
    (110, 195),
    (80, 240),
    (55, 270),
]
line(pts_pie)

# Stroke 3: 横折弯钩 — horizontal from left, turns down at right,
# curves along bottom, ends with small upward hook
pts_hzwg = [
    # horizontal
    (95, 150), (150, 148), (200, 146),
    # turn down (short vertical-ish)
    (202, 165), (203, 195), (208, 225),
    # curve right along bottom
    (220, 248), (240, 258), (258, 258),
]
line(pts_hzwg)
# hook up
line([(258, 258), (260, 235)])

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0082_尢/01_尢.png")
