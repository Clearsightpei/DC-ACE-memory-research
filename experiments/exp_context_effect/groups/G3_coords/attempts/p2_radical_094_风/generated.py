# p2_radical_094_风 (feng) — 4-stroke radical, G3 coord-format drawer.
#
# Composition (inline-fresh per TR8/TR9 — 风 has a distinctive
# curved envelope + two small inner strokes that no single bank
# primitive captures cleanly):
#   1. Left 撇 (pie): descends from upper-mid-left, sweeps to lower-left.
#   2. 横折弯钩 (heng-zhe-wan-gou): flat top starting at 撇's head,
#      arches over rightward, curves down the right side with a soft
#      inward bow, ends in an up-left hook near the bottom.
#   3. Inner 撇 (small pie): starts just under the top horizontal
#      slightly left of center, sweeps down-left to the interior.
#   4. Inner 乀 (short right-diagonal, dian-like tail): starts near
#      center under the top, sweeps down-right toward the right shaft.
#
# Math coords: center origin, +y up. PIL 300x300 white bg, black ink.

from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def _qbez(p0, p1, p2, steps):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        pts.append((x, y))
    return pts


def _stroke_bezier(t, path_pts, widths, ox=0, oy=0):
    """widths = (w0, wmid, wend, umid) — piecewise-linear width profile."""
    n = len(path_pts)
    w0, wmid, wend, umid = widths
    for i in range(n - 1):
        u = i / (n - 1)
        if u < umid:
            w = w0 + (wmid - w0) * (u / umid)
        else:
            w = wmid + (wend - wmid) * ((u - umid) / (1 - umid))
        w_int = max(1, int(round(w)))
        p1 = _to_pixel(ox + path_pts[i][0], oy + path_pts[i][1])
        p2 = _to_pixel(ox + path_pts[i + 1][0], oy + path_pts[i + 1][1])
        t.line([p1, p2], fill=(0, 0, 0), width=w_int)
        r = w_int / 2.0
        t.ellipse([p2[0] - r, p2[1] - r, p2[0] + r, p2[1] + r],
                  fill=(0, 0, 0))


def _stroke_line_taper(t, p0, p1, w0, w1, steps=40, ox=0, oy=0):
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        x0 = p0[0] + (p1[0] - p0[0]) * u0
        y0 = p0[1] + (p1[1] - p0[1]) * u0
        x1 = p0[0] + (p1[0] - p0[0]) * u1
        y1 = p0[1] + (p1[1] - p0[1]) * u1
        w = max(1, int(round(w0 + (w1 - w0) * u0)))
        a = _to_pixel(ox + x0, oy + y0)
        b = _to_pixel(ox + x1, oy + y1)
        t.line([a, b], fill=(0, 0, 0), width=w)


def draw_feng(t, ox=0, oy=0, scale=1.0):
    s = scale

    # ---- Stroke 1: left 撇 (pie) ----
    # head at top-left where the horizontal begins (-65, +100), sweeps
    # down and outward to lower-left tip (-110, -100). Bows leftward.
    pie_head = (-65 * s, 100 * s)
    pie_tail = (-110 * s, -100 * s)
    pie_ctrl = (-105 * s, 10 * s)
    pie_path = _qbez(pie_head, pie_ctrl, pie_tail, 60)
    _stroke_bezier(t, pie_path,
                   widths=(9 * s, 6 * s, 1 * s, 0.5), ox=ox, oy=oy)

    # ---- Stroke 2: 横折弯钩 (main envelope) ----
    # (a) horizontal top: from (-68, +100) rightward to (+72, +100)
    heng_start = (-68 * s, 100 * s)
    heng_end = (72 * s, 98 * s)
    _stroke_line_taper(t, heng_start, heng_end,
                       w0=6 * s, w1=8 * s, steps=40, ox=ox, oy=oy)

    # corner 顿笔 blob at top-right
    cx, cy = _to_pixel(ox + 72 * s, oy + 96 * s)
    rc = max(4, int(6 * s))
    t.ellipse([cx - rc, cy - rc, cx + rc + 1, cy + rc + 1],
              fill=(0, 0, 0))

    # (b) right descending arc: from (+72, +96) sweeping down and
    # inward to (+30, -100). Control point bulges right (bow outward).
    arc_start = (72 * s, 96 * s)
    arc_ctrl = (95 * s, -10 * s)
    arc_end = (30 * s, -100 * s)
    arc_path = _qbez(arc_start, arc_ctrl, arc_end, 60)
    _stroke_bezier(t, arc_path,
                   widths=(8 * s, 9 * s, 5 * s, 0.55), ox=ox, oy=oy)

    # (c) hook flick from arc_end going up-left
    hook_start = arc_end
    hook_ctrl = (15 * s, -92 * s)
    hook_tip = (5 * s, -75 * s)
    hook_path = _qbez(hook_start, hook_ctrl, hook_tip, 20)
    m = len(hook_path)
    for i in range(m - 1):
        u = i / (m - 1)
        w = 6 - (6 - 2) * u
        w_int = max(2, int(round(w * s)))
        p1 = _to_pixel(ox + hook_path[i][0], oy + hook_path[i][1])
        p2 = _to_pixel(ox + hook_path[i + 1][0], oy + hook_path[i + 1][1])
        t.line([p1, p2], fill=(0, 0, 0), width=w_int)

    # ---- Stroke 3: inner 撇 (small pie) ----
    # starts just under top horizontal at (-15, +55), sweeps down-left
    # to (-55, -50). Tapered to fine tip.
    ipie_head = (-15 * s, 55 * s)
    ipie_tail = (-55 * s, -50 * s)
    ipie_ctrl = (-38 * s, 5 * s)
    ipie_path = _qbez(ipie_head, ipie_ctrl, ipie_tail, 50)
    _stroke_bezier(t, ipie_path,
                   widths=(7 * s, 5 * s, 1 * s, 0.5), ox=ox, oy=oy)

    # ---- Stroke 4: inner 乀 / short down-right diagonal ----
    # starts near (+5, +40), sweeps down-right to (+40, -35). Thin
    # head, thicker belly, taper toward foot (小捺 / 反捺 shape).
    na_head = (5 * s, 40 * s)
    na_tail = (40 * s, -35 * s)
    na_ctrl = (18 * s, 0 * s)
    na_path = _qbez(na_head, na_ctrl, na_tail, 45)
    _stroke_bezier(t, na_path,
                   widths=(2 * s, 8 * s, 3 * s, 0.65), ox=ox, oy=oy)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), "white")
    t = ImageDraw.Draw(img)
    draw_feng(t, ox=0, oy=0, scale=1.0)
    out_path = __file__.rsplit("/", 1)[0] + "/01_风.png"
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
