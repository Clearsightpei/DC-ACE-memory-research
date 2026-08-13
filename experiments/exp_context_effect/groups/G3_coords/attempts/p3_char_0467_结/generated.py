# BANK_DEVIATION
# skipped: si_zi_pang.py
# reason: bank primitive ignores ox/oy/scale (hand-tuned pixel positions
#   baked in) — its 提 stroke sweeps across the full canvas and would
#   run under 吉 on the right of 结; inline a compact left-column 纟.
# fresh_component: si_zi_pang_compact_for_LR_left

# p3_char_0467_结 — 结 (jié): 纟 (left) + 吉 (right), 9 strokes.
# 吉 = 士 (top) + 口 (bottom).
# Recipe: fresh compact 纟 on left column; bank shi_male + kou stacked
# on right (mirrors 佶 recipe, ji_lucky.py).

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    "..", "..", "success_bank", "code"
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from shi_male import draw_shi_male      # noqa: E402
from kou import draw_kou                # noqa: E402


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


def _draw_pie_zhe_hook(draw, cx, cy, size, ink=6):
    p0 = (cx + size * 0.55, cy + size * 1.15)
    p2 = (cx, cy)
    p1 = ((p0[0] + p2[0]) / 2 + size * 0.1,
          (p0[1] + p2[1]) / 2 - size * 0.1)
    _tapered_bezier(draw, p0, p1, p2,
                    w_head=ink, w_tail=max(2, ink - 2), n=30)
    h0 = (cx, cy)
    h2 = (cx + size * 1.25, cy + size * 0.45)
    h1 = (h0[0] + size * 0.30, h0[1] + size * 0.10)
    _tapered_bezier(draw, h0, h1, h2,
                    w_head=ink + 1, w_tail=1.5, n=40, head_ramp=0.05)
    r = ink * 0.75
    px, py = _to_px(cx, cy)
    draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def draw_si_zi_pang_compact(t):
    """Compact 纟 confined to the left column: 3 strokes."""
    # Upper 撇折 hook (smaller, higher)
    _draw_pie_zhe_hook(t, cx=-95, cy=55, size=18, ink=6)
    # Middle 撇折 hook (slightly larger)
    _draw_pie_zhe_hook(t, cx=-100, cy=15, size=22, ink=7)
    # Bottom 提 — kept inside left column (~x=-115 → x=-25)
    p0 = (-115, -50)
    p2 = (-25, -30)
    p1 = ((p0[0] + p2[0]) / 2 - 3, (p0[1] + p2[1]) / 2 - 5)
    _tapered_bezier(t, p0, p1, p2,
                    w_head=12, w_tail=1.5, n=50, head_ramp=0.08)


def draw_jie_char(t, ox=0.0, oy=0.0, scale=1.0):
    """结 — fresh compact 纟 (left) + 吉 stacked (士 top + 口 bottom, right)."""
    draw_si_zi_pang_compact(t)
    # Right 吉: 士 upper half, 口 lower half of right column.
    draw_shi_male(t, ox=ox + 45 * scale, oy=oy + 55 * scale,
                  scale=0.55 * scale)
    draw_kou(t, ox=ox + 45 * scale, oy=oy + (-55) * scale,
             scale=0.55 * scale)


def _render(out_png):
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_jie_char(d, ox=0.0, oy=0.0, scale=1.0)
    img.save(out_png, "PNG")


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_结.png")
    _render(out)
    print("Wrote", out)
