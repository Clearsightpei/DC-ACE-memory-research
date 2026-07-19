"""G1 render of radical 乙 (1画: 横折弯钩). Revised pass — larger, smoother arc."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 7

# 乙 = one continuous stroke: horizontal → turn → curved sweep down-left →
# long horizontal along bottom → small upward hook at right.
# Sized to fill the frame like the GT.
path = [
    # top opening — slight upward-arching horizontal
    (90, 105),
    (110, 98),
    (135, 95),
    (160, 97),
    (180, 105),
    # turn (折) — corner rolling down
    (188, 118),
    (185, 135),
    # diagonal sweep down-left
    (170, 155),
    (150, 178),
    (125, 200),
    (105, 220),
    # bottom curve
    (95, 235),
    (100, 248),
    # long horizontal along the bottom
    (125, 253),
    (160, 254),
    (195, 252),
    (218, 248),
    (230, 240),
    # hook up on the right
    (232, 225),
    (230, 210),
    (225, 200),
]

draw.line(path, fill=INK, width=LW, joint="curve")

# Rounded end caps
r = LW // 2
for (x, y) in [path[0], path[-1]]:
    draw.ellipse([x - r, y - r, x + r, y + r], fill=INK)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_006_乙/01_乙.png"
img.save(out)
print(out)
