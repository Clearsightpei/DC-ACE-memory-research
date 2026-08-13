# BANK_DEVIATION
# skipped: zhu_top.py, gong.py
# reason: GT's 第 has 竹字头 top (two thin slanted-dot + short-horizontal groups)
#   and a 弟-like bottom (heng + inner box-frame + 八-flare + long piercing
#   shu-gou); neither zhu_top (龶) nor gong (弓) matches, and no 弟 primitive
#   exists in the bank.
# fresh_component: di_char_pil_inline (bamboo-header + di-bottom, thin MMH widths)

from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 4  # MMH-thin line width

def line(p1, p2, w=LW):
    d.line([p1, p2], fill=BLACK, width=w)

def poly(pts, w=LW):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill=BLACK, width=w)

# ----- TOP: 竹字头 (⺮) — two clusters side by side -----
# Left cluster: short 撇 (pie) + 横折 (small heng with a tiny down turn)
# pie: slanted line going down-left
line((75, 55), (55, 95))
# short heng starting near pie's midpoint, going right, then tiny down-turn
poly([(70, 85), (115, 78), (118, 105)])

# Right cluster (parallel, ~90px shifted)
line((175, 55), (155, 95))
poly([(170, 85), (215, 78), (218, 105)])

# ----- MIDDLE: long 横 spanning most of the width -----
line((35, 130), (265, 130))

# ----- INNER BOX/FRAME under the heng (compact) -----
# Left vertical descending from just below heng
line((80, 138), (80, 175))
# Top horizontal of box (small heng)
line((80, 155), (220, 155))
# Right vertical of box (down)
line((220, 155), (220, 178))
# Bottom horizontal of box
line((80, 178), (220, 178))

# ----- Second small heng under the box (弟's inner mark) -----
line((100, 200), (200, 200))

# ----- 八-flare under the box on both sides -----
# Left pie flaring down-left
line((80, 178), (55, 225))
# Right na-ish flaring down-right
line((220, 178), (245, 225))

# ----- Long vertical (竖) with hook at bottom piercing through center -----
# Starts at top heng, goes all the way down through the box
line((150, 130), (150, 265))
# hook curving left at bottom
line((150, 265), (120, 258))

out_path = os.path.join(os.path.dirname(__file__), "01_第.png")
img.save(out_path)
print("Wrote", out_path)
