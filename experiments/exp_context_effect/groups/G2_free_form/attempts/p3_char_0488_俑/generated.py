"""
Render 俑 (yong3) at 300x300, black ink on white.

Structure: 亻 (left, narrow ~1/3) + 甬 (right, ~2/3).

亻: 撇 top + long 竖.
甬: top mark 短撇, then 用-like frame:
    - top 一 (over the frame)
    - 冂 (left 竖 + right 横折钩) with UP-LEFT hook at bottom-right
    - central 竖 hanging into the frame
    - two inner 一 dividing the frame into three cells

Applying calligraphic-weight 4-moves: teardrop taper on 撇, shoulder dabs
at 折 joints, bezier for curves, UP-LEFT hook flick.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def bez(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0]
        y = u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]
        pts.append((x, y))
    return pts


def stroke(pts, widths):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(n - 1, 1)
        if isinstance(widths, tuple):
            w = widths[0] + (widths[1] - widths[0]) * t
        else:
            w = widths
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def dab(cx, cy, r):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


# ------------------- 亻 (left radical) -------------------
# 撇: from upper-center-left, sweep down-left, teardrop taper
pie1 = bez((78, 60), (68, 90), (55, 115), (40, 138), n=60)
stroke(pie1, (10, 4))

# 竖: long vertical from top-right of the 撇 origin, straight down
shu_left = bez((82, 78), (80, 140), (78, 200), (76, 258), n=60)
stroke(shu_left, (8, 7))

# ------------------- 甬 (right body) -------------------
# Top 短撇 (small marker atop 甬)
top_mark = bez((178, 40), (172, 50), (166, 58), (158, 66), n=40)
stroke(top_mark, (7, 3))

# Top 一 horizontal (wide, spans the right side)
h_top = bez((120, 78), (160, 76), (210, 76), (248, 80), n=60)
stroke(h_top, (7, 7))

# Left 竖 of 冂 (vertical drop, mildly bowed)
shu_L = bez((132, 88), (131, 145), (130, 200), (129, 258), n=60)
stroke(shu_L, (7, 7))

# Right 横折钩: horizontal from top-right of top-一, corner, vertical down, hook UP-LEFT
# horizontal segment
hf_h = bez((132, 100), (170, 98), (210, 98), (246, 100), n=40)
stroke(hf_h, (7, 7))
# shoulder dab at 折 joint
dab(246, 100, 5)
# vertical segment
hf_v = bez((246, 102), (245, 155), (243, 210), (241, 258), n=60)
stroke(hf_v, (7, 7))
# hook flick UP-and-LEFT
hook = bez((241, 258), (232, 254), (222, 249), (212, 244), n=30)
stroke(hook, (7, 3))

# Central 竖 (drops from just below the top 一, through the frame, past the bottom)
shu_C = bez((186, 90), (186, 150), (186, 210), (186, 268), n=60)
stroke(shu_C, (7, 7))
# hook flick UP-and-LEFT at bottom of center 竖
hook_c = bez((186, 268), (180, 262), (173, 256), (166, 250), n=25)
stroke(hook_c, (7, 3))

# Two inner horizontals dividing the frame (upper and lower 一)
inner_h1 = bez((135, 148), (170, 146), (210, 146), (243, 148), n=40)
stroke(inner_h1, (5, 5))

inner_h2 = bez((135, 200), (170, 198), (210, 198), (243, 200), n=40)
stroke(inner_h2, (5, 5))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0488_俑/01_俑.png")
