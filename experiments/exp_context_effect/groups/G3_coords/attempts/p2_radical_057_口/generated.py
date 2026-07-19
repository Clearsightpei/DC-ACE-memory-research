# p2_radical_057_口 — G3 coord-bank attempt.
#
# 口 is a 3-画 enclosing radical:
#   1) 竖 on the left (top-to-bottom vertical).
#   2) 横折 on top-right (horizontal head + right-turn descending down).
#   3) 横 across the bottom, closing the box.
#
# GT observations (gt/phase2/口.png):
#   - Small-ish box, occupying roughly the middle-lower of the canvas.
#   - Slight slant: top edge dips slightly to the right; right side leans
#     inward at the bottom (classic calligraphic 口 — not a rigid rectangle).
#   - Corners have small "lifts" (顿笔), especially bottom-right where the
#     final 横 stops short and rises.
#   - Ink weight ~ 8-10 px (radical scale, smaller than standalone strokes).
#
# Strategy (TR1-TR7 compliant):
#   - Use bank primitives `draw_shu`, `draw_heng`, `draw_heng_zhe` with
#     deliberate (ox, oy, scale) chosen for the small-box composition.
#   - Corners must weld: left-竖 top meets 横折 head-start; 横折 tail-bottom
#     meets bottom-横 right end; bottom-横 left end meets left-竖 bottom.
#
# Coord math (math convention: origin at canvas center, +y up):
#   Target box corners (math coords):
#     top-left     TL = (-55,  25)
#     top-right    TR = (+55,  25)
#     bottom-left  BL = (-55, -55)
#     bottom-right BR = (+55, -55)
#   The box is ~110 wide x 80 tall, centered at (0, -15) — slightly lower
#   than canvas middle to match GT placement.
#
# --- Primitive transforms ---
#
# TR6 — 竖 (left side) --------------------------------------------------
#   Standalone shu: center (0,0), length 200 px, thickness 12.
#   For 口 left side we need a vertical from TL(-55, 25) to BL(-55, -55):
#     length = 80 px  →  scale = 80/200 = 0.40  (but TR5 warns scale<0.4;
#     0.40 is borderline. We'll bump length to 90 → scale 0.45 by nudging
#     the top slightly higher; still inside the box footprint.)
#   Actually keep scale = 0.42 (length 84 px); the 竖 spans y=+27..-57.
#   center = midpoint of top/bot = (-55, -15).
#   shu default center = (0, 0). So ox = -55, oy = -15, scale = 0.42.
#
# TR6 — 横折 (top + right) ---------------------------------------------
#   Standalone heng_zhe internal coords (see heng_zhe.py at scale=1):
#     h_start = (-90, 60), corner = (80, 60), v_end = (80, -75).
#     H-width = 170 px, V-drop = 135 px, ratio ~ 1.26.
#   For 口 we need top edge from TL(-55,25) to TR(55,25) (110 wide) and
#   right edge from TR(55,25) down to BR(55,-55) (80 tall).
#   Uniform scale won't match both, but scaling by width ratio: 110/170 ≈ 0.65.
#   At scale=0.65: h_start=(-58.5, 39), corner=(52, 39), v_end=(52, -48.75).
#     Then ox = TR.x - corner.x = 55 - 52 = +3;
#          oy = TR.y - corner.y = 25 - 39 = -14.
#   → h_start world ≈ (-55.5, 25), corner ≈ (55, 25), v_end ≈ (55, -62.75).
#   Bottom of the right side lands ~7 px below BR — close enough for the
#   bottom 横 to weld under it (small overhang reads as a lift, GT-like).
#
# TR6 — 横 (bottom) ---------------------------------------------------
#   Standalone heng: length 200 px, thickness 12, centered (0,0).
#   Need horizontal at y ≈ -55 from BL(-55,-55) to BR(55,-55): length 110.
#   scale = 110/200 = 0.55. center at (0, -55).
#   → ox = 0, oy = -55, scale = 0.55.
#
# TR7 — eyeball sanity check:
#   TL ~ 竖 top (-55, +27)  vs  横折 h_start (-55.5, 25)   → within 2 px  OK
#   TR ~ 横折 corner (55, 25)                              → hard weld    OK
#   BR ~ 横折 v_end (55, -62.75) vs bottom-横 right (55,-55) → ~8 px lift OK
#   BL ~ 竖 bot (-55, -57) vs bottom-横 left (-55, -55)    → ~2 px lift  OK
#   All strokes within ~50 px of canvas edges → ample margin  OK
#
# All calls are TR1-deliberate. No default calls.

import os
import sys
from PIL import Image, ImageDraw

# Make the shared bank importable.
BANK_CODE = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
sys.path.insert(0, BANK_CODE)

from shu import draw_shu            # noqa: E402
from heng import draw_heng          # noqa: E402
from heng_zhe import draw_heng_zhe  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)

    # Revised for better GT match: bigger box, more centered vertically.
    # Target corners (math coords):
    #   TL = (-65, 50), TR = (65, 50), BL = (-65, -50), BR = (65, -50).
    # Box ~ 130 wide x 100 tall, centered at (0, 0).

    # 1) Left 竖: TL(-65,50) → BL(-65,-50). center=(-65, 0), length 100.
    #    scale = 100/200 = 0.50.
    draw_shu(draw, ox=-65, oy=0, scale=0.50)

    # 2) Top+right 横折 at scale 0.75:
    #    internal at s=0.75: h_start=(-67.5, 45), corner=(60, 45), v_end=(60,-56.25).
    #    weld corner to TR(65,50): ox = 65 - 60 = +5; oy = 50 - 45 = +5.
    #    world: h_start ≈ (-62.5, 50); corner = (65, 50); v_end = (65, -51.25).
    draw_heng_zhe(draw, ox=+5, oy=+5, scale=0.75)

    # 3) Bottom 横 at y=-50, length 130 → scale 0.65.
    draw_heng(draw, ox=0, oy=-50, scale=0.65)

    out_path = os.path.join(os.path.dirname(__file__), "01_口.png")
    img.save(out_path)
    print("wrote", out_path)


if __name__ == "__main__":
    main()
