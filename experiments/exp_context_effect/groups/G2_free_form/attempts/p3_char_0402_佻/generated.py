"""
佻 = 亻 (person radical, left) + 兆 (right body)

# SIGNATURE CHECK: (compound-only, no direct sibling row)
#   亻 = short 撇 + tall 竖 (per composition_rules 亻 + X).
#   兆 = mirrored pair of strokes flanking a central axis;
#        right half has 竖弯钩 with UP-and-LEFT hook.
#
# Left 亻: x=40-110, 撇 short then 竖 long.
# Right 兆 (x=120-280): 6 strokes
#   1. 撇 (upper-left of 兆)
#   2. 点 / short 竖 (below the 撇)
#   3. 提 (rising, inner-left, up toward center)
#   4. 竖弯钩 main right body: 竖 down then curl right + hook up-left
#   5. 撇 (upper-right slashing down-left across upper area)
#   6. 点 (mid-right small tick)
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
BR = 6

def stroke(points, width=BR):
    d.line(points, fill=INK, width=width, joint="curve")

# ---------- 亻 (left, x≈40-110) ----------
# 撇: (95, 55) -> (48, 138)
stroke([(95, 55), (80, 82), (63, 112), (48, 138)])
# 竖: (73, 120) -> (73, 250)
stroke([(73, 120), (73, 250)])

# ---------- 兆 (right, x≈130-275) ----------
# 1. upper-left 撇: (165, 80) -> (140, 140)
stroke([(165, 80), (156, 100), (148, 122), (140, 142)])

# 2. 点 just below the 撇 (short vertical-ish tick)
stroke([(132, 155), (128, 178)], width=BR + 1)

# 3. 提 rising from lower-left up toward center: (135, 220) -> (180, 190)
stroke([(133, 220), (155, 205), (180, 192)])

# 4. 竖弯钩 (right body): straight down then curl right then hook up-left
stroke([
    (215, 100), (215, 145), (215, 190), (218, 225),
    (228, 250), (250, 262), (270, 262),
])
# terminal hook up-and-left
stroke([(270, 262), (266, 250), (260, 242)])

# 5. upper-right 撇: (265, 90) -> (225, 165)
stroke([(265, 90), (252, 115), (238, 140), (225, 165)])

# 6. 点 mid-right tick
stroke([(258, 180), (270, 205)], width=BR + 1)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0402_佻/01_佻.png")
