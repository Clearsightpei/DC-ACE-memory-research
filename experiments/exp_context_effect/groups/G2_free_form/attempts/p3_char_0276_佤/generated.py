"""
p3_char_0276_佤 — G2 attempt (revised).
佤 = 亻 (left) + 瓦 (right).
瓦 stroke order (5 strokes): 横, 竖提, 横折弯钩(sweeping), 点
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def dab(pts, widths):
    for i in range(len(pts) - 1):
        w = int((widths[i] + widths[i + 1]) / 2)
        d.line([pts[i], pts[i + 1]], fill="black", width=max(2, w))
    for (x, y), w in zip(pts, widths):
        r = max(1, w // 2)
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")

def line(pts, w=6):
    d.line(pts, fill="black", width=w, joint="curve")

# ---- 亻 (left radical, thinner column) ----
# 撇
dab([(100, 65), (90, 100), (72, 145), (48, 200)], [9, 8, 7, 4])
# 竖
line([(88, 118), (88, 250)], w=7)

# ---- 瓦 (right) ----
# stroke 1: 横 (top horizontal) — slight rise to the right
dab([(135, 95), (185, 90), (240, 82)], [7, 7, 7])

# stroke 2: 竖提 — short vertical then tick up-right (upper-left inside)
# starts from ~top going down, then flick up-right
dab([(155, 95), (150, 145), (148, 165)], [7, 7, 7])
line([(148, 165), (185, 155)], w=6)  # 提 flick

# stroke 3: 横折弯钩 — starts at top right area, goes right, drops, sweeps left, hooks up
sweep = [
    (200, 90),   # start (upper, slightly right of stroke 1's midpoint on the top)
    (245, 92),   # short horizontal right
    (255, 115),  # turn down
    (260, 160),
    (255, 205),
    (240, 240),
    (215, 258),
    (180, 262),
    (150, 258),
]
widths_sw = [7, 7, 7, 7, 7, 7, 7, 7, 6]
dab(sweep, widths_sw)
# hook flick UP-and-LEFT from terminal
dab([(150, 258), (140, 240), (135, 228)], [6, 5, 3])

# stroke 4: 点 — small dot upper-mid interior
dab([(200, 130), (215, 148)], [4, 8])

out_png = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0276_佤/01_佤.png"
img.save(out_png)
print("wrote", out_png)
