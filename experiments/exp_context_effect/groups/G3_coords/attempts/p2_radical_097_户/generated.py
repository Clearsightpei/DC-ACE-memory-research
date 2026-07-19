# p2_radical_097_户 (hù) — 4-stroke radical
#
# Decomposition (from GT):
#   1. Top short dian/slanted mark — small tapered dot near top-center
#   2. 横 (heng) — horizontal, sitting a bit below the dot,
#      spans mid-upper canvas
#   3. 横折 — small "コ"-like frame directly under the heng
#      (forms the little box on the top-right that reads as 尸's belly)
#   4. Long 撇 (pie) — sweeps from the LEFT end of stroke 2's heng
#      down and to the LEFT, ending near bottom-left of canvas
#
# Per TR8 (INLINE-FRESH TEST): the long pie in 户 starts at the left
# end of the heng and sweeps the full height of the canvas. The bank
# `pie` primitive is tuned for a standalone diagonal sweep centered on
# canvas — its head is at (+65,+90) which doesn't anchor to a heng
# endpoint. Force-fitting would require large ox shift AND scale > 1
# to reach full height. Inline instead with hand-chosen endpoints.
#
# Similarly the heng+横折 combo is a compact stacked pair — inlining
# lets me match the exact 户 proportions (heng slightly longer than
# 横折's top; 横折's box small enough to sit within the heng's span).
#
# All coords use math-convention (center origin, +y up), converted to
# PIL 300x300 pixels via _to_pixel.

from PIL import Image, ImageDraw
import os

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def tapered_line(t, p0, p1, w0, w1, n=40):
    """Draw a tapered straight line from p0 to p1 in math coords."""
    prev = None
    for i in range(n + 1):
        u = i / n
        mx = p0[0] + (p1[0] - p0[0]) * u
        my = p0[1] + (p1[1] - p0[1]) * u
        px, py = _to_pixel(mx, my)
        w = w0 + (w1 - w0) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def tapered_bezier(t, p0, p_ctrl, p1, w0, w1, n=60):
    """Quadratic bezier with tapered width, math coords in/out."""
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p_ctrl[0] + u ** 2 * p1[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p_ctrl[1] + u ** 2 * p1[1]
        px, py = _to_pixel(bx, by)
        w = w0 + (w1 - w0) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def draw_hu(t):
    # Layout (math coords, +y up):
    # heng at math y = +55, from x=-70 to x=+65 (length 135, width ~10)
    # 横折 box top from x=-25 to x=+65 at math y=+15, drops to y=-40
    # top dian sits at approx (0, +90), tapered short slash going down-right
    # long pie: head at heng's left end (-70, +55), tail at (-95, -105)

    # ---- Stroke 1: top short slanted mark (like a small pie/dian) ----
    # From (+5, +105) sweeping down-left to (-15, +80). Thickens then tapers.
    tapered_bezier(t,
                   p0=(+8, +105),
                   p_ctrl=(-2, +95),
                   p1=(-18, +78),
                   w0=3, w1=8,
                   n=30)

    # ---- Stroke 2: heng ----
    # y = +55, x from -70 to +65
    tapered_line(t,
                 p0=(-70, +55),
                 p1=(+65, +55),
                 w0=9, w1=9,
                 n=40)
    # end blob (顿笔) at right end
    px, py = _to_pixel(+65, +55)
    t.ellipse([px - 6, py - 6, px + 6, py + 6], fill=(0, 0, 0))
    px, py = _to_pixel(-70, +55)
    t.ellipse([px - 5, py - 5, px + 5, py + 5], fill=(0, 0, 0))

    # ---- Stroke 3: 横折 forming the belly-box (closed by pie on left) ----
    # In GT this forms a rectangular belly: horizontal top from left-of-heng-middle
    # to heng's right end, then drops down to form the belly's right side, then
    # turns left and continues as a bottom horizontal closing at the pie shaft.
    # Actually MMH-style 户: it's heng-zhe (top+right) THEN a separate heng
    # underneath. But simpler: single heng-zhe forming right angle, plus a
    # bottom heng closing the box.
    # From GT: the belly box top starts around x=-50, y=+10; goes right to
    # x=+55, y=+10; drops to x=+55, y=-35; then bottom horizontal returns
    # to left edge (closed by pie).
    ink_w = 8
    # Top horizontal of belly
    a = _to_pixel(-50, +15)
    b = _to_pixel(+55, +15)
    # Right vertical
    c = _to_pixel(+55, -35)
    t.line([a, b], fill=(0, 0, 0), width=ink_w)
    t.line([b, c], fill=(0, 0, 0), width=ink_w)
    # 顿笔 at corner
    r = ink_w // 2 + 2
    t.ellipse([b[0] - r, b[1] - r, b[0] + r, b[1] + r], fill=(0, 0, 0))
    # end cap at bottom-right of belly
    t.ellipse([c[0] - 5, c[1] - 5, c[0] + 5, c[1] + 5], fill=(0, 0, 0))
    # Bottom horizontal closing the belly (from bottom-right to left)
    d = _to_pixel(-50, -35)
    t.line([c, d], fill=(0, 0, 0), width=ink_w)
    t.ellipse([d[0] - 4, d[1] - 4, d[0] + 4, d[1] + 4], fill=(0, 0, 0))

    # ---- Stroke 4: long 撇 sweeping from heng's left end down-left ----
    # Head at (-70, +55) — same pixel as heng's left endpoint (weld)
    # Tail at (-105, -125), thin. Control point pulled LEFT to bow the sweep.
    # The pie shaft passes through the left edges of both the top heng and
    # the belly box, closing the box's left side visually.
    tapered_bezier(t,
                   p0=(-70, +55),
                   p_ctrl=(-90, -30),
                   p1=(-105, -125),
                   w0=11, w1=1,
                   n=80)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), "white")
    t = ImageDraw.Draw(img)
    draw_hu(t)
    out_path = os.path.join(os.path.dirname(__file__), "01_户.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
