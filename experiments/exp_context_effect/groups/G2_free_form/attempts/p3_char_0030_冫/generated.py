"""
冫 — two-dots-of-water radical.
Reference: gt/phase3/冫.png shows:
  - upper stroke: a small right-going dot/curve (点), positioned upper-left of center
  - lower stroke: a longer, more curved down-left flick (撇-like dot),
    positioned below and slightly left, offset a bit right of the upper
Both dots occupy the LEFT-CENTER of the canvas; radical is left-oriented.

Structure per form_catalog:
  radical family 冫 is like 氵 but two strokes instead of three, no 提 at bottom.
  Both strokes are teardrops (thin→thick), tilted; top one down-right, bottom one down-left/curved.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def brush_stroke(pts, widths):
    """Draw a variable-width tapered stroke by dabbing circles along a path.
    pts: list of (x, y). widths: list of widths same length as pts."""
    n = len(pts)
    # dense sample between adjacent points
    for i in range(n - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        w0, w1 = widths[i], widths[i + 1]
        steps = max(20, int(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5))
        for s in range(steps + 1):
            t = s / steps
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            w = w0 + (w1 - w0) * t
            r = w / 2
            draw.ellipse([x - r, y - r, x + r, y + r], fill="black")


# --- Upper dot 点 ---
# Small curve, opens down-right. Starts thin at upper-left, thickens toward lower-right.
# Position: around (140, 100) → (165, 135).
upper_pts = [
    (138, 100),
    (145, 108),
    (154, 120),
    (163, 132),
    (168, 140),
]
upper_widths = [3, 5, 7, 9, 6]  # taper: thin start, thick middle, slight taper end
brush_stroke(upper_pts, upper_widths)

# --- Lower stroke: longer curved 撇-like dot ---
# Starts thin at upper-right, curves down-left, ends slightly thickening then tapering.
# Position: from (168, 170) to (140, 245).
lower_pts = [
    (170, 170),
    (165, 185),
    (158, 205),
    (150, 225),
    (144, 240),
    (140, 250),
]
lower_widths = [4, 6, 8, 9, 9, 5]
brush_stroke(lower_pts, lower_widths)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0030_冫/01_冫.png")
print("Saved 01_冫.png")
