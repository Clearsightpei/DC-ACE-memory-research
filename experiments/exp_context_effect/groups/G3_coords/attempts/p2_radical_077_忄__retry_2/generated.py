# RETRY MEMORY CHECKLIST (B4→B5 v7 evolution)
# Q1 (errata): Look up this item in errata.md. What is the fix idea?
#   errata says fail mode SHIFTED on retry_1 from "wrong-weight" to
#   "wrong-angle+off-position" — variant_dian was used for both dots
#   but angles+positions were subtly wrong AND shaft dominates. GT is
#   uniformly THIN (P12: MMH GTs use ~4-5px lines, NOT calligraphic
#   10-13px). Fix: drop shaft width to ~5px, dot tail_w to ~6-7px,
#   tighten dot spread, small leftward top-curl on shaft.
# Q2 (form_catalog): Search form_catalog.md for rows matching the
#   stroke(s) that caused the fail. Which rows are relevant?
#   "Mirror-dot family (忄, 丷, 火, 犬 side dot)" — worked example uses
#   `mirror_dian_pair(shaft_x=0, y_center=+10, spread=...)`. That row
#   directly matches this composition.
# Q3 (helpers): Does the fail category match any of these helpers?
#   - Mirror-dot pair (忄) → USE `mirror_dian_pair` (per form_catalog
#     worked example). Prior retry hand-tuned each dot separately and
#     broke the mirror. This time: import mirror_dian_pair + variant_dian.
#   - Uniform thin lines (MMH GT) → per P12, use w~4-6px NOT
#     calligraphic 10-13px. Prior retry used tail_w=12 (way too heavy).

"""p2_radical_077_忄 — retry_2 — heart-side radical (3 strokes).

Fix vs retry_1:
  - THIN lines throughout (P12): shaft ~5-6px, dots tail_w ~6-7px.
  - Use `mirror_dian_pair` helper for the two side dots (prior retry
    hand-tuned both and lost mirror symmetry).
  - Small subtle top-left curl on shaft (GT shows a modest curve at
    the top, not a big flourish).
"""

import sys
sys.path.insert(0, "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/success_bank/code")

from PIL import Image, ImageDraw
from _shared_helpers import (
    to_px, tapered_bezier, tapered_line, variant_dian, mirror_dian_pair
)

CANVAS = 300


def draw_shu_with_top_curl(draw, top_math, bot_math, w=5.0):
    """Central 竖 with a small leftward curl at the very top.
    Renders as: a tiny curl bezier feeding into the shaft top, then
    a straight-ish tapered vertical shaft."""
    # Top curl: small arc from slightly-upper-LEFT of shaft top, curving
    # DOWN and RIGHT into the shaft top. Keep it small (~10-12 px wide).
    curl_start = (top_math[0] - 10.0, top_math[1] + 6.0)
    curl_ctrl = (top_math[0] - 8.0, top_math[1] + 1.0)
    curl_end = top_math
    tapered_bezier(draw, curl_start, curl_ctrl, curl_end,
                   w_head=2.0, w_tail=w, n=24)

    # Main shaft: uniformly thin tapered vertical.
    tapered_line(draw, top_math, bot_math, w0=w, w1=w * 1.1, n=48)


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)

    # STROKE 3 (drawn first for underlay): central shaft.
    # GT shows shaft slightly right of center; near-top to near-bottom.
    shaft_x = 8.0
    shu_top = (shaft_x, 105.0)
    shu_bot = (shaft_x, -125.0)
    draw_shu_with_top_curl(d, shu_top, shu_bot, w=5.5)

    # STROKES 1 & 2: side dots. GT shows:
    #   - LEFT: a longer 撇-like sweep from upper-inner (near shaft)
    #     going DOWN-LEFT and OUT; slightly LOWER than the right dot.
    #   - RIGHT: a shorter 提-like tick going from lower-inner (near
    #     shaft) UP-RIGHT and OUT; slightly HIGHER than the left dot.
    # These are asymmetric, so mirror_dian_pair's pure mirror doesn't
    # fit. Use variant_dian directly with hand-picked endpoints, but
    # keep matched thin widths (P12).
    # Left 撇-dot: head near shaft upper, tail down-left further out.
    variant_dian(
        d,
        head=(shaft_x - 6.0, +42.0),
        tail=(shaft_x - 34.0, +18.0),
        w_head=1.5, w_tail=6.5, bow_perp=+2.0,
    )
    # Right 提-tick: head near shaft lower, tail up-right slightly out.
    # Note: for a 提 (rising tick), thin end is at the tail (up-right),
    # so keep w_tail small too — thin outward flick.
    variant_dian(
        d,
        head=(shaft_x + 6.0, +32.0),
        tail=(shaft_x + 28.0, +45.0),
        w_head=6.0, w_tail=1.5, bow_perp=+1.5,
    )

    out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p2_radical_077_忄__retry_2/01_忄.png"
    img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    render()
