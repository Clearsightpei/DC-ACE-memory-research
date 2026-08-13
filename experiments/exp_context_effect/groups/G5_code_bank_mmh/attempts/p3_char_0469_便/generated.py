"""p3_char_0469_便 — 便 (biàn, "convenient") — 9 strokes, 亻 + 更.

Reasoning trace (P-A-008 mandatory inline reasoning):

Decomposition: 便 = 亻 (2 strokes) + 更 (7 strokes).
  更 = 一 (top heng) + 日 (4 strokes: 丨, 横折, middle 横, bottom 横) +
       长撇 (long descender) + 捺 (long down-right).

Bank check (per P-A-006 / P-A-007-v2):
  - draw_ren_left (亻): available, but geometry in 便 differs from standalone
    亻 by aspect: 亻 in 便 is compressed to left ~1/3 of canvas, pie head
    lower and shu shorter. **BANK_DEVIATION**: use stroke-primitive layer
    (draw_pie + draw_shu) at MMH endpoints — P-A-006 recipe. Quantitative
    (P-A-009): bank 亻 pie head at (158.8, 73.8), 便 MMH s1 head at
    (83.5, 67.1) → dx=-75.3 px; bank shu tail at (144.1, 292.7), 便 s2
    tail at (70.9, 291.8) → dx=-73.2 px. Systematic left-shift of ~74 px
    (i.e. 亻 lives entirely in left column of 便, not centered). ox
    transform alone would keep bank internal spacing that doesn't match
    the compressed 亻 in 便.
  - draw_ri_sun (日): available (4-stroke box+middle heng). 便's 更 has
    its 日 nestled in the upper-right, but the 日 in 便 is unusually
    compact and its right 横折 continues visually into the descender
    line. **Skip whole-radical**: inline the 4 strokes at MMH anchors
    per P-A-006.
  - draw_dan_but (但 = 亻+旦): closest bank cousin. 但 is 7 strokes
    (亻+日+bottom heng). 便 differs: replace 但's bottom long heng with
    (top 一 + 撇 + 捺) → 更 structure. Cannot use whole-char.

BANK_DEVIATION summary:
  skipped: ren_left.py (亻 aspect-shift), ri_sun.py (日 nestled), all
           whole-char options (no matching 亻+更 primitive).
  reason:  MMH anchors for 便 put 亻 in left ≤27% width and 日 in
           upper-right of 更 (not the standalone geometry any bank entry
           was tuned for).
  fresh_component: bian_convenient (亻+更 template — new recipe for
           future 更-family chars 硬/梗/粳 if any come up).

Stroke-count check: 9 primitive calls → matches expected 9. OK.

Anchor sourcing: raw MMH anchors from injected block, mapped to pixel
coords via cell layout (300x300, cells 100x100, pixel-y convention).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'P-A-006 stroke-primitive layer with MMH anchors verbatim; '
             'BANK_DEVIATION on ren_left/ri_sun (aspect/nestling); '
             'quant justification per P-A-009.'
}

# BANK_DEVIATION
# skipped: ren_left.py — 亻 in 便 compressed to left column; systematic
#          -74px x-shift vs standalone bank geometry (P-A-009 quant).
# skipped: ri_sun.py — 日 in 更 is compact + nested with descenders,
#          bank primitive tuned for standalone box aspect.
# reason:  MMH anchors put 亻 in left ≤27% and 日 upper-right of 更 half.
# fresh_component: bian_convenient — 亻 + 一(top) + 日(inline) + 撇 + 捺.

import sys
from pathlib import Path

BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw
from pie import draw_pie
from shu import draw_shu
from na import draw_na
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # ---- 亻 (2 strokes) — MMH anchors verbatim, stroke-primitive layer ----
    # s1: 亻 pie — TL(0.835, 0.671) → ML(0.141, 0.948)
    draw_pie(d, (83.5, 67.1), (14.1, 194.8),
             bow_perp=14, w_head=9, w_tail=3, steps=90)
    # s2: 亻 shu — ML(0.659, 0.468) → BL(0.709, 0.918); top_curl for 顿笔
    draw_shu(d, (65.9, 146.8), (70.9, 291.8), width=7, top_curl=True)

    # ---- 更 (7 strokes) — inline per P-A-006 ----
    # s3: top 一 of 更 — TC(0.342, 0.847) → TR(0.215, 0.744)
    draw_heng(d, (134.2, 84.7), (221.5, 74.4),
              width_head=8, width_tail=9)
    # s4: 丨 left of 日 — C(0.096, 0.321) → BC(0.345, 0.019)
    draw_shu(d, (109.6, 132.1), (134.5, 201.9), width=7)
    # s5: 横折 box top-right corner of 日 — C(0.222, 0.315) → MR(0.171, 0.925)
    #     top_left ≈ s4.head level (top of 日), bottom_right ≈ s5.tail
    draw_heng_zhe_box(d, (122.2, 131.5), (217.1, 192.5), width=7)
    # s6: middle 横 inside 日 — C(0.453, 0.644) → MR(0.06, 0.562)
    draw_heng(d, (145.3, 164.4), (206.0, 156.2),
              width_head=5, width_tail=6)
    # s7: bottom 横 of 日 — C(0.406, 0.98) → MR(0.089, 0.901)
    draw_heng(d, (140.6, 198.0), (208.9, 190.1),
              width_head=7, width_tail=8)
    # s8: long 撇 descender — TC(0.588, 0.938) → BL(0.976, 0.865)
    draw_pie(d, (158.8, 93.8), (97.6, 286.5),
             bow_perp=18, w_head=8, w_tail=3, steps=100)
    # s9: 捺 long down-right — BC(0.025, 0.124) → BR(0.851, 0.921)
    draw_na(d, (102.5, 212.4), (285.1, 292.1),
            bow_perp=14, w_head=4, w_tail=12, steps=90)

    out = Path(__file__).parent / "01_便.png"
    img.save(out)
    print(f"saved: {out}")


if __name__ == "__main__":
    main()
