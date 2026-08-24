"""
名 (míng) — 6 strokes: 夕 (top) + 口 (bottom-right)
Revision: 口 was too disconnected; tighten box + move up-left, extend 撇 across.
Stroke order: 撇, 横折钩, 点, 竖, 横折, 横.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)
BLACK = (0, 0, 0)


def line(p1, p2, w=6):
    draw.line([p1, p2], fill=BLACK, width=w)


def poly(pts, w=6):
    for i in range(len(pts) - 1):
        line(pts[i], pts[i + 1], w)


# ---- 夕 (upper portion, sits center-top) ----
# 1. 撇 — long sweeping diagonal starting upper-mid, curves down through center
#    and sweeps out to lower-left corner. This dominates the character.
poly([(175, 40), (160, 75), (135, 125), (100, 185), (55, 260)], w=6)

# 2. 横折钩 — short horiz across the 撇 near upper part, then diagonal down-right,
#    ending with an UP-and-LEFT hook flick.
poly([(120, 95), (185, 90), (162, 155)], w=6)
# hook flick UP-and-LEFT (toward interior)
line((162, 155), (142, 148), w=6)

# 3. 点 — small dot inside the 夕 pocket (between 撇 and hook body)
poly([(135, 125), (150, 133)], w=7)

# ---- 口 (lower-right, sits below-right of 夕, snug against 撇's tail region) ----
# Box roughly x:140..230, y:195..260
# 4. 竖 — left vertical
line((145, 200), (143, 258), w=6)
# 5. 横折 — top horiz + right vertical
poly([(143, 200), (230, 197), (228, 258)], w=6)
# 6. 横 — bottom horiz
line((143, 258), (228, 258), w=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0265_名/01_名.png")
