# RETRY MEMORY CHECKLIST (B4->B5 v7 evolution)
# Q1 (errata): Look up this item in errata.md. What is the fix idea?
#   Prior fail: left 亻 pie floated with disconnected shu; right 匕 rendered
#   as detached shu_wan_gou + tiny pie above it. Fix idea: use ren_pang
#   (or inline 亻 with shu welded to pie midpoint) and inline 匕 with pie
#   tail landing ON 竖弯钩 shaft top per sandbox p2_radical_011_匕 fix.
# Q2 (form_catalog): Search form_catalog.md for rows matching the
#   stroke(s) that caused the fail. Which rows are relevant?
#   - 亻 identity alias (left-position radical, scale ~0.7 for chars)
#   - 匕 as pie welded to shu_wan_gou shaft top (compact form)
# Q3 (helpers): Does the fail category match any of these helpers?
#   - pie_point / weld: yes — 匕's 撇 tail must be computed to sit on
#     shu_wan_gou shaft-top pixel. I'll compute weld inline (simpler than
#     importing pie_point since geometry is straightforward here).
#   - Trust GT: 匕's shu_wan_gou is tall+narrow with a small hook, not
#     the calligraphic bank primitive scaled up. Inline it.

import os
import sys
import math
from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """math coords (center origin, +y up) -> PIL pixel (top-left, +y down)."""
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def _tapered_bezier(t, p0, p_ctrl, p1, w_head, w_tail, n=48):
    """Quadratic bezier in math coords, tapered from w_head to w_tail."""
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p_ctrl[0] + u ** 2 * p1[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p_ctrl[1] + u ** 2 * p1[1]
        pxy = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, pxy], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([pxy[0] - r, pxy[1] - r, pxy[0] + r, pxy[1] + r], fill=(0, 0, 0))
        prev = pxy


def _tapered_line(t, p0, p1, w_head, w_tail, n=24):
    """Straight line, tapered."""
    _tapered_bezier(t, p0, ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2), p1, w_head, w_tail, n=n)


def draw_ren_left(t):
    """左 亻: 撇 sweeping down-left + 竖 dropping from pie midpoint."""
    # pie: from upper-right of the radical, curving down-left
    pie_head = (-35, 90)
    pie_tail = (-95, -55)
    # gentle bow
    pie_ctrl = ((pie_head[0] + pie_tail[0]) / 2 - 6, (pie_head[1] + pie_tail[1]) / 2 + 4)
    _tapered_bezier(t, pie_head, pie_ctrl, pie_tail, w_head=9, w_tail=1.5, n=54)

    # shu: from midpoint-ish of pie down to bottom; welded to pie body
    # midpoint of pie is around x=-65, y=17 — but shu should visually descend
    # from a bit right-of-midpoint so it reads as attached
    shu_top = (-55, 25)
    shu_bot = (-55, -80)
    _tapered_line(t, shu_top, shu_bot, w_head=8, w_tail=7, n=16)


def draw_bi_right(t):
    """右 匕: 撇 landing on shaft top of 竖弯钩."""
    # 竖弯钩: shaft from (+15, +55) down to (+15, -30), then quarter arc
    # to (+55, -70), then hook up.
    shaft_top = (15, 55)
    shaft_bot = (15, -30)
    _tapered_line(t, shaft_top, shaft_bot, w_head=8, w_tail=8, n=14)

    # Quarter arc: center (+55, -30), radius 40, from 180deg to 270deg
    thickness = 8
    arc_cx, arc_cy = 55.0, -30.0
    r = 40.0
    prev = None
    for i in range(13):
        u = i / 12
        angle = math.pi + u * (math.pi / 2)  # 180 -> 270
        x = arc_cx + r * math.cos(angle)
        y = arc_cy + r * math.sin(angle)
        pxy = _to_pixel(x, y)
        if prev is not None:
            t.line([prev, pxy], fill=(0, 0, 0), width=thickness)
        prev = pxy

    # Tail horizontal: (+55, -70) to (+95, -70)
    tail_start = (55, -70)
    tail_end = (95, -70)
    xs, ys = _to_pixel(*tail_start)
    xe, ye = _to_pixel(*tail_end)
    t.line([(xs, ys), (xe, ye)], fill=(0, 0, 0), width=thickness)

    # Upward hook tapered from tail_end
    hook_base = tail_end
    hook_tip = (92, -45)
    n_h = 8
    for i in range(n_h):
        u0 = i / n_h
        u1 = (i + 1) / n_h
        p0 = (hook_base[0] + u0 * (hook_tip[0] - hook_base[0]),
              hook_base[1] + u0 * (hook_tip[1] - hook_base[1]))
        p1 = (hook_base[0] + u1 * (hook_tip[0] - hook_base[0]),
              hook_base[1] + u1 * (hook_tip[1] - hook_base[1]))
        w = max(1, int(round((thickness - 1) * (1 - (u0 + u1) / 2) + 1)))
        a, b = _to_pixel(*p0)
        c, d = _to_pixel(*p1)
        t.line([(a, b), (c, d)], fill=(0, 0, 0), width=w)

    # 撇 of 匕: from upper-right, sweeping down-left, tail lands ON shaft top
    pie_head = (75, 90)
    pie_tail = shaft_top  # weld exactly to shaft top pixel
    pie_ctrl = ((pie_head[0] + pie_tail[0]) / 2 + 2,
                (pie_head[1] + pie_tail[1]) / 2 + 5)
    _tapered_bezier(t, pie_head, pie_ctrl, pie_tail, w_head=8, w_tail=2, n=40)


def draw_hua(t):
    draw_ren_left(t)
    draw_bi_right(t)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_hua(draw)
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_化.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
