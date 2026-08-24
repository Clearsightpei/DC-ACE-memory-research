"""
Render 叉 (chā) — 3 strokes total:
  1. 横撇 (héng-piě): short 横 top-right → shoulder → long down-left 撇
  2. 点 (diǎn): small dot inside the upper region (between shoulder and 撇)
  3. 捺 (nà): starts near where the shoulder is, sweeps down-right,
     crossing the 撇 near vertical middle, ending wider than the 撇 tail.

Silhouette: wide-splayed V-with-cap plus interior dot — the identifying
mark distinguishing 叉 from 又.
Canvas 300x300, white bg, black ink.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke_polyline(pts, width_start, width_end, steps=40):
    """Draw a tapered polyline by sampling segments and dabbing circles."""
    # Sample a dense polyline via linear interpolation between control pts
    dense = []
    total_segs = len(pts) - 1
    for i in range(total_segs):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        for s in range(steps):
            t = s / steps
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            dense.append((x, y))
    dense.append(pts[-1])
    n = len(dense)
    for i, (x, y) in enumerate(dense):
        t = i / max(1, n - 1)
        w = width_start + (width_end - width_start) * t
        r = w / 2
        draw.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


def bezier_quad(p0, p1, p2, n=80):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def stroke_bezier(p0, p1, p2, width_start, width_end, n=80):
    pts = bezier_quad(p0, p1, p2, n)
    for i, (x, y) in enumerate(pts):
        t = i / n
        w = width_start + (width_end - width_start) * t
        r = w / 2
        draw.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


# --- Stroke 1: 横撇 ---
# short 横 across the top: from ~ (90, 110) to (215, 100)
# then shoulder turns down and to the left: long 撇 curving to bottom-left
# Do it as two parts:
#   1a: 横 short flat top
stroke_polyline([(90, 110), (215, 100)], 7, 7, steps=30)
#   1b: 撇 from shoulder (215, 100) curving down-left to (75, 240)
stroke_bezier((215, 100), (170, 175), (75, 240), 8, 4, n=90)

# --- Stroke 2: 点 (interior dot) ---
# Small short diagonal dot inside the upper cavity of the fork.
# Sits between the shoulder and where the 捺 crosses the 撇.
# Oriented down-right, thin→thick.
stroke_bezier((118, 145), (130, 152), (150, 162), 5, 9, n=50)

# --- Stroke 3: 捺 ---
# Starts from around the shoulder area (upper-left of the interior),
# sweeps down-right, crosses the 撇 clearly, and finishes with a broad
# foot in the lower-right. Thin at start → thick at foot.
# Start higher/more-left, end further right for a wide bottom fork.
stroke_bezier((105, 145), (185, 220), (265, 250), 3, 13, n=110)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0064_叉/01_叉.png")
print("wrote 01_叉.png")
