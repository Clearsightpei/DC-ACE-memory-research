"""Render 丫 (p3_char_0040) at 300x300, white bg, black ink.

Structure (from GT): 3 strokes.
  1) 撇 (left diagonal flick) — from upper-left going down-right to a
     central junction point.
  2) 点/短捺 (right diagonal) — from upper-right going down-left to
     the same central junction point.
  3) 竖 (through-going vertical) — from the junction straight down to
     near the bottom. Uniform width, no hook.

Layout guided by GT:
  - Junction center around (150, 140).
  - Left top around (95, 90); right top around (200, 90).
  - Vertical extends from junction down to about y=265.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)


def brush_line(draw, p0, p1, width_start, width_end, steps=60):
    """Interpolate a tapered line by dabbing filled circles."""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = (width_start + (width_end - width_start) * t) / 2.0
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


# Junction of the Y-fork
JX, JY = 150, 140

# Stroke 1: 撇 — left diagonal, upper-left to junction.
# Slight taper (thick at start, thinner at tip).
brush_line(draw, (95, 92), (JX - 2, JY), width_start=7, width_end=5)

# Stroke 2: 点/短捺 — right diagonal, upper-right to junction.
# Slight taper opposite: thin at top-right start, thicker as it dips to junction?
# In GT the right stroke looks a bit heavier at the top-right end tapering into junction.
brush_line(draw, (205, 92), (JX + 2, JY), width_start=6, width_end=6)

# Stroke 3: 竖 — through-going vertical from junction down.
# Uniform width, no hook. Slight 顿 dab at top (already covered by junction).
brush_line(draw, (JX, JY - 2), (JX, 268), width_start=8, width_end=7)

# Small 顿 dab at top of vertical to reinforce the junction.
draw.ellipse((JX - 4, JY - 4, JX + 4, JY + 4), fill=INK)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0040_丫/01_丫.png"
)
