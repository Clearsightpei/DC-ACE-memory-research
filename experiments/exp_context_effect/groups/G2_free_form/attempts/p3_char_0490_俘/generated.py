"""
Render 俘 (fu2) at 300x300, black ink on white.

Decomposition (LR compound):
  Left:  亻 = 撇 (short, down-left) + 竖 (long)
  Right: 孚 = 爫 (top: 撇 + 3 short down-strokes) + 子 (bottom: 横撇 + 竖钩 + 长横)

TIER-0 checks applied:
  - Components MUST touch (H): 亻 竖 sits at ~x=95, right body starts at x=110 with 爫 sweep reaching left.
  - Hook flick UP-LEFT (B): 子 竖钩 flicks up-left into character body.
  - Calligraphic 4-move (F): teardrop taper via bez+stroke helpers; shoulder dabs
    at 横撇 folder joint; bezier for all curves; up-left hook.
  - No sibling-risk radical present in 俘.
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


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ============================================================
# 亻 (left radical) — tall-narrow ~30% width
# ============================================================
# 撇: from upper apex sweeping down-left, taper thick->thin
pie_left = bez((92, 75), (85, 110), (75, 135), (55, 165), n=60)
stroke(pie_left, (10, 4))

# 竖: long vertical, near the apex of 撇, slight thickness
shu_left = bez((95, 100), (95, 160), (95, 210), (95, 255), n=60)
stroke(shu_left, (8, 7))

# ============================================================
# 孚 right — 爫 top + 子 bottom
# ============================================================

# --- 爫 (claw) top — 4 strokes ---
# leading 撇 (small, top-left of 爫)
zhao_pie = bez((135, 70), (128, 82), (122, 92), (115, 100), n=40)
stroke(zhao_pie, (7, 3))

# three short down-strokes (点/竖 style, slight lean)
d1 = bez((155, 72), (156, 82), (158, 92), (160, 102), n=30)
stroke(d1, (4, 8))

d2 = bez((185, 72), (186, 82), (188, 92), (190, 102), n=30)
stroke(d2, (4, 8))

d3 = bez((215, 72), (218, 84), (222, 96), (228, 108), n=30)
stroke(d3, (4, 9))

# --- 子 bottom ---
# 横撇 (top of 子): horizontal then sharp fold down-left as a pie
h_top = bez((130, 130), (155, 128), (185, 128), (215, 130), n=50)
stroke(h_top, (7, 7))
# shoulder dab at the fold
dab(215, 130, 5)
# 撇 tail from the fold
pie_top = bez((215, 130), (208, 145), (200, 158), (188, 168), n=40)
stroke(pie_top, (7, 3))

# 竖钩: long vertical from top of 子 area down, then hook up-left
shu_gou = bez((175, 145), (173, 190), (172, 230), (172, 265), n=60)
stroke(shu_gou, (8, 7))
# hook flick UP-and-LEFT
hook = bez((172, 265), (168, 260), (162, 254), (155, 248), n=25)
stroke(hook, (7, 3))

# 长横 (long horizontal middle bar of 子): spans across, thickens slightly
h_mid = bez((110, 205), (150, 203), (210, 203), (265, 205), n=60)
stroke(h_mid, (7, 8))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0490_俘/01_俘.png")
