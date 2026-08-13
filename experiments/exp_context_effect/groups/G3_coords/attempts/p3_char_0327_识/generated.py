# generated.py — 识 (shi, "recognize"), Phase-3 character, 7 strokes.
# Composition: 讠 (yan_pang, speech radical) on left + 只 (zhi) on right.
#
# GT observation:
#   Left band  (~x 30-100 PIL): tiny slanted dot up-top + a 横折提 shape
#     (short heng, folds down-left as a diagonal shu, then tick up-right).
#     4 strokes total for the radical? Actually MMH simplified 讠 = 2 strokes
#     (dot + 横折提). Thin ink ~5px per P12 (drawer_memory: reject calligraphic
#     weight for MMH-style thin GT).
#   Right band (~x 110-275): 只 — kou box on top + splayed pie/na feet
#     below. Bank #180 (zhi_only) works for this shape; scale it down
#     to ~0.72 and shift right to fit.
#
# Strategy: bank alias for 只 (proven B6 PASS), inline fresh for 讠
# (no bank entry, MMH-thin per P12).

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from zhi_only import draw_zhi  # noqa: E402

CANVAS = 300
CENTER = CANVAS // 2


def _to_pixel(ox, oy):
    return CENTER + ox, CENTER - oy


def _line(t, p1, p2, width=5):
    x1, y1 = _to_pixel(*p1)
    x2, y2 = _to_pixel(*p2)
    t.line([(x1, y1), (x2, y2)], fill=(0, 0, 0), width=width)


def draw_yan_pang(t, ox=0.0, oy=0.0, scale=1.0):
    """讠 speech radical (MMH simplified): tiny top dot + 横折提.

    Thin ink ~5 px (P12). Centered around given (ox, oy).
    """
    s = scale
    # 1) Top dot — small slanted tick from upper-left to lower-right.
    p1 = (ox + -18 * s, oy + 90 * s)
    p2 = (ox + -6 * s,  oy + 72 * s)
    _line(t, p1, p2, width=max(4, int(6 * s)))

    # 2) 横折提 — three-segment continuous stroke.
    #    (a) short heng slightly rising:
    a1 = (ox + -30 * s, oy + 35 * s)
    a2 = (ox + 18 * s,  oy + 42 * s)
    _line(t, a1, a2, width=max(4, int(5 * s)))
    #    (b) fold: diagonal shu going down-left (讠's characteristic slant):
    b1 = a2
    b2 = (ox + -18 * s, oy + -55 * s)
    _line(t, b1, b2, width=max(4, int(5 * s)))
    #    (c) tick up-right (提):
    c1 = b2
    c2 = (ox + 22 * s,  oy + -40 * s)
    _line(t, c1, c2, width=max(4, int(5 * s)))


def draw_shi(t):
    """识 = 讠 (left, ~30% width) + 只 (right, ~60% width)."""
    # Left radical, inline fresh.
    draw_yan_pang(t, ox=-95, oy=0, scale=1.0)
    # Right 只, bank alias, shifted right and slightly downsized.
    draw_zhi(t, ox=45, oy=0, scale=0.75)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_shi(t)
    out = os.path.join(os.path.dirname(__file__), "01_识.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
