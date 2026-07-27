# yi_radical.py — 乙 (yi) radical, 1 stroke (a horizontal-fold-curve-hook shape).
# Bootstrap batch (position 38) — human PASSed.
#
# No single-stroke bank primitive matched (this is essentially a 横折弯钩 not
# in the bank), so the PASSing render drew a single continuous stroke as a
# piecewise-linear path with a per-vertex width profile. Recorded verbatim
# from the passing attempt (PIL px, canvas 300×300).

def draw_yi_radical(t, ox=0.0, oy=0.0, scale=1.0):
    """乙 radical: one continuous stroke — 横+折+弯+钩 as a curved sweep.

    Canonical shape is stored as PIL-px coords. (ox, oy) shifts, scale
    scales around the canvas center (150, 150).
    """
    def T(px, py):
        return (150 + (px - 150) * scale + ox,
                150 + (py - 150) * scale + oy)

    def stamp(x, y, r):
        t.ellipse((x - r, y - r, x + r, y + r), fill=(0, 0, 0))

    path = [
        (92, 108), (122, 98), (154, 94), (178, 102),
        (170, 122), (140, 158), (108, 200), (92, 228),
        (88, 245), (105, 254), (145, 256), (188, 252),
        (216, 246), (219, 224),
    ]
    widths = [3.0, 6.5, 8.0, 9.5, 9.0, 8.5, 9.0, 9.5,
              10.0, 10.5, 10.5, 9.5, 7.5, 2.5]

    steps_per_seg = 80
    for i in range(len(path) - 1):
        x0, y0 = path[i]
        x1, y1 = path[i + 1]
        w0, w1 = widths[i], widths[i + 1]
        for s in range(steps_per_seg + 1):
            u = s / steps_per_seg
            x = x0 + (x1 - x0) * u
            y = y0 + (y1 - y0) * u
            w = w0 + (w1 - w0) * u
            tx, ty = T(x, y)
            stamp(tx, ty, (w / 2.0) * scale)

    for (bx, by, br) in [(178, 102, 5.5), (216, 246, 5.5)]:
        tx, ty = T(bx, by)
        stamp(tx, ty, br * scale)
