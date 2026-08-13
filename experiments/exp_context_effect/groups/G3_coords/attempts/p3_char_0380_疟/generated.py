# p3_char_0380_疟 (nüè, "malaria") — 8 strokes.
#
# Structure: 疒 envelope (5 strokes) + interior 匚-like element (3 strokes:
# top-inner heng, vertical, bottom heng closing right side).
#
# Composition plan:
#   - Reuse the 疒 envelope recipe from ne_sick.py (v9 rerun graduate):
#     inline top dot, thin heng roof, long uniform-ish pie, two 冫 marks
#     off the pie shaft.
#   - Interior element (fits inside the belly, right of pie shaft):
#     * top heng ~y=155, from x≈150 to x≈235
#     * right vertical dropping from that heng's right end to y≈245
#     * bottom heng ~y=245, from x≈145 to x≈245 (closes the frame)
#   - This mirrors the GT: a small rectangular-ish inner frame sitting
#     tucked in the belly of 疒.

import os
from PIL import Image, ImageDraw

_CANVAS = 300


def _tapered_line(draw, p0, p1, w_head, w_tail, n=28):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (x, y)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


def _tapered_bezier(draw, p0, p1, ctrl, w_head, w_tail, n=80):
    prev = None
    for i in range(n + 1):
        u = i / n
        omu = 1 - u
        x = omu * omu * p0[0] + 2 * omu * u * ctrl[0] + u * u * p1[0]
        y = omu * omu * p0[1] + 2 * omu * u * ctrl[1] + u * u * p1[1]
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (x, y)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


def draw_ne_envelope(draw):
    """Envelope strokes for 疒 — copied from ne_sick.py v9-graduate recipe."""
    # Stroke 1: top 点
    _tapered_line(draw, (198, 55), (215, 78), w_head=3.0, w_tail=6.5, n=18)
    # Stroke 2: heng roof
    _tapered_line(draw, (145, 108), (245, 105), w_head=4.5, w_tail=4.5, n=30)
    # Stroke 3: long 撇 descender
    _tapered_bezier(
        draw,
        p0=(145, 108),
        p1=(85, 278),
        ctrl=(108, 200),
        w_head=6.5,
        w_tail=4.0,
        n=90,
    )
    # Stroke 4: 冫 upper 点
    _tapered_line(draw, (78, 138), (100, 158), w_head=3.0, w_tail=6.0, n=18)
    # Stroke 5: 冫 lower 提
    _tapered_line(draw, (58, 218), (95, 202), w_head=7.5, w_tail=2.5, n=20)


def draw_interior(draw):
    """Interior 匚-like inner element (3 strokes) sitting in 疒's belly."""
    # Stroke 6: top inner heng — spans from just right of pie shaft to right side
    _tapered_line(draw, (150, 157), (240, 155), w_head=4.5, w_tail=4.5, n=30)
    # Stroke 7: right vertical — drops from top-heng's right end down to bottom
    _tapered_line(draw, (238, 155), (238, 246), w_head=4.5, w_tail=4.5, n=25)
    # Stroke 8: bottom heng — spans from pie belly right to right vertical
    _tapered_line(draw, (140, 245), (245, 245), w_head=5.0, w_tail=4.5, n=30)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_ne_envelope(draw)
    draw_interior(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_疟.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
