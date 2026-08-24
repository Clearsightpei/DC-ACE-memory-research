"""
p3_char_0270_伧 — 亻 (person radical) + 仓 (cang)
Revised: fix 亻 撇-crossing-竖 and separate 仓 lower box from 人 top clearly.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLK = (0, 0, 0)
LW = 5


def line(p1, p2, w=LW):
    d.line([p1, p2], fill=BLK, width=w)


def poly(pts, w=LW):
    d.line(pts, fill=BLK, width=w, joint="curve")


# ===== LEFT: 亻 (person radical) — centered around x=80 =====
# 撇: starts upper-right, sweeps down-left across the 竖
poly([(95, 85), (85, 110), (60, 165)], w=LW)
# 竖: straight down from where 撇 crosses
line((88, 105), (88, 265), w=LW)

# ===== RIGHT: 仓 — 人 top + 横折钩 body + short horizontal + curl =====
# 撇: apex at top, sweeps down-left
poly([(190, 65), (170, 100), (145, 145)], w=LW)
# 捺: apex, sweeps down-right with slight curve
poly([(190, 65), (215, 105), (245, 145)], w=LW)

# 横折钩: horizontal shoulder + vertical + hook
# shoulder starts a bit right of 撇 base, goes horizontally right
poly([(160, 170), (238, 170), (238, 255), (222, 262)], w=LW)

# Small internal horizontal (mouth top of 巳-like)
line((172, 205), (232, 205), w=LW)

# Bottom left short vertical + closure (the 巳/口-like bottom)
poly([(172, 205), (172, 245), (232, 245)], w=LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0270_伧/01_伧.png")
