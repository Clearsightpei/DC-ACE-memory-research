# p2_radical_040_屮 (che) — G3 coord-bank attempt.
#
# Decomposition (3 strokes, MMH order):
#   1. 竖 — long central vertical shaft.
#   2. 竖折 — left arm: short vertical descending on left side, then
#      right-angle turn to a short horizontal that welds into the
#      central shaft's bottom-ish middle.
#   3. 竖 — right short vertical (slightly leaning), sitting to the
#      right of the shaft; head high, tail lower.
#
# Bank plan (per TR1/TR6):
#   - Central shaft: reuse `draw_shu` (canonical 200-px vertical) with
#     a slight downward bias so more length shows below the arms.
#     Standalone shu is 200 tall centered at origin. Target center
#     (math coords): (0, -10). scale = 0.95. ox=0, oy=-10.
#   - Left 竖折: reuse `draw_shu_zhe`. Standalone primitive:
#       v_top=(-30,90), v_bottom=(-30,-70), h_right=(70,-70).
#     I want the vertical part on left of shaft (top ≈ (-42, +10)),
#     bottom-corner ≈ (-42, -35), horizontal going right to weld with
#     shaft at ≈ (0, -35). At scale=0.4:
#       primitive v_top = (0 + -30*0.4, 0 + 90*0.4) = (-12, 36) canvas-coord
#       primitive v_bot = (-12, -28)
#       primitive h_right= (28, -28)
#     I want v_top at (-42, +10); ox = -42 - (-12) = -30; oy = 10 - 36 = -26.
#     Then v_bot -> (-42, -54); h_right -> (16, -54). That gets welded
#     close-enough to the shaft's midline.
#     Actually to hit v_bot at math y=-35 (not -54) I use oy = 10 - 36 = -26
#     but that puts corner at -54. Recompute with scale=0.3:
#       primitive v_top = (-9, 27), v_bot=(-9,-21), h_right=(21,-21).
#       Want v_top at (-42, +10): ox=-42-(-9)=-33, oy=10-27=-17.
#       Then v_bot -> (-42, -38), h_right -> (-12, -38). But shaft is
#       at x=0 not -12. Need horizontal to reach shaft x=0.
#     Rather than fighting the primitive's fixed 100/70 aspect, INLINE
#     the 竖折 fresh (per TR5) so the horizontal actually reaches x=0.
#   - Right short vertical: reuse `draw_shu` at scale=0.32, ox=+40, oy=-10.
#     That gives a shaft of ~64 px length centered at (+40, -10),
#     spanning y=+22 to y=-42.
#
# Coord convention: math coords, +y up, origin at canvas center.

import os
import sys
from PIL import Image, ImageDraw

# Make bank primitives importable.
BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from shu import draw_shu, _to_pixel  # noqa: E402


CANVAS = 300


def draw_shu_zhe_inline(t, top_x=-42, top_y=10, corner_y=-40, right_x=0, ink=12):
    """Inline 竖折 tuned for 屮's left arm.

    top_x, top_y      — head of the vertical part (math coords).
    corner_y          — y of the elbow (same x as top).
    right_x           — where the horizontal ends (welds into shaft).
    """
    # Vertical segment.
    v_top = _to_pixel(top_x, top_y)
    v_bot = _to_pixel(top_x, corner_y)
    t.line([v_top, v_bot], fill=(0, 0, 0), width=ink)
    # Small corner blob (顿笔 per P6).
    r = ink // 2 + 1
    cx, cy = v_bot
    t.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))
    # Horizontal segment.
    h_left = v_bot
    h_right = _to_pixel(right_x, corner_y)
    t.line([h_left, h_right], fill=(0, 0, 0), width=ink)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # Stroke 1: central long 竖 (per TR1 — deliberate placement).
    # Standalone shu spans y=+100..-100 (200 px) at scale=1 centered at origin.
    # I want the shaft to span roughly math y=+80..-105, centered at (0, -12).
    # scale = (80 - (-105)) / 200 = 0.925 ≈ 0.93. ox=0, oy=-12.
    draw_shu(t, ox=0, oy=-12, scale=0.93)

    # Stroke 2: left 竖折 (inlined per TR5 — bank primitive's aspect
    # forces horizontal length = vertical length * 100/70 which doesn't
    # fit the required weld to shaft at x=0).
    # GT: left arm head sits around upper-mid area, horizontal near
    # middle-lower of shaft. Head (-45, +30), elbow (-45, -35), horizontal
    # welds at shaft x=0 y=-35.
    draw_shu_zhe_inline(t, top_x=-45, top_y=+30, corner_y=-35, right_x=0, ink=11)

    # Stroke 3: right short 竖 — GT has this reaching high, roughly
    # symmetric-ish with the left arm's vertical portion.
    # Length ~65 px, head at (+42, +30), tail at (+42, -35). Center (+42, -3),
    # scale = 65/200 = 0.325.
    draw_shu(t, ox=+42, oy=-3, scale=0.325)

    out = os.path.join(os.path.dirname(__file__), "01_屮.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
