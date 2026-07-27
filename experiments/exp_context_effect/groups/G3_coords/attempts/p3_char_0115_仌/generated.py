# p3_char_0115_仌 — 仌 (bīng, ancient form of 冰): two 人 stacked.
# Revision 1: first pass was too symmetric (∧∧-looking). GT shows:
#  - pie leans steeper (angled ~60° from vertical), na starts slightly
#    right of apex tip due to bezier bow, and na has a longer sweep.
#  - upper 人 is smaller, centered upper.
#  - lower 人 is larger, apex is up-left of center, na sweeps down-right.
import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from _shared_helpers import variant_pie, variant_na, kiss_apex  # noqa: E402


def draw_ren(draw, apex, pie_tail, na_tail, bow_pie=-6.0, bow_na=+8.0,
             w_head_pie=4.0, w_tail_pie=2.0,
             w_head_na=3.0, w_belly_na=4.5, w_tail_na=2.0):
    pie_h, na_h = kiss_apex(apex, pie_tail, na_tail, u_pie=0.0, bow_pie=bow_pie)
    variant_pie(draw, head=pie_h, tail=pie_tail,
                bow_perp=bow_pie, w_head=w_head_pie, w_tail=w_tail_pie)
    variant_na(draw, head=na_h, tail=na_tail,
               bow_perp=bow_na, w_head=w_head_na, w_belly=w_belly_na,
               w_tail=w_tail_na, belly_u=0.7)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Upper 人 — smaller. Apex upper-left of center. Longer pie sweeping down-left.
    # Math coords: apex ~(-10,+95); pie ends bottom-left ~(-60,+20); na
    # ends bottom-right ~(+55,+25) — but shorter na relative to pie.
    draw_ren(
        draw,
        apex=(-10, +95),
        pie_tail=(-58, +18),
        na_tail=(+55, +20),
        bow_pie=-8.0, bow_na=+6.0,
        w_head_pie=4.0, w_tail_pie=2.0,
        w_head_na=3.0, w_belly_na=4.0, w_tail_na=2.0,
    )

    # Lower 人 — larger. Apex a bit left of center, upper mid-canvas.
    # pie sweeps down-left long; na sweeps down-right longer (dominant in GT).
    draw_ren(
        draw,
        apex=(-5, +5),
        pie_tail=(-75, -105),
        na_tail=(+85, -110),
        bow_pie=-10.0, bow_na=+8.0,
        w_head_pie=4.5, w_tail_pie=2.0,
        w_head_na=3.0, w_belly_na=5.0, w_tail_na=2.5,
    )

    out = os.path.join(_HERE, "01_仌.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
