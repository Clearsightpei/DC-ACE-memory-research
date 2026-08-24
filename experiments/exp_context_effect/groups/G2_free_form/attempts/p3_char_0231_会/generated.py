"""
Item: p3_char_0231_会 (huì) — 6 strokes
Structure: 人 (roof) + 一 + 厶
Strokes: 撇, 捺, 横, 撇折, 点

Revision 2: enlarge 厶, better 撇折 topology, roof strokes with clear
apex origin, 捺 with terminal thickening/flick.
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(pts, width=8):
    d.line(pts, fill=BLACK, width=width, joint="curve")


# 1) 撇 — left roof, apex (150, 38) sweeping down-left with slight bow
pie = []
for i in range(41):
    t = i / 40.0
    x = 150 - 100 * t - 6 * (t * (1 - t))
    y = 38 + 130 * t
    pie.append((x, y))
stroke(pie, width=8)

# 2) 捺 — right roof, from apex (150, 42) down-right, thickening tail
na = []
for i in range(41):
    t = i / 40.0
    x = 150 + 105 * t
    y = 42 + 128 * t + 6 * (t * (1 - t))
    na.append((x, y))
stroke(na, width=8)
# thickened terminal flick of 捺 (short kick right-down)
d.line([(248, 168), (268, 178)], fill=BLACK, width=11)
d.line([(258, 172), (272, 176)], fill=BLACK, width=9)

# 3) 横 — main horizontal under roof, spanning wider than roof base
stroke([(40, 195), (260, 192)], width=9)

# 4) 撇折 of 厶 — start at (130, 215) go down-left to (95, 260) then
#    turn right (折) to (170, 265). Larger, clearer topology.
zhe_pie = []
for i in range(21):
    t = i / 20.0
    x = 130 - 35 * t
    y = 215 + 45 * t
    zhe_pie.append((x, y))
stroke(zhe_pie, width=8)
stroke([(95, 260), (175, 268)], width=8)

# 5) 点 — dot at right side, inside/above the 厶 base line
d.polygon(
    [(195, 232), (218, 242), (210, 255), (192, 248)],
    fill=BLACK,
)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0231_会/01_会.png"
)
