"""Render 改 (gǎi) to a 300x300 PNG. Left: 己 radical. Right: 攵 radical."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
T = 5


def poly(pts, w=T):
    d.line(pts, fill=INK, width=w, joint="curve")


# =========================================================
# LEFT SIDE — 己 (three strokes)
# ~x in [45, 140], y in [95, 215]
# =========================================================

# Stroke 1: 横折 (top horizontal then short down-turn)
poly([(48, 105), (135, 105), (135, 145)], w=T)

# Stroke 2: middle 横 (starts inside from left, meets stroke 1's down-turn)
poly([(55, 150), (135, 150)], w=T)

# Stroke 3: 竖弯钩 (start at same top-left as stroke 1 -> down -> sweep right -> hook up)
poly([(48, 108), (48, 210), (145, 210), (148, 190)], w=T)

# =========================================================
# RIGHT SIDE — 攵 (four strokes)
# ~x in [155, 280], y in [75, 265]
# =========================================================

# Stroke 1: short 撇 at top
poly([(200, 78), (182, 108)], w=T)

# Stroke 2: 横 slightly slanting up
poly([(168, 118), (245, 108)], w=T)

# Stroke 3: long 撇 (upper mid-right down to lower-left)
poly([(220, 95), (158, 262)], w=T)

# Stroke 4: 捺 (starts from middle of 撇, sweeps to lower-right)
poly([(192, 155), (278, 262)], w=T)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0349_改/01_改.png"
)
print("wrote PNG")
