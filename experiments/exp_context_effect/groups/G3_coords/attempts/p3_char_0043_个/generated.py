# generated.py — p3_char_0043_个 (gè)
# 3 strokes: 撇 (left-diagonal), 捺 (right-diagonal, kissing at apex),
# then a short 丨 (vertical shu) hanging under the apex.
#
# Uses X-crossing recipe (u_pie=0.0, 人-style kiss) from form_catalog,
# then draws a short shu below the apex using gun_radical scaled down
# and shifted downward.

import os
import sys

_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(_BANK))

from PIL import Image, ImageDraw  # noqa: E402
from _shared_helpers import variant_pie, variant_na, kiss_apex  # noqa: E402
from gun_radical import draw_gun_radical  # noqa: E402


def draw_ge(draw):
    # X-crossing top: 撇 + 捺 kissing at apex (人-style).
    # Apex placed near top; asymmetric — GT shows the na sweeping longer
    # and flatter to the right than the pie's descent left.
    pie_head = (0, 110)         # apex, near top-center
    pie_tail = (-90, -35)       # bottom-left endpoint
    na_tail = (105, -55)        # bottom-right endpoint (longer, flatter)

    pie_h, na_h = kiss_apex(pie_head, pie_tail, na_tail,
                            u_pie=0.0, bow_pie=-6.0)

    variant_pie(draw, head=pie_h, tail=pie_tail,
                bow_perp=-6.0, w_head=8.0, w_tail=1.5, n=60)
    variant_na(draw, head=na_h, tail=na_tail,
               bow_perp=+7.0, w_head=2.0, w_belly=10.0,
               w_tail=2.0, belly_u=0.70, n=70)

    # Short vertical shu hanging from just under the apex, going into
    # the lower half. gun_radical's shaft x sits at +4*scale relative to
    # its ox; nudge ox to center under apex (which is at x=0).
    # We want the shu's TOP (at oy + 85*scale in gun's coords) to sit
    # just below the apex (y ~ +75), so oy + 85*scale = 75 → oy ≈ 30.
    # (Then shaft bottom lands near y = 30 - 100*0.55 = -25 area — too
    # short; extend by lowering oy and lengthening scale slightly.)
    # Target: top ≈ y=+80, bottom ≈ y=-80.
    # scale=0.85: head at oy + 85*0.85 = oy+72; want +80 → oy=+8.
    # bottom at oy - 100*0.85 = 8 - 85 = -77. Good.
    draw_gun_radical(draw, ox=-4, oy=8, scale=0.85)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_ge(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_个.png")
    img.save(out)
    print("saved", out)


if __name__ == "__main__":
    main()
