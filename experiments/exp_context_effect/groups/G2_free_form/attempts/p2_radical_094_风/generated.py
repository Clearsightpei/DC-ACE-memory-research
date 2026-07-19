"""
风 (feng) — 4-stroke radical. Frame + two internal strokes.

Structural decomposition (image coords, y grows DOWN, 300×300):
  1. 撇 (pie) — left frame: starts near top-center, throws down-left,
     gentle bow with belly on lower-right. Tapered thick→thin.
  2. 横折弯钩 — right frame: short 横 at top (starts near stroke-1's
     start), 折 shoulder, 竖 descends, tangent-continuous arc into a
     rightward-then-flick? Actually for 风 the right frame is a
     横斜钩 form: short 横 → shoulder → long 斜钩 curving down-right
     with belly on lower-left → hook flick up-left. Per GT the
     right side is a single 横斜钩 (aka 横折弯钩 variant).
  3. Inner 撇 — small throw from upper-inside to lower-left.
  4. Inner 乀 (or 点/小捺) — small stroke going down-right, mirrors
     the inner 撇.

Applied memory:
- 撇 as Bezier with control point toward primary interior (mem 撇 recipe).
- 折 shoulder = one r+3 dab.
- Hook flick ~40 px, angle ~-115° up-and-left.
- 斜钩 Bezier belly-on-lower-left recipe from batch-2 (斜钩 entry).
- Shared corners at top: strokes 1 and 2 meet at the top (bootstrap
  principle 2 — shared joint, no inset). Actually looking at GT, the
  两 strokes don't quite share — 撇 begins slightly below the 横's
  start. But we'll place them very close, both near top-center.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def stroke_line(p0, p1, r_start, r_end, steps=300):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier(p0, p1, p2, r_start, r_end, steps=400, ease=1.0):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        tt = t ** ease
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t ** 2 * x2
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t ** 2 * y2
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


# ---- Stroke 1: 撇 (left frame) ----
# Starts top-center, throws down-left with gentle bow.
# Widened: end further left, more pronounced curve at scale.
p1_start = (110, 70)
p1_end = (40, 260)
p1_ctrl = (65, 175)  # pulled inward (right of chord)
dab(*p1_start, r=8)  # 顿笔 start
bezier(p1_start, p1_ctrl, p1_end, r_start=8, r_end=1.5, steps=400, ease=1.2)

# ---- Stroke 2: 横斜钩 (right frame — 横 + shoulder + 斜钩 + hook flick) ----
# Wider top 横, starting near stroke-1 top (shared joint region).
heng_start = (105, 70)
heng_end = (245, 60)  # slight up-tilt, wider
stroke_line(heng_start, heng_end, r_start=7, r_end=6, steps=250)
dab(*heng_start, r=8)  # 顿笔

# Shoulder dab at 横 end
shoulder = (245, 60)
dab(*shoulder, r=8)  # r+2 shoulder press

# 斜钩 body: Bezier from shoulder, belly on lower-left (concave to upper-right)
# End further out and lower to widen the frame.
sk_start = shoulder
sk_end = (260, 245)
sk_ctrl = (215, 220)  # pulled toward lower-left of chord midpoint (more belly)
bezier(sk_start, sk_ctrl, sk_end, r_start=7, r_end=5, steps=400)

# Hook flick from sk_end, up-and-slightly-left ~-125° (a touch more horizontal)
hook_len = 42
ang = math.radians(-125)
hk_end = (sk_end[0] + hook_len * math.cos(ang), sk_end[1] + hook_len * math.sin(ang))
dab(*sk_end, r=5)
stroke_line(sk_end, hk_end, r_start=5, r_end=1.2, steps=180)

# ---- Stroke 3: inner 撇 (small) ----
# Upper-inside → lower-left; start higher, throw further left.
i1_start = (155, 115)
i1_end = (100, 230)
i1_ctrl = (130, 170)
dab(*i1_start, r=6)
bezier(i1_start, i1_ctrl, i1_end, r_start=6, r_end=1.2, steps=250, ease=1.2)

# ---- Stroke 4: inner 乀 / small 捺 (going down-right) ----
# Starts at/near inner-撇 head, goes down-right, thin→thick with broad foot.
i2_start = (170, 130)
i2_end = (225, 235)
i2_ctrl = (190, 195)
bezier(i2_start, i2_ctrl, i2_end, r_start=2, r_end=7, steps=280, ease=0.85)
# terminal broad foot
dab(*i2_end, r=8)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_094_风/01_风.png")
