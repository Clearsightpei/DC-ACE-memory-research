# RETRY MEMORY CHECKLIST (B4->B5 v7 evolution; v8 unlock lifts this
# item's freeze — richer signatures + trust-GT posture)
# Q1 (errata): Look up this item in errata.md. What is the fix idea?
#   Terminal freeze lifted (INTERVENTIONS §v8). Prior kiss_apex retries
#   all failed because apex-kiss silhouette didn't read as calligraphic
#   人. GT actually shows 捺 head starting BELOW the 撇 apex on the
#   撇 shaft (~25-30% down), NOT a true apex kiss. Fix idea: drop
#   kiss_apex helper, place 捺 head on the 撇 body per what GT shows.
#   Copy the p3_char_0011_人 recipe (which visually reads well) but
#   thin the 捺 widths per P12 (MMH GT is thin uniform).
# Q2 (form_catalog): Search form_catalog.md for rows matching the
#   stroke(s) that caused the fail. Which rows are relevant?
#   撇 in 人-family standalone dominant (thin, w_head~5, strong bow);
#   捺 in 人-family dominant tail (thin GT, but visible foot swell).
# Q3 (helpers): Does the fail category match any of these helpers?
#   NO — v8 says trust GT over helpers. kiss_apex fails because GT
#   isn't a kiss. Use variant_pie + variant_na with explicit heads,
#   thin widths per P12. Add a tiny 起笔 tick above the 撇 apex to
#   match GT's small vertical head-nub.

"""p2_radical_028_人 (retry 5) — 人 radical, 2 strokes.

v8-unlock attempt. Terminal freeze lifted for this item per
INTERVENTIONS.md §v8. Prior 4 retries used kiss_apex with u_pie=0.0;
all failed. GT inspection: 撇 apex is high with tiny vertical tick;
捺 head is offset DOWN and slightly right of apex (starts on 撇 body
at ~25-30% length), tail sweeps down-right with modest foot swell.

Recipe adapted from p3_char_0011_人 (visually close to GT) with
thinner na widths matching MMH thin-uniform convention.
"""

import os
import sys
from PIL import Image, ImageDraw

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_G3_ROOT = os.path.abspath(os.path.join(_THIS_DIR, "..", ".."))
_HELPERS_DIR = os.path.join(_G3_ROOT, "success_bank", "code")
if _HELPERS_DIR not in sys.path:
    sys.path.insert(0, _HELPERS_DIR)

from _shared_helpers import variant_pie, variant_na, tapered_line  # noqa: E402

CANVAS = 300


def draw_ren(d):
    # Math coords (center 150,150; +y up).
    # 撇 apex at math(+2, +55) ~ PIL(152, 95).
    # 撇 tail at math(-92, -115) ~ PIL(58, 265).
    pie_head = (2, 55)
    pie_tail = (-92, -115)
    variant_pie(
        d,
        head=pie_head,
        tail=pie_tail,
        bow_perp=-10.0,
        w_head=6,
        w_tail=1.5,
        n=72,
    )

    # Tiny 起笔 tick above 撇 apex (matches GT's small vertical nub).
    tapered_line(d, (3, 65), (2, 56), 1.5, 3.0, n=10)

    # 捺: head starts BELOW apex on 撇 shaft (not a kiss).
    # GT head ~ PIL(158, 128) = math(+8, +22). Tail PIL(257, 262) =
    # math(+107, -112). Thin uniform per P12 with mild foot swell.
    na_head = (8, 22)
    na_tail = (105, -110)
    variant_na(
        d,
        head=na_head,
        tail=na_tail,
        bow_perp=+8.0,
        w_head=2.0,
        w_belly=6.5,
        w_tail=4.5,
        belly_u=0.78,
        n=72,
    )


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)
    draw_ren(d)
    out = os.path.join(_THIS_DIR, "01_人.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
