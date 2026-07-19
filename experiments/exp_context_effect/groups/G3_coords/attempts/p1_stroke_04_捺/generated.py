# p1_stroke_04_捺 — 捺 (rightward downward sweep) attempt
#
# 捺 mirrors 撇 across the vertical axis, but the calligraphic profile
# is different: thin start (upper-left), swelling belly, then a
# characteristic "foot" that tapers off toward the lower-right. In this
# attempt we hand-code a draw_na primitive in coord format matching the
# group's math-convention (center origin, +y up) storage style.

import os
import sys
from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel (top-left, +y down)."""
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_na(draw: ImageDraw.ImageDraw, ox: float = 0.0, oy: float = 0.0,
            scale: float = 1.0) -> None:
    """Draw one 捺 (rightward downward sweep) stroke.

    Canonical unit 捺: starts at upper-left head (-70, +80), curves down
    and rightward, swelling in the middle, then tapers off to a tail at
    (+80, -90). Profile: thin -> thick belly -> tapered foot.
    """
    # Endpoints in math coords, relative to (ox, oy)
    x0, y0 = -70.0 * scale, 80.0 * scale     # upper-left head (thin)
    x1, y1 = 80.0 * scale, -90.0 * scale     # lower-right tail
    # Control point: chord midpoint pulled slightly right and down to
    # create the characteristic outward bow of a 捺 (belly on the
    # lower-left of the chord).
    mx = (x0 + x1) / 2.0 + 10.0 * scale
    my = (y0 + y1) / 2.0 - 15.0 * scale

    n_segments = 60
    thickness_head = max(1, 2.0 * scale)   # thin entry
    thickness_belly = max(1, 18.0 * scale)  # thick middle
    thickness_tail = max(1, 3.0 * scale)   # tapered foot

    prev_pt = None
    for i in range(n_segments + 1):
        t = i / n_segments
        # Quadratic Bezier for the spine
        bx = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * mx + t ** 2 * x1
        by = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * my + t ** 2 * y1
        px, py = _to_pixel(ox + bx, oy + by)
        # Thickness profile: thin -> belly (~t=0.7) -> tapered tail.
        # Two linear ramps meeting at t=0.7 give the classic 捺 shape
        # where the widest point sits toward the tail-end, then tapers.
        t_belly = 0.7
        if t <= t_belly:
            w = thickness_head + (thickness_belly - thickness_head) * (t / t_belly)
        else:
            w = thickness_belly + (thickness_tail - thickness_belly) * ((t - t_belly) / (1 - t_belly))
        w_int = max(1, int(round(w)))
        if prev_pt is not None:
            draw.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_na(draw, ox=0.0, oy=0.0, scale=1.0)
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "01_捺.png")
    img.save(out_path)
    print(f"Wrote {out_path} ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    main()
