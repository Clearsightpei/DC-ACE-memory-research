# p3_char_0005_丿 — G3 attempt (revision).
#
# GT re-observation:
#   Both GT strokes are THIN throughout (roughly uniform ~3-4 px, only
#   very slight taper). NOT the heavy-head / thin-tail brush profile of
#   the pie_radical bank primitive (which uses w_head=14).
#   The GT looks like MMH-median rendering (thin uniform lines), not a
#   brush-inked calligraphic form.
#   Stroke 1 (dominant 丿): head ~PIL(155,80), curves down-and-left,
#     tail ~PIL(85,265). Math: head (+5,+70) → tail (-65,-115). Clear
#     left-and-down scoop, decently curved.
#   Stroke 2 (short right-falling): head ~PIL(180,100) → tail ~PIL(215,170).
#     Math: head (+30,+50) → tail (+65,-20). Straight-ish, thin.
#   The two strokes DO NOT touch — there is clear whitespace between them.
#
# Revision plan:
#   - Do NOT reuse pie_radical (its w_head=14 gives a heavy blob head
#     that does not match GT's uniform thin line). Per shared_rules
#     "if primitive doesn't fit without extreme transformation, draw
#     fresh". Inline both strokes with variant_pie at uniform-thin widths.
#   - Move stroke 1 left and down (head at +5,+70; tail at -65,-115).
#   - Move stroke 2 to sit clearly separated from stroke 1.
#   - Widths: w_head ~4, w_tail ~2 for both — matches GT median-line look.

import os
import sys
from PIL import Image, ImageDraw

SUCCESS_DIR = os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"
)
sys.path.insert(0, SUCCESS_DIR)

from _shared_helpers import variant_pie  # noqa: E402

CANVAS = 300


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Stroke 1 — dominant 丿, thin and long, curves down-left.
    # head (+5,+70) → tail (-65,-115). Bow to give the classic scoop.
    variant_pie(
        draw,
        head=(5.0, 70.0),
        tail=(-65.0, -115.0),
        bow_perp=-10.0,  # negative -> curves outward to the LEFT (viewer)
        w_head=4.0,
        w_tail=2.0,
        n=60,
    )

    # Stroke 2 — short right-falling, thin, upper-right area, disjoint.
    # head (+30,+50) → tail (+65,-20). Nearly straight, slight bow.
    variant_pie(
        draw,
        head=(30.0, 50.0),
        tail=(65.0, -20.0),
        bow_perp=-2.0,
        w_head=4.0,
        w_tail=2.0,
        n=36,
    )

    out_path = os.path.join(os.path.dirname(__file__), "01_丿.png")
    img.save(out_path)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
