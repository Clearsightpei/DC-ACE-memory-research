"""Render 国 (guo) at 300x300, white background, black ink."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 4

# Outer enclosure (口) — slightly rustic, gaps at corners like handwritten
# Bounding box for outer square
L, T, R, B = 70, 55, 225, 250

# Top stroke (horizontal): left-to-right
d.line([(L, T), (R, T + 5)], fill=INK, width=LW)
# Left vertical (starts slightly above the top-left corner, downward)
d.line([(L - 2, T - 5), (L + 2, B)], fill=INK, width=LW)
# Right vertical + bottom (as one continuous 横折 shape, right side then bottom)
d.line([(R, T + 5), (R - 3, B)], fill=INK, width=LW)
# Bottom stroke
d.line([(L, B), (R, B - 3)], fill=INK, width=LW)

# Inner 玉 (jade): three horizontals + vertical + dot
# Positioned within the enclosure
ix1, ix2 = 105, 195   # inner horizontal extent
iy_top = 105
iy_mid = 155
iy_bot = 210

# Top horizontal (short)
d.line([(ix1 + 10, iy_top), (ix2 - 10, iy_top + 2)], fill=INK, width=LW)
# Middle horizontal (longest, slightly wider)
d.line([(ix1, iy_mid), (ix2, iy_mid + 2)], fill=INK, width=LW)
# Bottom horizontal
d.line([(ix1 + 5, iy_bot), (ix2 - 5, iy_bot - 2)], fill=INK, width=LW)
# Central vertical connecting top and bottom horizontals
cx = (ix1 + ix2) // 2
d.line([(cx, iy_top), (cx, iy_bot)], fill=INK, width=LW)
# Dot (点) to the lower right of the vertical
d.line([(cx + 20, iy_mid + 15), (cx + 30, iy_mid + 28)], fill=INK, width=LW + 1)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0363_国/01_国.png")
print("saved")
