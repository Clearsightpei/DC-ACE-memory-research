"""G1 render of 俾 (bǐ): 亻 (left) + 卑 (right)."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
T = 4  # stroke thickness


def line(pts, w=T):
    d.line(pts, fill=BLACK, width=w, joint="curve")


# =========================================================
# LEFT: 亻 (person radical)
# =========================================================
# 撇: starts upper right, curves down-left
line([(95, 65), (85, 95), (70, 130), (55, 175)])
# 竖: from middle of the 撇 straight down
line([(83, 100), (83, 245)])

# =========================================================
# RIGHT: 卑, occupying roughly x=120..270
# =========================================================
# Stroke 1: 撇 at very top (short diagonal from upper-right to left)
line([(210, 55), (195, 68), (175, 78)])

# Stroke 2: top horizontal (top of upper 田-like box)
line([(155, 80), (240, 78)])

# Stroke 3: left vertical of upper box
line([(155, 80), (155, 145)])

# Stroke 4: right vertical of upper box (turn from top horizontal)
line([(240, 78), (243, 145)])

# Stroke 5: middle horizontal inside upper box
line([(158, 112), (240, 110)])

# Stroke 6: bottom horizontal of upper box
line([(155, 145), (243, 145)])

# Stroke 7: small horizontal stub below upper box (the "十" horizontal of 卑's neck)
line([(175, 175), (223, 175)])

# Stroke 8: long wide horizontal near bottom (the 一 of 卑)
line([(120, 220), (280, 220)])

# Stroke 9: central long vertical from top down through bottom
line([(199, 60), (199, 275)])

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0562_俾/01_俾.png")
print("saved")
