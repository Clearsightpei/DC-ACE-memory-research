# p3_char_0118_从 (cóng, "follow") — two 人 side by side.
# Each 人 = 撇 + 捺 kissing at apex (u_pie=0.0, per form_catalog X-crossing
# family "人 → u_pie=0.0"). Follows the ji_meet_char.py recipe (kiss_apex
# helper) but with 2 人-units (left slightly smaller, right full).
# Thin uniform widths matching GT (MMH-thin).
import os, sys
from PIL import Image, ImageDraw

_HELPERS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            "..", "..", "success_bank",
                                            "code"))
if _HELPERS_DIR not in sys.path:
    sys.path.insert(0, _HELPERS_DIR)
from _shared_helpers import (variant_pie, variant_na, kiss_apex)  # noqa: E402


def draw_ren_unit(draw, apex, pie_tail, na_tail,
                  w_pie_h=4.0, w_pie_t=2.0,
                  w_na_h=3.0, w_na_belly=4.5, w_na_tail=2.0,
                  bow_pie=-5.0, bow_na=+5.0, belly_u=0.7):
    """Draw one 人 (pie + na kissing at `apex`)."""
    pie_h, na_h = kiss_apex(apex, pie_tail, na_tail,
                            u_pie=0.0, bow_pie=bow_pie)
    variant_pie(draw, head=pie_h, tail=pie_tail,
                bow_perp=bow_pie, w_head=w_pie_h, w_tail=w_pie_t)
    variant_na(draw, head=na_h, tail=na_tail,
               bow_perp=bow_na, w_head=w_na_h, w_belly=w_na_belly,
               w_tail=w_na_tail, belly_u=belly_u)


def render():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)

    # LEFT 人 — smaller, positioned in left half.
    # Apex around math (-50, +80), pie sweeps to lower-left corner,
    # na short to lower-middle (in GT the left 人's 捺 is compressed).
    draw_ren_unit(draw,
                  apex=(-50, +80),
                  pie_tail=(-115, -125),
                  na_tail=(-10, -30),  # short compressed na
                  w_pie_h=4.0, w_pie_t=2.0,
                  w_na_h=2.5, w_na_belly=3.5, w_na_tail=2.0,
                  bow_pie=-7.0, bow_na=+3.0, belly_u=0.7)

    # RIGHT 人 — larger, full na sweeping to lower-right corner.
    draw_ren_unit(draw,
                  apex=(+35, +100),
                  pie_tail=(-15, -30),  # short-ish pie (crosses through the left 人's na zone)
                  na_tail=(+115, -130),
                  w_pie_h=4.5, w_pie_t=2.0,
                  w_na_h=3.0, w_na_belly=5.0, w_na_tail=2.0,
                  bow_pie=-6.0, bow_na=+7.0, belly_u=0.7)

    out = os.path.join(os.path.dirname(__file__), "01_从.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    render()
