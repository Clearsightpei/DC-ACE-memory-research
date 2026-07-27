# p2_radical_030_入 — retry #4 (B5 v7-third-pass memory-index compliant)
#
# RETRY MEMORY CHECKLIST (B4->B5 v7 evolution)
# Q1 (errata): Look up this item in errata.md. What is the fix idea?
#   errata says 入 is retry_n=4, over the terminal-freeze cap, listed as
#   "same as 人" — heads don't kiss at apex / weld point across all
#   retries. Fix idea (form_catalog X-crossing family + B4 lesson):
#   compute the exact weld pixel BEFORE calling variants; and match
#   GT ink weight (MMH thin) rather than calligraphic (P12).
# Q2 (form_catalog): Search form_catalog.md for rows matching the
#   stroke(s) that caused the fail. Which rows are relevant?
#   "X-crossing family (人, 入, 大, 犬, 乂, 文)" section explicitly
#   gives the 入 recipe: u_pie=0.30 (na starts on pie shaft, apex up).
#   Also references gene "亼-roof" (ji_meet_char.py) as SUCCESS
#   template for kiss_apex use with thin uniform widths (w=3-4).
# Q3 (helpers): Does the fail category match any of these helpers?
#   X-crossing / apex-kiss / cross-shaft weld -> USE kiss_apex + pie_point
#   from _shared_helpers.py. This is exactly the weld-computing helper
#   the form_catalog says the prior B3/B4 retries skipped. B4 evidence
#   grepped for "kiss_apex" in retry attempts -> zero adoption, causing
#   persistent fail. This attempt will import and use kiss_apex.
#   Also: match GT weight (P12) -> use thinner widths, not calligraphic.

import os
import sys
from PIL import Image, ImageDraw

# Import helpers from the group's shared helper module.
_HELPERS_DIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
))
if _HELPERS_DIR not in sys.path:
    sys.path.insert(0, _HELPERS_DIR)

from _shared_helpers import (  # noqa: E402
    variant_pie, variant_na, kiss_apex, pie_point,
)


def draw_ru(draw):
    """入 radical, 2 strokes. Math coords (center origin, +y up).

    Recipe follows form_catalog X-crossing family, 入 variant:
      - u_pie = 0.30 (na starts ~30% down pie shaft, not at apex).
      - kiss_apex computes the exact weld pixel; both strokes share it.
      - Widths kept thin (~4-5 px) to match GT's MMH thin-line style
        (P12): the GT shows roughly uniform slender strokes, NOT the
        calligraphic 9/12-belly widths retry_3 used.
    """
    # REVISION (pass 2): first pass looked like 入 but pie top was too
    # straight and na extended too far right, making the silhouette
    # slightly asymmetric vs GT. Adjustments:
    #  - Bow pie more (-11) so top has the classic curl seen in GT.
    #  - Move weld higher on shaft (u=0.22) so na head sits nearer to
    #    the top of the pie, matching GT where na starts high.
    #  - Shorten na horizontally (+70 instead of +80) so 入 doesn't
    #    look lopsided; GT's na tail is only slightly right of center.
    #  - Bump na bow slightly for a subtle sag.

    # Pie: from upper-mid slightly right of center down-left. Extra
    # bow so top curl reads.
    pie_head = (+8, +78)
    pie_tail = (-72, -100)
    bow_pie = -11.0

    # Na: starts on pie shaft high up (u=0.22, 入-style), sweeps
    # down-right to lower-right tail.
    na_tail = (+70, -95)

    pie_h_used, na_h = kiss_apex(pie_head, pie_tail, na_tail,
                                 u_pie=0.22, bow_pie=bow_pie)

    # Draw pie first with thin widths matching MMH GT.
    variant_pie(draw, head=pie_h_used, tail=pie_tail,
                bow_perp=bow_pie, w_head=5, w_tail=2, n=64)

    # Na: thin head at the weld, small belly, thin tail. Overall
    # weight matches GT thin-line style (P12).
    variant_na(draw, head=na_h, tail=na_tail,
               bow_perp=+9.0, w_head=2, w_belly=6, w_tail=2,
               belly_u=0.70, n=64)


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_ru(d)
    out = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "01_入.png"
    )
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
