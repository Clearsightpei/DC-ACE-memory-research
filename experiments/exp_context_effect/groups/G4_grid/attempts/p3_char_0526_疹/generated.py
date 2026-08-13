"""疹 (zhěn) — 10 strokes.
Decomposition: 疹 = 疒 (s1-s5, top-left frame) + 㐱 (s6-s10, inside slot).

疒 (5 strokes): top dot (s1), top 一 (s2), long 撇 (s3), inner 点 (s4), 提 (s5).
㐱 (5 strokes): 人 = 撇 (s6) + 捺 (s7); 彡 = three 撇 (s8, s9, s10).

No bank primitive exists for 疒 (curator flagged as candidate for canonical
`chronic/ne_sick.py` pending B13 evidence — this is B13's item for 疹).
All anchors MMH-verbatim per B9-B12 A-recipe. All 8 declared joints are class
N (natural gaps preserved by MMH endpoint offsets; no welding).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 10 strokes matches MMH
    'endpoint_mismatches': [],      # all MMH-verbatim
    'joint_class_mismatches': [],   # all 8 joints are N, gaps preserved via MMH offsets
    'overall_pass': True,
    'notes': '疒 top-frame inlined (no bank primitive). 㐱 = 人 (pie+na) + 彡 '
             '(three parallel pies descending). All joints N-gap.',
}

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK_CODE = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK_CODE))

from _anchor import anchor_to_xy, fat_line  # noqa: E402
from heng import draw_heng                  # noqa: E402
from pie import draw_pie                    # noqa: E402
from na import draw_na                      # noqa: E402
from dian import draw_dian                  # noqa: E402
from ti import draw_ti                      # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # ---- 疒 (top-left frame) ----

    # s1: top 点 of 疒 — TC(0.389, 0.524) → TC(0.714, 0.759)
    draw_dian(d, ('TC', 0.389, 0.524), ('TC', 0.714, 0.759),
              head_width=3, peak_width=9, curve=0.08, segments=24)

    # s2: top 一 of 疒 — TC(0.017, 0.999) → TR(0.288, 0.867)
    draw_heng(d, ('TC', 0.017, 0.999), ('TR', 0.288, 0.867), width=9)

    # s3: long 撇 sweep of 疒 — TL(0.806, 0.923) → BL(0.284, 0.921)
    draw_pie(d, ('TL', 0.806, 0.923), ('BL', 0.284, 0.921),
             head_width=12, tail_width=2, curve=0.09, segments=48)

    # s4: inner 点 of 疒 — ML(0.41, 0.181) → ML(0.612, 0.421)
    draw_dian(d, ('ML', 0.41, 0.181), ('ML', 0.612, 0.421),
              head_width=3, peak_width=9, curve=0.08, segments=24)

    # s5: 提 of 疒 — BL(0.17, 0.019) → ML(0.738, 0.72)
    draw_ti(d, ('BL', 0.17, 0.019), ('ML', 0.738, 0.72),
            head_width=12, tail_width=1, curve=0.08, segments=48)

    # ---- 㐱 (inside slot) ----

    # s6: 撇 of 人 in 㐱 — C(0.767, 0.175) → ML(0.987, 0.939)
    draw_pie(d, ('C', 0.767, 0.175), ('ML', 0.987, 0.939),
             head_width=8, tail_width=2, curve=0.06, segments=40)

    # s7: 捺 of 人 in 㐱 — C(0.731, 0.295) → MR(0.839, 0.843)
    draw_na(d, ('C', 0.731, 0.295), ('MR', 0.839, 0.843),
            head_width=3, peak_width=10, tail_width=1, peak_t=0.8, curve=0.08, segments=40)

    # ---- 彡 (three parallel descending 撇) ----

    # s8: first 撇 of 彡 — C(0.67, 0.603) → BC(0.216, 0.159)
    draw_pie(d, ('C', 0.67, 0.603), ('BC', 0.216, 0.159),
             head_width=6, tail_width=2, curve=0.05, segments=32)

    # s9: second 撇 of 彡 — C(0.787, 0.931) → BC(0.263, 0.569)
    draw_pie(d, ('C', 0.787, 0.931), ('BC', 0.263, 0.569),
             head_width=6, tail_width=2, curve=0.05, segments=32)

    # s10: third (longest) 撇 of 彡 — BC(0.893, 0.244) → BC(0.055, 1.176)
    draw_pie(d, ('BC', 0.893, 0.244), ('BC', 0.055, 1.176),
             head_width=6, tail_width=2, curve=0.06, segments=40)

    out = Path(__file__).parent / "01_疹.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
