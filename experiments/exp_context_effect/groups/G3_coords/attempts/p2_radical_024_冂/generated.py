# p2_radical_024_冂 — coord-format render (G3).
#
# 冂 = 2 strokes:
#   1. Left 竖 — a vertical stroke on the LEFT side, slightly bowed left,
#      hanging slightly lower than the right vertical (per GT).
#   2. 横折钩 — horizontal top + right vertical, ending with a short
#      up-and-left hook flick at the base. The horizontal starts weld to
#      the top of the left 竖.
#
# TR-compliance notes:
# - shu primitive: default center (0,0), length 200. For left-竖 we want
#   center ≈ (-65, -10) math coords, length ≈ 170 → scale 0.85, ox=-65, oy=-10.
# - heng_zhe_gou primitive: default has horizontal from (-90,60) to (80,60)
#   then down to (80,-70). At scale=0.90 and (ox=+3, oy=+20), the horizontal
#   sits high with its left end near (-78, +74) ≈ pixel (72, 76), meeting the
#   top of the left 竖 (which tops at (-65, +75)). Right shaft descends to
#   (75, -50) ≈ pixel (225, 200), matching the GT right foot with hook.
#
# Coord math: center-origin, +y up.

import sys
import os
from PIL import Image, ImageDraw

# Make bank primitives importable.
BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(BANK))

from shu import draw_shu
from heng_zhe_gou import draw_heng_zhe_gou


CANVAS = 300


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # Stroke 1: LEFT 竖.
    # standalone shu: center (0,0), length 200.
    # Enlarge to fill canvas: scale=1.05 → length ~210.
    # Center at (-72, -25). Top ≈ (-72, +80), bottom ≈ (-72, -130).
    # This gives a long left vertical that hangs slightly lower than the right foot.
    draw_shu(d, ox=-72, oy=-25, scale=1.05)

    # Stroke 2: 横折钩 spanning top and right side.
    # standalone heng_zhe_gou at scale=1.05:
    #   horizontal from (-94, +63) to (+84, +63), then down to (+84, -73),
    #   then hook flicks up-and-left.
    # We want the horizontal to START near the top of the left 竖 (x=-72, y=+82)
    # and to run right to x ≈ +80. Translate:
    #   ox = +22 → horizontal from (-72, ...) to (+106, ...)
    #   oy = +22 → horizontal y = +85 (welds to top of left 竖)
    #   right shaft descends from (+106, +85) to (+106, -51). Hook flicks in.
    #   Right foot at math y=-51 ≈ pixel y=201, matches GT right foot with hook.
    draw_heng_zhe_gou(d, ox=+22, oy=+22, scale=1.05)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_冂.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
