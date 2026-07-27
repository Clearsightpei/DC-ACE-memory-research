"""
Render 千 (qian) to a 300x300 PNG.

Structure (from form_catalog sibling table 干 vs 千):
- Stroke 1: 撇-lid on top — a short flat-then-diagonal flick from
  upper-right sweeping down-left, acting as the top lid (replaces
  the top 横 of 干). Small tail on the right that curls up.
- Stroke 2: 横 — LONGER than the lid, sits mid-canvas, slight up-tilt.
- Stroke 3: 竖 through-going — straight vertical passing through the
  横, extending well above (into the lid junction) and well below,
  NO hook (per sibling table: "干 no hook; 千 no hook").
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(points, width=8):
    """Draw a polyline with round joins."""
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill=BLACK, width=width)
    for p in points:
        draw.ellipse(
            [p[0] - width / 2, p[1] - width / 2,
             p[0] + width / 2, p[1] + width / 2],
            fill=BLACK,
        )


# ---------- Stroke 1: 撇-lid on top ----------
# Starts upper-right, sweeps down-left. Slight arc so it reads as a
# 撇 not a straight 横. Right end has a small up-curl (the 顿 dab).
# y ~ 75 at start, dipping to ~ 100 at left tip.
lid = [
    (218, 72),   # upper-right start (small curl tip)
    (205, 85),   # curl down
    (180, 88),   # flat-ish shoulder — apex sits near 竖 axis
    (150, 95),   # over the 竖 line
    (115, 110),  # dipping left
    (80, 132),   # left tail tip
]
stroke(lid, width=8)

# ---------- Stroke 2: 横 (middle bar), longer than the lid ----------
# Slight up-tilt (3 deg). Spans wide across the middle.
heng = [
    (48, 168),   # left end
    (150, 160),  # midpoint (slightly higher)
    (255, 155),  # right end
]
stroke(heng, width=9)

# ---------- Stroke 3: 竖 through-going, NO hook ----------
# Passes through the 横; top just under lid junction, bottom well down.
shu = [
    (152, 95),   # top (meets the lid at its apex)
    (152, 175),  # through the 横
    (152, 275),  # bottom (no hook, extends well below)
]
stroke(shu, width=9)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0075_千/01_千.png"
)
print("wrote 01_千.png")
