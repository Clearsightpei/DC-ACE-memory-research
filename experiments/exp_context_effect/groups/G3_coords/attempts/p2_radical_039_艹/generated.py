# p2_radical_039_艹 (cao, "grass") — G3 coord format.
#
# GT observation:
#   - A long horizontal 横 that tilts slightly UP to the right (calligraphic
#     rise), centered vertically around the middle of the canvas.
#   - Two short 竖 (verticals) crossing the 横. Left one sits ~1/3 across
#     the heng; right one sits ~2/3 across. Both extend BELOW the heng
#     more than above (tops just barely poke above; tails drop noticeably).
#   - Right vertical often has a slight left-lean (撇-like); left one is
#     nearly vertical or slight right-lean.
#
# Composition strategy (per TR1-TR5):
#   - Heng: reuse draw_heng from bank at scale ~1.1 to be nice and long,
#     with a slight upward tilt done by tilting the endpoints in math coords
#     (bank heng is flat, so we inline a tilted version rather than force
#     the bank primitive with rotation it doesn't support).
#   - Verticals: inline directly (short shu; scale=0.28 is below the
#     TR5 threshold of 0.4 for reusing bank primitives, so inline).

import sys
import os
from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel (top-left, +y down)."""
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_tilted_heng(t, x_left, x_right, y_left, y_right, thickness=11):
    """Inlined tilted heng — bank heng is flat; we need a rising line."""
    p_left = _to_pixel(x_left, y_left)
    p_right = _to_pixel(x_right, y_right)
    t.line([p_left, p_right], fill=(0, 0, 0), width=thickness)
    # Round caps to avoid visible flat ends.
    r = thickness / 2.0
    for (px, py) in (p_left, p_right):
        t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def draw_short_vertical(t, ox, oy_top, oy_bot, thickness=9, lean=0.0):
    """Inlined short 竖 with optional small lean (top x = ox + lean,
    bottom x = ox - lean, i.e. positive lean = leaning right at top)."""
    p_top = _to_pixel(ox + lean, oy_top)
    p_bot = _to_pixel(ox - lean, oy_bot)
    t.line([p_top, p_bot], fill=(0, 0, 0), width=thickness)
    r = thickness / 2.0
    for (px, py) in (p_top, p_bot):
        t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # --- Heng: long, centered near vertical middle, tilted slightly upward
    # to the right. In math coords: y increases up.
    # Center of heng at (ox=0, oy=0) roughly; left endpoint drops a bit,
    # right endpoint lifts a bit. Length ~ 200 px total.
    x_left = -115
    x_right = 115
    y_left = -12   # dips a bit more below center on the left
    y_right = +18  # stronger rise on the right (calligraphic tilt)
    draw_tilted_heng(t, x_left, x_right, y_left, y_right, thickness=10)

    # --- Left vertical: crosses the heng at about x = -40.
    # The heng at x=-40 has y-value linearly interpolated:
    #   frac = (-40 - x_left) / (x_right - x_left) = 70/220 ≈ 0.318
    #   y_at_x = y_left + frac * (y_right - y_left) = -5 + 0.318 * 17 ≈ 0.4
    # Vertical extends from ~+18 (just above heng) down to ~-55 (below).
    draw_short_vertical(t, ox=-40, oy_top=+18, oy_bot=-58,
                        thickness=9, lean=+3)

    # --- Right vertical: crosses the heng at about x = +38.
    #   frac = (38 - (-110)) / 220 = 148/220 ≈ 0.673
    #   y_at_x = -5 + 0.673 * 17 ≈ 6.4
    # Vertical extends from ~+22 down to ~-55, with a slight left-lean at
    # bottom (撇-like feel).
    draw_short_vertical(t, ox=+42, oy_top=+28, oy_bot=-58,
                        thickness=9, lean=-8)

    out_path = os.path.join(os.path.dirname(__file__), "01_艹.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
