# p3_char_0191_仫 — 亻(ren_pang) + 幺 (yao, right).
# 5 strokes total: 亻(2) + 幺 (3: small pie + 撇折 + 点).
# G3: callable Python. Left uses ren_pang bank primitive; right inline fresh
# (幺 not in bank; the two stacked 撇折-like loops are hand-tuned tapered beziers,
# similar in spirit to si_zi_pang but only two hooks, no bottom 提).

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402

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
            draw.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))
        prev = pt


def _draw_pie_zhe_hook(draw, cx, cy, size, ink=6):
    """Small angular 撇折 hook: pie down-left then heng-ish right, meeting at (cx,cy)."""
    # short pie into the corner
    p0 = (cx + size * 0.55, cy + size * 1.10)
    p2 = (cx, cy)
    p1 = ((p0[0] + p2[0]) / 2 + size * 0.10,
          (p0[1] + p2[1]) / 2 - size * 0.10)
    _tapered_bezier(draw, p0, p1, p2, w_head=ink, w_tail=max(2, ink - 2), n=30)
    # heng-ish right-down segment
    h0 = (cx, cy)
    h2 = (cx + size * 1.55, cy + size * 0.55)
    h1 = (h0[0] + size * 0.35, h0[1] + size * 0.10)
    _tapered_bezier(draw, h0, h1, h2, w_head=ink + 1, w_tail=1.5, n=40, head_ramp=0.05)
    # small corner dot
    r = ink * 0.7
    px, py = _to_px(cx, cy)
    draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def _draw_dian(draw, cx, cy, length=14, w_head=3, w_tail=8):
    """Small down-right 点 (dot)."""
    p0 = (cx, cy)
    p2 = (cx + length * 0.7, cy - length * 0.9)
    p1 = ((p0[0] + p2[0]) / 2, (p0[1] + p2[1]) / 2 + 2)
    _tapered_bezier(draw, p0, p1, p2, w_head=w_head, w_tail=w_tail, n=25, head_ramp=0.05)


def draw_yao_right(t):
    """幺 spanning the right half. Two stacked 撇折 loops + closing dot.
    Coords are canvas-centered math (y up)."""
    # top short 撇 (pie) — near top of right half
    p0 = (55, 95)
    p2 = (25, 50)
    p1 = ((p0[0] + p2[0]) / 2 + 5, (p0[1] + p2[1]) / 2 + 4)
    _tapered_bezier(t, p0, p1, p2, w_head=3, w_tail=6, n=25, head_ramp=0.1)
    # upper 撇折 hook — mid-upper right, larger
    _draw_pie_zhe_hook(t, cx=30, cy=30, size=28, ink=5)
    # lower 撇折 hook — lower-right, larger
    _draw_pie_zhe_hook(t, cx=25, cy=-30, size=32, ink=6)
    # 点 at the bottom-right of the lower hook
    _draw_dian(t, cx=72, cy=-55, length=18, w_head=3, w_tail=8)


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)
    # Left: 亻 shifted to left half — pie compressed, shu tall
    draw_ren_pang(d, ox=-55, oy=10, scale=1.15)
    # Right: 幺
    draw_yao_right(d)
    out = os.path.join(_HERE, "01_仫.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    render()
