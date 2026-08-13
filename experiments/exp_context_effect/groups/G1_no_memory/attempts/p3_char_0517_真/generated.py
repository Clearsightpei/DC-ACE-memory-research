"""G1 render of 真 (zhen).
Structure (top→bottom):
  - short vertical at top (匕-like ten)
  - horizontal cross bar (top of 目)
  - 目 box with 3 internal horizontals
  - long horizontal underneath (base)
  - two short slanted feet (八)
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 5

def line(p1, p2, w=LW):
    d.line([p1, p2], fill="black", width=w)

# 1. Top short vertical (little tail on top)
line((150, 30), (150, 55))

# 2. Top horizontal (long) — spans wider than the 目 box
line((70, 65), (230, 65))

# 3. 目 box — under the top horizontal
BOX_L, BOX_R = 95, 205
BOX_T, BOX_B = 65, 175
# left vertical
line((BOX_L, BOX_T), (BOX_L, BOX_B))
# right vertical
line((BOX_R, BOX_T), (BOX_R, BOX_B))
# bottom of box
line((BOX_L, BOX_B), (BOX_R, BOX_B))
# 3 internal horizontals evenly spaced
h1 = BOX_T + (BOX_B - BOX_T) * 1 // 4
h2 = BOX_T + (BOX_B - BOX_T) * 2 // 4
h3 = BOX_T + (BOX_B - BOX_T) * 3 // 4
line((BOX_L + 6, h1), (BOX_R - 6, h1))
line((BOX_L + 6, h2), (BOX_R - 6, h2))
line((BOX_L + 6, h3), (BOX_R - 6, h3))

# 4. Long horizontal base (widest stroke)
line((45, 210), (255, 210))

# 5. Two feet (八 shape) below the base
# left foot: slants down-left
line((125, 220), (95, 265))
# right foot: slants down-right (捺-like)
line((170, 220), (215, 265))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0517_真/01_真.png")
