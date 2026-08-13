# BANK_DEVIATION
# skipped: (no bank entry for 乍/zha; top half rendered fresh)
# reason: no 乍 primitive in bank; only xin (bottom) reused as-is
# fresh_component: zha_top_for_zen (乍 top of 怎)
"""
怎 (zěn) — top-bottom composition: 乍 (top) + 心 (bottom).
Top 乍: 5 strokes — 撇 + 横 + 竖 + 横 + 横.
Bottom 心: reuse bank xin.py, shifted to bottom half.
"""
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from xin import draw_xin  # noqa: E402

CANVAS = 300


def _to_pixel(x, y):
    return (CANVAS / 2 + x, CANVAS / 2 - y)


def _line(draw, p0, p1, w):
    draw.line([_to_pixel(*p0), _to_pixel(*p1)], fill=(0, 0, 0), width=w)
    # endcaps
    for p in (p0, p1):
        px, py = _to_pixel(*p)
        r = w / 2.0
        draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def _tapered_bezier(draw, p0, p1, p2, w0, w1, n=32):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        pt = _to_pixel(bx, by)
        if prev is not None:
            w = w0 * (1 - u) + w1 * u
            wi = max(1, int(round(w)))
            draw.line([prev, pt], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))
        prev = pt


def draw_zha_top(d):
    """乍 top half of 怎. Sits in upper half of canvas."""
    # Long 撇: starts near top-right, sweeps down-left with slight curve.
    _tapered_bezier(d,
                    (20, 105),     # head (upper-right)
                    (-15, 60),
                    (-55, 20),     # tail (lower-left)
                    w0=6, w1=4)

    # 横 short — top horizontal, crosses 撇 near its head area
    _line(d, (-5, 90), (55, 85), 5)

    # 竖 — vertical descending from right end of top 横
    _line(d, (35, 88), (35, 25), 5)

    # 横 middle — inside the box
    _line(d, (-5, 55), (55, 55), 5)

    # 横 bottom — longer, base of 乍
    _line(d, (-45, 25), (60, 25), 6)


def draw_zen(d):
    draw_zha_top(d)
    # 心 at bottom half — shift down
    draw_xin(d, ox=0, oy=-75, scale=0.90)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)
    draw_zen(d)
    out = os.path.join(_HERE, "01_怎.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
