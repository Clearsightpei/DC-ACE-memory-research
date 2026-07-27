# p2_radical_083_丬 — G3 retry_1.
#
# Errata diagnosis (prior attempt failed):
#   - Right spine was drawn as a plain vertical line, missing the small
#     horizontal at the top that turns into the vertical (the GT for 丬
#     actually shows the top-right stroke as a 横折 pattern like the
#     right side of 爿/日).
#   - 提 (rising stroke) landed too far LEFT of the spine — never met it.
#   - Upper 撇/dian was too weak and misplaced (should meet the top of
#     the 横折 area, sit inside the upper-left quadrant).
#   - Fix idea from errata: use `variant_dian` with w_tail ~5 for compact
#     upper stroke; make 提 tip actually reach the spine; give the top of
#     the spine a small leftward horizontal or corner.
#
# Read of GT: 3 strokes total —
#   1) short upper 点 / 短撇: upper-left quadrant, thin head → slightly
#      thicker tail, pointing down-left (P10 dian family).
#   2) short 提 (rising): starts lower-left, tip rises to meet the spine
#      near its middle.
#   3) long vertical spine (with small top-left hook / corner): from
#      near top of canvas down past middle, terminating cleanly.
#
# Coord convention: math (center origin, +y up). Canvas 300x300.
# All rendered directly in PIL — no turtle.

from PIL import Image, ImageDraw
import os, sys

CANVAS_SIZE = 300

# Adaptive helpers from _shared_helpers (v7 addition)
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)
from _shared_helpers import (  # noqa: E402
    to_px, tapered_bezier, tapered_line, variant_pie, variant_dian,
)


def draw_spine(draw):
    """Right-side spine — long shu with a very slight leftward flick at top.
    GT: plain long vertical with subtle curl at its top (no full roof).
    Math coords: spine top (+45, +95), spine bottom (+45, -125).
    """
    # Very short top-left curl (subtle, ~10 px) to mimic GT's top hook curve.
    tapered_line(draw, (+35, +100), (+45, +95), 4, 5, n=12)
    # Long vertical spine — width 5 (thin per GT aesthetic).
    tapered_line(draw, (+45, +95), (+45, -125), 5, 5, n=40)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Stroke 3 (spine) — draw first as an anchor.
    draw_spine(draw)

    # Stroke 2: 提 (rising). Starts lower-left, tip meets (stops at) the spine.
    # Head at math (-55, -20), tip at (+42, +18) — stops just left of x=+45 spine.
    tapered_line(draw, (-55, -20), (+42, +18), w0=8, w1=1, n=40)

    # Stroke 1: upper short 撇/点 — above the 提, in upper-left quadrant.
    # From (+0, +60) going down-left to (-45, +30). Slight curve.
    variant_dian(draw, head=(+0, +60), tail=(-45, +30),
                 w_head=2.0, w_tail=5.0, bow_perp=-2.5, n=36)

    out_path = os.path.join(_HERE, "01_丬.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
