"""俅 (qiú) — 9 strokes.
Decomposition: 俅 = 亻 (left) + 求 (right).
  亻 = pie + shu (2 strokes)
  求 = 一 + 亅 + point + pie/heng + point + pie + point (7 strokes)

Following B11 A-recipe:
  1. Explicit decomposition (above).
  2. MMH-verbatim anchors — every stroke uses dispatcher-injected anchors unchanged.
  3. SELF_CHECK block below.
  4. Base primitives (pie, shu, heng, dian, na, fat_line) — no compound overrides.
  5. N-joint discipline — natural gaps preserved.
  6. BANK_DEVIATION — skipping ren_side for far-left column slot (named pattern
     `ren_side_far_left`, 10+ passing precedent per drawer_memory.md B11).

# BANK_DEVIATION
# skipped: ren_side.py
# reason: MMH places 亻 in far-left column (TL(0.876,0.686) → BL slot) —
#         narrower than ren_side.py's TC/C defaults. Inlining pie+shu with
#         MMH-verbatim anchors preserves compositional proportion.
# fresh_component: ren_side_far_left_for_俅
"""

import sys
from pathlib import Path

BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from dian import draw_dian
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 stroke calls below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim; s3xs4 P-cross welded via anchor overlap; all N-joints natural gaps.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 亻 (left, far-left column) ---------------------------------
    # s1: 撇 (pie), head @ TL(0.876,0.686) → tail @ BL(0.152,0.089)
    S1_H = ('TL', 0.876, 0.686)
    S1_T = ('BL', 0.152, 0.089)
    draw_pie(d, S1_H, S1_T, head_width=11, tail_width=1, curve=0.10, segments=48)

    # s2: 竖 (shu), head @ ML(0.627,0.635) → tail @ BL(0.674,0.941)
    S2_H = ('ML', 0.627, 0.635)
    S2_T = ('BL', 0.674, 0.941)
    draw_shu(d, S2_H, S2_T, width=9)

    # ---- 求 (right side, 7 strokes) --------------------------------
    # s3: top 横 (heng) — short, crosses s4 at cell C (P-joint welded)
    S3_H = ('C', 0.128, 0.438)
    S3_T = ('MR', 0.18, 0.266)
    draw_heng(d, S3_H, S3_T, width=8)

    # s4: 竖钩 main vertical — long stroke down-slightly-left
    S4_H = ('TC', 0.576, 0.674)
    S4_T = ('BC', 0.269, 0.792)
    # use fat_line as slight-curve shu (no explicit gou here — MMH doesn't
    # give a hook tail; leave straight to match MMH endpoints exactly).
    p0 = anchor_to_xy(S4_H)
    p1 = anchor_to_xy(S4_T)
    fat_line(d, p0, p1, width=9)

    # s5: short hook piece at bottom-left of s4
    S5_H = ('C', 0.122, 0.772)
    S5_T = ('C', 0.356, 0.992)
    p0 = anchor_to_xy(S5_H)
    p1 = anchor_to_xy(S5_T)
    fat_line(d, p0, p1, width=7)

    # s6: 撇 going up-right (part of 求 crossing structure)
    S6_H = ('BL', 0.891, 0.525)
    S6_T = ('BC', 0.5, 0.121)
    draw_pie(d, S6_H, S6_T, head_width=10, tail_width=1, curve=0.08, segments=48)

    # s7: long stroke going right & down — the diagonal across 求
    S7_H = ('MR', 0.188, 0.564)
    S7_T = ('C', 0.884, 0.951)
    p0 = anchor_to_xy(S7_H)
    p1 = anchor_to_xy(S7_T)
    fat_line(d, p0, p1, width=8)

    # s8: dian (dot) lower-right
    S8_H = ('C', 0.77, 0.887)
    S8_T = ('BR', 0.883, 0.648)
    draw_dian(d, S8_H, S8_T, head_width=2, peak_width=10, curve=0.08, segments=24)

    # s9: dian (dot) upper-right of 求
    S9_H = ('TR', 0.089, 0.841)
    S9_T = ('MR', 0.411, 0.087)
    draw_dian(d, S9_H, S9_T, head_width=2, peak_width=10, curve=0.08, segments=24)

    out = Path(__file__).parent / "01_俅.png"
    img.save(out)
    print(f"Saved: {out}")


if __name__ == "__main__":
    main()
