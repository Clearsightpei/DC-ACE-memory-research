"""
Render 前 (qian2) at 300x300, black ink on white.

Structural read:
  Top: 䒑 = 丷 (left slanting-down-left stroke + right slanting-down-right dot)
       + 一 (long horizontal below the 丷)
  Bottom-left: 月 body — left 撇, right 横折钩 forming the box,
       two inner 一 horizontals
  Bottom-right: 刂 — short left 竖, tall right 竖钩 (hook UP-LEFT)

Total 9 strokes. Applies the 4-move calligraphic weight recipe:
  teardrop tapers, shoulder dabs at 折, Bezier for curves, hook UP-LEFT.
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

# --- Top: 丷 ---
# Left stroke: short 撇 slanting down-left
left_top = bez((130, 30), (125, 40), (118, 55), (110, 68), n=30)
stroke(left_top, (4, 8))
# Right stroke: short 点 slanting down-right
right_top = bez((175, 30), (182, 42), (188, 55), (192, 68), n=30)
stroke(right_top, (4, 9))

# --- Long horizontal 一 ---
h_main = bez((35, 92), (100, 88), (200, 88), (265, 94), n=80)
stroke(h_main, (7, 7))
# small entry dab on left
dab(37, 92, 5)
# small terminal dab on right
dab(263, 94, 6)

# --- Bottom-left: 月 body ---
# Left 撇: from near top of month, sweeps down-left with slight bow
yue_pie = bez((90, 105), (82, 160), (70, 220), (52, 275), n=80)
stroke(yue_pie, (9, 4))

# 横折钩: horizontal from (90, 108) to (155, 108), then down to (155, 265), then hook up-left
# top segment
top_seg = bez((90, 108), (110, 106), (135, 106), (155, 110), n=40)
stroke(top_seg, (6, 7))
# shoulder dab at the corner
dab(155, 110, 6)
# vertical segment
vert_seg = bez((155, 110), (155, 170), (155, 220), (155, 265), n=60)
stroke(vert_seg, (7, 7))
# hook flick UP-and-LEFT
hook1 = bez((155, 265), (150, 260), (144, 254), (137, 248), n=25)
stroke(hook1, (7, 3))

# Inner horizontals
inner1 = bez((90, 165), (115, 163), (140, 163), (152, 165), n=40)
stroke(inner1, (5, 5))
inner2 = bez((90, 215), (115, 213), (140, 213), (152, 215), n=40)
stroke(inner2, (5, 5))

# --- Bottom-right: 刂 ---
# Short left 竖
short_vert = bez((195, 130), (196, 175), (196, 210), (196, 230), n=40)
stroke(short_vert, (6, 6))

# Tall right 竖钩
tall_vert = bez((245, 108), (246, 170), (247, 220), (247, 265), n=60)
stroke(tall_vert, (8, 8))
# hook UP-and-LEFT
hook2 = bez((247, 265), (241, 259), (234, 253), (226, 247), n=25)
stroke(hook2, (8, 3))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0441_前/01_前.png")
