# 冘 — 4 strokes: top dot + heng-gou (冖 cover) + 撇 + 横折弯钩 (几 bottom).
# Reuses ji.py's bottom recipe with recentering, and renders top dot + 横钩 fresh.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ji import draw_ji, _tapered_bezier, _tapered_line, _apply  # noqa: E402


def draw_dian_dot(draw, cx, cy, r=5):
    """Small top dot 点."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))


def draw_heng_gou_cover(draw, ox=0, oy=0, scale=1.0):
    """冖-style cover: horizontal with small hook down at right end.
    Coords authored on 300x300 canvas."""
    # main horizontal
    _tapered_line(draw, (75.0, 105.0), (225.0, 105.0),
                  6, 8, ox, oy, scale, steps=40)
    # 顿笔 blob at right
    rx, ry = _apply(225.0, 105.0, ox, oy, scale)
    r = 5 * scale
    draw.ellipse([rx - r, ry - r, rx + r, ry + r], fill=(0, 0, 0))
    # small hook down-left
    _tapered_line(draw, (225.0, 105.0), (218.0, 122.0),
                  8, 3, ox, oy, scale, steps=12)


def draw_you(img_draw, ox=0, oy=0, scale=1.0):
    """冘: top dot + 冖 cover + 几-bottom (撇 + 横折弯钩)."""
    # 1) top dot centered above cover — a proper short 点 stroke.
    # Position near (148, 70) — small droplet from upper-left to lower-right.
    _tapered_bezier(img_draw, (146.0, 62.0), (150.0, 70.0), (156.0, 82.0),
                    5, 10, ox, oy, scale, steps=20)
    # blob at bottom of dot for weight
    bx, by = _apply(156.0, 82.0, ox, oy, scale)
    r = 5 * scale
    img_draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))

    # 2) 冖 cover — narrower than my first attempt, matches GT shorter cover.
    _tapered_line(img_draw, (90.0, 108.0), (215.0, 108.0),
                  5, 7, ox, oy, scale, steps=40)
    # 顿笔 blob at right
    rx, ry = _apply(215.0, 108.0, ox, oy, scale)
    r = 5 * scale
    img_draw.ellipse([rx - r, ry - r, rx + r, ry + r], fill=(0, 0, 0))
    # small hook down at right end
    _tapered_line(img_draw, (215.0, 108.0), (210.0, 122.0),
                  7, 3, ox, oy, scale, steps=10)

    # 3) 撇 — from just inside left of cover down to bottom-left.
    _tapered_bezier(img_draw, (115.0, 108.0), (95.0, 180.0), (70.0, 260.0),
                    9, 3, ox, oy, scale, steps=60)

    # 4) 横折弯钩 — right side, from cover's right area sweeping down and right-hooking up.
    # vertical descent with slight left bow
    _tapered_bezier(img_draw, (195.0, 108.0), (188.0, 180.0), (185.0, 250.0),
                    10, 9, ox, oy, scale, steps=40)
    # 弯 sweep right
    _tapered_bezier(img_draw, (185.0, 250.0), (205.0, 268.0), (230.0, 265.0),
                    9, 8, ox, oy, scale, steps=30)
    # blob at hook base
    hx, hy = _apply(230.0, 265.0, ox, oy, scale)
    r = 5 * scale
    img_draw.ellipse([hx - r, hy - r, hx + r, hy + r], fill=(0, 0, 0))
    # upward hook
    _tapered_line(img_draw, (230.0, 265.0), (227.0, 240.0),
                  8, 2, ox, oy, scale, steps=14)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_you(draw, ox=0, oy=0, scale=1.0)
    out = os.path.join(_HERE, "01_冘.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
