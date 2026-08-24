"""
Render 紧 (jǐn) at 300x300, black ink on white.

Structural read from GT (simplified form):
  Top-left  (~half of top row): stylized 臣 remnant — one 竖 on the far left,
            then a 竖折 fragment (short 竖 + short 横) forming a small block.
  Top-right (~half of top row): 又 — 撇 (down-left) + 捺 (down-right) crossing.
            The 又's 撇 starts high above the top-left block's tops and sweeps
            down through the block; the 捺 sweeps down-right with foot flare.
  Bottom    : 糸 (simplified) — 幺-ish loop (small 撇折 + 点) sitting above 小
              (center 竖钩 with UP-LEFT flick + left 撇 + right 点).
  Components MUST touch (Tier-0 H). No calligraphic uniform lines (Tier-0 F).
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

def shoulder(x, y, r=5):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# =========================================================================
# TOP HALF (y ~ 25..145) — 臤-like structure
# =========================================================================

# --- top-left: 臣 remnant (two-vertical + small horizontal joint) ---
# leftmost 竖 — tall vertical
v1 = bez((55, 40), (55, 70), (55, 100), (55, 140), n=40)
stroke(v1, (7, 7))

# 竖折 fragment: short 竖 then short 横 baseline
v2 = bez((90, 55), (90, 80), (90, 110), (90, 140), n=40)
stroke(v2, (7, 7))
shoulder(90, 140, 5)
# short 横 baseline of the top-left block
h_base = bez((55, 140), (75, 140), (95, 140), (115, 140), n=30)
stroke(h_base, (6, 6))
# top cap 横 tying the two verticals (like 川 with top bar, GT has a top rail)
h_top = bez((52, 55), (75, 52), (90, 52), (108, 55), n=30)
stroke(h_top, (5, 5))

# --- top-right: 又 ---
# 撇 (from high center, sweeps down-left through top-left block area)
pie = bez((175, 30), (160, 65), (140, 100), (110, 135), n=80)
stroke(pie, (11, 4))

# 横撇 shoulder — start with a small 横 then the 撇 above already crosses
h_yg = bez((160, 55), (200, 55), (230, 58), (250, 62), n=40)
stroke(h_yg, (6, 5))

# 捺 (starts near where the 横 meets 撇, sweeps down-right, foot flare)
na = bez((195, 70), (215, 100), (240, 130), (265, 155), n=80)
stroke(na, (5, 12))
foot = bez((265, 155), (270, 158), (275, 160), (280, 162), n=20)
stroke(foot, (12, 3))

# =========================================================================
# BOTTOM HALF (y ~ 155..280) — 糸 (simplified: 幺 + 小)
# =========================================================================

# --- 幺 top loop (simplified: 撇折 + 点) ---
# 撇折 upper piece: small 撇 down-left, folds into 提/横
pie_small = bez((150, 160), (140, 172), (128, 182), (118, 190), n=40)
stroke(pie_small, (7, 3))
shoulder(118, 190, 4)
tik = bez((118, 190), (135, 195), (155, 200), (175, 200), n=40)
stroke(tik, (6, 5))

# small 撇折 lower piece
pie_small2 = bez((165, 200), (155, 212), (143, 220), (130, 228), n=40)
stroke(pie_small2, (6, 3))
shoulder(130, 228, 4)
tik2 = bez((130, 228), (150, 232), (170, 232), (185, 230), n=40)
stroke(tik2, (5, 4))

# --- 小 bottom (center 竖钩 + left 撇 + right 点) ---
# center 竖钩
sg = bez((152, 232), (152, 250), (152, 265), (150, 278), n=50)
stroke(sg, (7, 7))
# hook flick UP-and-LEFT
hook = bez((150, 278), (145, 273), (140, 268), (135, 262), n=20)
stroke(hook, (7, 3))

# left 撇 (from around the 幺 base, sweeps down-left)
left_pie = bez((115, 240), (105, 255), (98, 268), (92, 280), n=40)
stroke(left_pie, (7, 3))

# right 点
right_dot = bez((188, 240), (200, 252), (210, 265), (218, 275), n=40)
stroke(right_dot, (4, 8))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0539_紧/01_紧.png")
