# RETRY MEMORY CHECKLIST (B4->B5 v7 evolution)
# Q1 (errata): Look up this item in errata.md. What is the fix idea?
#   Errata says retry_n=4: prior retry used variant_dian for both dots as
#   a symmetric mirror pair (per form_catalog "mirrored dot pair" guidance),
#   with heavy ~12px tails. But the ACTUAL MMH GT for 丷 is asymmetric and
#   thin: LEFT = short 点 (small comma-arc, ~30px), RIGHT = longer 撇
#   (diagonal slash from upper-right down-left, ~50px). Prior retries kept
#   force-fitting the "mirror" model. Fix: abandon mirror_dian_pair;
#   render asymmetric per GT with MMH-thin ~4px widths (P12 — matches
#   B4 lesson that MMH GTs are thin uniform lines, not calligraphic).
# Q2 (form_catalog): Search form_catalog.md for rows matching the
#   stroke(s) that caused the fail. Which rows are relevant?
#   Relevant: "dian in top-radical context" (thin ~4px, short span) and
#   "pie short at radical-top" (thin, ~40-50px). Both point away from
#   the mirror_dian_pair helper. The prior "mirrored dot pair" row
#   MISLED us because 丷 in MMH-GT-space is NOT actually a mirror pair.
# Q3 (helpers): Does the fail category match any of these helpers?
#   - X-crossing / apex-kiss / cross-shaft weld -> N/A
#   - Mirror-dot pair -> NO (this was the bug; GT is asymmetric)
#   - Per-stroke form (angle/taper/bow) -> YES: use variant_dian for the
#     small LEFT 点 and variant_pie for the longer RIGHT 撇, both at
#     THIN widths (w=~4px) per P12 (MMH thin-line profile), NOT the
#     calligraphic 12-15px defaults.
#   - Uniform thin lines (MMH GT) -> YES, P12: keep widths uniform-ish
#     and low (3-5px). This is the primary lever.
#
# GT observation (gt/phase2/丷.png, 300x300):
#   - LEFT mark: small arc around pixel (115, 155) -> (128, 175). Reads
#     as a tiny curved 点/短撇. Thin ~4px. Slants DOWN-RIGHT.
#   - RIGHT mark: long slash from ~(180, 150) DOWN-LEFT to ~(155, 200).
#     Reads as a thin 撇 (pie). Thin ~4px, slight bow.
#   - Both sit above canvas mid-vertical (y_center ~ 175 px).
#   - Composition is asymmetric — NOT a mirrored pair.

import sys
sys.path.insert(0, "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/success_bank/code")

from PIL import Image, ImageDraw
from _shared_helpers import variant_pie, variant_dian

CANVAS = 300

OUT = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p2_radical_021_丷__retry_4/01_丷.png"


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)

    # Math coord convention: center (150,150), +y UP.
    # GT pixel (115, 155) -> math (-35, -5)   [PIL y=155 -> math y = 150-155 = -5]
    # GT pixel (128, 175) -> math (-22, -25)
    # GT pixel (180, 150) -> math ( 30,   0)
    # GT pixel (155, 200) -> math (  5, -50)
    # All strokes should read as MMH-thin ~4px (P12 rule for MMH GTs).

    # LEFT 点: small short curved dot, slanting down-right
    variant_dian(
        draw,
        head=(-35.0, -5.0),    # thin start (upper-left)
        tail=(-22.0, -25.0),   # slightly wider end (lower-right)
        w_head=3.0,
        w_tail=5.0,
        bow_perp=-2.0,         # slight downward bow (arcs down)
    )

    # RIGHT 撇 (short pie): long thin diagonal from upper-right to lower-left,
    # tapering to a thin tail. Per P12: MMH-thin widths.
    variant_pie(
        draw,
        head=(30.0, 0.0),      # upper-right start (slightly wider)
        tail=(5.0, -50.0),     # lower-left tail (thin)
        w_head=5.0,
        w_tail=2.5,
        bow_perp=-3.0,         # mild leftward bow (typical pie curl)
    )

    return img


if __name__ == "__main__":
    out = render()
    out.save(OUT)
    print(f"Saved {OUT}")
