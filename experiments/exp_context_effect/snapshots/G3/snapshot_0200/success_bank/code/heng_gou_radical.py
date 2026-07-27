# heng_gou_radical.py — 乛 radical, 1 stroke (heng-gou variant).
# Bootstrap batch (position 36) — human PASSed.
#
# Per TR5: default heng_gou primitive was too heavy/wide. The PASSing
# render inlined a thinner, shorter horizontal (spans PIL 90..205, mid-canvas)
# with a small hook. Recorded verbatim from the passing attempt.

CANVAS_SIZE = 300


def draw_heng_gou_radical(t, ox=0.0, oy=0.0, scale=1.0):
    """乛 radical: mid-canvas thin horizontal with a small down-left hook.

    Canonical placement in PIL coords: horizontal from (90,128) to (205,138),
    顿笔 blob at right end, hook down-left to (190,168). (ox, oy) shifts
    everything in PIL px; scale scales endpoints around the internal origin
    (canvas center 150,150).
    """
    # Transform: (px, py) -> (150 + (px-150)*scale + ox, 150 + (py-150)*scale + oy)
    def T(px, py):
        return (150 + (px - 150) * scale + ox,
                150 + (py - 150) * scale + oy)

    x0, y0 = 90, 128
    x1, y1 = 205, 138

    line_w_start = max(1, int(4 * scale))
    line_w_end = max(1, int(7 * scale))
    steps = 20
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * t0
        ya = y0 + (y1 - y0) * t0
        xb = x0 + (x1 - x0) * t1
        yb = y0 + (y1 - y0) * t1
        w = max(1, int(line_w_start + (line_w_end - line_w_start) * t0))
        t.line([T(xa, ya), T(xb, yb)], fill=(0, 0, 0), width=w)

    r = max(1, int(5 * scale))
    cx, cy = T(x1, y1)
    t.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    hx0, hy0 = x1 + 1, y1 + 1
    hx1, hy1 = x1 - int(15 * scale), y1 + int(30 * scale)
    hsteps = 12
    for i in range(hsteps):
        t0 = i / hsteps
        t1 = (i + 1) / hsteps
        xa = hx0 + (hx1 - hx0) * t0
        ya = hy0 + (hy1 - hy0) * t0
        xb = hx0 + (hx1 - hx0) * t1
        yb = hy0 + (hy1 - hy0) * t1
        w = max(1, int((8 - 7 * t0) * scale))
        t.line([T(xa, ya), T(xb, yb)], fill=(0, 0, 0), width=w)
