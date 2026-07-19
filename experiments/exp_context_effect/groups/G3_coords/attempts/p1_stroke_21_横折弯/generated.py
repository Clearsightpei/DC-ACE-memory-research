# 横折弯 (heng-zhe-wan) — horizontal, 90-deg turn down, then curved sweep right.
# Coord format: math coords (center origin, +y up), converted to PIL pixels.
# Composition: 横 segment -> corner 顿笔 -> 竖 segment -> quarter arc -> 横 right.
# Reuses concept from heng_zhe.py (horizontal+turn) and shu_wan.py (arc to horizontal).

import math
import os
from PIL import Image, ImageDraw

CANVAS_SIZE = 300
TH = 12  # ink thickness


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def _stroke_line(draw, p_a_math, p_b_math, width):
    a = _to_pixel(*p_a_math)
    b = _to_pixel(*p_b_math)
    draw.line([a, b], fill=(0, 0, 0), width=width)
    r = width // 2
    for pt in (a, b):
        draw.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))


def draw_heng_zhe_wan(draw, ox=0, oy=0, scale=1.0):
    """
    横折弯 layout in math coords (unscaled):
      Start at (-90, 70)  — left end of top 横
      Turn corner at (70, 70)  — top-right, 90-deg down
      Vertical segment down to (70, -30)
      Quarter arc sweeping right, center at (100, -30), radius 30
        -> arc ends at (100, -60)
      Horizontal segment ending at (95, -60)  (short bend tail)
    """
    ink = max(1, int(round(TH * scale)))

    p_h_start = (-90 * scale, 70 * scale)
    p_corner = (70 * scale, 70 * scale)
    p_v_end = (70 * scale, -30 * scale)
    arc_r = 30 * scale
    arc_cx = p_v_end[0] + arc_r  # 100 * scale
    arc_cy = p_v_end[1]          # -30 * scale
    p_arc_end = (arc_cx, arc_cy - arc_r)  # (100, -60) — bottom of arc
    p_h_end = (95 * scale, -60 * scale)   # very short horizontal tail

    # 1) top horizontal
    _stroke_line(draw,
                 (ox + p_h_start[0], oy + p_h_start[1]),
                 (ox + p_corner[0],  oy + p_corner[1]),
                 ink)

    # 2) corner 顿笔 blob (per P6)
    cx_px, cy_px = _to_pixel(ox + p_corner[0], oy + p_corner[1])
    blob_r = max(2, int(round(ink * 0.7)))
    draw.ellipse(
        [cx_px - blob_r, cy_px - blob_r, cx_px + blob_r, cy_px + blob_r],
        fill=(0, 0, 0),
    )

    # 3) vertical descending
    _stroke_line(draw,
                 (ox + p_corner[0], oy + p_corner[1]),
                 (ox + p_v_end[0],  oy + p_v_end[1]),
                 ink)

    # 4) quarter arc sweeping down-right, stamped-circle style (per P3)
    steps = 30
    for i in range(steps + 1):
        # angle from 180deg -> 270deg in math coords (arc bulges down-right)
        ang = math.radians(180 + (i / steps) * 90)
        dx = arc_r * math.cos(ang)
        dy = arc_r * math.sin(ang)  # sin negative in this range -> dips below center
        cxp, cyp = _to_pixel(ox + arc_cx, oy + arc_cy)
        # dx in math = dx in pixels; dy in math flips (subtract) when converting.
        px = cxp + dx
        py = cyp - dy
        r = ink // 2
        draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))

    # 5) short horizontal continuation to the right end
    _stroke_line(draw,
                 (ox + p_arc_end[0], oy + p_arc_end[1]),
                 (ox + p_h_end[0],   oy + p_h_end[1]),
                 ink)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_heng_zhe_wan(draw, ox=0, oy=0, scale=1.0)

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "01_横折弯.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
