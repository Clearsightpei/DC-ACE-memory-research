"""
Render 容 (rong2) at 300x300, black ink on white.

Structural decomposition (10 strokes):
  宀 roof (3): 点 (top center), 点/短竖 (left shoulder), 横钩 (long h + down-left flick)
  八 splay (2): left 撇, right 点
  人 (2): 撇, 捺 (crossing, spans wider)
  口 bottom (3): 竖, 横折, 横

Applies calligraphic-weight 4-move recipe:
  - Teardrop taper on 撇/捺/点
  - Shoulder dab at 折 joints (横钩 corner, 口 top-right corner)
  - Bezier curves for all sweeping strokes
  - Hook flicks UP-and-LEFT (into character body)
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

# ===== 宀 roof =====
# top center 点 — a small down-right dot
top_dot = bez((148, 32), (152, 40), (156, 48), (160, 55), n=25)
stroke(top_dot, (3, 8))

# left shoulder 点/短撇 dropping from roof-left
left_sh = bez((70, 60), (72, 72), (74, 80), (75, 92), n=30)
stroke(left_sh, (7, 4))

# 横钩: long horizontal at y~72, ending with a shoulder dab + down-left hook flick
h_roof = bez((70, 72), (130, 68), (190, 68), (240, 74), n=60)
stroke(h_roof, (6, 7))
# shoulder dab at right corner
dab(240, 74, 5.5)
# hook: down-and-slightly-left flick
hook_roof = bez((240, 74), (238, 82), (234, 88), (228, 94), n=25)
stroke(hook_roof, (7, 3))

# ===== 八 (splay under the roof) =====
# left 撇: from ~(120,105) down-left
ba_left = bez((125, 108), (115, 122), (108, 133), (100, 145), n=40)
stroke(ba_left, (7, 3))
# right 点: from ~(190,108) down-right
ba_right = bez((190, 108), (200, 120), (208, 130), (216, 142), n=40)
stroke(ba_right, (3, 8))

# ===== 人 (crossing strokes below 八) =====
# 撇: from top-center apex down-left, longer sweep
ren_pie = bez((155, 138), (135, 165), (108, 190), (75, 215), n=70)
stroke(ren_pie, (10, 4))
# 捺: from apex down-right with S-belly and foot flare
ren_na = bez((160, 145), (185, 175), (210, 200), (232, 218), n=70)
stroke(ren_na, (4, 12))
# foot flare (flat tail of 捺)
foot = bez((232, 218), (240, 219), (247, 220), (253, 220), n=20)
stroke(foot, (12, 3))

# ===== 口 (bottom mouth) =====
# 口 sits centered near bottom, touching the 人 sweep (component-touch rule H)
L, R, T, B = 115, 200, 212, 270

# 竖 (left side)
kou_v = bez((L, T), (L, T + 15), (L, T + 30), (L, B), n=40)
stroke(kou_v, (6, 6))
# 横折 (top horizontal + right vertical, one stroke with shoulder dab)
kou_hz_h = bez((L + 2, T), (L + 25, T - 2), (R - 25, T - 2), (R, T), n=40)
stroke(kou_hz_h, (6, 6))
dab(R, T, 4.5)
kou_hz_v = bez((R, T), (R, T + 15), (R, T + 30), (R, B), n=40)
stroke(kou_hz_v, (6, 6))
# 横 (bottom, closes)
kou_bot = bez((L, B), (L + 25, B + 2), (R - 25, B + 2), (R, B), n=40)
stroke(kou_bot, (6, 6))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0547_容/01_容.png")
