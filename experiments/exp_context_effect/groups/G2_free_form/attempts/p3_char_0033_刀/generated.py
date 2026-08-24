"""Render 刀 (dāo, knife) — Phase 3, item p3_char_0033_刀.

Revised against CLEAN GT (2026-07-19).

Observations from clean GT:
- 横 spans approx x=60 to x=180 at y≈80, slight up-tilt.
- Right side (from shoulder): descends as a curving diagonal going
  down-and-slightly-right, then a small hook flicks up-left at the
  bottom. Not a bulging belly — more of a graceful concave-left curve
  that ends around (170, 240) with a hook up-left.
- 撇 starts ABOVE the 横 at the top-right area (x≈150, y≈55), crosses
  through the 横 near x=135, sweeps down-left ending at (55, 265).
  Thick at top, thin at end.

Strokes (order):
  1. 横折钩 (héng-zhé-gōu)
  2. 撇 (pie) — body-crossing diagonal
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def taper_stroke(pts, r_start, r_end):
    dense = []
    for i in range(len(pts) - 1):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        seg_len = math.hypot(x1 - x0, y1 - y0)
        n = max(2, int(seg_len))
        for k in range(n):
            t = k / n
            dense.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t))
    dense.append(pts[-1])
    N = len(dense) - 1
    for i, (x, y) in enumerate(dense):
        t = i / N if N > 0 else 0
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# ---------- Stroke 1: 横折钩 ----------
# Segment A: top 横 (short, slight up-tilt)
heng_start = (60, 85)
heng_end = (180, 78)
taper_stroke([heng_start, heng_end], r_start=4.5, r_end=5.0)

# Shoulder dab
shoulder = (183, 82)
dab(shoulder[0], shoulder[1], 5.0)

# Segment B: curving diagonal descending. Slight bow, ending lower-right.
shu_pts = [
    (183, 82),
    (188, 130),
    (188, 175),
    (180, 215),
    (168, 245),   # hook base
]
taper_stroke(shu_pts, r_start=5.0, r_end=4.2)

# Segment C: hook flick up-left
hook_base = (168, 245)
hook_len = 28
hook_dx = -hook_len * math.cos(math.radians(30))
hook_dy = -hook_len * math.sin(math.radians(30))
hook_end = (hook_base[0] + hook_dx, hook_base[1] + hook_dy)
dab(hook_base[0], hook_base[1], 4.2)
taper_stroke([hook_base, hook_end], r_start=4.2, r_end=1.3)

# ---------- Stroke 2: 撇 ----------
# Starts above the 横 top-right, crosses through 横, sweeps down-left.
pie_start = (152, 55)
pie_cross = (135, 85)
pie_mid = (100, 165)
pie_end = (52, 268)
taper_stroke(
    [pie_start, pie_cross, pie_mid, pie_end],
    r_start=6.5,
    r_end=1.2,
)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0033_刀/01_刀.png"
img.save(out)
print(f"Saved {out}")
