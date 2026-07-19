# generated.py — 厄 (è), 4-画 radical.
#
# Decomposition (TR8 INLINE-FRESH test applied):
#   1. Outer 厂 envelope = wide heng + nearly-vertical 丿 descending left.
#      -> `draw_chang` from bank fits exactly at default (厂 is envelope
#      of 厄 too). TR1 satisfied: default is deliberately chosen because
#      the composition uses 厂 as full envelope, same role as standalone.
#   2. Inner 㔾 = 横折 (short top-horizontal then drop) + 竖弯钩
#      (descends then curves right-up-hook at bottom-right).
#      -> Inlined fresh. Bank has no matching primitive at the required
#      compact scale, and per TR8, force-fitting heng_zhe + shu_wan_gou
#      at scale ~0.4 each would produce mismatched widths / detached
#      corners (屮 failure mode from B1).
#
# Layout (math coords, +y up, center origin):
#   heng of 厂: centered ~(+5, +70), width ~170
#   pie  of 厂: from (-80,+65) to (-105,-105), nearly vertical
#   Inner 横折: top-horizontal from (-45, +40) to (+55, +40), then
#              drops to corner (+55, +40) — corner blob — then down to
#              (+55, -20). This is one continuous stroke.
#   Inner 竖弯钩: separate stroke starting from (-30, +25) descending
#                to (-30, -55), then curving right along the bottom to
#                (+55, -70), then a short up-hook to (+40, -55).

import os
import sys

from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from chang import draw_chang  # noqa: E402

CANVAS = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel."""
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def _tapered_line(draw, p0, p1, w0, w1, steps=24):
    """Tapered straight segment between math-coord endpoints."""
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
        pa = _to_pixel(xa, ya)
        pb = _to_pixel(xb, yb)
        draw.line([pa, pb], fill=(0, 0, 0), width=w)


def _tapered_bezier(draw, p0, p1, p2, w0, w1, steps=48):
    """Quadratic bezier with taper from w0 to w1 (math coords)."""
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    prev = None
    prev_w = None
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * x1 + u * u * x2
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * y1 + u * u * y2
        w = max(1, int(round(w0 + (w1 - w0) * u)))
        p = _to_pixel(bx, by)
        if prev is not None:
            draw.line([prev, p], fill=(0, 0, 0), width=prev_w)
            r = w / 2.0
            draw.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=(0, 0, 0))
        prev = p
        prev_w = w


def draw_e(t):
    """Draw 厄 on ImageDraw t at (0,0) default placement, scale 1.0."""

    # ---- Stroke 1+2: 厂 envelope, reused verbatim at default. TR1 note:
    # default is deliberate here — 厂 in 厄 IS the full envelope, same
    # role as standalone. TR8 check: silhouette matches primitive.
    draw_chang(t, ox=0, oy=0, scale=1.0)

    # ---- Stroke 3: inner 横折 — small top-horizontal + drop, sits INSIDE
    # the 厂 envelope (right of pie, below the heng). Compact.
    # Top-horizontal: (-15, +30) -> (+55, +30). Thin, tapered.
    _tapered_line(t, (-15, 30), (55, 30), w0=7, w1=8, steps=24)
    # Corner 顿笔 blob at (+55, +30).
    cx, cy = _to_pixel(55, 30)
    t.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=(0, 0, 0))
    # Drop: (+55, +30) -> (+55, -25), short vertical.
    _tapered_line(t, (55, 30), (55, -25), w0=8, w1=7, steps=20)

    # ---- Stroke 4: inner 竖弯钩 — starts inside 厂 (right of pie),
    # descends nearly vertical, sweeps right along the base, hooks up.
    # Shaft: (-15, +15) -> (-18, -55).
    _tapered_bezier(t, (-15, 15), (-20, -20), (-18, -55),
                    w0=8, w1=9, steps=40)
    # Sweep base to right: (-18, -55) -> (+55, -70).
    _tapered_bezier(t, (-18, -55), (25, -78), (55, -70),
                    w0=9, w1=8, steps=48)
    # Hook up-and-slightly-left from (+55, -70) tip: -> (+42, -50).
    _tapered_line(t, (55, -70), (42, -50), w0=8, w1=2, steps=16)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_e(draw)
    out_path = os.path.join(_HERE, "01_厄.png")
    img.save(out_path)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
