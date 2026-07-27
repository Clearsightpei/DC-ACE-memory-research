"""Render 牙 (radical, 4 strokes) to 300x300 PNG.

Stroke analysis from GT (memory-informed):
  Stroke 1: 横 — short horizontal at upper-left, tilts slightly down-left
            (it's actually the top of a 横折 combining with stroke 2)
  Stroke 2: 竖折 — short 竖 going down from stroke-1 end, then flat 横
            going right (forms the small hook shape upper-left)
  Stroke 3: 竖钩 — long vertical starting from top-right of the flat
            piece, descends straight down, small hook at bottom-left
  Stroke 4: 撇 — long sweeping 撇 that starts at the top-right area,
            crosses through the body diagonally down to lower-left.
            This is the "body-crossing diagonal" 撇 (form_catalog).

Layout (silhouette-first):
  aspect: square-ish (~70% x, ~75% y)
  center of mass: centered, with tail extending lower-left
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def stroke(points, width=6):
    """Draw a stroke as a polyline with round joints/caps."""
    for i in range(len(points) - 1):
        d.line([points[i], points[i + 1]], fill=INK, width=width)
    # round the joints
    for p in points:
        d.ellipse(
            [p[0] - width // 2, p[1] - width // 2,
             p[0] + width // 2, p[1] + width // 2],
            fill=INK,
        )


def tapered_stroke(points, w_start=6, w_end=6, steps=40):
    """Draw a stroke sampled along polyline with tapering width."""
    # flatten polyline into evenly-sampled points
    import math
    seg_lens = []
    total = 0.0
    for i in range(len(points) - 1):
        dx = points[i + 1][0] - points[i][0]
        dy = points[i + 1][1] - points[i][1]
        L = math.hypot(dx, dy)
        seg_lens.append(L)
        total += L
    if total == 0:
        return
    for k in range(steps + 1):
        t = k / steps
        target = t * total
        # find segment
        acc = 0.0
        for i, L in enumerate(seg_lens):
            if acc + L >= target or i == len(seg_lens) - 1:
                lt = (target - acc) / L if L > 0 else 0
                x = points[i][0] + lt * (points[i + 1][0] - points[i][0])
                y = points[i][1] + lt * (points[i + 1][1] - points[i][1])
                break
            acc += L
        w = w_start + (w_end - w_start) * t
        r = w / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill=INK)


# --- Stroke 1: 横 (short top horizontal, upper-left) ---
# starts around x=95, y=95, ends around x=150, y=100 (slight down-tilt)
tapered_stroke([(95, 95), (150, 103)], w_start=7, w_end=6, steps=25)

# --- Stroke 2: 竖折 (drops down from stroke-1's right end, then flat right) ---
# The horizontal must EXTEND past the right vertical (crosses through it)
tapered_stroke([(150, 103), (110, 158)], w_start=6, w_end=6, steps=25)
# horizontal crosses through the right vertical, extends to ~x=230
tapered_stroke([(110, 158), (230, 158)], w_start=6, w_end=6, steps=35)

# --- Stroke 3: 竖钩 (right-side vertical hook, descends from top-right) ---
# Starts higher near x=210, y=88 (above the middle horizontal), goes
# straight down through it, ends near y=265 with small left hook
tapered_stroke([(212, 88), (215, 262)], w_start=7, w_end=6, steps=45)
# small hook at bottom pointing left
tapered_stroke([(215, 262), (195, 250)], w_start=6, w_end=3, steps=15)

# --- Stroke 4: 撇 (long sweeping diagonal from upper area to lower-left) ---
# Body-crossing 撇: starts at ~(200, 90) up top, sweeps down-left through
# the body, exits at lower-left ~(50, 278). Gentle bow.
tapered_stroke(
    [(200, 92), (172, 145), (135, 198), (92, 242), (50, 280)],
    w_start=7, w_end=3, steps=90,
)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_127_牙/01_牙.png")
print("saved 01_牙.png")
