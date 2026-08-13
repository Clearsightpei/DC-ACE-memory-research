"""Render 部 (bù) at 300x300, white bg, black ink."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# ==== LEFT COMPONENT: 咅 ====
# 立 top
# 1. top dot
line([(80, 40), (92, 58)], width=5)
# 2. top horizontal
line([(58, 70), (128, 70)], width=5)
# 3. left dot (下点)
line([(62, 90), (54, 110)], width=5)
# 4. right dot
line([(118, 90), (128, 110)], width=5)
# 5. bottom long horizontal of 立
line([(30, 132), (150, 132)], width=5)

# 口 (box) x=55..130, y=170..245
# left vertical
line([(58, 168), (58, 248)], width=5)
# top + right (single stroke: horizontal then down)
line([(58, 168), (132, 168), (132, 248)], width=5)
# bottom horizontal (closing)
line([(58, 248), (132, 248)], width=5)

# ==== RIGHT COMPONENT: 阝 (right ear) ====
# The ear is two smooth loops. Use many points to make smooth curves.
# Upper hump: starts at top, curves right-down-left back to middle
upper = [
    (188, 55),
    (210, 50), (232, 55), (245, 75),
    (248, 100), (238, 118), (215, 128),
    (195, 130),
]
line(upper, width=5)
# Lower hump: continues from middle out again
lower = [
    (195, 130),
    (220, 132), (240, 145), (245, 165),
    (240, 185), (220, 200), (195, 205),
]
line(lower, width=5)

# vertical descender (long, hooking slightly)
line([(198, 128), (198, 285)], width=5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0525_部/01_部.png")
print("done")
