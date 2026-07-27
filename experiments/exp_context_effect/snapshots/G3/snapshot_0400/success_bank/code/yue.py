# yue.py — 月 (yuè, moon), 4 strokes.
# PASSed at p2_radical_130_月 (B3 pos 157, 2026-07-22).
# Inline PIL recipe: 撇 (nearly-vertical scoop) + 横折钩 (tall) +
# two interior 横. Aspect taller than 日, narrower than kou; bottom open.
def _tapered_line(draw, p0, p1, w0, w1, steps=24):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = max(1, int(round(w0 + (w1 - w0) * u0)))
        draw.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)


def _tapered_bezier(draw, p0, p1, p2, w0, w1, steps=40):
    prev = None
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        w = max(1, int(round(w0 + (w1 - w0) * u)))
        if prev is not None:
            draw.line([prev, (bx, by)], fill=(0, 0, 0), width=w)
            r = w / 2.0
            draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def draw_yue(D, ox=0, oy=0, scale=1.0):
    """Draw 月. PIL px base coords; ox/oy shift px, scale uniform."""
    def X(x): return 150 + (x - 150) * scale + ox
    def Y(y): return 150 + (y - 150) * scale + oy

    X_TOP_LEFT = X(128)
    X_TOP_RIGHT = X(200)
    X_RIGHT = X(200)
    Y_TOP = Y(55)
    Y_HOOK = Y(250)
    PIE_TAIL_X = X(85)
    PIE_TAIL_Y = Y(255)

    # 撇
    p0 = (X_TOP_LEFT, Y_TOP)
    p2 = (PIE_TAIL_X, PIE_TAIL_Y)
    ctrl_x = X_TOP_LEFT - 2
    ctrl_y = Y_TOP + (PIE_TAIL_Y - Y_TOP) * 0.72
    _tapered_bezier(D, p0, (ctrl_x, ctrl_y), p2,
                    w0=int(12 * scale), w1=max(1, int(2 * scale)), steps=56)
    D.ellipse([p0[0] - 7, p0[1] - 4, p0[0] + 4, p0[1] + 7], fill=(0, 0, 0))

    # 横折钩
    _tapered_line(D, (X_TOP_LEFT, Y_TOP), (X_TOP_RIGHT, Y_TOP),
                  w0=int(10 * scale), w1=int(11 * scale), steps=24)
    D.ellipse([X_TOP_RIGHT - 6, Y_TOP - 6, X_TOP_RIGHT + 6, Y_TOP + 6],
              fill=(0, 0, 0))
    _tapered_line(D, (X_TOP_RIGHT, Y_TOP), (X_RIGHT, Y_HOOK),
                  w0=int(11 * scale), w1=int(10 * scale), steps=32)
    hook_end = (X_RIGHT - 22 * scale, Y_HOOK - 20 * scale)
    _tapered_line(D, (X_RIGHT + 1, Y_HOOK + 2), hook_end,
                  w0=int(10 * scale), w1=max(1, int(2 * scale)), steps=16)
    D.ellipse([X_RIGHT - 6, Y_HOOK - 6, X_RIGHT + 6, Y_HOOK + 6],
              fill=(0, 0, 0))

    # Interior hengs
    Y_H1 = Y(122)
    _tapered_line(D, (X_TOP_LEFT + 3, Y_H1 + 2), (X_RIGHT - 12, Y_H1 - 1),
                  w0=int(5 * scale), w1=int(7 * scale), steps=16)
    Y_H2 = Y(185)
    _tapered_line(D, (X_TOP_LEFT - 6, Y_H2 + 2), (X_RIGHT - 12, Y_H2 - 1),
                  w0=int(5 * scale), w1=int(7 * scale), steps=16)
