# heng_pie_wan_gou.py — 横撇弯钩 coord primitive.
# Compound: short 横 + sharp 撇 down-left + 弯 curved arc + up-left 钩 flick.
# Appears in 阝, 那, 队. Extracted from attempts/p1_stroke_24_横撇弯钩/generated.py
# after human PASS.

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def _qbez(p0, p1, p2, steps):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        pts.append((x, y))
    return pts


def _stroke_line_taper(t, p0_math, p1_math, w0, w1, steps=40, ox=0, oy=0):
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        x0 = p0_math[0] + (p1_math[0] - p0_math[0]) * u0
        y0 = p0_math[1] + (p1_math[1] - p0_math[1]) * u0
        x1 = p0_math[0] + (p1_math[0] - p0_math[0]) * u1
        y1 = p0_math[1] + (p1_math[1] - p0_math[1]) * u1
        w = max(1, int(round(w0 + (w1 - w0) * u0)))
        a = _to_pixel(ox + x0, oy + y0)
        b = _to_pixel(ox + x1, oy + y1)
        t.line([a, b], fill=(0, 0, 0), width=w)


def _stroke_bezier(t, path_pts, widths, ox=0, oy=0):
    n = len(path_pts)
    for i in range(n - 1):
        u = i / (n - 1)
        w0, wmid, wend, umid = widths
        if u < umid:
            w = w0 + (wmid - w0) * (u / umid)
        else:
            w = wmid + (wend - wmid) * ((u - umid) / (1 - umid))
        w_int = max(2, int(round(w)))
        p1 = _to_pixel(ox + path_pts[i][0], oy + path_pts[i][1])
        p2 = _to_pixel(ox + path_pts[i + 1][0], oy + path_pts[i + 1][1])
        t.line([p1, p2], fill=(0, 0, 0), width=w_int)
        r = w_int / 2.0
        t.ellipse([p2[0] - r, p2[1] - r, p2[0] + r, p2[1] + r], fill=(0, 0, 0))


def draw_heng_pie_wan_gou(t, ox=0, oy=0, scale=1.0):
    """横撇弯钩 = short 横 → 撇 downstroke → 弯 arc → up-left 钩."""
    # 横
    heng_start = (-55 * scale, 95 * scale)
    heng_end = (35 * scale, 100 * scale)
    _stroke_line_taper(t, heng_start, heng_end,
                       w0=8 * scale, w1=11 * scale, steps=40, ox=ox, oy=oy)

    corner1 = _to_pixel(ox + 37 * scale, oy + 98 * scale)
    r1 = max(4, int(7 * scale))
    t.ellipse([corner1[0] - r1, corner1[1] - r1,
               corner1[0] + r1 + 1, corner1[1] + r1 + 2],
              fill=(0, 0, 0))

    # 撇
    pie_start = (38 * scale, 95 * scale)
    pie_end = (-30 * scale, 5 * scale)
    _stroke_line_taper(t, pie_start, pie_end,
                       w0=11 * scale, w1=7 * scale, steps=50, ox=ox, oy=oy)

    # 弯
    arc_start = pie_end
    arc_ctrl = (30 * scale, -50 * scale)
    arc_end = (-10 * scale, -95 * scale)
    arc = _qbez(arc_start, arc_ctrl, arc_end, 50)
    _stroke_bezier(t, arc, widths=(7 * scale, 11 * scale, 6 * scale, 0.55),
                   ox=ox, oy=oy)

    # 钩
    hook_start = arc_end
    hook_ctrl = (-25 * scale, -85 * scale)
    hook_tip = (-45 * scale, -70 * scale)
    hook = _qbez(hook_start, hook_ctrl, hook_tip, 20)
    m = len(hook)
    for i in range(m - 1):
        u = i / (m - 1)
        w = 6 - (6 - 2) * u
        w_int = max(2, int(round(w * scale)))
        p1 = _to_pixel(ox + hook[i][0], oy + hook[i][1])
        p2 = _to_pixel(ox + hook[i + 1][0], oy + hook[i + 1][1])
        t.line([p1, p2], fill=(0, 0, 0), width=w_int)
