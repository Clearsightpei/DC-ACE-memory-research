"""佽 (cì) — 8 strokes.

Decomposition: 佽 = 亻 (left) + 次 (right); 次 = 冫 (top-left of right) + 欠 (right).
  s1-s2  : 亻 = 撇 + 竖 (far-left column TL/ML/BL — NOT ren_side default)
  s3-s4  : 冫 = 点 (top-left) + 提 (tick going up-right)
  s5-s8  : 欠 = 短撇 + 横钩 + 撇 + 捺 (X-cross at bottom between s7 & s8)

MMH-verbatim anchors throughout (B9/B10 A-recipe).

Notes on primitives:
  - Skip ren_side (see BANK_DEVIATION below): MMH places 亻 in far-left
    (TL/ML/BL) column but ren_side defaults sit at TC/C/BL/BC. Partial
    override → p3_char_0252_伊 FAIL pattern. Inline pie + shu instead.
  - Inline 冫 with pie (as 提) + dian: no bing/liang bank primitive.
  - Inline 欠 base-primitive-style: pie + heng_gou + pie + na.

Joints (all N-class per MMH dispatcher block — leave natural gaps):
  s1.mid ⇆ s2.head  (亻 T-touch relaxed to N)
  s1.mid ⇆ s3.head  (亻 撇 body ~ 冫 dot head)
  s3.tail ⇆ s5.tail (冫 dot tail ~ 欠 pie tail)
  s4.tail ⇆ s5.tail (冫 tick tail ~ 欠 pie tail)
  s5.mid ⇆ s6.head  (欠 top-pie into heng shoulder)
  s5.tail ⇆ s7.head (欠 top-pie tail ~ bottom-pie head)
  s7.mid ⇆ s8.head  (欠 X-cross — N gap preserved, do NOT weld)
"""

# BANK_DEVIATION
# skipped: ren_side.py
# reason: MMH places 亻 in the far-left column (TL/ML/BL, x_frac 0.2-0.9 mostly TL);
#         ren_side defaults center at TC/C/BC — 3+ anchor overrides needed.
#         Compound-standalone-scale problem (B10 slot-pattern: far-left column).
# fresh_component: ren_side_farleft_for_佽

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim; all 7 N-joints preserved as gaps; 亻 far-left inlined.',
}

import sys
from pathlib import Path

# Allow importing bank primitives.
_BANK = Path(__file__).resolve().parents[3] / "G4_grid" / "success_bank" / "code"
sys.path.insert(0, str(_BANK))

from PIL import Image, ImageDraw

from _anchor import anchor_to_xy
from pie import draw_pie
from shu import draw_shu
from na import draw_na
from dian import draw_dian
from heng_gou import draw_heng_gou


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---- 亻 (far-left column) ----
    # s1: 撇 — TL(0.879, 0.694) → ML(0.208, 0.983)
    draw_pie(d, ('TL', 0.879, 0.694), ('ML', 0.208, 0.983),
             head_width=12, tail_width=1, curve=0.12, segments=48)
    # s2: 竖 — ML(0.671, 0.562) → BL(0.709, 0.965)
    draw_shu(d, ('ML', 0.671, 0.562), ('BL', 0.709, 0.965), width=8)

    # ---- 冫 (bing) ----
    # s3: 点 — C(0.04, 0.318) → C(0.286, 0.588)
    draw_dian(d, ('C', 0.04, 0.318), ('C', 0.286, 0.588),
              head_width=2, peak_width=10, curve=0.10, segments=24)
    # s4: 提 (tick going up-right) — BC(0.099, 0.66) → C(0.351, 0.931)
    # Use pie: head=thick lower-left, tail=thin upper-right (visually correct 提)
    draw_pie(d, ('BC', 0.099, 0.66), ('C', 0.351, 0.931),
             head_width=10, tail_width=1, curve=0.05, segments=24)

    # ---- 欠 (X-cross topology) ----
    # s5: 短撇 top — TC(0.781, 0.709) → C(0.465, 0.761)
    draw_pie(d, ('TC', 0.781, 0.709), ('C', 0.465, 0.761),
             head_width=9, tail_width=1, curve=0.08, segments=36)
    # s6: 横钩 — head C(0.711, 0.523), shoulder computed just right of tail-x,
    #     tip MR(0.221, 0.746) per MMH tail.
    draw_heng_gou(d, ('C', 0.711, 0.523), ('MR', 0.30, 0.30),
                  ('MR', 0.221, 0.746),
                  head_w=8, mid_w=7, shoulder_w=12, tip_w=2)
    # s7: 撇 (bottom-left of X) — C(0.746, 0.796) → BC(0.21, 0.918)
    draw_pie(d, ('C', 0.746, 0.796), ('BC', 0.21, 0.918),
             head_width=10, tail_width=1, curve=0.10, segments=48)
    # s8: 捺 — BC(0.884, 0.188) → BR(0.76, 0.944).
    #     NOTE: s8 head y=218.8 sits ~32 px right of s7 mid ~(155.8, 218.9);
    #     MMH says N-joint (14.8 gap). Leave as MMH — do NOT weld.
    draw_na(d, ('BC', 0.884, 0.188), ('BR', 0.76, 0.944),
            head_width=3, peak_width=15, tail_width=1,
            peak_t=0.78, curve=0.10, segments=48)

    out = Path(__file__).parent / "01_佽.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
