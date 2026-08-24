"""佾 (yì) — retry_1. 8 strokes.

TRAJECTORY DIFF (from PNG comparison, main→retry_1):
  Main (C verdict) visual gaps vs GT:
    1. 亻 撇 too HEAVY (head_width=11) and too CURVED (curve=0.10); GT
       shows a lighter, gently-curved sweep. → lighten head_width to 8,
       curve to 0.06.
    2. 月 (BC/BR slot) inner hengs barely visible; errata literally says
       "inner heng at y=0.72 and y=0.82". MMH puts s7 at y≈202 (=0.67)
       and s8 at y≈234 (=0.78) — close but too high. Pull s7 down to
       y_frac 0.20 in BC (y=220 = 0.73) and s8 to y_frac 0.50 in BC
       (y=250 = 0.83) per errata guidance.
    3. 月 outline felt cramped — s6 corner sat at C(0.96,0.545) but
       tail at BC(0.720,0.856) made a slanted right edge. Push corner
       toward MR-boundary for a cleaner vertical drop; anchor MMH-close.
    4. 八 (top-right) 撇 head_width=10 too heavy — reduce to 7 for
       calligraphic thinness.

  Fixes applied:
    - Lighter, tapered 亻 撇 (head_width 8, curve 0.06)
    - Inner hengs of 月 repositioned per errata (y_frac 0.20 & 0.50 in BC)
    - Lighter 八 strokes for balance
    - Preserve MMH stroke count = 8 and anchor cells (within ±0.20)
"""

# BANK_DEVIATION
# skipped: ren_side.py, ba.py, yue.py
# reason: 亻/八/月 are placed in compressed compositional slots per MMH
#   (far-left col, top-right band, BC/BR bottom slot) that don't match
#   the standalone-sized bank primitives — inline with base primitives
#   preserves slot proportion and lets us tune inner-heng y per errata.
# fresh_component: ren_side_far_left_for_佾,
#                  ba_top_right_band_for_佾,
#                  yue_bc_compression_with_errata_hengs_for_佾

import sys, os
from PIL import Image, ImageDraw

BANK = "<REPO_ROOT>/experiments/exp_context_effect/groups/G4_grid/success_bank/code"
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, fat_line
from pie import draw_pie
from shu import draw_shu
from na import draw_na
from heng import draw_heng
from heng_zhe_gou import draw_heng_zhe_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 8 strokes (亻:2 + 八:2 + 月:4)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 7 joints N — natural gaps preserved
    'overall_pass': True,
    'notes': 'retry_1: lightened 亻 撇 and 八 strokes; repositioned 月 '
             'inner hengs per errata (y_frac 0.20 & 0.50 in BC).',
}


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---- 亻 (left radical, 2 strokes) ----
    # s1: 撇 — MMH head TL(0.87,0.66) tail ML(0.17,0.95)
    #      Lighter (8) with mild curve (0.06) — GT sweep is gentle.
    draw_pie(d, ('TL', 0.873, 0.659), ('ML', 0.173, 0.948),
             head_width=8, tail_width=1, curve=0.06, segments=48)
    # s2: 竖 — MMH head ML(0.63,0.57) tail BL(0.67,0.92); N-joint w/ s1 mid
    draw_shu(d, ('ML', 0.627, 0.570), ('BL', 0.668, 0.915), width=8)

    # ---- 八 (top-right, 2 strokes) ----
    # s3: 左撇 — MMH head TC(0.36,0.88) tail ML(0.94,0.62)
    draw_pie(d, ('TC', 0.362, 0.876), ('ML', 0.938, 0.620),
             head_width=7, tail_width=2, curve=0.10, segments=48)
    # s4: 右捺 — MMH head TC(0.75,0.67) tail MR(0.85,0.45)
    draw_na(d, ('TC', 0.749, 0.668), ('MR', 0.848, 0.450),
            head_width=2, peak_width=8, tail_width=4)

    # ---- 月 (bottom-right slot, 4 strokes: 撇 + 横折钩 + 2 inner 横) ----
    # s5: 左撇 — MMH head C(0.30,0.54) tail BC(0.24,0.92)
    draw_pie(d, ('C', 0.298, 0.535), ('BC', 0.239, 0.918),
             head_width=8, tail_width=3, curve=0.04, segments=40)
    # s6: 横折钩 — head C(0.48,0.58), corner near MR/C border, tail BC-right
    #      Cleaner vertical drop; keep hook flick.
    draw_heng_zhe_gou(d,
                      head=('C',  0.477, 0.579),
                      corner=('MR', 0.00, 0.58),   # ~ (200, 158), just past C→MR seam
                      tail=('BC', 0.72, 0.86),
                      tip=('BC', 0.56, 0.80),
                      h_width=7, v_width=7, shoulder=9, tip_w=2)
    # s7: 上 inner 横 — errata: y ≈ 0.72 canvas. Use BC anchor y_frac 0.20 → y=220.
    #      x span roughly from inner-left (~135) to inner-right (~185).
    draw_heng(d, ('BC', 0.35, 0.20), ('BC', 0.85, 0.20), width=5)
    # s8: 下 inner 横 — errata: y ≈ 0.82 canvas. Use BC anchor y_frac 0.50 → y=250.
    draw_heng(d, ('BC', 0.35, 0.50), ('BC', 0.85, 0.50), width=5)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '01_佾.png')
    img.save(out)
    print(f"Saved {out}")


if __name__ == '__main__':
    main()
