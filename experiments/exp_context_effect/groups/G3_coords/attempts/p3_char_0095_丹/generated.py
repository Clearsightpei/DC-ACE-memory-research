# 丹 (dān) — 4 strokes: 撇 + 横折钩 (frame) + 点 (inside) + 横 (crossing wider)
# Adapted from yue.py frame recipe; horizontal is a single wide crossing
# through the frame, and one interior dot sits in the upper cell.
from PIL import Image, ImageDraw
import os


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


def draw_dan(D, ox=0, oy=0, scale=1.0):
    def X(x): return 150 + (x - 150) * scale + ox
    def Y(y): return 150 + (y - 150) * scale + oy

    # Frame anchors — centered box, thin lines per P12 (MMH GT is uniform-thin)
    X_TOP_LEFT = X(110)
    X_TOP_RIGHT = X(205)
    X_RIGHT = X(205)
    Y_TOP = Y(80)
    Y_HOOK = Y(245)
    PIE_TAIL_X = X(55)
    PIE_TAIL_Y = Y(265)

    W = max(2, int(4 * scale))  # uniform thin width per P12

    # 1) 撇 — nearly vertical scoop down-left from top-left corner
    p0 = (X_TOP_LEFT, Y_TOP)
    p2 = (PIE_TAIL_X, PIE_TAIL_Y)
    ctrl_x = X_TOP_LEFT - 4
    ctrl_y = Y_TOP + (PIE_TAIL_Y - Y_TOP) * 0.72
    _tapered_bezier(D, p0, (ctrl_x, ctrl_y), p2,
                    w0=W, w1=max(1, W - 1), steps=56)

    # 2) 横折钩 — top horizontal + right vertical + hook
    _tapered_line(D, (X_TOP_LEFT, Y_TOP), (X_TOP_RIGHT, Y_TOP),
                  w0=W, w1=W, steps=24)
    _tapered_line(D, (X_TOP_RIGHT, Y_TOP), (X_RIGHT, Y_HOOK),
                  w0=W, w1=W, steps=32)
    hook_end = (X_RIGHT - 18 * scale, Y_HOOK - 15 * scale)
    _tapered_line(D, (X_RIGHT, Y_HOOK), hook_end,
                  w0=W, w1=max(1, W - 1), steps=16)

    # 3) 点 — a short slanted dot in the upper interior cell
    dx0, dy0 = X(150), Y(115)
    dx1, dy1 = X(160), Y(140)
    _tapered_line(D, (dx0, dy0), (dx1, dy1),
                  w0=max(2, W), w1=max(3, W + 1), steps=12)
    D.ellipse([dx1 - 3, dy1 - 3, dx1 + 3, dy1 + 3], fill=(0, 0, 0))

    # 4) 横 — a wide horizontal that CROSSES the frame (extends outside both sides)
    Y_MID = Y(175)
    _tapered_line(D, (X(35), Y_MID), (X(260), Y_MID),
                  w0=W, w1=W, steps=32)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_dan(D)
    out = os.path.join(os.path.dirname(__file__), "01_丹.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
