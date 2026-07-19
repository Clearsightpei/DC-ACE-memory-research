# 歹 (radical, 4画) — G3 attempt (REVISION 1)
#
# Diagnosis from render-1:
#   - Long pie tail extended past bottom of canvas (too deep). Shorten.
#   - Interior 丶 rendered as long slash bleeding out of enclosure. Use
#     a smaller, more compact dot (reduce scale, tighter placement).
#   - Short 丿 tick was floating; attach it to just under the top heng.
#   - Top heng slightly too long — tighten span.
#
# Structure (from GT, 4 strokes):
#   1. 一 (top heng): compact horizontal at top.
#   2. 丿 (short pie): small tick attached below the heng's mid-left.
#   3. 横撇 (compound): short heng in upper interior turning into a long
#      tapered 撇 sweeping down-left through the lower body.
#   4. 丶 (small dian): compact dot inside the enclosure, upper-right.
#
# Bank use (TR audit unchanged from v1): only dian.py reused, at smaller
# scale + tighter placement. Everything else inline fresh.

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))

from PIL import Image, ImageDraw
from dian import draw_dian

CANVAS = 300


def _to_pixel(ox, oy):
    return (CANVAS / 2 + ox, CANVAS / 2 - oy)


def draw_top_heng(d):
    """一 across the top. Slight rise. Endpoints tightened.
    math (-80, +95) -> (+70, +105) i.e. PIL (70, 55) -> (220, 45).
    """
    x0, y0 = -80.0, 95.0
    x1, y1 = 70.0, 105.0
    n = 40
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = x0 + (x1 - x0) * u
        by = y0 + (y1 - y0) * u
        p = _to_pixel(bx, by)
        w = 7.5 + 1.5 * (1 - abs(0.5 - u) * 2) * 0.7
        w_int = max(1, int(round(w)))
        if prev is not None:
            d.line([prev, p], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=(0, 0, 0))
        prev = p


def draw_short_pie(d):
    """Short 丿 tick attached under the top heng's mid-left area.
    Head at math (-40, +90) (just under heng), tail at (-65, +40).
    Head thick ~7, tail thin ~1. Compact scoop.
    """
    x0, y0 = -40.0, 90.0
    x1, y1 = -65.0, 40.0
    mx = (x0 + x1) / 2.0 - 3.0
    my = (y0 + y1) / 2.0 + 3.0
    n = 40
    w_head, w_tail = 6.5, 1.0
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        p = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            d.line([prev, p], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=(0, 0, 0))
        prev = p


def draw_heng_pie_composite(d):
    """横撇: short heng in upper interior, sharp turn to long tapered pie.
    Shortened pie tail so it doesn't leave canvas.
    Heng: math (-25, +65) -> (+50, +72). PIL (125, 85) -> (200, 78).
    Corner blob at math (+52, +70).
    Pie: head math (+52, +65), tail math (-50, -75). Tail is PIL (100, 225)
    — safely inside canvas with margin.
    """
    heng_start = (-25.0, 65.0)
    heng_end = (50.0, 72.0)
    n_h = 30
    prev = None
    for i in range(n_h + 1):
        u = i / n_h
        bx = heng_start[0] + (heng_end[0] - heng_start[0]) * u
        by = heng_start[1] + (heng_end[1] - heng_start[1]) * u
        p = _to_pixel(bx, by)
        w = 7 - 0.5 * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            d.line([prev, p], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=(0, 0, 0))
        prev = p

    cx, cy = _to_pixel(52.0, 68.0)
    r = 5
    d.ellipse([cx - r, cy - r, cx + r + 1, cy + r + 1], fill=(0, 0, 0))

    # Shortened pie
    x0, y0 = 52.0, 63.0
    x1, y1 = -50.0, -75.0
    mx = (x0 + x1) / 2.0 - 6.0
    my = (y0 + y1) / 2.0 + 6.0
    n_p = 60
    w_head, w_tail = 9.0, 1.0
    prev = None
    for i in range(n_p + 1):
        u = i / n_p
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        p = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            d.line([prev, p], fill=(0, 0, 0), width=w_int)
            rr = w / 2.0
            d.ellipse([p[0] - rr, p[1] - rr, p[0] + rr, p[1] + rr], fill=(0, 0, 0))
        prev = p


def draw_interior_dian(d):
    """Small 丶 inside upper-right pocket.
    Placement: math (+8, +35), i.e. PIL (158, 115).
    Primitive default center ~ (+1.5, +2.5).
    ox = 8 - 1.5 = 6.5 → +7
    oy = 35 - 2.5 = 32.5 → +33
    Scale=0.4 (smaller than v1's 0.55) so the dot stays compact.
    """
    draw_dian(d, ox=7.0, oy=33.0, scale=0.4)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)

    draw_top_heng(d)
    draw_short_pie(d)
    draw_heng_pie_composite(d)
    draw_interior_dian(d)

    out = os.path.join(os.path.dirname(__file__), "01_歹.png")
    img.save(out, "PNG")
    print("wrote", out)


if __name__ == "__main__":
    main()
