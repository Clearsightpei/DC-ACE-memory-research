"""
p3_char_0363_国 — G2 render.

国 = enclosure 囗 + 玉 inside.
Structure:
  - Outer 囗: 竖 (left), 横折 (top+right), 横 (bottom closing)
  - Inside 玉:
      - top 横 (short)
      - middle 横 (short)
      - 竖 (connects top and bottom horizontals)
      - bottom 横 (a bit longer than upper two)
      - 点 (dot) at lower-right of 玉

No hooks in 国 — the 横折 is a plain corner, no hook flick.
Aspect: 国 is a slightly-tall square-ish enclosure.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
BW = 6  # brush width — clean visible strokes at 300x300

# ---- outer 囗 (enclosure) ----
# The GT shows the box occupying roughly x:60..230, y:40..255
L, R = 60, 230
T, B = 40, 255

# left 竖: slight lean inward at top of GT — draw straight vertical
d.line([(L, T + 5), (L - 2, B)], fill=INK, width=BW)

# top+right 横折 (one continuous stroke: horizontal then down):
# top horizontal from just above-left of L to R, then folds down to B
d.line([(L - 4, T), (R, T + 4)], fill=INK, width=BW)   # top 横
d.line([(R, T + 2), (R + 2, B - 5)], fill=INK, width=BW)  # right 竖 (folded)

# bottom 横 closes the box
d.line([(L - 4, B), (R + 4, B - 2)], fill=INK, width=BW)

# ---- inner 玉 ----
# 玉 sits inside the box. Approx bounds x:100..190, y:90..220
ix1, ix2 = 100, 190
iy_top, iy_mid, iy_bot = 100, 155, 210

# top 横 (short-ish)
d.line([(ix1 + 5, iy_top), (ix2 - 5, iy_top + 2)], fill=INK, width=BW)

# middle 横 (short)
d.line([(ix1 + 8, iy_mid), (ix2 - 8, iy_mid + 1)], fill=INK, width=BW)

# 竖 (central vertical connecting top -> bottom rows)
cx = (ix1 + ix2) // 2
d.line([(cx, iy_top - 2), (cx, iy_bot)], fill=INK, width=BW)

# bottom 横 (widest of the three horizontals in 玉)
d.line([(ix1 - 2, iy_bot), (ix2 + 2, iy_bot - 2)], fill=INK, width=BW)

# 点 at lower-right of 玉 (between middle and bottom, right of vertical)
dot_x, dot_y = cx + 20, iy_mid + 20
d.line([(dot_x, dot_y), (dot_x + 12, dot_y + 10)], fill=INK, width=BW)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0363_国/01_国.png"
)
