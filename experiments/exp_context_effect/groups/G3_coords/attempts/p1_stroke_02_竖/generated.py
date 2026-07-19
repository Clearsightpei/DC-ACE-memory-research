# p1_stroke_02_竖 — vertical stroke, top to bottom
#
# Draws one 竖 stroke centered on a 300x300 canvas.
# Uses a coord-form primitive draw_shu(draw, ox, oy, scale) inline
# (mirroring the shape of the shared heng.py primitive).

from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel (top-left, +y down)."""
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_shu(draw: ImageDraw.ImageDraw, ox: float = 0.0, oy: float = 0.0,
             scale: float = 1.0) -> None:
    """Draw one 竖 (vertical) stroke centered at (ox, oy) with given scale.

    Canonical unit 竖: length 200 px, thickness 12 px, from top to bottom.
    """
    half_len = 100.0 * scale
    thickness = max(1, int(round(12.0 * scale)))

    x_top, y_top = _to_pixel(ox, oy + half_len)
    x_bot, y_bot = _to_pixel(ox, oy - half_len)

    draw.line([(x_top, y_top), (x_bot, y_bot)],
              fill=(0, 0, 0), width=thickness)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    # Centered, canonical scale
    draw_shu(draw, ox=0, oy=0, scale=1.0)
    out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p1_stroke_02_竖/01_竖.png"
    img.save(out)
    print(f"Saved {out} ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    main()
