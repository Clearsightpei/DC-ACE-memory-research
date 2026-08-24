# BANK_DEVIATION
# skipped: you.py, tu.py
# reason: bank entries are turtle-based; ne_sick envelope is PIL-based, so
#         mixing renderers into one canvas is impractical. Inlining 又 and
#         土 in PIL-pixel coords to match the envelope's ink weight.
# fresh_component: you_pil_for_neck_interior, tu_pil_for_neck_interior
#
# p3_char_0542_痉 — 痉 (jìng, spasm). Composition: 疒 envelope + 圣 interior.
# 圣 = 又 (top) + 土 (bottom), stacked inside the sickness envelope's
# right belly.

import os
import sys

_BANK = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/success_bank/code"
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from ne_sick import draw_ne_chuang, _tapered_line, _tapered_bezier

_CANVAS = 300


def draw_you_interior(draw):
    """又 in the interior right of the 疒 envelope. 2 strokes.
    Roughly x=160..260, y=115..190."""
    # Stroke 1: 横撇 — top short heng then curves down-left.
    # A single bezier from top-right down-left.
    _tapered_bezier(
        draw,
        p0=(168, 128),
        p1=(238, 130),
        ctrl=(200, 125),
        w_head=5.0,
        w_tail=5.0,
        n=30,
    )
    # 撇 tail continues from heng right-third down-left.
    _tapered_bezier(
        draw,
        p0=(215, 132),
        p1=(168, 195),
        ctrl=(195, 175),
        w_head=5.5,
        w_tail=3.5,
        n=50,
    )
    # Stroke 2: 捺 — swoops down-right, crossing the 撇 shaft.
    _tapered_bezier(
        draw,
        p0=(200, 145),
        p1=(263, 195),
        ctrl=(228, 172),
        w_head=3.5,
        w_tail=7.0,
        n=50,
    )


def draw_tu_interior(draw):
    """土 in the interior bottom of the 疒 envelope. 3 strokes.
    Roughly x=155..265, y=210..278."""
    # Top heng (shorter).
    _tapered_line(draw, (175, 218), (245, 218), w_head=5.0, w_tail=5.0, n=25)
    # Center 竖.
    _tapered_line(draw, (210, 218), (210, 272), w_head=5.5, w_tail=5.5, n=25)
    # Bottom heng (longer).
    _tapered_line(draw, (155, 274), (270, 274), w_head=5.5, w_tail=5.5, n=30)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # 疒 envelope (bank primitive, PIL-native, uniform thin widths).
    draw_ne_chuang(draw)

    # 圣 interior (fresh inline).
    draw_you_interior(draw)
    draw_tu_interior(draw)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_痉.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
