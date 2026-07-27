"""
p2_radical_109_攴 — retry_2 (G2)

Errata fix for retry_2 (from errata.md B3 note):
  "卜 top + 又 bottom present but the two halves overlap oddly;
   stacking gap unclear. Fix: enforce a clear ~20 px whitespace band
   between the two halves."

Structure (from GT + errata diagnosis):
  Top half = 卜: short 竖 (vertical) + small dot to its right at mid-height.
  Gap: clear ~20 px whitespace band around y=130-150.
  Bottom half = 又 (form_catalog "又 as two-stroke fork" line 273):
    - 横撇 top: short 横 → shoulder → long down-left 撇
    - 捺 crossing from shoulder area down-right past 撇's tip
    - 捺 dominates in length; wide-splayed V-with-cap silhouette

Layout coords (300x300 canvas, y grows DOWN in PIL):
  Top 卜:
    竖:  (140, 50) → (140, 128)     [short vertical, ~80 px]
    点:  small teardrop centered at (172, 92), ~28 px long, down-right
  --- whitespace band y=128..148 (20 px clear) ---
  Bottom 又:
    横撇:
      横: (85, 155) → (175, 152)     [short horizontal, slight up-tilt]
      shoulder at (175, 152), then
      撇: (175, 152) → (70, 270)     [long down-left sweep]
    捺:
      starts thin near (118, 165), sweeps down-right,
      ends thick at (250, 270)      [dominant right-leg]
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# ---------- helpers ----------

def stroke(pts, widths):
    """Draw a variable-width stroke by dabbing circles along a polyline.
    pts: list of (x,y). widths: list of radii, same length as pts."""
    n = len(pts)
    assert len(widths) == n
    # Densify: interpolate points and widths
    dense_pts = []
    dense_w = []
    for i in range(n - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        w0, w1 = widths[i], widths[i + 1]
        seg = max(1, int(math.hypot(x1 - x0, y1 - y0)))
        for k in range(seg):
            t = k / seg
            dense_pts.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t))
            dense_w.append(w0 + (w1 - w0) * t)
    dense_pts.append(pts[-1])
    dense_w.append(widths[-1])
    for (x, y), r in zip(dense_pts, dense_w):
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier(p0, p1, p2, n=60):
    out = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        out.append((x, y))
    return out


# ============================================================
# TOP HALF: 卜  (short 竖 + right-side dot)
# ============================================================

# 竖: short vertical, uniform thickness ~5 px
vertical_pts = [(140, 50), (140, 90), (140, 128)]
vertical_w = [4.5, 5.0, 4.5]
stroke(vertical_pts, vertical_w)

# 点: small teardrop on the right of the 竖, at mid-height (~y=92).
# Starts thin at upper-left, thickens down-and-right, ends with press.
dot_pts = [(148, 84), (160, 90), (172, 98), (178, 104)]
dot_w = [2.5, 4.0, 5.5, 6.5]
stroke(dot_pts, dot_w)

# ============================================================
# WHITESPACE BAND: y = 128 .. 148  (20 px clear)
# ============================================================

# ============================================================
# BOTTOM HALF: 又  (横撇 + 捺 fork)
# ============================================================

# 横撇: short 横 → shoulder → long down-left 撇.
# Piece 1: the 横 (short, slight up-tilt on the right)
heng_pts = [(85, 158), (130, 154), (172, 152)]
heng_w = [4.5, 5.0, 5.5]  # slight thickening toward shoulder
stroke(heng_pts, heng_w)

# Piece 2: the 撇 (long down-left sweep from the shoulder).
# Bezier for a smooth curving 撇, thick at shoulder → thin at tip.
pie_curve = bezier((172, 152), (135, 200), (70, 272), n=80)
# Render with tapering width from 6 -> 1.5
n_pie = len(pie_curve)
for i, (x, y) in enumerate(pie_curve):
    t = i / (n_pie - 1)
    r = 6.5 - 5.0 * t
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

# Small "shoulder dab" to make the horizontal→撇 corner clean
draw.ellipse((172 - 5.5, 152 - 5.5, 172 + 5.5, 152 + 5.5), fill="black")

# 捺: dominant right-leg, thin start → thick end, crossing the 撇.
# Start thin at upper-middle (near the shoulder's y-line but LEFT of shoulder),
# sweep down-right past the 撇's tip x-range, end with broad terminal foot.
na_curve = bezier((115, 168), (175, 215), (250, 272), n=80)
n_na = len(na_curve)
for i, (x, y) in enumerate(na_curve):
    t = i / (n_na - 1)
    r = 2.0 + 8.0 * t   # thin (2) → thick (10)
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

# Broad terminal foot: extra press at the 捺's terminal tail
foot_x, foot_y = na_curve[-1]
draw.ellipse((foot_x - 10, foot_y - 6, foot_x + 6, foot_y + 6), fill="black")

# ============================================================
# SAVE
# ============================================================

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_109_攴__retry_2/01_攴.png"
img.save(out)
print(f"Saved {out}  size={img.size}")
