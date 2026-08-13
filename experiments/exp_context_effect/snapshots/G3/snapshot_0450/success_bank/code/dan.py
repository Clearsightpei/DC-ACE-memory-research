# dan.py — 丹 (dān), 4 strokes: 撇 + 横折钩 frame + 点 (inside) + 横 crossing.
# PASSed at p3_char_0095_丹 (B5, pos 257). Adapted from yue.py frame recipe.
# ox/oy/scale threaded via math->pixel wrapper.


def draw_dan(D, ox=0, oy=0, scale=1.0):
    def X(x): return 150 + (x - 150) * scale + ox
    def Y(y): return 150 + (y - 150) * scale + oy

    X_TOP_LEFT = X(110)
    X_TOP_RIGHT = X(205)
    X_RIGHT = X(205)
    Y_TOP = Y(80)
    Y_HOOK = Y(245)
    PIE_TAIL_X = X(55)
    PIE_TAIL_Y = Y(265)
    W = max(2, int(4 * scale))

    def _tapered_line(p0, p1, w0, w1, steps=24):
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
            D.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)

    def _tapered_bezier(p0, p1, p2, w0, w1, steps=40):
        prev = None
        for i in range(steps + 1):
            u = i / steps
            bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
            by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
            w = max(1, int(round(w0 + (w1 - w0) * u)))
            if prev is not None:
                D.line([prev, (bx, by)], fill=(0, 0, 0), width=w)
                r = w / 2.0
                D.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
            prev = (bx, by)

    # Stroke 1: 撇
    p0 = (X_TOP_LEFT, Y_TOP)
    p2 = (PIE_TAIL_X, PIE_TAIL_Y)
    ctrl_x = X_TOP_LEFT - 4
    ctrl_y = Y_TOP + (PIE_TAIL_Y - Y_TOP) * 0.72
    _tapered_bezier(p0, (ctrl_x, ctrl_y), p2,
                    w0=W, w1=max(1, W - 1), steps=56)

    # Stroke 2: 横折钩 frame
    _tapered_line((X_TOP_LEFT, Y_TOP), (X_TOP_RIGHT, Y_TOP), W, W, 24)
    _tapered_line((X_TOP_RIGHT, Y_TOP), (X_RIGHT, Y_HOOK), W, W, 32)
    hook_end = (X_RIGHT - 18 * scale, Y_HOOK - 15 * scale)
    _tapered_line((X_RIGHT, Y_HOOK), hook_end,
                  W, max(1, W - 1), 16)

    # Stroke 3: 点 inside
    dx0, dy0 = X(150), Y(115)
    dx1, dy1 = X(160), Y(140)
    _tapered_line((dx0, dy0), (dx1, dy1),
                  max(2, W), max(3, W + 1), 12)
    D.ellipse([dx1 - 3, dy1 - 3, dx1 + 3, dy1 + 3], fill=(0, 0, 0))

    # Stroke 4: 横 crossing (extends outside frame)
    Y_MID = Y(175)
    _tapered_line((X(35), Y_MID), (X(260), Y_MID), W, W, 32)
