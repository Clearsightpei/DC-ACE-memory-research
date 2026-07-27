"""
p3_char_0026_冂  —  the 3-sided bracket radical/char (open at bottom).

Structure (from GT):
  Two strokes.
  Stroke 1: left 竖 (short vertical) — starts a bit BELOW the top of the
            right-stroke's horizontal, descends to the bottom-left.
  Stroke 2: 横折(钩) — a horizontal that starts left of / at the top of
            stroke 1, runs rightward, then folds DOWN forming the right
            vertical wall, ending with a small leftward hook at the base.

Aspect-ratio family (per radical_position_rules.md): off-center 匚 —
3-sided box, 1 side open (bottom). Centered horizontally, taller than
wide-flat but not as tall as square.

Canvas: 300 x 300 white, black ink.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def dab(cx, cy, r):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=BLACK)


def taper_line(x1, y1, x2, y2, w1, w2, steps=40):
    """A stroke with tapered width from (x1,y1)@w1 to (x2,y2)@w2."""
    for i in range(steps + 1):
        t = i / steps
        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t
        w = w1 + (w2 - w1) * t
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


# ---------- Stroke 1: left 竖 (short vertical) ----------
# Starts LOWER than the top 横 to leave the characteristic small
# gap at the top-left corner (matches GT). Starts ~(72, 102) and
# drops to (74, 255). Slight rightward drift, blunt end.
dab(72, 102, 7)  # start 顿 dab
taper_line(72, 102, 74, 255, w1=10, w2=8, steps=90)
dab(74, 255, 5)  # blunt end

# ---------- Stroke 2: 横折(钩) — top + right wall + small hook ----------
# GT top 横 starts with a pronounced 顿 dab that sits slightly LOWER
# and to the LEFT of where the horizontal line proper begins, giving
# a small "step" at the top-left. Runs rightward, slight up-tilt,
# then folds DOWN at the top-right corner. Descends the right wall
# and finishes with a tiny leftward hook.
# Start dab (the diagonal press at the left end of top 横).
dab(80, 85, 8)
# Top horizontal, slight up-tilt right (y decreases slightly).
taper_line(80, 82, 228, 74, w1=10, w2=10, steps=100)
# Shoulder dab at the top-right corner.
dab(230, 76, 9)
# Right vertical descending to near bottom, slight inward drift.
taper_line(230, 76, 222, 250, w1=10, w2=9, steps=100)
# Tiny leftward hook at the base (matches faint hook in GT).
taper_line(222, 250, 210, 253, w1=9, w2=4, steps=20)
dab(210, 253, 4)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0026_冂/01_冂.png"
)
print("wrote 01_冂.png")
