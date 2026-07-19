"""
Render 勹 (bao-radical, 2 strokes) at 300x300, PIL brush-dab technique.

Strokes:
1. 撇 (pie): short throw-away at top-left, upper-right start -> lower-left tip.
2. 横折钩 (heng-zhe-gou): 横 at top, shoulder turn, long curved 竖 sweeping
   down and slightly left, terminating in a small up-and-left hook.

Image coords: y grows DOWN.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_taper(p0, p1, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_taper(p0, p1, p2, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ---- Stroke 1: 撇 (moved up-left, longer) ----------------------------------
# Upper-right start -> lower-left tip, gentle bow, thick->thin.
# GT: 撇 starts near top-center and sweeps down-left further; small gap
# between 撇 tip and 横 start.
p0 = (128, 65)
p2 = (75, 160)
ctrl = (108, 105)
dab(p0[0], p0[1], 8)  # 顿笔 at start
bezier_taper(p0, ctrl, p2, r0=7, r1=1.5, steps=450)

# ---- Stroke 2: 横折钩 (larger, extends further down) -----------------------
# 横 primary: left -> right at top, slight up-tilt, longer.
heng_start = (135, 70)
heng_end = (230, 62)
dab(heng_start[0], heng_start[1], 7)   # start 顿
line_taper(heng_start, heng_end, r0=5.5, r1=5.5, steps=380)

# Shoulder dab at corner
shoulder = heng_end
dab(shoulder[0], shoulder[1], 8.5)  # r+3 press

# Curved 竖 sweeping down; longer and reaches further toward bottom.
# Bezier with belly on right — the sweep is the visual anchor of 勹.
zhu_start = shoulder
zhu_end = (180, 260)
zhu_ctrl = (245, 170)  # control pulled right to bow body outward
bezier_taper(zhu_start, zhu_ctrl, zhu_end, r0=6, r1=4.5, steps=500)

# Hook flick from bottom endpoint, up-and-left ~ -130°.
hook_len = 26
hook_angle = math.radians(-130)
hook_end = (
    zhu_end[0] + hook_len * math.cos(hook_angle),
    zhu_end[1] + hook_len * math.sin(hook_angle),
)
line_taper(zhu_end, hook_end, r0=5.5, r1=1.2, steps=220)

# ---------------------------------------------------------------------------
img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_010_勹/01_勹.png"
)
