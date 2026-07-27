"""乇 (tuō) — 3 strokes: short 撇 (top) + long 横 crossing + 竖弯钩.
Structural cousin of 毛 minus the middle 短横; use mao's approach as template.
"""
import os
import sys
from PIL import Image, ImageDraw

_BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/success_bank/code"
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from shu_wan_gou import draw_shu_wan_gou  # noqa: E402

CANVAS = 300


def _tapered_line_px(draw, p0, p1, w0, w1, n=24):
    for i in range(n):
        u0 = i / n
        u1 = (i + 1) / n
        x0 = p0[0] + u0 * (p1[0] - p0[0])
        y0 = p0[1] + u0 * (p1[1] - p0[1])
        x1 = p0[0] + u1 * (p1[0] - p0[0])
        y1 = p0[1] + u1 * (p1[1] - p0[1])
        w = w0 + (w1 - w0) * ((u0 + u1) / 2)
        draw.line([(x0, y0), (x1, y1)], fill=(0, 0, 0),
                  width=max(1, int(round(w))))


def _bez_px(draw, p0, pc, p1, w0, w1, n=40):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * pc[0] + u ** 2 * p1[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * pc[1] + u ** 2 * p1[1]
        w = w0 + (w1 - w0) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (bx, by)], fill=(0, 0, 0), width=wi)
        prev = (bx, by)


def draw_tuo(draw, ox=0.0, oy=0.0, scale=1.0):
    """乇 — 3 strokes. PIL pixel coords.
    Revision 1: thin the shu_wan_gou shaft (GT strokes are thinner); pull 撇 to
    slope from upper-right down to the top of the shaft (not floating above)."""
    # Stroke 3 anchor: shaft top at math(-5, +45) → PIL(145, 105); use inline thinner shaft.
    # Draw the 竖弯钩 fresh at thickness 8 (GT is thin uniform, not brush-thick).
    # Shaft: from PIL(145, 100) down to (145, 190)
    _tapered_line_px(draw, (145.0, 100.0), (145.0, 190.0), 8.0, 8.0)
    # Curve: quarter circle in PIL coords from (145,190) to (185, 230), center (185, 190) r=40
    # Parametrize: x = cx - r*cos(θ), y = cy + r*sin(θ), θ from 0 to π/2
    import math as _m
    prev = None
    cx, cy, r = 185.0, 190.0, 40.0
    for i in range(13):
        u = i / 12
        ang = u * (_m.pi / 2)
        px = cx - r * _m.cos(ang)
        py = cy + r * _m.sin(ang)
        if prev is not None:
            draw.line([prev, (px, py)], fill=(0, 0, 0), width=8)
        prev = (px, py)
    # Tail horizontal (a bit): from (185, 230) to (225, 230)
    _tapered_line_px(draw, (185.0, 230.0), (225.0, 230.0), 8.0, 8.0)
    # Upward hook tapered
    _tapered_line_px(draw, (225.0, 230.0), (220.0, 205.0), 7.0, 2.0, n=12)

    # Stroke 2: long 横 crossing through middle, thinner uniform
    _tapered_line_px(draw, (55.0, 158.0), (235.0, 152.0), 8.0, 7.0)
    t_end = (235.0, 152.0)
    draw.ellipse([t_end[0] - 4.0, t_end[1] - 4.0, t_end[0] + 4.0, t_end[1] + 4.0],
                 fill=(0, 0, 0))

    # Stroke 1: short 撇 from upper-right, ending at/near the shaft top
    _bez_px(draw, (195.0, 95.0), (170.0, 105.0), (145.0, 105.0), 8.0, 2.0)


if __name__ == "__main__":
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_tuo(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_乇.png")
    img.save(out)
    print(f"wrote {out}")
