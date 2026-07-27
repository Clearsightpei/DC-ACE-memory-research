# p3_char_0125_円 — 円 (Japanese "yen"), 4 strokes.
# Similar to 月 (yue) but: wider aspect (more square), right side is
# 横折 (no hook), interior has two short 横. Left stroke is a soft
# curved 竖/撇 (mild inward bow at bottom).
# Adapted inline from yue.py's PIL recipe.

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


def draw_en(D, ox=0, oy=0, scale=1.0):
    """Draw 円. PIL px base coords; ox/oy shift px, scale uniform."""
    def X(x): return 150 + (x - 150) * scale + ox
    def Y(y): return 150 + (y - 150) * scale + oy

    # Wider than 月: left ~95, right ~215
    X_TOP_LEFT = X(95)
    X_TOP_RIGHT = X(215)
    X_RIGHT = X(215)
    Y_TOP = Y(60)
    Y_BOTTOM = Y(250)
    PIE_TAIL_X = X(88)   # only mild curve at bottom
    PIE_TAIL_Y = Y(252)

    # Stroke 1: 竖/撇 (left side, mild inward curl at bottom)
    p0 = (X_TOP_LEFT, Y_TOP)
    p2 = (PIE_TAIL_X, PIE_TAIL_Y)
    ctrl_x = X_TOP_LEFT - 1
    ctrl_y = Y_TOP + (PIE_TAIL_Y - Y_TOP) * 0.75
    _tapered_bezier(D, p0, (ctrl_x, ctrl_y), p2,
                    w0=int(10 * scale), w1=max(1, int(3 * scale)), steps=56)
    # small head cap
    D.ellipse([p0[0] - 6, p0[1] - 3, p0[0] + 4, p0[1] + 6], fill=(0, 0, 0))

    # Stroke 2: 横折 (top heng then right vertical) — NO hook
    _tapered_line(D, (X_TOP_LEFT, Y_TOP), (X_TOP_RIGHT, Y_TOP),
                  w0=int(9 * scale), w1=int(10 * scale), steps=24)
    # small corner cap
    D.ellipse([X_TOP_RIGHT - 6, Y_TOP - 6, X_TOP_RIGHT + 6, Y_TOP + 6],
              fill=(0, 0, 0))
    _tapered_line(D, (X_TOP_RIGHT, Y_TOP), (X_RIGHT, Y_BOTTOM),
                  w0=int(10 * scale), w1=int(9 * scale), steps=32)

    # Stroke 3: interior heng (upper) — short; sits between the sides
    Y_H1 = Y(135)
    _tapered_line(D, (X_TOP_LEFT + 6, Y_H1 + 1), (X_RIGHT - 10, Y_H1 - 1),
                  w0=int(5 * scale), w1=int(6 * scale), steps=16)

    # Stroke 4: interior heng (lower) — slightly shorter
    Y_H2 = Y(195)
    _tapered_line(D, (X_TOP_LEFT + 4, Y_H2 + 2), (X_RIGHT - 12, Y_H2 - 1),
                  w0=int(5 * scale), w1=int(6 * scale), steps=16)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_en(D)
    img.save("01_円.png")
