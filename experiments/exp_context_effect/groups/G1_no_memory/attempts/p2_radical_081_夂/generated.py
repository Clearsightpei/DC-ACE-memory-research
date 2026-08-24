"""G1 render for radical 夂 (3 strokes).

Strokes (per standard MMH decomposition of 夂):
 1. Short 撇 at top — a small tick going down-left.
 2. 横撇 — horizontal-ish top going right then a long 撇 bending down-left.
 3. 捺 — long sweeping stroke down-right, crossing the 撇.

Rendered with PIL on a 300x300 white canvas.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(points, widths):
    """Draw a variable-width stroke by connecting circles + lines."""
    # Draw thick line segments with tapered width.
    n = len(points)
    for i in range(n - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        w1 = widths[i]
        w2 = widths[i + 1]
        # interpolate a few sub-segments for smoother taper
        steps = 12
        for s in range(steps):
            t1 = s / steps
            t2 = (s + 1) / steps
            xa = x1 + (x2 - x1) * t1
            ya = y1 + (y2 - y1) * t1
            xb = x1 + (x2 - x1) * t2
            yb = y1 + (y2 - y1) * t2
            wa = w1 + (w2 - w1) * t1
            wb = w1 + (w2 - w1) * t2
            wm = (wa + wb) / 2
            d.line([(xa, ya), (xb, yb)], fill=BLACK, width=max(1, int(round(wm))))
            # end caps as circles
            r = wm / 2
            d.ellipse([xa - r, ya - r, xa + r, ya + r], fill=BLACK)
            d.ellipse([xb - r, yb - r, xb + r, yb + r], fill=BLACK)


# Stroke 1: short 撇 (top tick) — small tick above the 横撇 corner
s1_pts = [(135, 78), (122, 100)]
s1_w = [5, 3]
stroke(s1_pts, s1_w)

# Stroke 2: 横撇 — horizontal top going right, bends down-left as long 撇
s2_pts = [
    (105, 115),   # start upper-left
    (140, 110),   # horizontal segment
    (175, 115),   # top-right corner
    (168, 135),   # slight descent (the bend)
    (150, 165),   # curve down-left
    (115, 205),   # long 撇 tail
    (80, 240),    # tail tip
]
s2_w = [5, 6, 7, 6, 5, 4, 2]
stroke(s2_pts, s2_w)

# Stroke 3: 捺 — starts intersecting the 撇, sweeps down-right with heavy foot
s3_pts = [
    (135, 145),   # start (intersects stroke 2)
    (160, 175),
    (185, 200),
    (210, 220),
    (232, 232),   # heavy foot
    (255, 235),   # tapered tail extending right
]
s3_w = [4, 6, 8, 10, 11, 3]
stroke(s3_pts, s3_w)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_081_夂/01_夂.png"
img.save(out)
print(f"wrote {out}")
