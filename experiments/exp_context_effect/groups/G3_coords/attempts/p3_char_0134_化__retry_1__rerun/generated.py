# VISUAL DIFF (retry_1 PNG vs GT PNG) — mandatory Step 0
# 1. Left 亻: prior 竖 is COMPLETELY DISCONNECTED from the 撇 — there is a
#    visible white gap between the pie's belly and the shu's top. In GT the
#    shu clearly meets the pie at about the pie's mid-descent. Fix: put
#    shu_top ON the pie curve, not below/right of it.
# 2. Right 匕: prior 撇 is a tiny stub in the upper-right corner (from
#    ~(75,90) to (15,55) — spans only ~40 units diagonally). In GT the 匕
#    撇 is a LONG sweep starting at upper-right and traveling ALL the way
#    across to the top of the 竖弯钩 shaft. The prior pie is roughly a
#    third of its needed length.
# 3. Right 匕: prior 竖弯钩 shaft is far too SHORT (only y=55 down to
#    y=-30, ~85 units) and the arc/tail sits too low, making the whole 匕
#    look squat and half-height. In GT the 竖弯钩 shaft descends from near
#    top of the right cell all the way to lower area (~130+ units) then
#    sweeps right and up. Fix: extend shaft, push arc+hook further out.
# 4. Right 匕 hook: prior hook is a thin degenerate tail; GT shows a clear
#    upward hook of moderate length at the end of the horizontal sweep.
#
# RETRY MEMORY CHECKLIST (memory_index.md requirement for retries)
# Q1 (errata): Prior fail — 亻 shu disconnected from pie; 匕 rendered as
#   nearly-empty right half with tiny pie + short shu_wan_gou. Fix idea:
#   inline 亻 with shu_top ON the pie curve; inline 匕 with LONG pie
#   sweeping across to shaft top + tall shu_wan_gou.
# Q2 (form_catalog): 亻 identity alias (left-position radical); 匕 as
#   pie welded to shu_wan_gou shaft-top pixel (compact form).
# Q3 (helpers): weld — 匕's 撇 tail must sit on shu_wan_gou shaft top.
#   Compute weld inline (geometry straightforward). Trust GT over bank:
#   GT's shu_wan_gou is tall & thin with a distinct upward hook — do not
#   scale a squat bank primitive.

import os
import math
from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """math coords (center origin, +y up) -> PIL pixel (top-left, +y down)."""
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def _tapered_bezier(t, p0, p_ctrl, p1, w_head, w_tail, n=60):
    """Quadratic bezier in math coords, tapered from w_head -> w_tail."""
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
    _tapered_bezier(t, p0, ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2), p1, w_head, w_tail, n=n)


def _bezier_point(p0, p_ctrl, p1, u):
    bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p_ctrl[0] + u ** 2 * p1[0]
    by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p_ctrl[1] + u ** 2 * p1[1]
    return (bx, by)


def draw_ren_left(t):
    """左 亻 — pie sweeping down-left, shu dropping from ON the pie curve."""
    # pie: from upper-right of radical, curving down-left. Long sweep.
    pie_head = (-30, 100)
    pie_tail = (-105, -95)
    pie_ctrl = ((pie_head[0] + pie_tail[0]) / 2 - 5,
                (pie_head[1] + pie_tail[1]) / 2 + 8)
    _tapered_bezier(t, pie_head, pie_ctrl, pie_tail, w_head=8, w_tail=1.5, n=64)

    # shu: attach ON the pie curve. Pick a point about 40% down the pie
    # so it visually reads as sprouting from the pie's mid-descent.
    weld = _bezier_point(pie_head, pie_ctrl, pie_tail, 0.42)
    shu_top = weld  # start exactly on the pie
    shu_bot = (weld[0] + 4, -110)  # slight rightward drift so it doesn't lean
    # keep shu vertical from the weld — override x to be constant
    shu_bot = (weld[0], -110)
    _tapered_line(t, shu_top, shu_bot, w_head=8, w_tail=7, n=20)


def draw_bi_right(t):
    """右 匕 — long pie welded to top of a tall 竖弯钩."""
    # --- 竖弯钩 first so we know shaft top pixel ---
    shaft_top = (-5, 55)
    shaft_bot = (-5, -55)
    _tapered_line(t, shaft_top, shaft_bot, w_head=8, w_tail=8, n=16)

    # quarter arc from shaft_bot around to horizontal sweep
    thickness = 8
    arc_cx, arc_cy = 40.0, -55.0
    r = 45.0
    prev = None
    for i in range(17):
        u = i / 16
        angle = math.pi + u * (math.pi / 2)  # 180 -> 270 deg
        x = arc_cx + r * math.cos(angle)
        y = arc_cy + r * math.sin(angle)
        pxy = _to_pixel(x, y)
        if prev is not None:
            t.line([prev, pxy], fill=(0, 0, 0), width=thickness)
        prev = pxy

    # horizontal tail from end of arc rightward
    tail_start = (40.0, -100.0)
    tail_end = (100.0, -100.0)
    xs, ys = _to_pixel(*tail_start)
    xe, ye = _to_pixel(*tail_end)
    t.line([(xs, ys), (xe, ye)], fill=(0, 0, 0), width=thickness)

    # upward hook from tail_end
    hook_base = tail_end
    hook_tip = (100.0, -55.0)
    n_h = 12
    for i in range(n_h):
        u0 = i / n_h
        u1 = (i + 1) / n_h
        p0 = (hook_base[0] + u0 * (hook_tip[0] - hook_base[0]),
              hook_base[1] + u0 * (hook_tip[1] - hook_base[1]))
        p1 = (hook_base[0] + u1 * (hook_tip[0] - hook_base[0]),
              hook_base[1] + u1 * (hook_tip[1] - hook_base[1]))
        w_mid = (thickness - 1) * (1 - (u0 + u1) / 2) + 1.5
        w = max(1, int(round(w_mid)))
        a, b = _to_pixel(*p0)
        c, d = _to_pixel(*p1)
        t.line([(a, b), (c, d)], fill=(0, 0, 0), width=w)

    # --- 撇 of 匕: LONG sweep from upper-right ending ON shaft top ---
    pie_head = (85, 105)
    pie_tail = shaft_top  # exact weld pixel
    pie_ctrl = ((pie_head[0] + pie_tail[0]) / 2 + 8,
                (pie_head[1] + pie_tail[1]) / 2 + 10)
    _tapered_bezier(t, pie_head, pie_ctrl, pie_tail, w_head=8, w_tail=2, n=54)


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
