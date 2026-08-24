"""Render 盎 (abundant) — 央 (top, 5 strokes) + 皿 (bottom, 5 strokes) = 10 strokes.

Top 央 (5 strokes, MMH order):
  1. 竖    left vertical of small top box
  2. 横折  top horizontal + right vertical of small top box
  3. 一    long middle horizontal (extends beyond box)
  4. 撇    down-left from middle
  5. 捺    down-right from middle (taper)

Bottom 皿 (5 strokes, based on p3_char_0195_皿):
  1. 竖    left outer vertical
  2. 竖折  top + right vertical
  3. 竖    inner-left vertical
  4. 竖    inner-right vertical
  5. 一    wide bottom horizontal (extends beyond box)

TIER-0 rule H: components must touch — 央's 撇/捺 sweep down to
y=~150, and 皿's top-horizontal sits at y=~155, so the two components
overlap along their shared boundary.

TIER-0 rule F: use tapered strokes (bez + stroke helpers) for
撇/捺/点 to avoid the C-verdict uniform-polyline regression.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)

def bez(p0, p1, p2, p3, n=48):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0]
        y = u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]
        pts.append((x, y))
    return pts

def stroke(pts, widths=(6, 6)):
    """Draw tapered stroke by sampling ellipses at each point."""
    n = len(pts)
    w0, w1 = widths
    for i, (x, y) in enumerate(pts):
        t = i / max(n - 1, 1)
        r = (w0 * (1 - t) + w1 * t) / 2.0
        d.ellipse([x - r, y - r, x + r, y + r], fill=INK)

def line_tapered(p0, p1, widths=(6, 6), n=30):
    pts = [(p0[0] + (p1[0]-p0[0])*i/n, p0[1] + (p1[1]-p0[1])*i/n) for i in range(n+1)]
    stroke(pts, widths=widths)

def poly(pts, width=6):
    d.line(pts, fill=INK, width=width, joint="curve")

# ============================================================
# TOP: 央 (approx y = 30..150)
# ============================================================

# Stroke 1: 竖 — left vertical of small top box (top of 央)
poly([(122, 35), (122, 88)], width=6)

# Stroke 2: 横折 — top horizontal + right vertical of top box
poly([(119, 33), (183, 32), (183, 88)], width=6)
# Shoulder dab at the corner (TIER-0 rule F.2)
d.ellipse([178, 28, 188, 38], fill=INK)

# Stroke 3: 一 — long middle horizontal (this IS the bottom of the top box, extends far)
poly([(65, 90), (238, 87)], width=7)

# Stroke 4: 撇 — from top-center of horizontal down-left, curved, thick→thin
p_pie = bez((150, 92), (128, 115), (108, 135), (78, 152), n=48)
stroke(p_pie, widths=(9, 3))

# Stroke 5: 捺 — from top-center of horizontal down-right, S-curve, thin→thick with foot
p_na = bez((150, 92), (172, 115), (195, 133), (225, 152), n=48)
stroke(p_na, widths=(4, 10))
d.ellipse([218, 146, 232, 158], fill=INK)

# ============================================================
# BOTTOM: 皿 (approx y = 155..270)
# ============================================================

# Stroke 1: 竖 — left outer vertical (slight inward lean at top)
line_tapered((90, 168), (83, 253), widths=(6, 6))

# Stroke 2: 竖折 — top horizontal then right vertical
poly([(90, 165), (222, 158), (228, 253)], width=6)
# shoulder dab at top-right corner
d.ellipse([224, 154, 234, 164], fill=INK)

# Stroke 3: 竖 — inner-left short vertical
poly([(133, 172), (133, 253)], width=5)

# Stroke 4: 竖 — inner-right short vertical
poly([(178, 172), (181, 253)], width=5)

# Stroke 5: 一 — long bottom horizontal, extends beyond box
poly([(42, 268), (265, 264)], width=8)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0550_盎/01_盎.png")
print("Wrote 01_盎.png")
