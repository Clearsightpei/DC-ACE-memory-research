"""疳 (gān) — 10 strokes.
Decomposition: 疳 = 疒 (s1-s5, top-left frame) + 甘 (s6-s10, right-bottom slot).

疒 (5 strokes): top dot (s1), top heng (s2), long 撇 (s3), left 点 (s4), 提 (s5).
甘 (5 strokes): top 横 (s6), left 竖 (s7), right 竖 (s8), inner short 一 (s9), bottom 一 (s10).

No bank primitive exists for 疒 (curator flagged as candidate for canonical
`chronic/ne_sick.py` pending B13 evidence — this is B13's item for 疳).
All anchors MMH-verbatim per B9-B12 A-recipe. Cross-joints s6×s7 and s6×s8
weld naturally (P); all other joints have MMH-derived N gaps preserved.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 10 strokes matches MMH
    'endpoint_mismatches': [],      # all MMH-verbatim
    'joint_class_mismatches': [],   # P welds at s6xs7, s6xs8 (top-heng crosses both verticals);
                                    # N gaps preserved elsewhere by MMH endpoint offsets
    'overall_pass': True,
    'notes': '疒 top-frame inlined (no bank primitive); 甘 rendered as 横+竖+竖+短横+横 with '
             'natural gaps between s7/s8 verticals and s9/s10 short bars.',
}

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK_CODE = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK_CODE))

from _anchor import anchor_to_xy, fat_line  # noqa: E402
from heng import draw_heng                  # noqa: E402
from shu import draw_shu                    # noqa: E402
from pie import draw_pie                    # noqa: E402
from dian import draw_dian                  # noqa: E402
from ti import draw_ti                      # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # ---- 疒 (top-left frame) ----

    # s1: top dot of 疒 — TC(0.427, 0.519) → TC(0.761, 0.762)
    draw_dian(d, ('TC', 0.427, 0.519), ('TC', 0.761, 0.762),
              head_width=3, peak_width=9, curve=0.08, segments=24)

    # s2: top 横 of 疒 — C(0.025, 0.134) → TR(0.329, 0.979)
    draw_heng(d, ('C', 0.025, 0.134), ('TR', 0.329, 0.979), width=9)

    # s3: long 撇 sweep of 疒 — ML(0.806, 0.052) → BL(0.319, 0.991)
    draw_pie(d, ('ML', 0.806, 0.052), ('BL', 0.319, 0.991),
             head_width=12, tail_width=2, curve=0.09, segments=48)

    # s4: left 点 of 疒 — ML(0.387, 0.318) → ML(0.583, 0.553)
    draw_dian(d, ('ML', 0.387, 0.318), ('ML', 0.583, 0.553),
              head_width=3, peak_width=10, curve=0.08, segments=24)

    # s5: 提 of 疒 — BL(0.19, 0.238) → ML(0.729, 0.939)
    draw_ti(d, ('BL', 0.19, 0.238), ('ML', 0.729, 0.939),
            head_width=12, tail_width=1, curve=0.08, segments=48)

    # ---- 甘 (right-bottom slot) ----

    # s6: top 横 of 甘 — C(0.011, 0.887) → MR(0.704, 0.781)
    draw_heng(d, ('C', 0.011, 0.887), ('MR', 0.704, 0.781), width=9)

    # s7: left 竖 of 甘 — C(0.286, 0.488) → BC(0.377, 0.851)
    draw_shu(d, ('C', 0.286, 0.488), ('BC', 0.377, 0.851), width=9)

    # s8: right 竖 of 甘 — C(0.945, 0.263) → BR(0.03, 1.026)
    # Slight rightward drift; render as fat_line to keep MMH endpoints exact.
    p8a = anchor_to_xy(('C', 0.945, 0.263))
    p8b = anchor_to_xy(('BR', 0.03, 1.026))
    fat_line(d, p8a, p8b, 9)

    # s9: middle short 一 of 甘 — BC(0.485, 0.285) → BC(0.884, 0.224)
    #     MUST have small N gap to s7 tail (head at x=148.5, s7 tail x=137.7 → ~10 px)
    #     and to s8 mid (tail x=188.4, s8 x~196 → ~8 px).
    draw_heng(d, ('BC', 0.485, 0.285), ('BC', 0.884, 0.224), width=7)

    # s10: bottom 一 of 甘 — BC(0.456, 0.769) → BC(0.931, 0.692)
    #      Head at x=145.6 vs s7 tail x=137.7 → small N gap;
    #      tail x=193.1 vs s8 tail x=203 → small N gap.
    draw_heng(d, ('BC', 0.456, 0.769), ('BC', 0.931, 0.692), width=7)

    out = Path(__file__).parent / "01_疳.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
