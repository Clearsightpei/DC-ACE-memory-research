# heng_gou.py — 横钩 (heng gou, horizontal-then-hook) coord primitive.
# Extracted from attempts/p1_stroke_10_横钩/generated.py after human PASS.
# Description: 横然后末尾勾一下 — a horizontal stroke that ends with a
# small downward-left hook. Uses raw PIL pixel coords (top-left origin,
# +y down) rather than the math-coord _to_pixel helper — matches the
# original passing attempt exactly.


def draw_henggou(draw, ox=0, oy=0, scale=1.0):
    # Horizontal segment — slight rightward-tilt-down feel via slight thickness
    # Start ~ left-upper, end ~ right (just past horizontal middle).
    x0 = 55 + ox
    y0 = 120 + oy
    x1 = 245 + ox
    y1 = 130 + oy  # slight downward slope typical of 横

    # Main 横: draw as a tapered polygon (thin at start, thicker at end — 顿笔)
    line_w_start = int(9 * scale)
    line_w_end = int(13 * scale)

    # Base horizontal — draw as several segments with growing width
    steps = 20
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * t0
        ya = y0 + (y1 - y0) * t0
        xb = x0 + (x1 - x0) * t1
        yb = y0 + (y1 - y0) * t1
        w = int(line_w_start + (line_w_end - line_w_start) * t0)
        draw.line([(xa, ya), (xb, yb)], fill="black", width=w)

    # 顿笔 at end of 横 — a small blob (thicker circle)
    r = int(9 * scale)
    draw.ellipse([x1 - r, y1 - r, x1 + r, y1 + r], fill="black")

    # 钩 (hook): a short stroke going down-and-to-the-left from the 顿笔 point.
    hx0 = x1 + int(2 * scale)
    hy0 = y1 + int(2 * scale)
    hx1 = x1 - int(20 * scale)
    hy1 = y1 + int(38 * scale)

    # Taper the hook: thick at base, thin at tip
    hsteps = 12
    for i in range(hsteps):
        t0 = i / hsteps
        t1 = (i + 1) / hsteps
        xa = hx0 + (hx1 - hx0) * t0
        ya = hy0 + (hy1 - hy0) * t0
        xb = hx0 + (hx1 - hx0) * t1
        yb = hy0 + (hy1 - hy0) * t1
        w = max(1, int((13 - 12 * t0) * scale))
        draw.line([(xa, ya), (xb, yb)], fill="black", width=w)
