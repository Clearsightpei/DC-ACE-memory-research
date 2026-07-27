"""
牛 (radical 106) — retry_1.

Prior attempt failure: top 撇 was too short/near-horizontal, reading as
a small tick attached to the upper 横. Also upper and lower 横 lengths
were not sufficiently differentiated.

Fix for retry (from errata):
  - Top 撇: proper diagonal, ~65 px long, sweeping from upper-middle
    (145, 55) down-left to (95, 115). Steep angle so it reads as a
    real 撇, not a horizontal tick. Thick->thin taper.
  - Upper 横 shorter (~105 px), slightly rising left->right.
  - Lower 横 clearly LONGER (~180 px), positioned lower on canvas.
  - 竖 passes THROUGH all horizontals, extending ~15 px above top 横
    intersection and well below the bottom 横 (through-going axis).
  - Length ratio upper:lower ~= 0.58 (exaggerate the difference).
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def stroke_tapered(draw, p0, p1, r0, r1, steps=60):
    """Draw a tapered line from p0 to p1, radius r0 -> r1."""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def stroke_bezier(draw, p0, p1, p2, r0, r1, steps=80):
    """Quadratic Bezier with taper."""
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


# --- Stroke 1: top 撇 (steep down-left diagonal) ---
# Start upper-middle-ish, end at where the upper 横 will begin (left side).
# Gentle rightward bow via bezier control pulled slightly right.
stroke_bezier(
    draw,
    p0=(150, 55),          # start upper (顿 dab)
    p1=(130, 80),          # control pulled slightly right for gentle bow
    p2=(90, 118),          # end lower-left (tip)
    r0=5.5, r1=1.5,
    steps=90,
)

# --- Stroke 2: upper 横 (shorter, slight rise left->right) ---
# Starts near where 撇 tip lands and extends rightward past the vertical.
stroke_tapered(
    draw,
    p0=(92, 120),
    p1=(198, 108),         # slight rise
    r0=4.5, r1=4.5,
    steps=80,
)
# Small 顿 press at right end
draw.ellipse((198 - 5, 108 - 5, 198 + 5, 108 + 5), fill="black")

# --- Stroke 3: lower 横 (LONGER, dominant) ---
stroke_tapered(
    draw,
    p0=(55, 178),
    p1=(245, 172),         # slight rise but almost flat
    r0=5.0, r1=5.0,
    steps=100,
)
# 顿 dabs at both ends
draw.ellipse((55 - 6, 178 - 6, 55 + 6, 178 + 6), fill="black")
draw.ellipse((245 - 6, 172 - 6, 245 + 6, 172 + 6), fill="black")

# --- Stroke 4: 竖 (through-going axis) ---
# Passes through both 横s, extends ~15 px above upper 横 and well below lower 横.
# Positioned slightly left of center (~x=142) matching GT.
stroke_tapered(
    draw,
    p0=(142, 92),          # above upper 横
    p1=(142, 275),         # well below lower 横
    r0=5.0, r1=4.0,
    steps=120,
)
# 顿 dab at top
draw.ellipse((142 - 6, 92 - 6, 142 + 6, 92 + 6), fill="black")

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_106_牛__retry_1/01_牛.png"
)
