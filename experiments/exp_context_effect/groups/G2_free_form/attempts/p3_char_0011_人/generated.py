"""Render 人 (person) — two-stroke apex character.

Guidance used from G2 memory:
- form_catalog 捺 as right-leg of two-stroke apex (人/大/天/木-lower):
  starts THIN at apex, ends THICK at lower-right with broad flat foot.
- Sibling rule (人 vs 入): 人 has apex at same y for both strokes.
  BUT: in the clean GT the 捺 in fact starts slightly BELOW & RIGHT of
  the 撇's top — the two strokes do NOT share a single apex pixel;
  they cross near the top with a small visible gap. That's the
  handwritten character. Rendering that way.
- radical_position_rules: silhouette-first — 人 is a wide-flat
  triangular splay, bottom-heavy, roughly square aspect. GT shows
  strokes extending nearly to the bottom edge; the top starts around
  y=75–105 and both tails reach ~y=270.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def sample_bezier(p0, p1, p2, n=200):
    """Quadratic Bezier sampling."""
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def stroke_taper(pts, w_start, w_end):
    """Draw a tapered stroke by dabbing circles along the path."""
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1) if n > 1 else 0
        r = w_start * (1 - t) + w_end * t
        draw.ellipse(
            [x - r, y - r, x + r, y + r],
            fill="black",
        )


# ---- Stroke 1: 撇 (top → bottom-left, curves leftward) ----
# Top at (140, 75). End at (35, 275) — reaches farther left/down for
# the wider triangular splay seen in the GT.
p0 = (140, 75)
p2 = (35, 275)
# Control point pulled right for a natural pie curve.
mid = ((p0[0] + p2[0]) / 2, (p0[1] + p2[1]) / 2)
p1 = (mid[0] + 24, mid[1] - 4)
pie_pts = sample_bezier(p0, p1, p2, n=240)
# 撇 tapers thick-to-thin: fat near top, pointy tail.
stroke_taper(pie_pts, w_start=5.5, w_end=1.0)

# Small starting 顿 dab (upper-right tick before the sweep).
draw.ellipse([140 - 4, 75 - 5, 140 + 5, 75 + 4], fill="black")


# ---- Stroke 2: 捺 (starts BELOW and RIGHT of 撇's top,
#                    sweeps to bottom-right with thick flat foot) ----
# Start at (158, 115). End at (275, 260) — sweep wider to the right.
q0 = (158, 115)
q2 = (275, 258)
qmid = ((q0[0] + q2[0]) / 2, (q0[1] + q2[1]) / 2)
# Bow the 捺 downward (sagging arc).
q1 = (qmid[0] - 6, qmid[1] + 20)
na_pts = sample_bezier(q0, q1, q2, n=240)
# 捺 tapers thin-to-thick.
stroke_taper(na_pts, w_start=1.5, w_end=8.0)

# Broad flat terminal foot on the 捺 — horizontally elongated dab.
foot_x, foot_y = na_pts[-1]
for k in range(0, 14):
    r = 7.5 - k * 0.3
    if r <= 1:
        break
    draw.ellipse(
        [foot_x + k * 1.3 - r, foot_y - r * 0.55,
         foot_x + k * 1.3 + r, foot_y + r * 0.55],
        fill="black",
    )


img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p3_char_0011_人/01_人.png"
)
print("wrote 01_人.png")
