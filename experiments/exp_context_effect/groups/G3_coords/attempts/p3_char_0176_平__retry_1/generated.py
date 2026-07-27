# p3_char_0176_平__retry_1 — 平 (píng), 5 strokes.
#
# RETRY MEMORY CHECKLIST (B4→B5 v7 evolution)
# Q1 (errata): Look up this item in errata.md. What is the fix idea?
#   Prior fail: top pair of "dots" rendered as long slashes descending
#   from the top heng — too long. Fix: use mirror_dian_pair with tiny
#   w_tail=3 sitting at y≈+60, ABOVE the top heng (not descending
#   through it). Horizontals + vertical were correct — keep them.
# Q2 (form_catalog): Search form_catalog.md for rows matching the
#   stroke(s) that caused the fail. Which rows are relevant?
#   Mirror-dot pair (丷-family). Small dots above a heng — same class
#   as the top of 半, 兰, 首-like shapes.
# Q3 (helpers): Does the fail category match any of these helpers?
#   Mirror-dot pair → mirror_dian_pair from _shared_helpers.
#   Using inline tapered mini-dians here (tiny, w_head=6→w_tail=2)
#   so the mirror symmetry is explicit and the dots stay ABOVE the
#   top heng at y ≈ +60. Uniform thin widths per P12 for hengs/shu.
#
# Stroke order (MMH): 1) 丶 left dot, 2) 丿 right sweep,
# 3) short top 一, 4) long middle 一, 5) 丨 vertical through hengs.

import os
from PIL import Image, ImageDraw

CANVAS = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel (top-left, +y down)."""
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def _tapered_line(t, x0, y0, x1, y1, w_head, w_tail, n=24):
    """Straight tapered line from (x0,y0) to (x1,y1) in math coords."""
    prev = None
    for i in range(n + 1):
        u = i / n
        mx = x0 + (x1 - x0) * u
        my = y0 + (y1 - y0) * u
        px, py = _to_pixel(mx, my)
        if prev is not None:
            w = w_head * (1 - u) + w_tail * u
            wi = max(1, int(round(w)))
            t.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def _thin_line(t, x0, y0, x1, y1, w=5):
    """Uniform-width thin line in math coords (matches MMH GT style)."""
    p0 = _to_pixel(x0, y0)
    p1 = _to_pixel(x1, y1)
    t.line([p0, p1], fill=(0, 0, 0), width=w)


def draw_ping(t, ox=0.0, oy=0.0, scale=1.0):
    """Draw 平. Dots are SMALL mirror pair ABOVE top heng."""
    W = 5  # uniform thin width for hengs / shu

    # 1) Left 丶: small tapered dot ABOVE top heng, slanting down-left.
    #    Head near (-8, +90) (thick), tail at (-28, +65) (thin).
    _tapered_line(t,
                  x0=ox + (-8)  * scale, y0=oy + 90 * scale,
                  x1=ox + (-28) * scale, y1=oy + 65 * scale,
                  w_head=6, w_tail=2)

    # 2) Right 丿: small tapered dot ABOVE top heng, mirror of (1).
    _tapered_line(t,
                  x0=ox + 8  * scale, y0=oy + 90 * scale,
                  x1=ox + 28 * scale, y1=oy + 65 * scale,
                  w_head=6, w_tail=2)

    # 3) Short top 一 — sits below the two dots.
    _thin_line(t,
               x0=ox + (-45) * scale, y0=oy + 55 * scale,
               x1=ox + 45  * scale,   y1=oy + 55 * scale,
               w=W)

    # 4) Long middle 横 — wide, centered.
    _thin_line(t,
               x0=ox + (-115) * scale, y0=oy + 5 * scale,
               x1=ox + 115  * scale,   y1=oy + 5 * scale,
               w=W)

    # 5) Long vertical 竖 — from just above middle heng down past bottom.
    _thin_line(t,
               x0=ox + 0, y0=oy + 45  * scale,
               x1=ox + 0, y1=oy + (-130) * scale,
               w=W)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_ping(t, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_平.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
