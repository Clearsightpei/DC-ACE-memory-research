"""
Render 乩 (p3_char_0228) — G2 attempt.

Structure: left 占 (卜 over 口) + right 乚 (竖弯 with UP-LEFT hook flick).

Notes from memory_index:
- Hook rule (Tier-0 B): 乚 = 竖弯钩 — after arc, flick UP-and-LEFT (~-105° to -115°).
- radical_position_rules: left-right compound; left 占 slightly narrower,
  right 乚 broad sweeping arc, roughly equal-width halves.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 7  # stroke width


def line(p1, p2, w=LW):
    d.line([p1, p2], fill=INK, width=w)


def polyline(pts, w=LW):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=INK, width=w)
    for p in pts:
        d.ellipse([p[0] - w // 2, p[1] - w // 2, p[0] + w // 2, p[1] + w // 2], fill=INK)


def dot(pt, r=6):
    d.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=INK)


# --- LEFT: 占 -------------------------------------------------
# 口 box first (define center for alignment) — center x = 87
BOX_L, BOX_R = 45, 130
BOX_T, BOX_B = 160, 245
BOX_CX = (BOX_L + BOX_R) // 2  # 87

# 卜 on top (vertical + dot), centered over 口
polyline([(BOX_CX, 45), (BOX_CX, 135)])  # 竖 of 卜
# dot (点) right of the 竖
polyline([(BOX_CX + 22, 80), (BOX_CX + 38, 100)], w=LW)
dot((BOX_CX + 38, 100), r=5)

# 口 (small box) — 3 strokes: 竖 left, 横折 top+right, 横 close
polyline([(BOX_L, BOX_T), (BOX_L, BOX_B)])
polyline([(BOX_L, BOX_T), (BOX_R, BOX_T), (BOX_R, BOX_B)])
polyline([(BOX_L, BOX_B), (BOX_R, BOX_B)])

# --- RIGHT: 乚 (竖弯钩) --------------------------------------
# vertical down, sweeping arc right, hook flick UP-and-LEFT
# approximate with polyline of arc segments
right_stroke = [
    (200, 45),
    (200, 100),
    (200, 160),
    (202, 200),
    (210, 230),
    (228, 252),
    (252, 262),
    (275, 262),
]
polyline(right_stroke, w=LW)
# hook flick UP-and-LEFT from terminal
polyline([(275, 262), (272, 245), (265, 235)], w=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0228_乩/01_乩.png")
print("wrote 01_乩.png")
