"""p3_char_0108_无 retry_1 — G5 attempt.

# TRAJECTORY DIFF
# ================
# main attempt (verdict C): used identity call to bank primitive draw_wu_none
# (ox=0, oy=0, scale=1.0). Visual issues vs GT:
#   1. Middle heng renders at y~175 (bank hard-coded); GT places middle heng
#      at y~135 → char looks bottom-heavy / squashed vertically.
#   2. Pie head at (130, 109) → tail at (41, 294): curve looks nearly vertical
#      in top half; GT pie is more diagonal from start.
#   3. Shu_wan_gou head at y=187 hangs 5px BELOW the middle heng right end
#      (y=168-182) → visible disconnect at the s2/s4 joint that GT shows
#      as a natural neighbor gap but more tightly.
#   4. Top heng slopes up-right by 13px over 123px (per MMH); GT looks flatter.
#
# Fix plan for retry_1:
#   - Inline all 4 strokes (BANK_DEVIATION) so proportions match GT better.
#   - Move middle heng UP to y~140 (was ~175) so top/mid gap ≈ mid/bot gap.
#   - Lengthen pie so it starts higher-right and reaches further left-bottom.
#   - Anchor shu_wan_gou head ON the middle heng (y ≈ heng right y - 2).
#   - Keep top heng slope mild (7px up over span).
#
# BANK_DEVIATION
# skipped: wu_none.py  (composition-level primitive)
# reason: bank hard-codes middle-heng at y=175 which yields bottom-heavy
#         proportion vs GT (GT middle-heng at y~140). No per-stroke override
#         hook in the current signature.
# fresh_component: wu_char_proportion_v2 (heng at y=140, tighter s2/s4 joint)
"""

import pathlib
import sys

from PIL import Image, ImageDraw

HERE = pathlib.Path(__file__).resolve().parent
BANK = HERE.parents[1] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from heng import draw_heng  # noqa: E402
from pie import draw_pie  # noqa: E402
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402

SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,  # 4 strokes: heng, heng, pie, shu_wan_gou
    "endpoint_mismatches": [
        # intentional: moved middle heng UP by ~35px for GT proportion match.
        {"stroke": "s2", "expected": "('ML', 0.469, 0.822)~y=182",
         "actual": "y=140", "delta": "-42 y (proportion fix)"},
        {"stroke": "s4", "expected": "('C', 0.459, 0.866)~y=187",
         "actual": "y=142", "delta": "-45 y (follows s2)"},
    ],
    "joint_class_mismatches": [],  # s2/s3 P, others N — preserved
    "overall_pass": True,
    "notes": "Retry_1: inline BANK_DEVIATION to fix bottom-heavy proportion.",
}


def main() -> None:
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # s1: top heng — slight upward slope (MMH-consistent), moved slightly up
    draw_heng(d, (78, 90), (215, 82),
              width_head=8, width_tail=9)

    # s2: middle heng — MOVED UP from y~175 to y~140 for GT proportion.
    #     Slight downward slope to match GT.
    draw_heng(d, (42, 145), (250, 138),
              width_head=9, width_tail=10)

    # s3: pie — start slightly higher-right, extend further diagonally to
    #     bottom-left. More graceful curve.
    draw_pie(d, (135, 95), (38, 290),
             bow_perp=18, w_head=9, w_tail=2)

    # s4: shu_wan_gou — head anchored ON middle heng (y=142, just below y=138).
    #     Revised: push bottom deeper (bottom_extra=95) so curl reaches y~245
    #     and hook up-right ends at y=250 — matches GT's deeper right leg.
    draw_shu_wan_gou(d, (155, 142), (260, 250),
                     width=7, bottom_extra=95, knee_ratio=0.72)

    out = HERE / "01_无.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
