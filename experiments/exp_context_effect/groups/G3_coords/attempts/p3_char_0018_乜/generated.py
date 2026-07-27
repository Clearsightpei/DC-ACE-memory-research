# p3_char_0018_乜 — G3 first attempt.
# 乜 has 2 strokes:
#   S1: 横撇 (top): short horizontal, then sharp pie down-left
#   S2: 竖弯钩 (base): diagonal shaft down-left → long horizontal along bottom → hook up on right
#
# Approach: inline fresh using _shared_helpers.tapered_bezier / tapered_line.
# 横撇 primitive doesn't quite fit (乜 has a longer/lower pie tail); the
# bottom stroke is a diagonal-start 竖弯钩 not aligned with the pure
# vertical shu_wan_gou primitive, so inline both fresh.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(_BANK))

from _shared_helpers import tapered_bezier, tapered_line, to_px  # noqa: E402


def draw_ye_mie(t, ox=0.0, oy=0.0, scale=1.0):
    """乜 (miē / niè), 2 strokes."""

    def T(p):
        return (p[0] * scale + ox, p[1] * scale + oy)

    # -----------------------------------------------------------------
    # S1: 横撇 — short heng across top, then sharp pie down-left
    # -----------------------------------------------------------------
    # Short flat heng: math (-45, +42) -> (+15, +45). Slight upward tilt.
    tapered_line(t, T((-45, 42)), T((15, 45)), 8 * scale, 9 * scale, n=24)
    # 顿笔 blob at corner (+15, +45) — PIL(165, 105)
    cx, cy = to_px(*T((15, 45)))
    t.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=(0, 0, 0))
    # 撇 tail: sharp diagonal down-left from corner to (-45, +8), tapered.
    tapered_bezier(t, T((15, 45)), T((-15, 30)), T((-45, 8)),
                   9 * scale, 2 * scale, n=32)

    # -----------------------------------------------------------------
    # S2: 竖弯钩 with diagonal start
    # -----------------------------------------------------------------
    # Head: starts higher-right around (+20, +20), plunges down-left to
    # about (-45, -30), then curves along the bottom rightward to
    # (+55, -75), then hooks up on the right side to (+55, -35).
    # Use two bezier segments + straight hook.

    # Shaft: diagonal descent, thin taper (bezier for slight bow).
    tapered_bezier(t, T((20, 25)), T((-15, 0)), T((-45, -30)),
                   9 * scale, 10 * scale, n=40)
    # Bottom sweep: from (-45, -30) curving through (0, -70) to (+55, -75).
    tapered_bezier(t, T((-45, -30)), T((-5, -78)), T((55, -75)),
                   10 * scale, 9 * scale, n=48)
    # Hook up: from (+55, -75) rising up-and-slightly-left to (+52, -38).
    tapered_line(t, T((55, -75)), T((52, -38)), 9 * scale, 2 * scale, n=18)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_ye_mie(t, ox=0.0, oy=10.0, scale=1.0)
    out_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "01_乜.png",
    )
    img.save(out_path)
    print("wrote", out_path)


if __name__ == "__main__":
    main()
