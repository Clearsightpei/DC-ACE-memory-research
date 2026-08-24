"""
冋 (jiong) — 冂 enclosure with 口 inside near top.
Strokes (5):
  1. 撇 short left-top flick (starts the 冂 outer)
  2. 横折钩 top + right vertical + bottom-left flick hook (冂 outer)
  3. 竖 short left vertical of inner 口
  4. 横折 top + right vertical of inner 口
  5. 横 bottom of inner 口
Actually simpler: outer 冂 is 2 strokes (left 竖 + 横折钩), inner 口 is 3 strokes.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)
LW = 7  # line width

# Outer 冂 --------------------------------------------------------
# Stroke 1: left 竖 (long, slight taper) — from top-left down
# Slight 撇 head at top
d.line([(70, 55), (60, 260)], fill=BLACK, width=LW)

# Stroke 2: 横折钩 — top horizontal + right vertical + left-flick hook (UP-and-LEFT)
# top
d.line([(70, 55), (240, 62)], fill=BLACK, width=LW)
# right vertical (fold down)
d.line([(240, 62), (245, 260)], fill=BLACK, width=LW)
# bottom hook flick — UP-and-LEFT into interior (per memory hook rule)
d.line([(245, 260), (220, 235)], fill=BLACK, width=LW)

# Inner 口 (small, positioned upper-center, near top) -------------
x0, y0, x1, y1 = 115, 100, 195, 165
# Stroke 3: left 竖 of 口
d.line([(x0, y0), (x0, y1)], fill=BLACK, width=LW-1)
# Stroke 4: 横折 top + right side
d.line([(x0, y0), (x1, y0 + 3)], fill=BLACK, width=LW-1)
d.line([(x1, y0 + 3), (x1, y1)], fill=BLACK, width=LW-1)
# Stroke 5: bottom 横
d.line([(x0, y1), (x1, y1)], fill=BLACK, width=LW-1)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0205_冋/01_冋.png")
