#!/usr/bin/env python3
# 仃 (dīng) — 亻 (left) + 丁 (right). 5 strokes total.
# Composition: ren_pang bank primitive on the left, ding_char on the right.
# Per form_catalog: 亻 is identity alias radical; here it needs slight
# compression + left-shift so 丁 has room on the right.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from heng import draw_heng          # noqa: E402
from shu_gou import draw_shu_gou    # noqa: E402


def draw(t, ox=0, oy=0, scale=1.0):
    # 亻 on the left. Compress further (scale 0.70) and shift left so its
    # bulk (pie sweep) lives around x in [-100, -30]. Move up (oy=+10) so
    # its top matches the character top.
    draw_ren_pang(t, ox=ox + (-55) * scale, oy=oy + 10 * scale,
                  scale=0.70 * scale)

    # 丁 on the right. Bump scale so its shu_gou extends the full height
    # of the character, matching 亻's vertical span. heng sits high, then
    # shu_gou descends nearly full-height.
    right_ox = ox + 35 * scale
    right_oy = oy + 0 * scale
    right_scale = 0.75 * scale
    # heng: top crossbar of 丁
    draw_heng(t, ox=right_ox + 0 * right_scale,
              oy=right_oy + 55 * right_scale, scale=0.75 * right_scale)
    # shu_gou: descends from just under heng
    draw_shu_gou(t, ox=right_ox + 5 * right_scale,
                 oy=right_oy - 10 * right_scale, scale=0.75 * right_scale)


def main():
    img = Image.new("RGB", (300, 300), "white")
    t = ImageDraw.Draw(img)
    draw(t)
    out = os.path.join(os.path.dirname(__file__), "01_仃.png")
    img.save(out)


if __name__ == "__main__":
    main()
