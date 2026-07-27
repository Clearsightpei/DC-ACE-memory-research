# 月 (yuè, moon) — 4 strokes.
# p2_radical_130_月, G3 coord-bank first attempt.
#
# Decomposition (per GT):
#   Stroke 1: 撇 — long tall curve from upper-mid-right down to lower-left,
#             gently bowed, tail curls left at the bottom.
#   Stroke 2: 横折钩 — top heng across, corner turn down along the right wall,
#             hook up-and-left at the base.
#   Stroke 3: 横 — upper interior bar.
#   Stroke 4: 横 — lower interior bar.
#
# Aspect: taller than 日, narrower than kou. Bottom is open (no bottom heng).
# Approach: inline fresh in PIL px coords per P11 (form-catalog says 月's
# 撇 is a nearly-vertical scoop — bank pie has too much horizontal sweep,
# and shu is too straight). Right side uses inline heng_zhe_gou form
# matched to the tall aspect (heng_zhe_gou primitive scales the width too;
# for a tall thin radical we want the hook slim).

from PIL import Image, ImageDraw
import os

CANVAS = 300
IMG = Image.new("RGB", (CANVAS, CANVAS), "white")
D = ImageDraw.Draw(IMG)


def _tapered_line(draw, p0, p1, w0, w1, steps=24):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = max(1, int(round(w0 + (w1 - w0) * u0)))
        draw.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)


def _tapered_bezier(draw, p0, p1, p2, w0, w1, steps=40):
    """Quadratic Bezier from p0 to p2 with control p1, tapered width."""
    prev = None
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        w = max(1, int(round(w0 + (w1 - w0) * u)))
        if prev is not None:
            draw.line([prev, (bx, by)], fill=(0, 0, 0), width=w)
            r = w / 2.0
            draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


# --- Geometry (PIL px, y grows down) ---
# Box: right wall at x=200. Top y=55, bottom y=250.
# 撇 starts at (128, 55) with a small leftward blob (顿笔),
# runs mostly vertical then scoops left to (85, 255).
X_TOP_LEFT = 128      # where 撇 starts (upper end of left stroke)
X_TOP_RIGHT = 200     # top-right corner (heng-zhe corner)
X_RIGHT = 200         # right wall vertical
Y_TOP = 55
Y_HOOK = 250          # bottom of the right (hook base)
PIE_TAIL_X = 85       # 撇 tail x (scoops left)
PIE_TAIL_Y = 255      # 撇 tail y (roughly at hook level)

# --- Stroke 1: 撇 (long left curve) ---
# Bezier: nearly vertical for the top ~60%, then bows left in the last third.
# To get that shape we use a control point at (X_TOP_LEFT - 4, y_mid_lower).
p0 = (X_TOP_LEFT, Y_TOP)
p2 = (PIE_TAIL_X, PIE_TAIL_Y)
# Control point biased toward upper section vertical, lower section curving:
# place ctrl at same x as head, y at ~70% down.
ctrl_x = X_TOP_LEFT - 2
ctrl_y = Y_TOP + (PIE_TAIL_Y - Y_TOP) * 0.72
_tapered_bezier(D, p0, (ctrl_x, ctrl_y), p2, w0=12, w1=2, steps=56)
# 顿笔 blob at head of 撇 (upper-left bulge visible in GT)
D.ellipse([p0[0] - 7, p0[1] - 4, p0[0] + 4, p0[1] + 7], fill=(0, 0, 0))

# --- Stroke 2: 横折钩 (top heng + right shu + hook) ---
# Top heng from (X_TOP_LEFT, Y_TOP) to (X_TOP_RIGHT, Y_TOP)
_tapered_line(D, (X_TOP_LEFT, Y_TOP), (X_TOP_RIGHT, Y_TOP),
              w0=10, w1=11, steps=24)
# 顿笔 at top-right corner
D.ellipse([X_TOP_RIGHT - 6, Y_TOP - 6, X_TOP_RIGHT + 6, Y_TOP + 6],
          fill=(0, 0, 0))
# Right vertical wall
_tapered_line(D, (X_TOP_RIGHT, Y_TOP), (X_RIGHT, Y_HOOK),
              w0=11, w1=10, steps=32)
# Hook at bottom: short up-and-left tick from (X_RIGHT, Y_HOOK)
hook_end = (X_RIGHT - 22, Y_HOOK - 20)
_tapered_line(D, (X_RIGHT + 1, Y_HOOK + 2), hook_end,
              w0=10, w1=2, steps=16)
# 顿笔 at hook base
D.ellipse([X_RIGHT - 6, Y_HOOK - 6, X_RIGHT + 6, Y_HOOK + 6],
          fill=(0, 0, 0))

# --- Stroke 3: upper interior 横 ---
# Slight tilt up-right, spans from just right of 撇 to just short of right wall.
Y_H1 = 122
_tapered_line(D, (X_TOP_LEFT + 3, Y_H1 + 2), (X_RIGHT - 12, Y_H1 - 1),
              w0=5, w1=7, steps=16)

# --- Stroke 4: lower interior 横 ---
Y_H2 = 185
_tapered_line(D, (X_TOP_LEFT - 6, Y_H2 + 2), (X_RIGHT - 12, Y_H2 - 1),
              w0=5, w1=7, steps=16)


OUT = os.path.join(os.path.dirname(__file__), "01_月.png")
IMG.save(OUT)
print(f"wrote {OUT}")
