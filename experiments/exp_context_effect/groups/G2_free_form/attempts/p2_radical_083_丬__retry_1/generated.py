"""
丬 (radical 083) — retry_1.

Prior attempt: two dots + straight 竖 (looked like 冫 + 丨). The 点
and 提 were too far LEFT and did not touch the 竖.

Fix (from errata):
- 点 top ~ (100, 90) with down-right taper.
- 提 middle rising up-right from (90, 155) → TOUCHING the 竖 at right.
- 竖 straight vertical at x≈175, spanning y=70..260.

Cross-ref: form_catalog "点" entries + "竖 as through-going axis".
Silhouette: asymmetric bracket — small strokes on LEFT bracketing
the tall 竖 on the RIGHT.
"""

from PIL import Image, ImageDraw
import math

W = H = 300
BG = 255
INK = 0
img = Image.new("L", (W, H), BG)
d = ImageDraw.Draw(img)


def dab(cx, cy, r):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=INK)


def taper_stroke(p0, p1, r0, r1, steps=48, bow=0.0, bow_dir=(0, 0)):
    """Draw a tapered stroke via overlapping dabs from p0 to p1.
    bow: 0..1 pull toward a control point offset by bow_dir * bow_amt.
    """
    x0, y0 = p0
    x1, y1 = p1
    # Control point for a slight curve if bow != 0
    mx = (x0 + x1) / 2 + bow_dir[0] * bow
    my = (y0 + y1) / 2 + bow_dir[1] * bow
    for i in range(steps + 1):
        t = i / steps
        # Quadratic Bezier
        xa = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * mx + t * t * x1
        ya = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * my + t * t * y1
        r = r0 + (r1 - r0) * t
        dab(xa, ya, r)


# ---------- Stroke 1: 点/短撇 (top-left, sweeping down-LEFT) ----------
# GT shows the top stroke starting near the 竖's upper area and sweeping
# DOWN-and-LEFT (thick→thin), gently curved. This is a 短撇 form.
# Start near the 竖 (upper) at x≈165, y≈78, end at x≈95, y≈128.
taper_stroke(
    p0=(165, 78),
    p1=(95, 128),
    r0=6.5,
    r1=1.8,
    steps=48,
    bow=10.0,
    bow_dir=(0, -1),  # slight upward bow → concave-down curve
)
# Start 顿 press near the 竖.
dab(165, 78, 6)


# ---------- Stroke 2: 提 (middle rising stroke) ----------
# Starts lower-left, rises up-right, tip TOUCHES the 竖.
# Thick at start, thin at tip.
taper_stroke(
    p0=(80, 178),
    p1=(172, 152),
    r0=7.0,
    r1=2.0,
    steps=50,
    bow=0.0,
    bow_dir=(0, 0),
)
# Start 顿 press.
dab(80, 178, 7)


# ---------- Stroke 3: 竖 (tall right vertical) ----------
# Straight vertical at x=175 spanning y=70..262 with 顿 press top & bottom.
x_v = 175
r_v = 6
# Top 顿 dab
dab(x_v, 72, r_v + 1)
# Body — draw as filled rectangle with rounded caps
d.rounded_rectangle(
    (x_v - r_v, 72, x_v + r_v, 262),
    radius=r_v,
    fill=INK,
)
# Bottom slight taper (small dab)
dab(x_v, 262, r_v)


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_083_丬__retry_1/01_丬.png")
print("saved 01_丬.png")
