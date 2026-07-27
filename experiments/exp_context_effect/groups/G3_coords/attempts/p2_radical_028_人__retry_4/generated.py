# RETRY MEMORY CHECKLIST (B4→B5 v7 evolution)
# Q1 (errata): Look up this item in errata.md. What is the fix idea?
#   Errata note: "heads still don't kiss at apex - fail mode SAME across
#   all retries". Retry_3 used inline _tb bezier but pie and na still
#   didn't share the apex pixel. Fix: use kiss_apex helper to compute
#   the shared apex pixel EXPLICITLY, then pass identical head coord
#   into variant_pie and variant_na (u_pie=0.0 for 人 style).
# Q2 (form_catalog): Search form_catalog.md for rows matching the
#   stroke(s) that caused the fail. Which rows are relevant?
#   "X-crossing family (人, 入, 大, 犬, 乂, 文)" worked example gives
#   the exact recipe. Also 亼-roof rows for 撇/捺 (thin uniform w~4)
#   from ji_meet_char.py, which is a validated PASSED X-crossing recipe.
# Q3 (helpers): Does the fail category match any of these helpers?
#   YES: X-crossing / apex-kiss / cross-shaft weld -> use `kiss_apex`
#   from _shared_helpers.py. Also uniform thin lines per P12 (MMH GT
#   is thin uniform ~4px). Use variant_pie + variant_na with modest
#   widths (w_head~5, w_tail~2 for pie; w_head~2 w_belly~6 w_tail~2
#   for na) rather than heavy calligraphic widths.

"""p2_radical_028_人 (retry 4) — 人 radical, 2 strokes (撇 + 捺).

Failure history:
  - retry_1: both strokes bowed outward (gothic arch), too round.
  - retry_2: still no apex kiss.
  - retry_3: PIL inline _tb — apex heads at (150,90) vs (155,100),
    a visible 5px gap.
Fix: use kiss_apex(u_pie=0.0) so pie_head and na_head are the SAME
math-coord pixel. Then pass identical `head=` to both variants.
Widths kept thin per P12 (MMH GT is thin uniform lines, not
calligraphic).
"""

import os
import sys
from PIL import Image, ImageDraw

# Import G3 shared helpers from the success_bank/code directory.
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_G3_ROOT = os.path.abspath(os.path.join(_THIS_DIR, "..", ".."))
_HELPERS_DIR = os.path.join(_G3_ROOT, "success_bank", "code")
if _HELPERS_DIR not in sys.path:
    sys.path.insert(0, _HELPERS_DIR)

from _shared_helpers import variant_pie, variant_na, kiss_apex  # noqa: E402

CANVAS = 300


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)

    # Math coords (center origin, +y up). GT 人 sits with apex slightly
    # above center and legs sweeping to lower corners.
    # Apex at math ~(0, +65). Pie tail lower-left ~(-70, -80).
    # Na tail lower-right ~(+70, -80).
    # Revision 1: pass 1 legs too short/steep (silhouette a narrow ^).
    # GT legs reach near-bottom corners. Extend tails outward and down.
    pie_head = (0, 62)
    pie_tail = (-95, -108)
    na_tail = (88, -100)

    # kiss_apex u_pie=0.0 -> both heads land on pie_head (apex kiss).
    pie_h, na_h = kiss_apex(
        pie_head, pie_tail, na_tail=na_tail, u_pie=0.0, bow_pie=-8.0
    )

    # 撇 (pie): apex -> lower-left with mild leftward bow.
    # Thin per P12: w_head=5 (small 顿笔), w_tail=2 (thin tail).
    variant_pie(
        d,
        head=pie_h,
        tail=pie_tail,
        bow_perp=-10.0,
        w_head=5,
        w_tail=2,
        n=72,
    )

    # 捺 (na): apex -> lower-right, gentle belly, thin foot.
    # Thin per P12: w_head=2, w_belly=6, w_tail=2. Belly at 0.7.
    variant_na(
        d,
        head=na_h,
        tail=na_tail,
        bow_perp=+10.0,
        w_head=2,
        w_belly=6,
        w_tail=2,
        belly_u=0.72,
        n=72,
    )

    out = os.path.join(_THIS_DIR, "01_人.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
