"""p2_radical_063_山 — G3 coord-bank drawer.

山 decomposition (standard MMH stroke order):
  1. Middle 竖 (tall, centered).
  2. 竖折 (left short vertical descending to bottom, turning right into
     the base horizontal that spans the whole radical).
  3. Right 竖 (short, sitting on the base horizontal).

Bank primitives used:
  - draw_shu  → middle 竖 and right 竖.
  - draw_shu_zhe → left short vertical + bottom horizontal in one call.

TR compliance:
  - Every call carries a deliberate (ox, oy, scale) with a comment.
  - Bottom horizontal spans from x=-50 to x=+50 (via shu_zhe's h_left
    at ox-30*s to h_right at ox+70*s). We solve (ox, scale) so that
    the horizontal endpoints land at (-50, -50) and (+50, -50) in
    math coords, i.e. the whole base is 100 px wide.
    -> scale s = 1.0, ox = -20 -> h_left = -50, h_right = +50, both
       at oy = -50. Left vertical top at y = 90 * s + oy_center; we
       want left top ≈ +5 math -> oy_center = 5 - 90 = -85? Adjust
       via scale to shorten. Use s = 0.75 → h_left = -50 (ox = -27.5),
       h_right = +50 (ox = -27.5 + 70*0.75 = 25.0). That misses. So
       use two calls / different math: parameterize directly.

We inline coord math around draw_shu_zhe by picking scale + ox such
that the horizontal spans exactly [-55, +55] at y = -50, and the
left vertical rises from (-55, -50) to (-55, +10).

  shu_zhe with scale s and (ox, oy):
    v_top    = (ox - 30 s, oy + 90 s)
    v_bottom = (ox - 30 s, oy - 70 s)
    h_right  = (ox + 70 s, oy - 70 s)

  Choose s = 0.80, oy = 6.
    v_top    = (ox - 24, 78 + 6)  = (ox - 24, 84) [not what we want]

The mismatch shows TR5 in action: shu_zhe's internal proportions
(v_top at +90 s above origin, h ends at -70 s below origin, h_right
at +70 s to the right) don't match 山's base proportions cleanly.
Per TR5 we INLINE the recipe for the 竖折 stroke instead of forcing
scale.

Layout targets in math coords (center origin, +y up):
  Middle 竖: top (0, +55), bottom (0, -50).  length 105.
  Left 竖折: left vert from (-50, +5) to (-50, -50); horizontal from
             (-50, -50) to (+50, -50). Length h ≈ 100, v ≈ 55.
  Right 竖: from (+50, +20) to (+50, -50). length 70.

All strokes share y = -50 baseline where the horizontal lives.
"""

from PIL import Image, ImageDraw
import os
import sys

CANVAS_SIZE = 300
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from shu import draw_shu  # noqa: E402


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_shan(t):
    # ---- Stroke 1: middle 竖 (tallest, centered) ----
    # Middle reaches upper third. top (0, +80), bottom (0, -40).
    # length 120 -> half_len 60 -> scale = 0.60. center at (0, +20).
    draw_shu(t, ox=0, oy=20, scale=0.60)

    # ---- Stroke 2: 竖折 (left vertical + bottom horizontal), INLINED ----
    # Per TR5, shu_zhe primitive proportions don't fit; inline the recipe.
    # Left vertical: top (-50, +30), bottom (-50, -40). Length 70.
    # Slight leftward flair at top (calligraphic entry).
    v_top = (-50 + 3, 30)     # small right bias at head, taller
    v_bot = (-50, -40)
    h_left = (-50, -40)
    h_right = (55, -40)       # slight rightward extension past x=50
    ink = 10

    t.line([_to_pixel(*v_top), _to_pixel(*v_bot)],
           fill=(0, 0, 0), width=ink)
    t.line([_to_pixel(*h_left), _to_pixel(*h_right)],
           fill=(0, 0, 0), width=ink)
    # round joint corner
    r = ink // 2
    for pt in (v_top, v_bot, h_left, h_right):
        px, py = _to_pixel(*pt)
        t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))

    # ---- Stroke 3: right 竖 (short, slightly shorter than left) ----
    # target: from (+50, +20) down to (+50, -40). length 60, half_len 30,
    # center (+50, -10). scale = 0.30.
    draw_shu(t, ox=50, oy=-10, scale=0.30)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_shan(t)
    out = os.path.join(HERE, "01_山.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
