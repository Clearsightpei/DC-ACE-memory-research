"""G1 render of 取 (qǔ) — ear (耳) + hand (又). Revision 1."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 4

def line(a, b, w=LW):
    d.line([a, b], fill="black", width=w)

# 耳 on left. GT shows a wide top horizontal, left vertical, two inner
# horizontals, a bottom horizontal that extends slightly left, and a
# long vertical drop from the right side.
# 1) top horizontal (slightly slanted up-right per GT)
line((40, 90), (155, 78))
# 2) left vertical
line((55, 85), (55, 215))
# 3) upper inner horizontal
line((70, 130), (140, 130))
# 4) lower inner horizontal
line((70, 165), (140, 165))
# 5) right vertical (short — becomes part of 耳's frame)
line((150, 80), (150, 200))
# 6) bottom long horizontal, extends a bit left of frame
line((35, 210), (155, 208))
# 7) long tail — the last stroke of 耳 drops vertically down from right
line((145, 208), (145, 285))

# 又 on right — two strokes crossing
# 1) 横撇: short horizontal top, then long curve sweeping down-left
line((175, 105), (255, 100))
line((255, 100), (180, 245))
# 2) 捺: from upper crossing point, sweep down-right to lower corner
line((200, 155), (285, 240))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0401_取/01_取.png")
