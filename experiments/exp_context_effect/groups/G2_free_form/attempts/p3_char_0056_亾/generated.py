"""Render 亾 (variant of 亡): 4 strokes.
Layout from GT:
 - Left tall 竖 descending down the left third.
 - Inside the corner: 撇 (short apex flick down-left) then 捺 (long flat sweep right).
 - Bottom 横 spanning left-third to right side (base of the ㄴ bracket).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def brush_line(pts, width=8):
    # taper-free simple polyline via multiple joined segments
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=BLACK, width=width)
    for p in pts:
        d.ellipse([p[0] - width // 2, p[1] - width // 2,
                   p[0] + width // 2, p[1] + width // 2], fill=BLACK)


# 1) Left 竖 — tall vertical on left, from top down; stops short of the base.
brush_line([(72, 85), (72, 245)], width=8)

# 2) 撇 inside — apex sits shifted left; short flick down-left to meet vertical.
brush_line([(140, 95), (128, 135), (115, 180), (108, 220)], width=8)

# 3) 捺 inside — from apex a long very flat sweep to the right with slight arc.
brush_line([(140, 95), (170, 130), (215, 175), (255, 210)], width=8)

# 4) Bottom 横 — flat base, slightly detached from the vertical.
brush_line([(60, 262), (260, 262)], width=9)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0056_亾/01_亾.png")
