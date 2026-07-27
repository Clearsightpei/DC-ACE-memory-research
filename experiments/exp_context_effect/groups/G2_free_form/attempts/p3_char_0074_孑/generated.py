"""
孑 — 3 strokes:
  1) 横撇 — flat 横 across top that turns down-left into a 撇 tail.
  2) 弯钩 — smooth arc-like vertical body starting near the 横撇
     shoulder, sweeping down and slightly left, ending with a
     tiny up-and-left hook flick.
  3) 提 — a short rising stroke from the middle of the body
     going up-right. IMPORTANT: this stroke does NOT cross to
     the left of the body — that would make it 子, not 孑.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(cx, cy, r):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill="black")


def stroke(pts, r_start, r_end):
    """Draw a stroke as densely-sampled brush dabs along a polyline
    (or single segment) with linear width taper."""
    total = 0.0
    seg = []
    for i in range(len(pts) - 1):
        d = math.hypot(pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1])
        seg.append(d)
        total += d
    acc = 0.0
    for i in range(len(pts) - 1):
        d = seg[i]
        n = max(4, int(d * 2))
        for k in range(n + 1):
            t_local = k / n
            # global t across whole stroke, for width
            t = (acc + t_local * d) / total if total > 0 else 0
            x = pts[i][0] + (pts[i + 1][0] - pts[i][0]) * t_local
            y = pts[i][1] + (pts[i + 1][1] - pts[i][1]) * t_local
            r = r_start + (r_end - r_start) * t
            dab(x, y, r)
        acc += d


def bezier(p0, p1, p2, r_start, r_end, n=80):
    """Quadratic Bezier with width taper."""
    for k in range(n + 1):
        t = k / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# --- Stroke 1: 横撇 -------------------------------------------------
# Flat top 横 from left to right, small upward tilt, then shoulder
# and a 撇 tail flicking down-and-left.
stroke([(75, 75), (210, 65)], r_start=3.0, r_end=4.0)
# shoulder press dab
dab(210, 65, 5.5)
# 撇 tail — slight bow with control point pulled left
bezier((210, 65), (190, 95), (165, 120), r_start=5.0, r_end=1.5, n=70)


# --- Stroke 2: 弯钩 -------------------------------------------------
# Body starts near shoulder, curves down and slightly left, ending
# lower on canvas, then hook flicks up-and-left.
bezier((198, 85), (178, 180), (155, 260), r_start=3.5, r_end=3.5, n=110)
# hook flick — from bottom endpoint, up-and-left, tapering to a point
bezier((155, 260), (140, 255), (120, 240), r_start=3.5, r_end=1.0, n=50)


# --- Stroke 3: 提 --------------------------------------------------
# Rising stroke from the RIGHT side of the body, going UP-and-RIGHT.
# Does NOT extend to the left of the body (that would make it 子).
# Placed roughly mid-body (around y ~ 175).
stroke([(180, 180), (260, 150)], r_start=4.5, r_end=1.2)


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0074_孑/01_孑.png")
