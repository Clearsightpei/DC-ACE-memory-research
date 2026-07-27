"""Render 刀 (dāo, knife) — Phase 3, item p3_char_0033_刀, retry #2.

Prior retry_1 read as 力 despite crossing-撇 fix. Root cause looking at GT:
- GT 撇 is a graceful ARC (not a straight diagonal). It starts near the
  top area, curves out and sweeps down-left with belly convex to the
  right.
- GT 横折钩 body has a subtle rightward belly then curves inward — not
  a plumb vertical.
- The 撇 top-poke is small and close to the shoulder, but the whole 撇
  is much CURVIER, not a straight ramp bisecting the enclosed area.
- Also the whole character is airier / thinner than my retry_1.

Fix (retry_2):
- Thinner strokes overall (r≈3.5 vs 4.8).
- 横折钩 body has a gentle rightward bulge then curves back left toward
  the hook — swan-neck.
- 撇 starts high (y≈55), makes a smooth arc through the top of the 横
  near x≈150, then sweeps in a CURVE (not straight) to bottom-left,
  belly convex-right so it clearly reads as 撇 not as a diagonal ramp.
- Hook flick modest, UP-and-LEFT.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def taper_stroke(pts, r_start, r_end):
    # Bezier-like smoothing via Catmull-Rom through control points
    dense = []
    for i in range(len(pts) - 1):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        seg_len = math.hypot(x1 - x0, y1 - y0)
        n = max(2, int(seg_len * 2))
        for k in range(n):
            t = k / n
            dense.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t))
    dense.append(pts[-1])
    N = len(dense) - 1
    for i, (x, y) in enumerate(dense):
        t = i / N if N > 0 else 0
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def smooth_curve(ctrl_pts, r_start, r_end, samples=200):
    """Quadratic bezier chain through control points."""
    # Use a simple parametric spline: quadratic beziers between successive triples
    dense = []
    n = len(ctrl_pts)
    for i in range(n - 2):
        p0 = ctrl_pts[i]
        p1 = ctrl_pts[i + 1]
        p2 = ctrl_pts[i + 2]
        # blend halves
        a = ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2) if i > 0 else p0
        c = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2) if i < n - 3 else p2
        for k in range(samples // (n - 2)):
            t = k / (samples // (n - 2))
            x = (1 - t) ** 2 * a[0] + 2 * (1 - t) * t * p1[0] + t * t * c[0]
            y = (1 - t) ** 2 * a[1] + 2 * (1 - t) * t * p1[1] + t * t * c[1]
            dense.append((x, y))
    dense.append(ctrl_pts[-1])
    N = len(dense) - 1
    for i, (x, y) in enumerate(dense):
        t = i / N if N > 0 else 0
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# ---------- Stroke 1: 横折钩 ----------
# top 横 — very slight upward tilt, thin
heng_pts = [(60, 92), (78, 86), (140, 82), (185, 80)]
taper_stroke(heng_pts, r_start=3.5, r_end=4.0)

# shoulder
dab(188, 82, 4.2)

# 竖 body — swan-neck: gentle bulge right, then curve back left toward hook
shu_ctrl = [
    (188, 82),
    (195, 115),
    (198, 155),
    (192, 200),
    (175, 235),
    (150, 250),  # hook base
]
smooth_curve(shu_ctrl, r_start=4.2, r_end=3.5)

# hook flick — up-and-left
hook_base = (150, 250)
hook_len = 26
ang = math.radians(30)
hook_end = (hook_base[0] - hook_len * math.cos(ang), hook_base[1] - hook_len * math.sin(ang))
taper_stroke([hook_base, hook_end], r_start=3.8, r_end=1.0)

# ---------- Stroke 2: 撇 (刀 signature: crosses near RIGHT/shoulder) ----------
# 刀 vs 力: In 力, 撇 crosses 横 near the LEFT end. In 刀, 撇 crosses
# near the RIGHT end (near the shoulder). Top nub small — just a few
# px above 横 — right next to the shoulder. Then sweeps down-left in a
# graceful arc to bottom-left.
pie_ctrl = [
    (172, 62),   # top start — above 横, near RIGHT end (near shoulder)
    (165, 88),   # crosses 横 close to shoulder (x≈165)
    (140, 130),
    (105, 175),
    (70, 225),
    (35, 278),   # bottom-left endpoint
]
smooth_curve(pie_ctrl, r_start=5.0, r_end=0.8)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0033_刀__retry_2/01_刀.png"
img.save(out)
print(f"Saved {out}")
