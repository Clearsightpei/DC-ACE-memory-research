# p3_char_0068_纟 — silk radical as standalone character.
# Revision: initial IDENTITY alias of si_zi_pang.py rendered the two
# upper 撇折 hooks overlapping (they collapsed into one shape). GT
# shows THREE clearly separated tiers: small hook at top, larger hook
# in middle, long 提 at bottom. Fix: re-inline the hook helper from
# si_zi_pang and space the two hooks farther vertically (top hook
# higher, more y-gap between hooks).

import os
from PIL import Image, ImageDraw

CANVAS = 300


def _to_px(x, y):
    return (CANVAS / 2 + x, CANVAS / 2 - y)


def _tapered_bezier(draw, p0, p1, p2, w_head, w_tail, n=40, head_ramp=0.1):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        pt = _to_px(bx, by)
        if u < head_ramp:
            w = w_head
        else:
            w = w_head + (w_tail - w_head) * ((u - head_ramp) / (1 - head_ramp))
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, pt], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r],
                         fill=(0, 0, 0))
        prev = pt


def _draw_pie_zhe_hook(draw, cx, cy, size, ink=7):
    # Small 撇 descending to (cx, cy), then a 提-like rightward stroke.
    p0 = (cx + size * 0.55, cy + size * 1.15)
    p2 = (cx, cy)
    p1 = ((p0[0] + p2[0]) / 2 + size * 0.1,
          (p0[1] + p2[1]) / 2 - size * 0.1)
    _tapered_bezier(draw, p0, p1, p2, w_head=ink, w_tail=max(2, ink - 2), n=30)
    h0 = (cx, cy)
    h2 = (cx + size * 1.7, cy + size * 0.55)
    h1 = (h0[0] + size * 0.35, h0[1] + size * 0.1)
    _tapered_bezier(draw, h0, h1, h2, w_head=ink + 1, w_tail=1.5, n=40, head_ramp=0.05)
    r = ink * 0.75
    px, py = _to_px(cx, cy)
    draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    # Top hook (smaller) — raised higher; corner around y=80
    _draw_pie_zhe_hook(draw, cx=-12, cy=80, size=20, ink=6)
    # Middle hook (larger) — corner around y=15 (well below top hook)
    _draw_pie_zhe_hook(draw, cx=-18, cy=15, size=25, ink=7)
    # Long 提 at bottom
    p0 = (-65, -70)
    p2 = (60, -45)
    p1 = ((p0[0] + p2[0]) / 2 - 3, (p0[1] + p2[1]) / 2 - 6)
    _tapered_bezier(draw, p0, p1, p2, w_head=14, w_tail=1.5, n=60, head_ramp=0.08)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_纟.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
