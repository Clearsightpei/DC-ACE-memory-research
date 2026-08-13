# p3_char_0516_疰 — 疰 (zhù) = 疒 (envelope) + 主 (interior).
#
# GT decomposition (from gt/phase3/疰.png):
#   Envelope 疒: top dot, thin heng roof, long left-descending 撇,
#     two 冫 marks tucked in upper-left belly.
#   Interior 主: 5 strokes — top dot, top heng, middle heng, shu,
#     bottom heng — sitting in the right/lower belly area.
#
# Composition strategy (same pattern as shan_hernia.py):
#   - Envelope: reuse draw_ne_chuang from ne_sick.py (v9 rerun graduate).
#   - Interior 主: inline fresh in PIL pixel coords, scaled/positioned
#     to fit the belly (bank zhu_master uses canvas-center math coords,
#     which don't fit the belly slot). No BANK_DEVIATION note needed —
#     this is the same coord-system-mismatch pattern as shan_hernia
#     (interior inline is cleaner than mixing coord systems).

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from ne_sick import draw_ne_chuang, _tapered_line  # noqa: E402

_CANVAS = 300


def draw_zhu_interior(draw, cx=200, w=5):
    """主 rendered inline in the belly of 疒.

    5 strokes: top dot, top heng, middle heng, shu, bottom heng.
    Graduated heng width ladder (top < middle < bottom).
    Shu starts AT top heng (no over-stub).
    """
    # Stroke 1: top dot 丶 (canonical lean: upper-left → lower-right).
    draw.line([(cx - 6, 120), (cx + 6, 133)], fill=(0, 0, 0), width=w + 1)

    # Stroke 2: top heng — shortest.
    top_y = 148
    draw.line([(cx - 24, top_y), (cx + 24, top_y)],
              fill=(0, 0, 0), width=w)

    # Stroke 3: middle heng — wider.
    mid_y = 195
    draw.line([(cx - 34, mid_y), (cx + 34, mid_y)],
              fill=(0, 0, 0), width=w)

    # Stroke 4: shu — starts AT top heng, ends at bottom heng.
    bot_y = 258
    draw.line([(cx, top_y), (cx, bot_y)],
              fill=(0, 0, 0), width=w)

    # Stroke 5: bottom heng — widest.
    draw.line([(cx - 48, bot_y), (cx + 48, bot_y)],
              fill=(0, 0, 0), width=w)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    # Envelope 疒 from bank.
    draw_ne_chuang(draw)
    # Interior 主 in the belly (right of pie shaft, below heng roof).
    draw_zhu_interior(draw, cx=200, w=5)
    out = os.path.join(_HERE, "01_疰.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
