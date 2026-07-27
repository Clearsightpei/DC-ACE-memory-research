"""
p3_char_0169_疋 — G2 attempt

Structure (5 strokes) inferred from GT:
1) Top 横 — short horizontal near top, mid-left to mid-right
2) 竖 (short) descending on the right, ending with a small tick
3) Short 横 — small horizontal near middle-right (the 'T' cross)
4) 撇 — long diagonal from upper mid-left sweeping down-left to bottom
5) 捺 (long, near-horizontal) — sweeping from mid-lower area right and
   down to bottom-right, tapering (a 平捺)

The overall shape sits in the middle-lower part of the canvas; top
horizontal is narrow, bottom捺 is the widest element.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke_line(pts, width=6):
    """Draw a polyline with rounded joints (brush-like)."""
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=BLACK, width=width)
    # round the joints/end-caps
    for x, y in pts:
        r = width / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


def tapered_stroke(pts, w_start=8, w_end=3, steps=40):
    """Draw a stroke tapering from w_start to w_end along a polyline."""
    # sample points along the polyline uniformly
    # compute cumulative lengths
    segs = []
    total = 0.0
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        L = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
        segs.append(L)
        total += L
    if total == 0:
        return
    # walk along
    samples = []
    for s in range(steps + 1):
        t = s / steps * total
        acc = 0.0
        for i, L in enumerate(segs):
            if acc + L >= t or i == len(segs) - 1:
                u = 0 if L == 0 else (t - acc) / L
                x0, y0 = pts[i]
                x1, y1 = pts[i + 1]
                x = x0 + (x1 - x0) * u
                y = y0 + (y1 - y0) * u
                samples.append((x, y))
                break
            acc += L
    for i, (x, y) in enumerate(samples):
        f = i / max(1, len(samples) - 1)
        w = w_start + (w_end - w_start) * f
        r = w / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


# --- Stroke 1: top 横 (a bit tilted, thin) — the "口" top bar
stroke_line([(85, 100), (195, 95)], width=6)

# --- Stroke 2: 竖折 on right — short 竖 down from top-right, then
# a tiny hook/turn. Actually GT shows a small 折 shape at top-right.
# It goes down and slightly right terminating around y≈150.
stroke_line([(195, 95), (200, 108), (195, 155)], width=6)

# --- Stroke 3: short 横 crossbar in the middle (the little "T" cross)
# Under the vertical, small horizontal
stroke_line([(150, 150), (200, 148)], width=5)

# --- Stroke 4: 撇 — long diagonal starting near the LEFT end of the
# top 横, sweeping down-left to the bottom-left area. Slight curve.
tapered_stroke(
    [(88, 100), (80, 140), (70, 180), (55, 220), (40, 258)],
    w_start=8,
    w_end=3,
    steps=60,
)

# --- Stroke 5: 平捺 — starts from mid-body (where 撇 passes through the
# lower-middle area), sweeping right and slightly down, tapering out.
tapered_stroke(
    [(90, 235), (130, 250), (180, 258), (230, 260), (270, 258)],
    w_start=7,
    w_end=3,
    steps=60,
)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0169_疋/01_疋.png"
)
print("Wrote 01_疋.png")
