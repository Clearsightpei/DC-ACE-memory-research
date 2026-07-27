"""
Render 水 (radical, 4 strokes) at 300x300, white bg, black ink.

Analysis of GT (from viewing gt/phase2/水.png):
- Silhouette family: square-ish, centered, ~70% wide x ~65% tall
- Center of mass: centered, slightly bottom-heavy from the sweeping legs
- Stroke count: 4 named strokes (per MMH radical for 水)
  1. 竖钩 (vertical with tiny hook to left at bottom) — the central axis
  2. 横撇 (small 横+撇 combo on the upper-left) — the horizontal-then-flick
  3. 撇 (long sweeping 撇) — the left leg
  4. 捺 (long sweeping 捺) — the right leg
- Central 竖钩 dominates vertically; the two "wings" sweep out from mid-height.
- Left side has an extra small 横撇 detail above the sweeping 撇 leg.

PIL brush-dab technique: draw thick tapered strokes using overlapping
ellipse dabs along a Bezier/interpolated path with variable radius.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def dab_stroke(pts, r0, r1):
    """Draw a tapered stroke by dabbing ellipses along interpolated pts.
    Radius linearly interpolates from r0 (start) to r1 (end)."""
    if len(pts) < 2:
        return
    # Densify path
    dense = []
    for i in range(len(pts) - 1):
        x1, y1 = pts[i]
        x2, y2 = pts[i + 1]
        dist = math.hypot(x2 - x1, y2 - y1)
        steps = max(2, int(dist))
        for s in range(steps):
            t = s / steps
            dense.append((x1 + (x2 - x1) * t, y1 + (y2 - y1) * t))
    dense.append(pts[-1])
    n = len(dense)
    for i, (x, y) in enumerate(dense):
        t = i / max(1, n - 1)
        r = r0 + (r1 - r0) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


def bezier(p0, p1, p2, n=40):
    """Quadratic bezier sampling."""
    out = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        out.append((x, y))
    return out


# ---- Stroke 1: 竖钩 (central vertical with tiny hook at bottom-left) ----
# Starts near top-center, ends near bottom-center with a small leftward flick.
# Extend it further down to match GT's tall central axis.
vertical = [(155, 45), (154, 90), (153, 140), (152, 195), (151, 250)]
dab_stroke(vertical, r0=4.8, r1=4.0)
# The little hook: a short flick going up-left from the bottom
hook = [(151, 250), (143, 246), (136, 240)]
dab_stroke(hook, r0=4.0, r1=1.8)

# ---- Stroke 2: 横撇 (short horizontal then a flick down-left) ----
# Small piece up-left of the vertical, higher than before.
h_start = (95, 118)
h_mid = (122, 116)   # short horizontal to the right
# Do it as two segments: 横 then 撇 as continuous stroke
heng_pt = [h_start, (108, 117), h_mid]
dab_stroke(heng_pt, r0=2.6, r1=3.0)
# Flick down-left (the 撇 part) — steep and short
flick = [h_mid, (112, 135), (100, 152), (88, 165)]
dab_stroke(flick, r0=3.0, r1=1.5)

# ---- Stroke 3: 撇 (long sweeping left leg) ----
# Starts near middle-left of central axis area, sweeps down-left to lower-left.
# Adjust to start slightly right of center axis, curve out further.
pie_pts = bezier((138, 140), (105, 200), (55, 255), n=60)
n = len(pie_pts)
for i, (x, y) in enumerate(pie_pts):
    t = i / (n - 1)
    r = 4.8 * (1 - t) + 1.5 * t
    draw.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)

# ---- Stroke 4: 捺 (long sweeping right leg) ----
# Starts near middle-central, sweeps down-right, thickens toward end with foot.
na_pts = bezier((165, 140), (205, 195), (260, 245), n=60)
n = len(na_pts)
for i, (x, y) in enumerate(na_pts):
    t = i / (n - 1)
    if t < 0.85:
        r = 2.5 + (5.8 - 2.5) * (t / 0.85)
    else:
        r = 5.8 + (7.5 - 5.8) * ((t - 0.85) / 0.15)
    draw.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)

# Small terminal press for 捺's foot
draw.ellipse((252, 238, 268, 252), fill=BLACK)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_119_水/01_水.png"
)
print("wrote 01_水.png")
