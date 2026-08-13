# p3_char_0237_行 — 行 (xíng, "walk/OK"). 6 strokes:
#   Left 彳: pie₁ (upper), pie₂ (mid), shu (long vertical descender).
#   Right 亍: short heng (top), longer heng (middle), shu descender.
# GT shows thin uniform ink (~3-4px), calligraphic MMH style.
# Free-form G3 rendering with math-coord center origin. Callable-function
# form preserved (G3 constraint).

from PIL import Image, ImageDraw
import os

CANVAS = 300
CX, CY = CANVAS / 2, CANVAS / 2


def to_px(mx, my):
    """math coords (center origin, +y up) -> PIL pixel"""
    return CX + mx, CY - my


def stroke_line(draw, p0, p1, width=4):
    x0, y0 = to_px(*p0)
    x1, y1 = to_px(*p1)
    draw.line([(x0, y0), (x1, y1)], fill=(0, 0, 0), width=width)


def stroke_bezier(draw, p0, p1, p2, width=4, n=40, taper_to=None):
    """Quadratic bezier from p0->p2 with control p1.
    Optional taper_to sets end width."""
    pts = []
    for i in range(n + 1):
        u = i / n
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        pts.append((x, y))
    for i in range(len(pts) - 1):
        u = i / (len(pts) - 1)
        w = width
        if taper_to is not None:
            w = max(1, width + (taper_to - width) * u)
        x0, y0 = to_px(*pts[i])
        x1, y1 = to_px(*pts[i + 1])
        draw.line([(x0, y0), (x1, y1)], fill=(0, 0, 0), width=int(round(w)))


def draw_xing(draw):
    # ---- LEFT: 彳 (double-standing-person) — occupies x in [-110, -20] ----
    # Two short 撇 (pie) strokes upper-left, plus long 竖 descending.
    # Pie₁: upper. Head upper-right, tail lower-left.
    stroke_bezier(draw,
                  p0=(-40, 70),   # head
                  p1=(-60, 55),   # ctrl (bow left)
                  p2=(-95, 30),   # tail
                  width=5, taper_to=2)
    # Pie₂: mid, slightly bigger and starts from the shu column.
    stroke_bezier(draw,
                  p0=(-30, 25),   # head near right
                  p1=(-55, 5),    # ctrl
                  p2=(-100, -20), # tail lower-left
                  width=5, taper_to=2)
    # Shu (vertical descender) of 彳 — starts where pie₂ head is, descends.
    stroke_line(draw, (-40, 20), (-40, -110), width=4)

    # ---- RIGHT: 亍 — occupies x in [15, 115] ----
    # Short heng (top).
    stroke_line(draw, (30, 78), (95, 80), width=4)
    # Longer heng (middle) — spans right half, slightly rising.
    stroke_line(draw, (15, 22), (115, 26), width=4)
    # Vertical descender (shu) hanging from middle heng, slight rightward
    # curve at bottom (GT hook-tendency).
    stroke_bezier(draw,
                  p0=(70, 18),
                  p1=(72, -50),
                  p2=(80, -115),
                  width=4)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_xing(draw)
    out = os.path.join(os.path.dirname(__file__), "01_行.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
