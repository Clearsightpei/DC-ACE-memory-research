"""Render 还 (p3_char_0305) — 7 strokes.

Structure: 不 (upper right) + 辶 (walking radical, wraps left/bottom).

不 (4 strokes, compressed into upper-right quadrant):
  1. 横 — long top horizontal, slight tilt.
  2. 撇 — from just below middle of 横, sweeps down-left.
  3. 竖 — center down.
  4. 点 — small dot on right.

辶 (3 strokes, wrapping):
  5. 点 — small teardrop, upper-left area.
  6. 横折折撇 — short compact z-body on left.
  7. 平捺 — long shallow smile across the bottom (concave-up),
     supporting 不 above.
"""
from PIL import Image, ImageDraw
import math

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def taper(points, w_start, w_end, steps=None):
    if steps is None:
        steps = max(len(points) - 1, 30)
    lens = [0.0]
    for i in range(1, len(points)):
        x0, y0 = points[i - 1]
        x1, y1 = points[i]
        lens.append(lens[-1] + math.hypot(x1 - x0, y1 - y0))
    total = lens[-1]
    if total == 0:
        return

    def at(t):
        target = t * total
        for i in range(1, len(lens)):
            if lens[i] >= target:
                seg = lens[i] - lens[i - 1]
                u = 0 if seg == 0 else (target - lens[i - 1]) / seg
                x0, y0 = points[i - 1]
                x1, y1 = points[i]
                return (x0 + u * (x1 - x0), y0 + u * (y1 - y0))
        return points[-1]

    prev = at(0)
    for i in range(1, steps + 1):
        t = i / steps
        cur = at(t)
        w = w_start + (w_end - w_start) * t
        d.line([prev, cur], fill=BLACK, width=max(int(round(w)), 1))
        r = max(int(round(w / 2)), 1)
        d.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r], fill=BLACK)
        prev = cur


def bezier_taper(p0, p1, p2, w0, w1, steps=200):
    prev = p0
    for i in range(1, steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        w = w0 + (w1 - w0) * t
        d.line([prev, (x, y)], fill=BLACK, width=max(int(round(w)), 1))
        r = max(int(round(w / 2)), 1)
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)
        prev = (x, y)


# ============ 不 (upper right quadrant) ============
# 横 — top horizontal, slight upward tilt to right
heng = [(105, 78), (170, 72), (245, 72)]
taper(heng, 6, 8)

# 撇 — from just under 横, sweeps down-left
pie = [(180, 80), (160, 130), (135, 175), (115, 205)]
taper(pie, 9, 3)

# 竖 — from 横 down to middle
shu = [(195, 82), (195, 145), (195, 205)]
taper(shu, 7, 6)

# 点 — small diagonal dot right of 竖
dian = [(220, 145), (238, 168), (252, 185)]
taper(dian, 3, 8)


# ============ 辶 (wraps left/bottom) ============
# Stroke 5: 点 — small teardrop, upper-left area
bezier_taper((55, 75), (62, 90), (75, 105), 2, 6, steps=80)

# Stroke 6: 横折折撇 — compact z-body on left
# short 横 → shoulder → down-left slant → shoulder → short right → bowed 撇
body_pts_a = [(45, 130), (85, 122)]
taper(body_pts_a, 4, 4)
body_pts_b = [(85, 122), (55, 155)]
taper(body_pts_b, 4, 4)
body_pts_c = [(55, 155), (90, 152)]
taper(body_pts_c, 4, 4)
# bowed 撇 tail down-and-left
bezier_taper((90, 152), (78, 180), (45, 215), 4, 2, steps=140)

# Stroke 7: 平捺 — long shallow smile across bottom, concave-up
# entering from lower-left, sweeping right with broad flat foot
bezier_taper((32, 235), (150, 288), (280, 250), 3, 9, steps=280)
# foot thickening at right end
for k in range(0, 12):
    x = 280 + k * 0.7
    y = 250 + k * 0.4
    r = 8 - k * 0.3
    d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0305_还/01_还.png"
img.save(out)
print("Saved:", out)
