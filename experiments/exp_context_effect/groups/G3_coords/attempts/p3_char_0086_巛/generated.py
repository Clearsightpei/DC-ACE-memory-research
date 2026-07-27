# p3_char_0086_巛 (chuan, "river") — first attempt.
# Three curved wavy verticals, all similar shape.
# Adapted from chuan.py's _draw_left_curve helper: quadratic bezier with
# small hook at top (short 撇-like tick) and downward tail.
# The GT shows each stroke = short right-leaning top tick + long wavy vertical
# ending with a small right-bending tail. Draw three of them side-by-side.

import os
from PIL import Image, ImageDraw

CANVAS = 300
OUT_PNG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_巛.png")


def _to_pixel(mx, my):
    return CANVAS / 2 + mx, CANVAS / 2 - my


def _draw_wave_stroke(draw, ox, oy, scale=1.0):
    """One 巛-stroke: tiny top tick + long curved wavy vertical.

    In math coords (y up), a stroke spans roughly y=+60 (top) to y=-70 (bottom).
    Horizontal amplitude ~10 px. Slight S-bend: leans left in middle, tail
    curves right and down.
    """
    # Top tick (short pie-like segment) — leans down-right → down-left
    tick_pts = [
        (2.0, 85.0),
        (-8.0, 72.0),
    ]
    prev = None
    ink = max(1, int(4 * scale))  # GT is thin — per principle P12
    for (bx, by) in tick_pts:
        px, py = _to_pixel(ox + bx * scale, oy + by * scale)
        if prev is not None:
            draw.line([prev, (px, py)], fill=(0, 0, 0), width=ink)
        prev = (px, py)

    # Main wavy vertical — quadratic bezier chain (S-ish, more pronounced)
    def bezier_quad(p0, p1, p2, n=40):
        pts = []
        for i in range(n + 1):
            u = i / n
            bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
            by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
            pts.append((bx, by))
        return pts

    # Segment 1: (-8, 72) → bulge left → (-4, 0)
    seg1 = bezier_quad((-8.0, 72.0), (-22.0, 35.0), (-4.0, 0.0), n=45)
    # Segment 2: (-4, 0) → curve right/down → (-10, -80) — reversing bow
    seg2 = bezier_quad((-4.0, 0.0), (-2.0, -45.0), (-10.0, -80.0), n=40)
    # Tail flicks right-down
    tail = [(-10.0, -80.0), (2.0, -92.0)]

    all_pts = seg1 + seg2[1:] + tail[1:]
    prev = None
    for (bx, by) in all_pts:
        px, py = _to_pixel(ox + bx * scale, oy + by * scale)
        if prev is not None:
            draw.line([prev, (px, py)], fill=(0, 0, 0), width=ink)
        prev = (px, py)


def draw_chuan_3(draw):
    """巛 = three wavy strokes evenly spaced."""
    # Center each stroke horizontally: x = -55, 0, +55 (math coords)
    _draw_wave_stroke(draw, ox=-55, oy=-10, scale=1.0)
    _draw_wave_stroke(draw, ox=  0, oy=-10, scale=1.0)
    _draw_wave_stroke(draw, ox= 55, oy=-10, scale=1.0)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_chuan_3(draw)
    img.save(OUT_PNG)
    print(f"Wrote {OUT_PNG}")


if __name__ == "__main__":
    main()
