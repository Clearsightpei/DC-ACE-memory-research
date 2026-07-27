"""Render 二 (p3_char_0015) at 300x300, white background, black ink.

二 is 2 horizontal strokes:
- Top 横: SHORTER, upper region, slight upward tilt (right end higher).
- Bottom 横: LONGER (dominant), lower region, slight upward tilt with 顿
  dabs at both ends.

Length ratio follows the form_catalog "short-over-long" family
(analogous to 干's top~110 / bottom~170; 二 exaggerates a bit more
since it's the whole glyph).

Uses PIL brush-dab technique from drawer_memory.md.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def heng(x0, y0, x1, y1, r=5, dun=2, steps=None):
    """Horizontal stroke with 顿-dabs at endpoints and uniform body."""
    if steps is None:
        dist = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
        steps = max(int(dist * 3), 200)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        dab(x, y, r)
    dab(x0, y0, r + dun)
    dab(x1, y1, r + dun)


# --- top 横 (shorter) ---
# Upper region, x from ~95 to ~200 (span ~105 px), gentle upward tilt.
heng(95, 122, 200, 115, r=5, dun=1)

# --- bottom 横 (longer, dominant) ---
# Lower region, x from ~45 to ~260 (span ~215 px), gentle upward tilt.
heng(45, 220, 260, 210, r=5.5, dun=1)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0015_二/01_二.png"
)
