"""Render 夕 (evening) radical, 3 strokes, to a 300x300 PNG.

Revised after comparing v1 to GT.
Stroke breakdown (from GT):
  1. 撇 (piě) — starts near top-center, angles slightly then sweeps
     down-and-left ending near bottom-left.
  2. 横折撇 — short flat top starting mid-top, turns and sweeps
     down-left forming the right-side arc; ends higher/shorter than
     stroke 1, curling under.
  3. 点 (diǎn) — small tapered dot in the enclosure middle.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def bezier(p0, p1, p2, p3, steps=120):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = ((1 - t) ** 3) * p0[0] + 3 * ((1 - t) ** 2) * t * p1[0] + 3 * (1 - t) * (t ** 2) * p2[0] + (t ** 3) * p3[0]
        y = ((1 - t) ** 3) * p0[1] + 3 * ((1 - t) ** 2) * t * p1[1] + 3 * (1 - t) * (t ** 2) * p2[1] + (t ** 3) * p3[1]
        pts.append((x, y))
    return pts


def stroke_var(pts, w_start, w_end):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(1, n - 1)
        w = w_start * (1 - t) + w_end * t
        r = w / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


def stroke_poly(segments):
    # segments: list of (p0,p1,p2,p3, w_start, w_end)
    pts_all = []
    widths = []
    for (p0, p1, p2, p3, ws, we) in segments:
        seg = bezier(p0, p1, p2, p3, steps=80)
        for i, pt in enumerate(seg):
            t = i / (len(seg) - 1)
            widths.append(ws * (1 - t) + we * t)
            pts_all.append(pt)
    for (x, y), w in zip(pts_all, widths):
        r = w / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


# Stroke 1: long 撇 (left/outer stroke) — from about (155,80) sweeping
# down-left with a slight bend, ending near (70, 260)
curve1 = bezier((155, 78), (150, 130), (120, 190), (72, 262), steps=140)
stroke_var(curve1, 5.5, 1.5)

# Stroke 2: 横折撇 — short horizontal top from (150,95) going right to (200,90),
# then turning and sweeping down-left curving in, ending near (110, 235)
# We'll model this as two connected beziers.
seg_a = bezier((150, 95), (170, 90), (188, 88), (200, 92), steps=60)
seg_b = bezier((200, 92), (210, 130), (185, 190), (110, 238), steps=120)
stroke_var(seg_a, 4.5, 4.5)
stroke_var(seg_b, 4.5, 1.8)

# Stroke 3: 点 (dot) inside the enclosure — around (150, 175)
dot = bezier((142, 168), (148, 173), (156, 180), (164, 188), steps=40)
stroke_var(dot, 2.5, 5.0)


out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_075_夕/01_夕.png"
img.save(out)
print(f"wrote {out}")
