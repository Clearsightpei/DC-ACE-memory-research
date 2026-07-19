# p1_stroke_06_提 — 提 (rising stroke, lower-left to upper-right) attempt
#
# 提 (tí) is a rising stroke: it starts with a small pressed head at the
# lower-left, sweeps upward and to the right along a slightly curved
# path, and tapers to a sharp point at the upper-right. Unlike 撇 (which
# descends left) or 捺 (which descends right with a foot), 提 goes UP
# and to the right, and terminates in a needle-like point (like the
# tail of a 挑 in calligraphy).
#
# Coordinate storage format matches G3's math-convention (center origin,
# +y up). Endpoints in unit coords: head at (-70, -70), tip at (+80, +60).

import os
from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel (top-left, +y down)."""
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_ti(draw: ImageDraw.ImageDraw, ox: float = 0.0, oy: float = 0.0,
            scale: float = 1.0) -> None:
    """Draw one 提 (rising stroke) from lower-left to upper-right.

    Canonical unit 提:
      - Head at (-70, -70): pressed, thickest
      - Tip at (+80, +60): tapered to a point
      - Slight upward bow along the middle (control point above chord)
      - Thickness ramps from thick head to needle point
    """
    x0, y0 = -70.0 * scale, -70.0 * scale   # lower-left head (thick)
    x1, y1 = 80.0 * scale, 60.0 * scale     # upper-right tip (point)
    # Control point: chord midpoint pulled slightly up-left to create
    # the characteristic gentle upward arc of a 提.
    mx = (x0 + x1) / 2.0 - 5.0 * scale
    my = (y0 + y1) / 2.0 + 12.0 * scale

    n_segments = 60
    thickness_head = max(1, 16.0 * scale)  # thick pressed head
    thickness_tip = 1.0                    # needle point

    prev_pt = None
    for i in range(n_segments + 1):
        t = i / n_segments
        # Quadratic Bezier spine
        bx = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * mx + t ** 2 * x1
        by = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * my + t ** 2 * y1
        px, py = _to_pixel(ox + bx, oy + by)
        # Linear taper from thick head to needle tip.
        # Small initial "press" plateau: hold near-max thickness for
        # the first ~10% to render the calligraphic head.
        if t < 0.1:
            w = thickness_head
        else:
            w = thickness_head + (thickness_tip - thickness_head) * ((t - 0.1) / 0.9)
        w_int = max(1, int(round(w)))
        if prev_pt is not None:
            draw.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_ti(draw, ox=0.0, oy=0.0, scale=1.0)
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "01_提.png")
    img.save(out_path)
    print(f"Wrote {out_path} ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    main()
