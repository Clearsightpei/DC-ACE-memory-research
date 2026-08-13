"""
找 = 扌 (left, 3 strokes: 横, 竖钩, 提) + 戈 (right, 4 strokes: 横, 斜钩, 撇, 点)
Total 7 strokes.

Hook rule: all hooks flick UP-and-LEFT into character body.
- 扌's 竖钩: terminal flick up-left.
- 戈's 斜钩: after sweeping down-right arc, flick up-left.

Layout: 扌 tall-narrow on left (x ~35-115), 戈 wider on right (x ~120-280).
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 6


def line(pts, w=LW):
    d.line(pts, fill=INK, width=w, joint="curve")


def curve(pts, w=LW, steps=40):
    # sample Bezier-like via segments
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=INK, width=w, joint="curve")


# ---------- 扌 (left) ----------
# 1) 横 — short slightly up-slanting horizontal
line([(35, 105), (120, 98)])

# 2) 竖钩 — long vertical from top to lower, then hook up-left
line([(80, 65), (80, 225)])
# hook flick up-and-left
line([(80, 225), (60, 210)])

# 3) 提 — rising stroke from lower-left up-right, crossing 竖
line([(45, 175), (120, 148)])

# ---------- 戈 (right) ----------
# 4) 横 — long horizontal, slightly rising
line([(130, 118), (255, 108)])

# 5) 斜钩 — starts near top of 横, sweeps down-right in a gentle curve, hook up-left
sk = [
    (175, 88),
    (195, 110),
    (215, 135),
    (235, 165),
    (255, 200),
    (275, 240),
]
for i in range(len(sk) - 1):
    line([sk[i], sk[i + 1]])
# hook up-and-left at end
line([(275, 240), (250, 225)])

# 6) 撇 — from upper area near 横, arcs down-left; shorter than 斜钩
line([(200, 118), (185, 145), (165, 175), (145, 210)])

# 7) 点 — small dot upper-right of 戈 (short down-right slash)
line([(250, 75), (268, 92)], w=7)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0353_找/01_找.png"
)
print("saved")
