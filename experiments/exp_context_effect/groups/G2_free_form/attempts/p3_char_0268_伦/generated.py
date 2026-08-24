"""
伦 = 亻 (left) + 仑 (right, = 人 over 匕)
SIGNATURE CHECK (from sibling_signature_checklist / TIER-0):
  - 人 component: 撇 and 捺 cross NEAR THE TOP (not centered), 捺 has
    thickening tail going down-right.
  - 匕 component: 撇 crosses through the vertical near top; 竖弯钩
    goes DOWN, curves RIGHT, then hook flicks UP-and-LEFT (~-110°).
Hook rule: 竖弯钩 terminal flicks UP-and-LEFT, back into body.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def bezier(p0, p1, p2, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts

def brush(pts, w0, w1):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(1, n - 1)
        r = (w0 * (1 - t) + w1 * t) / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill="black")

def stroke_line(p0, p1, w0, w1, n=40):
    pts = [(p0[0] + (p1[0] - p0[0]) * i / n, p0[1] + (p1[1] - p0[1]) * i / n)
           for i in range(n + 1)]
    brush(pts, w0, w1)

# ============================================================
# LEFT: 亻 (person radical) — occupies x in ~[40, 110]
# ============================================================
# 撇 — starts upper, curves down-left
pie_left = bezier((92, 55), (78, 130), (48, 200), n=80)
brush(pie_left, 9, 5)

# 竖 — vertical stroke from mid of 撇 down
stroke_line((82, 130), (82, 240), 9, 8, n=60)

# ============================================================
# RIGHT: 仑 — 人 on top + 匕 below
# Right block occupies x in ~[120, 275]
# ============================================================

# --- 人 (top) --- crosses high, wide spread
# 撇 from apex down-left
pie_top = bezier((190, 55), (170, 100), (130, 155), n=80)
brush(pie_top, 8, 5)

# 捺 from near apex down-right, thickening
na_pts = bezier((193, 60), (215, 110), (255, 160), n=80)
brush(na_pts, 5, 11)

# --- 匕 (bottom under 人) --- roughly x in [140, 265], y in [155, 260]
# 撇 — a slanting stroke going down-left from upper right
pie_bi = bezier((215, 155), (190, 175), (155, 205), n=60)
brush(pie_bi, 7, 5)

# 竖弯钩 — vertical down, curve right along bottom, hook up-left
# vertical part
vert = [(165, 165 + i * (235 - 165) / 40) for i in range(41)]
brush(vert, 9, 9)
# curve from bottom of vertical rightward
curve = bezier((165, 235), (170, 258), (245, 258), n=60)
brush(curve, 9, 9)
# hook: flick UP-and-LEFT from right end (~-110°)
hook_start = (245, 258)
hook_end = (232, 232)
stroke_line(hook_start, hook_end, 9, 3, n=30)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0268_伦/01_伦.png")
print("saved")
