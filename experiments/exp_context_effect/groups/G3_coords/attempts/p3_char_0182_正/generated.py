# p3_char_0182_正 — 正 (zhèng), 5 strokes: 横 竖 横 竖 横.
# Structure: top heng, left-side shu, short mid heng, small mid shu, bottom long heng.
# Revision 2: per P12 (memory_index B5 note) MMH GT uses uniform thin ~4px lines.
# The frozen heng/shu primitives render 12px which is too thick for GT match, so
# this revision inlines thin lines at ~4px width via a small helper. Coord layout
# still follows the primitive canonical (math coords, center origin, +y up).
import os
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
CANVAS = 300
THIN = 4


def _to_px(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def _thin_heng(d, ox, oy, scale=1.0):
    half = 100.0 * scale
    d.line([_to_px(ox - half, oy), _to_px(ox + half, oy)],
           fill=(0, 0, 0), width=THIN)


def _thin_shu(d, ox, oy, scale=1.0):
    half = 100.0 * scale
    d.line([_to_px(ox, oy + half), _to_px(ox, oy - half)],
           fill=(0, 0, 0), width=THIN)


def draw_zheng(d, ox=0, oy=0, scale=1.0):
    # Stroke 1 — top heng: length ~130 (scale 0.65), center x≈+5, y≈+65.
    _thin_heng(d, ox + 5 * scale, oy + 65 * scale, 0.65 * scale)
    # Stroke 2 — left shu: from just under top-heng left end down to bottom heng.
    #   Top-heng left end at x=-60. Shu descends from y≈+65 to y≈-70; midpoint y≈-2, length ~135, scale 0.68.
    _thin_shu(d, ox - 58 * scale, oy - 2 * scale, 0.68 * scale)
    # Stroke 3 — mid short heng: right side, lower-mid height.
    #   length ~85 (scale 0.42), center x≈+15, y≈-10 (closer to bottom-heng than top).
    _thin_heng(d, ox + 15 * scale, oy - 10 * scale, 0.42 * scale)
    # Stroke 4 — small mid shu: short vertical between top and mid heng, right of left-shu.
    #   length ~55 (scale 0.28), center y≈+28, x≈+10.
    _thin_shu(d, ox + 10 * scale, oy + 28 * scale, 0.28 * scale)
    # Stroke 5 — bottom long heng: widest, base.
    #   length ~200 (scale 1.00), center x≈+5, y≈-72.
    _thin_heng(d, ox + 5 * scale, oy - 72 * scale, 1.00 * scale)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_zheng(d, ox=0, oy=0, scale=1.0)
    out = os.path.join(_HERE, "01_正.png")
    img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
