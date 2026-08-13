# p3_char_0452_疬 (lì, sickness) — 疒 envelope + 力 inside (right-lower).
#
# Composition: 疒 uses the bank ne_sick recipe (draw_ne_chuang) as-is since
# the envelope naturally spans the full canvas at the same proportions
# needed here. 力 is inlined into the right-lower belly (no bank primitive
# exists for 力). Thin uniform widths per GT-thin posture.

import os
import sys

from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ne_sick import draw_ne_chuang, _tapered_line, _tapered_bezier  # noqa: E402

_CANVAS = 300


def draw_li_interior(draw, ox=0, oy=0):
    """Render 力 tucked into 疒's right-lower belly.

    Two strokes:
      1. 横折钩 — short heng across the interior, turns down, ends with a
         small left-pointing hook.
      2. 撇 — from near the heng's left, sweeping down-left across.
    """
    # 横折钩: heng segment
    _tapered_line(draw,
                  (150 + ox, 148 + oy),
                  (222 + ox, 145 + oy),
                  w_head=5.5, w_tail=5.0, n=24)
    # 横折钩: 折 (turn) — right side going down, slight inward curve
    _tapered_bezier(draw,
                    p0=(222 + ox, 145 + oy),
                    p1=(210 + ox, 245 + oy),
                    ctrl=(220 + ox, 195 + oy),
                    w_head=5.5, w_tail=5.5, n=40)
    # 横折钩: 钩 (small left-pointing hook)
    _tapered_line(draw,
                  (210 + ox, 245 + oy),
                  (192 + ox, 235 + oy),
                  w_head=6.0, w_tail=2.5, n=14)

    # 撇: from top-interior, sweeping down-left, crossing the vertical
    _tapered_bezier(draw,
                    p0=(175 + ox, 152 + oy),
                    p1=(138 + ox, 268 + oy),
                    ctrl=(158 + ox, 220 + oy),
                    w_head=5.5, w_tail=3.5, n=60)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_ne_chuang(draw)
    draw_li_interior(draw)
    out = os.path.join(_HERE, "01_疬.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
