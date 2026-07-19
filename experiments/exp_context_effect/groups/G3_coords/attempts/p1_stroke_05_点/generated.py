# generated.py — p1_stroke_05_点 (dian, short diagonal dot)
#
# 点画：短小的斜点。A short, teardrop-shaped diagonal dot that starts
# thin at the upper-left, thickens as it descends toward the lower-right,
# and terminates in a rounded, slightly heavier tail. Canonical size:
# runs from about (-15, +25) to (+18, -20) in math coords centered at
# canvas center (300x300, +y up).
#
# Coordinate convention matches G3's pie.py / heng.py: math coords
# (center origin, +y up), converted to PIL pixel coords for rendering.

from PIL import Image, ImageDraw
import os

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel (top-left, +y down)."""
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_dian(draw: ImageDraw.ImageDraw, ox: float = 0.0, oy: float = 0.0,
              scale: float = 1.0) -> None:
    """Draw one 点 (short diagonal dot) stroke.

    Canonical unit 点: starts thin at upper-left (-15, +25), curves down
    and rightward to a heavier rounded tail at (+18, -20). Thickness
    grows from ~3 px at the head to ~14 px at the tail (opposite of
    撇's taper — 点 is heavier at the bottom).
    """
    # Endpoints in math coords, relative to (ox, oy)
    x0, y0 = -15.0 * scale, 25.0 * scale     # thin upper-left head
    x1, y1 = 18.0 * scale, -20.0 * scale     # heavy lower-right tail
    # Control point: pulled slightly down-left of chord midpoint so the
    # dot bows out on its lower-left side (characteristic 点 shape).
    mx = (x0 + x1) / 2.0 - 4.0 * scale
    my = (y0 + y1) / 2.0 - 4.0 * scale

    n_segments = 40
    thickness_head = max(1, 3.0 * scale)
    thickness_tail = max(1, 14.0 * scale)

    prev_pt = None
    for i in range(n_segments + 1):
        t = i / n_segments
        bx = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * mx + t ** 2 * x1
        by = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * my + t ** 2 * y1
        px, py = _to_pixel(ox + bx, oy + by)
        if prev_pt is not None:
            w = thickness_head * (1 - t) + thickness_tail * t
            w_int = max(1, int(round(w)))
            draw.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    # Center the dot on the canvas.
    draw_dian(draw, ox=0.0, oy=0.0, scale=1.0)
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "01_点.png")
    img.save(out_path)
    print(f"saved: {out_path} ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    main()
