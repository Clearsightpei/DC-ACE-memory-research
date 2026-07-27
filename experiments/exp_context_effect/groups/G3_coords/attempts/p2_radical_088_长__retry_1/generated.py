# p2_radical_088_长 — RETRY 1.
#
# Prior attempt failure (from vision):
#   - Short 撇 rendered as a tiny blob-with-tick above the heng.
#   - 竖提 shaft too thin and detached on the left; ti flick invisible.
#   - 捺 too thin; started mid-heng and swung right without a
#     credible sweeping belly.
#   - Overall composition too compressed / too small.
#
# Errata fix idea (verbatim from errata.md):
#   "5-stroke complex radical with distinctive 竖提 + long swept 捺.
#    Force-fit lost the long 捺 sweep. Fix: inline 捺 with variant_na,
#    bow_perp≈+12."
#
# Retry redesign — full inline via v7 adaptive helpers:
#   - Read GT again: 长 is 4 strokes (not 5). Stroke order:
#       (1) short 撇   — tiny top flick at upper-left, tail lands on
#                        the shaft's top region.
#       (2) short 横   — a stub that crosses through the shaft near
#                        the top (does NOT span canvas; ~55px wide).
#       (3) 竖提       — the dominant left backbone: tall vertical
#                        shaft with a strong up-right ti flick at bot.
#       (4) long 捺    — sweeps from the upper region of the shaft
#                        (near the top-right area) down and across
#                        to lower-right. This is the visually
#                        dominant stroke; wants a real BELLY.
#
# Approach: draw everything with inline adaptive helpers so we can
# tune angle/taper/curvature independently (v7 memory evolution;
# see form_catalog.md, principles_stroke_family.md P11).
#
# Math coords: origin at (150,150), +y up.

import os
import sys
from PIL import Image, ImageDraw

BANK_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK_DIR)

from _shared_helpers import (  # noqa: E402
    variant_pie,
    variant_na,
    tapered_line,
    to_px,
)

CANVAS_SIZE = 300


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---- Layout plan (math coords) ----
    # Shaft (竖提 vertical) sits at math x = -30 (left of center).
    # Shaft top math y = +85, shaft bottom math y = -75.
    # Ti flick from shaft bottom up-right to about (+25, -35).
    # Short 横 stub crosses shaft near top: math y ≈ +55,
    #   from x=-70 to x=-5 (~65 px, short).
    # Short 撇 comes from just left of shaft-top: head (-15, +100),
    #   tail welds onto the shaft-top area at (-42, +82).
    # Long 捺: head near (-20, +75), tail sweeping down-right to
    #   about (+115, -110). Big belly via bow_perp=+12.

    # ---- Stroke 3 first (backbone): 竖提 shaft ----
    # Inline as a fat tapered_line + a strong ti flick,
    # rather than use draw_shu_ti primitive (which is too thin
    # and its ti flicks too far — collides with 捺 space).
    shaft_top = (-30, +85)
    shaft_bot = (-30, -75)
    tapered_line(d, shaft_top, shaft_bot, w0=13, w1=13, n=40)
    # rounded top cap
    top_px = to_px(*shaft_top)
    d.ellipse([top_px[0] - 7, top_px[1] - 5,
               top_px[0] + 7, top_px[1] + 5], fill=(0, 0, 0))
    # ti flick: from shaft bottom up-and-right, tapered heavy->thin
    ti_end = (+28, -38)
    tapered_line(d, shaft_bot, ti_end, w0=13, w1=2, n=32)

    # ---- Stroke 2: 横 crossing THROUGH the shaft ----
    # Re-examined GT: heng extends both left of the shaft (~15px stub)
    # and rightward beyond (~85px), for a total span ~100px, so it
    # visibly crosses the shaft. Thickness matches shaft (~12).
    heng_left = (-50, +55)
    heng_right = (+55, +55)
    tapered_line(d, heng_left, heng_right, w0=12, w1=12, n=28)

    # ---- Stroke 1: short 撇 at upper-left ----
    # Inline via variant_pie. In GT this is a distinct small stroke
    # sitting above the heng at the LEFT of the shaft, angling down-
    # left with tail landing near the shaft-heng junction. Make it
    # big enough to be recognizable, offset LEFT of the shaft.
    variant_pie(
        d,
        head=(-15, +105),
        tail=(-55, +62),
        bow_perp=-5.0,
        w_head=10.0,
        w_tail=2.0,
    )

    # ---- Stroke 4: long 捺 (DOMINANT) ----
    # Per errata: variant_na with bow_perp≈+12 for real belly.
    # Head at RIGHT END of the heng (upper-right region), sweeping
    # down and to the far lower-right — this is the classic 长 捺
    # geometry (not glued to shaft top).
    variant_na(
        d,
        head=(+50, +58),
        tail=(+125, -110),
        bow_perp=+12.0,
        w_head=3.0,
        w_belly=16.0,
        w_tail=3.0,
        belly_u=0.72,
    )

    out_path = os.path.join(os.path.dirname(__file__), "01_长.png")
    img.save(out_path)
    print(f"Saved {out_path}")


if __name__ == "__main__":
    main()
