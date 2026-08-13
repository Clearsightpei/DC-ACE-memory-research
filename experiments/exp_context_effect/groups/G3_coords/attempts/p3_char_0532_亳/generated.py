# BANK_DEVIATION
# skipped: tou_radical.py
# reason: 亳 stacks 亠 + 口 + 冖 + 乇 in a tight tower; the bank 亠 primitive's
#         scale/spacing was tuned for standalone use and would leave the 口
#         too small below the wide lid. Inlining lets me size dot, lids, 口,
#         and 乇-bottom relative to the same canvas plan.
# fresh_component: bo_tower_inline (亳 built from PIL primitives against GT).

from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
TH = 5  # base stroke thickness


def line(p1, p2, w=TH):
    d.line([p1, p2], fill=INK, width=w)


def poly(pts, w=TH):
    d.line(pts, fill=INK, width=w, joint="curve")


# ---- top dot 点 (small slanted mark, upper-center) ----
line((148, 30), (156, 42), w=6)

# ---- top heng 一 (wide lid) ----
line((78, 62), (222, 60), w=5)

# ---- 口 (small box under the lid) ----
# left 竖
line((122, 78), (122, 108), w=5)
# 横折 (top + right down)
poly([(122, 78), (178, 78), (180, 110)], w=5)
# bottom 横 (closing)
line((122, 108), (180, 110), w=5)

# ---- 冖 wider cover with side legs ----
# left tiny 点/tick that touches the heng start
line((66, 128), (78, 140), w=5)
# main heng of 冖 sweeping right, curving down at the right end (横钩)
poly([(76, 138), (150, 136), (222, 140), (232, 160)], w=5)

# ---- 乇 bottom: 撇 + 一 + 竖弯钩 ----
# 撇 — starts up above the heng, sweeps down-left
poly([(160, 158), (148, 172), (132, 188)], w=5)
# heng across
line((92, 192), (218, 190), w=5)
# 竖弯钩 (vertical from just under the pie, curls right and hooks up)
poly([(158, 172), (156, 250), (166, 268), (206, 270), (222, 262), (222, 244)], w=5)

os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_亳.png")
img.save(out)
print("saved", out)
