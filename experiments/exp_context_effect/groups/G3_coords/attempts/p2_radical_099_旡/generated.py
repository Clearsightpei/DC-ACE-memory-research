"""
旡 (jì) — 4-stroke radical. p2_radical_099_旡.

Structure (from GT observation):
  1. Short 横 at top (upper horizontal, ~1/3 canvas width, high-center)
  2. Longer 横 below (second horizontal, slightly longer, spans mid-upper)
  3. Long 撇 descending from upper-right through the horizontals down to
     bottom-left (this is the sweeping diagonal spine)
  4. 竖弯钩 on the right — vertical descender that curves right and hooks up

Per TR8 (INLINE-FRESH TEST): 4-stroke radical with distinctive curl and
crossing geometry. Force-fitting bank primitives (heng+heng+pie+shu_wan_gou)
would compress badly. Inline all four strokes fresh, hand-picked endpoints.

PIL, 300×300 canvas, math-coord convention (center origin, +y up),
converted internally to PIL pixel coords.
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
CX, CY = W / 2, H / 2


def to_px(mx, my):
    """math coords -> PIL pixel coords (y-flip)."""
    return (CX + mx, CY - my)


def tapered_line(draw, p0, p1, w0, w1, steps=40):
    """Draw a tapered line from p0 (width w0) to p1 (width w1) using
    stamped ellipses."""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        u = i / steps
        x = x0 + (x1 - x0) * u
        y = y0 + (y1 - y0) * u
        w = w0 + (w1 - w0) * u
        r = w / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill='black')


def tapered_bezier(draw, p0, p1, p2, w0, w1, steps=60):
    """Quadratic bezier from p0 -> p2 with control p1, width tapered
    from w0 to w1."""
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * x1 + u ** 2 * x2
        y = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * y1 + u ** 2 * y2
        w = w0 + (w1 - w0) * u
        r = w / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill='black')


def tapered_bezier_3w(draw, p0, p1, p2, w0, wmid, w1, steps=60):
    """Quadratic bezier with 3-point width profile (thin-belly-thin or
    similar)."""
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * x1 + u ** 2 * x2
        y = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * y1 + u ** 2 * y2
        # 3-point width: interpolate w0->wmid->w1 across u
        if u < 0.5:
            uu = u / 0.5
            w = w0 + (wmid - w0) * uu
        else:
            uu = (u - 0.5) / 0.5
            w = wmid + (w1 - wmid) * uu
        r = w / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill='black')


def draw_ji():
    img = Image.new('RGB', (W, H), 'white')
    d = ImageDraw.Draw(img)

    # ---- Stroke 1: top short 横 ----
    # From GT: short horizontal in upper-center, roughly y=+55 in math coords.
    # Spans about x = -25 to +30. Uniform width ~7.
    p0 = to_px(-25, 55)
    p1 = to_px(30, 55)
    tapered_line(d, p0, p1, 7, 6, steps=40)

    # ---- Stroke 2: second 横 (longer), below stroke 1 ----
    # GT shows this second horizontal is longer, spans roughly x=-45 to +45,
    # at y=+25. Actually GT shows this as a heng-zhe-like shape on the LEFT:
    # the left end drops down slightly forming a small hook/foot.
    # Simpler read: longer horizontal at y=+25, slight taper.
    # But looking again — the second horizontal has a small U-shape at left,
    # suggesting a 横折 (heng bends down). Let's model as heng with a small
    # descending tick at the left end.
    # Main horizontal:
    p0 = to_px(-45, 25)
    p1 = to_px(45, 25)
    tapered_line(d, p0, p1, 7, 7, steps=45)
    # Small vertical tick descending from left end (part of the "U" glimpse):
    p0 = to_px(-45, 25)
    p1 = to_px(-45, 5)
    tapered_line(d, p0, p1, 6, 5, steps=15)
    # Small horizontal foot returning right:
    p0 = to_px(-45, 5)
    p1 = to_px(-25, 5)
    tapered_line(d, p0, p1, 5, 4, steps=12)

    # ---- Stroke 3: long 撇 descending from upper-right to bottom-left ----
    # GT shows a long diagonal sweeping stroke that crosses through both
    # horizontals and descends to the bottom-left. Thick head, tapered tail.
    # Start higher and more to the right, sweep more diagonally.
    p0 = to_px(25, 55)     # head, upper right area (starts near top heng right end)
    ctrl = to_px(-5, -20)  # control point creates gentle scoop
    p2 = to_px(-55, -95)   # tail, bottom-left
    tapered_bezier(d, p0, ctrl, p2, 9, 2, steps=70)

    # ---- Stroke 4: 竖弯钩 on the right — descender that curves right and
    # then flicks up (hook).
    # Body: vertical bezier from top to bottom-right
    p0 = to_px(30, 25)      # top of shaft (starts near right end of 2nd heng)
    ctrl = to_px(35, -55)   # gentle rightward bow
    p2 = to_px(58, -85)     # bottom-right, where curve starts
    tapered_bezier(d, p0, ctrl, p2, 7, 8, steps=50)
    # Curve into horizontal foot:
    p0 = to_px(58, -85)
    ctrl = to_px(70, -95)
    p2 = to_px(80, -80)     # rightmost point of the curve
    tapered_bezier(d, p0, ctrl, p2, 8, 7, steps=25)
    # Hook flicking up from the rightmost point:
    p0 = to_px(80, -80)
    p1 = to_px(76, -60)
    tapered_line(d, p0, p1, 7, 1, steps=22)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '01_旡.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    draw_ji()
