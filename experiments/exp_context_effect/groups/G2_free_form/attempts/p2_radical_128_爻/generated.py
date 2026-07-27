"""
爻 (yao) — 4-stroke radical, two chevrons (乂) stacked.

Silhouette check (radical_position_rules.md):
- Aspect: square-ish (~70% × 80%), slightly tall.
- Two visual planes: TOP chevron (smaller, upper-center), BOTTOM
  chevron (larger, wider spread near baseline).
- Center of mass: slight bottom-heavy (bottom 乂 is wider).

Stroke plan (top-down, each 乂 = 撇 then 捺):
1. Top 撇: upper-right → mid-lower-left (short/steep-ish)
2. Top 捺: upper-left of top-撇's top → down-right, thickening
3. Bottom 撇: upper-right → far-lower-left (longer, wider)
4. Bottom 捺: upper-left → far-lower-right, thickening (bigger foot)

The two 乂 do NOT connect; the bottom-撇 starts BELOW the top-捺's tail.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def stroke(p_start, p_end, w_start, w_end, steps=60):
    """Taper stroke via overlapping circles from start-width to end-width."""
    x0, y0 = p_start
    x1, y1 = p_end
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = w_start + (w_end - w_start) * t
        d.ellipse([x - r, y - r, x + r, y + r], fill="black")


def dab(cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill="black")


def curved_stroke(p_start, p_ctrl, p_end, w_start, w_end, steps=80):
    """Quadratic-bezier taper stroke."""
    x0, y0 = p_start
    xc, yc = p_ctrl
    x1, y1 = p_end
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * x0 + 2 * u * t * xc + t * t * x1
        y = u * u * y0 + 2 * u * t * yc + t * t * y1
        r = w_start + (w_end - w_start) * t
        d.ellipse([x - r, y - r, x + r, y + r], fill="black")


# ---- TOP 乂 (smaller, upper) ----
# Top 撇: upper-right, gently bowed rightward, ends lower-left
dab(178, 62, 3)
curved_stroke((178, 62), (150, 100), (108, 148),
              w_start=3.0, w_end=1.6)

# Top 捺: upper-left → lower-right, thin→thick with a small hook-shoulder
# start near the top 撇 origin, cross through it
curved_stroke((118, 62), (152, 110), (188, 148),
              w_start=1.5, w_end=3.5)
# foot press
dab(188, 148, 3.5)

# ---- BOTTOM 乂 (larger, wider) ----
# Bottom 撇: from upper-right (~x=205, y=160), sweeping down-left to far lower-left
dab(205, 160, 3.5)
curved_stroke((205, 160), (155, 210), (65, 268),
              w_start=3.2, w_end=1.6)

# Bottom 捺: upper-left → far lower-right, ending in broad near-horizontal foot
# use two-segment: main diagonal, then a flatter final flare
curved_stroke((95, 160), (165, 225), (235, 265),
              w_start=1.5, w_end=4.5)
# broad flat foot — extend a short near-horizontal splay
stroke((235, 265), (250, 268), w_start=4.5, w_end=2.5, steps=30)
dab(235, 265, 4.5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_128_爻/01_爻.png")
print("wrote 01_爻.png")
