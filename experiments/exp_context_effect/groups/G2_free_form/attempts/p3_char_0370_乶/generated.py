"""
Render 乶 (Korean hanja: 甫 on top + 乙 on bottom).

Layout from GT:
- Top ~55%: 甫-like element (compact, upper-left biased)
  - horizontal top
  - short 撇 on left
  - vertical central + rectangular "田-ish" interior
  - dot at upper right
- Bottom ~45%: 乙 — large sweeping curve, starts upper-left,
  drops, sweeps right along baseline with terminal hook.

Free-form PIL render, black on white, 300x300.
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def line(p1, p2, w=6):
    d.line([p1, p2], fill=BLACK, width=w)


def curve(points, w=6, steps=60):
    # Piecewise quadratic Bezier through control-point list [P0, C1, P1, C2, P2, ...].
    # Simpler: treat as polyline of many samples via Catmull-Rom.
    from math import comb
    # Bezier of arbitrary degree.
    n = len(points) - 1
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = 0.0
        y = 0.0
        for k, (px, py) in enumerate(points):
            b = comb(n, k) * (t ** k) * ((1 - t) ** (n - k))
            x += b * px
            y += b * py
        pts.append((x, y))
    for a, b in zip(pts, pts[1:]):
        d.line([a, b], fill=BLACK, width=w)


# ---------- TOP: 甫-ish element ----------
# Bounding box roughly x: 70..200, y: 40..165

# Top horizontal (long-ish)
line((70, 55), (200, 55), w=7)

# Left 撇 dropping from just left of the horizontal's left end
curve([(78, 55), (60, 90), (55, 130)], w=7, steps=30)

# Top-right dot/short stroke (a small tick above-right)
curve([(200, 40), (215, 50), (218, 65)], w=7, steps=20)

# Interior box (like 田/用) beneath the top horizontal
# left vertical
line((95, 70), (95, 165), w=6)
# right vertical
line((175, 70), (175, 165), w=6)
# middle vertical extending down past box
line((135, 55), (135, 175), w=7)
# middle horizontal
line((95, 118), (175, 118), w=6)
# bottom horizontal of the box
line((95, 165), (175, 165), w=6)


# ---------- BOTTOM: 乙 (large sweeping curve) ----------
# 乙 = short diagonal top, then a big S-sweep to the right with terminal hook.
# Two sub-strokes to keep it clean.
# (1) short down-left tick at top of the 乙
curve([(95, 175), (85, 190), (70, 215)], w=8, steps=30)
# (2) big sweep: from that endpoint, arc under the top element, sweep right along baseline, hook up
curve(
    [
        (70, 215),
        (110, 260),
        (180, 280),
        (240, 265),
        (245, 245),
    ],
    w=8,
    steps=100,
)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0370_乶/01_乶.png"
)
