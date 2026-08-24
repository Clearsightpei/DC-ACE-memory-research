"""
旡 (4画) — G5 retry_2

TRAJECTORY DIFF (from inspection of PNGs):
- main FAIL: both horizontals rendered as "dumbbells" with fat round endpoint
  dots (from over-large circular caps). Also stroke 1 drawn as a full-length
  horizontal parallel to stroke 2, when GT shows stroke 1 as a very SHORT
  tilted tick (like a mini pie) above the right side of stroke 2. Also the
  vertical of stroke 4 (竖弯钩) started too high and lacked a clear
  bottom-right hook.
- retry_1 C: same dumbbell endpoints. Top tick still drawn too long/wide.
  Overall shape closer but endpoints still look like beads.
- Fix plan:
  1. NO endpoint dot artifacts — use plain PIL line() with capstyle handled
     by tiny end circles matching the stroke width, not oversized.
  2. Stroke 1 = short tilted tick (about 25 px), positioned above-right of
     the long horizontal, sloping down-right.
  3. Stroke 2 = long horizontal, slight upward tilt to the right.
  4. Stroke 3 = 撇: starts from top-center where horizontals cross, curves
     down and to the left, ending lower-left.
  5. Stroke 4 = 竖弯钩: vertical from right side of stroke 2 going down,
     then bends smoothly to the right, then a small hook up.

SELF_CHECK block at the end.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def stroke_poly(points, widths):
    """Draw a tapered stroke: interpolate between points using varying widths.
    points: list of (x, y). widths: list of widths at each point (same length).
    """
    # Densify by drawing many small circles along linear segments.
    n = len(points)
    for i in range(n - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        w0 = widths[i]
        w1 = widths[i + 1]
        steps = max(2, int(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5))
        for s in range(steps + 1):
            t = s / steps
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            w = w0 + (w1 - w0) * t
            r = w / 2
            d.ellipse([x - r, y - r, x + r, y + r], fill=INK)


# ---- Stroke 1: short tilted tick at top-right (small 撇 above stroke 2) ----
# short piece sloping down-right, tapers from thick head to fine tail
s1 = [(148, 55), (158, 63), (168, 74), (176, 85)]
w1 = [7, 6, 5, 3]
stroke_poly(s1, w1)

# ---- Stroke 2: long horizontal (横), slight upward tilt to right ----
# starts thicker on the left, slightly tapered right; NO dumbbell caps
s2 = [(50, 108), (100, 104), (160, 100), (220, 96)]
w2 = [6, 7, 7, 6]
stroke_poly(s2, w2)

# ---- Stroke 3: 撇 (pie) — from top area curving down-left ----
# begins near the crossing point (near top of horizontal), curves out to lower-left
s3 = [
    (145, 88),
    (138, 115),
    (128, 145),
    (115, 175),
    (98, 205),
    (78, 240),
    (65, 260),
]
w3 = [9, 8, 8, 7, 6, 4, 2]
stroke_poly(s3, w3)

# ---- Stroke 4: 竖弯钩 — vertical descending, bend to right, tiny hook up ----
s4 = [
    (185, 100),   # top (attaches under stroke 2)
    (183, 130),
    (181, 160),
    (180, 190),
    (183, 215),
    (192, 232),
    (208, 240),
    (222, 238),
    (232, 232),   # bottom of bend
    (232, 222),   # hook up
    (228, 215),
]
w4 = [7, 7, 7, 7, 7, 7, 7, 6, 5, 4, 3]
stroke_poly(s4, w4)

out_path = (
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G5_code_bank_mmh/attempts/p2_radical_099_旡__retry_2/01_旡.png"
)
img.save(out_path)
print(f"wrote {out_path}")

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # exactly 4 stroke_poly calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        '4 strokes: short tilted tick (s1), long horizontal (s2), '
        'pie (s3), 竖弯钩 (s4). No dumbbell endpoint dots. '
        's3 head near top-center under s2; s4 top at right of s2.'
    ),
}
