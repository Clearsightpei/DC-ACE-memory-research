"""
出 (chū) — "to exit / out". 5 strokes.
Structure: two stacked U-shapes sharing a central vertical.
- Bottom U is WIDER and taller.
- Top U is NARROWER and shorter, sitting on top of bottom U's baseline.
- Central vertical: tallest element, spans from top of upper-U through
  bottom of lower-U, extending above the top U.

Stroke order (standard):
  1. 竖 middle vertical (the top portion, going down through upper U)
  2. 竖折 upper-U left-vertical + bottom-horizontal
  3. 竖 upper-U right short vertical
  4. 竖折 lower-U left-vertical + bottom-horizontal (wider, taller)
  5. 竖 lower-U right vertical

Rendered as PIL brush-dabs, 300x300, black on white.
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def stroke_line(p0, p1, r_start=4.5, r_end=4.5, steps=250):
    """Straight tapered stroke via brush-dabs."""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def stroke_polyline(pts, r=4.5):
    """Uniform-width polyline via segments of stroke_line."""
    for a, b in zip(pts[:-1], pts[1:]):
        stroke_line(a, b, r_start=r, r_end=r, steps=200)


# ---------- Layout ----------
# Central vertical: x ≈ 150, extends from y=40 (top) to y=255 (bottom of lower U)
CX = 150

# Upper U (narrower):
UP_LEFT_X = 118
UP_RIGHT_X = 182
UP_TOP_Y = 95         # left/right verticals top
UP_BOT_Y = 155        # baseline (bottom horizontal of upper U)

# Lower U (wider, taller):
LO_LEFT_X = 75
LO_RIGHT_X = 225
LO_TOP_Y = 155        # left/right verticals top (sits on upper-U baseline)
LO_BOT_Y = 260        # baseline (bottom horizontal of lower U)

# ---------- Stroke 1: 竖 center vertical (spans top-to-bottom) ----------
# In the GT the central vertical starts ~40px above the upper-U top and
# runs down to the lower-U baseline.
stroke_line((CX, 55), (CX, LO_BOT_Y - 5), r_start=5.0, r_end=5.0)

# ---------- Stroke 2: 竖折 upper-U (left vertical + bottom horizontal) ----------
stroke_polyline([(UP_LEFT_X, UP_TOP_Y),
                 (UP_LEFT_X, UP_BOT_Y),
                 (UP_RIGHT_X, UP_BOT_Y)], r=4.5)

# ---------- Stroke 3: 竖 upper-U right short vertical ----------
stroke_line((UP_RIGHT_X, UP_TOP_Y), (UP_RIGHT_X, UP_BOT_Y), r_start=4.5, r_end=4.5)

# ---------- Stroke 4: 竖折 lower-U (left vertical + bottom horizontal) ----------
stroke_polyline([(LO_LEFT_X, LO_TOP_Y),
                 (LO_LEFT_X, LO_BOT_Y),
                 (LO_RIGHT_X, LO_BOT_Y)], r=5.0)

# ---------- Stroke 5: 竖 lower-U right vertical ----------
stroke_line((LO_RIGHT_X, LO_TOP_Y), (LO_RIGHT_X, LO_BOT_Y), r_start=5.0, r_end=5.0)

# ---------- Save ----------
out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0158_出/01_出.png"
img.save(out)
print(f"Wrote {out}")
