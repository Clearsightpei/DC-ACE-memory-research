"""
Retry #1 for p2_radical_133_止.

Prior attempt (memory_index note): drew like 出 — two verticals + top +
bottom bar. Wrong topology.

Canonical 止 structure (4 strokes, per errata fix + GT PNG check):
  1. Central 竖: tall vertical through middle (dominant axis).
  2. Short 横 crossing that 竖 at upper-mid, extending to the left
     (forms the left "shelf"). Actually MMH stroke order is:
     竖 first, then 横 (left short), then 竖 (short left), then 横 (bottom wide).
  3. Short 竖 on the LEFT rising from the left-横 up (the "top-left flick").
     Wait — re-reading GT: the little upper-left stroke is a short 竖
     descending from top to mid, and there's a short 横 flick to the RIGHT
     of the central 竖 at mid-height.
  4. Bottom 横: wide, spanning the full width.

Cross-ref form_catalog:
  - "竖 as through-going axis" for the central tall 竖
  - "横 as top-vs-bottom length-differentiator" for bottom 横 dominance
  - form_catalog sibling table: 止 vs 上 (上 lacks the extra shelf)

Layout (300x300 canvas, math-ish coords, PIL draws top-left origin):
  - Central 竖 at x=150, from y=70 to y=245  (tall vertical axis)
  - Short LEFT 竖 at x=95, from y=125 to y=245 (short left leg)
  - Short 横 flick to the RIGHT of central at mid height:
      from (150,155) to (215,150) — small shelf on the right
  - Bottom 横: wide, from (55,245) to (250,240) — spans full width
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def stroke(pts, width=10):
    """Draw a smooth stroke through the given points as a poly-line."""
    d.line(pts, fill=INK, width=width, joint="curve")
    # end caps
    for (x, y) in (pts[0], pts[-1]):
        d.ellipse([x - width / 2, y - width / 2, x + width / 2, y + width / 2], fill=INK)


# Stroke 1 — central tall 竖 (through-going axis). Tall, dominant.
stroke([(148, 65), (148, 240)], width=11)

# Stroke 2 — short 横 flick to the RIGHT of central 竖 at mid-height
# (the small right shelf — 止's signature). Start just right of central,
# short and slightly upward-slanting.
stroke([(148, 158), (210, 150)], width=10)

# Stroke 3 — short LEFT 竖 (compact left leg — shorter than central).
stroke([(95, 130), (95, 240)], width=10)

# Stroke 4 — bottom wide 横 spanning full width (the dominant 底横).
stroke([(50, 240), (255, 238)], width=12)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_133_止__retry_1/01_止.png"
)
