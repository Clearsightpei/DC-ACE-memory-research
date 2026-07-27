# 用 (yòng, "use"), 5 strokes.
# Recipe: adapt yue.py frame (撇 + 横折钩 + 2 interior 横) to a WIDER
# rectangle, and add a central 竖 that extends below the bottom edge.
# GT shows: wide frame, left side ~ near-vertical 撇 with slight scoop,
# top-right 横折钩, two evenly-spaced interior hengs that touch the
# central shu, central shu descends past the frame bottom.

from PIL import Image, ImageDraw


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


def draw_yong(D, ox=0, oy=0, scale=1.0):
    def X(x): return 150 + (x - 150) * scale + ox
    def Y(y): return 150 + (y - 150) * scale + oy

    # Wider frame than 月 — 用 is a wider rectangle
    X_TOP_LEFT = X(85)
    X_TOP_RIGHT = X(225)
    X_RIGHT = X(225)
    Y_TOP = Y(60)
    Y_HOOK = Y(250)
    PIE_TAIL_X = X(60)
    PIE_TAIL_Y = Y(262)
    X_MID = X(150)

    # 1) 撇 (left side, near-vertical with tail scoop)
    p0 = (X_TOP_LEFT, Y_TOP)
    p2 = (PIE_TAIL_X, PIE_TAIL_Y)
    ctrl_x = X_TOP_LEFT - 2
    ctrl_y = Y_TOP + (PIE_TAIL_Y - Y_TOP) * 0.72
    _tapered_bezier(D, p0, (ctrl_x, ctrl_y), p2,
                    w0=int(12 * scale), w1=max(1, int(2 * scale)), steps=56)
    D.ellipse([p0[0] - 7, p0[1] - 4, p0[0] + 4, p0[1] + 7], fill=(0, 0, 0))

    # 2) 横折钩 (top heng + right 竖 + hook)
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

    # 3) Interior heng 1 (upper)
    Y_H1 = Y(130)
    _tapered_line(D, (X_TOP_LEFT + 3, Y_H1 + 2), (X_RIGHT - 6, Y_H1 - 1),
                  w0=int(5 * scale), w1=int(7 * scale), steps=20)

    # 4) Interior heng 2 (lower)
    Y_H2 = Y(195)
    _tapered_line(D, (X_TOP_LEFT - 4, Y_H2 + 2), (X_RIGHT - 6, Y_H2 - 1),
                  w0=int(5 * scale), w1=int(7 * scale), steps=20)

    # 5) Central 竖 — from just below Y_TOP; only slightly past bottom
    Y_SHU_TOP = Y(78)
    Y_SHU_BOT = Y(265)
    _tapered_line(D, (X_MID, Y_SHU_TOP), (X_MID, Y_SHU_BOT),
                  w0=int(9 * scale), w1=int(8 * scale), steps=30)
    # small starter cap
    D.ellipse([X_MID - 5, Y_SHU_TOP - 3, X_MID + 5, Y_SHU_TOP + 5],
              fill=(0, 0, 0))


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_yong(D)
    img.save(
        "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0168_用/01_用.png"
    )
