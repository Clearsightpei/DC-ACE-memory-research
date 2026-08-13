"""亥 (hai) — G3 rendering.

Structure (6 strokes, top-down):
  1. 点 — top dot on the 亠 lid
  2. 横 — long horizontal of the 亠 lid
  3. 短撇 — short slanted pie under the heng, upper-left of middle
  4. 折 / 乛 — small horizontal-turn to the right of #3
  5. 长撇 — long pie sweeping from mid to bottom-left
  6. 长捺 — long na crossing #5, sweeping from mid to bottom-right

Inline PIL rendering (callable-python unit preserved).
GT-first: proportions and stroke shapes matched to gt/phase3/亥.png.
"""
from PIL import Image, ImageDraw


def _tapered_line(draw, p0, p1, w0, w1, steps=40):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * t0
        ya = y0 + (y1 - y0) * t0
        xb = x0 + (x1 - x0) * t1
        yb = y0 + (y1 - y0) * t1
        w = w0 + (w1 - w0) * ((t0 + t1) / 2)
        draw.line([(xa, ya), (xb, yb)], fill=0, width=max(1, int(round(w))))


def _tapered_bezier(draw, p0, p1, p2, w0, w1, steps=60):
    def bez(t):
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        return (x, y)
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        a = bez(t0)
        b = bez(t1)
        w = w0 + (w1 - w0) * ((t0 + t1) / 2)
        draw.line([a, b], fill=0, width=max(1, int(round(w))))


def draw_hai(img_size=300):
    img = Image.new("L", (img_size, img_size), 255)
    draw = ImageDraw.Draw(img)

    # 1. 点 — small slanted top dot (upper-center)
    _tapered_line(draw, (152, 48), (162, 62), 3, 4)

    # 2. 横 — long horizontal lid, very slight upward tilt to right
    _tapered_bezier(draw, (55, 110), (150, 102), (245, 104), 4, 4)

    # 3. 短撇 — short pie under the heng, upper-left of middle zone
    _tapered_line(draw, (138, 122), (120, 150), 4, 2)

    # 4. 折 / 乛 — small horizontal-then-turn (like a compressed 乛)
    _tapered_bezier(draw, (140, 145), (172, 148), (178, 175), 3, 3)

    # 5. 长撇 — long pie sweeping from mid-upper to bottom-left
    _tapered_bezier(draw, (150, 160), (108, 215), (65, 275), 6, 2)

    # 6. 长捺 — long na from mid crossing #5, sweeping to bottom-right
    _tapered_bezier(draw, (135, 195), (185, 240), (245, 282), 3, 7)

    return img


if __name__ == "__main__":
    import os
    out_dir = os.path.dirname(os.path.abspath(__file__))
    img = draw_hai(300)
    img.save(os.path.join(out_dir, "01_亥.png"))
    print("wrote", os.path.join(out_dir, "01_亥.png"))
