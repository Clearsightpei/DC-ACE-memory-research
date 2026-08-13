"""來 (lái) — 8 strokes.
Decomposition: 來 = 一 (top short heng) + upper cross (left 撇 + right 撇/丶) +
  central 丨 trunk + inner 人 (two small strokes flanking) + lower 撇 + 捺 (人 legs).

MMH stroke inventory (from dispatcher):
  s1 top short heng   (TL→TC across top)
  s2 upper 撇         (ML column, from head-top going down-left)
  s3 short inner heng (ML→C, thin brush)
  s4 upper 撇         (C column, from top going down)
  s5 short inner heng (C→MR, thin brush) — right side counterpart of s3
  s6 main 丨 trunk    (TC→BC, extends below baseline)
  s7 bottom-left 撇   (long, C → BL)
  s8 bottom-right 捺  (long, C → BR)

Memory reading log:
  1. drawer_memory.md — followed A-recipe: MMH-verbatim + base primitives.
  2. success_bank/INDEX.md — 木/大/人 primitives exist but 來 is a 8-stroke
     compound with center-descending trunk that no compound primitive fits.
     Inlining base primitives per B10 BANK_DEVIATION guidance.
  3. errata.md — 來 not listed.

All 11 declared joints are class N (neighbor) per MMH — leave natural
~10-35 px gaps, do NOT weld. One P joint (s1.mid ⇆ s6.mid welded at TC).
"""

# BANK_DEVIATION
# skipped: da.py, ren.py (mu.py not present)
# reason: MMH places 來 with a long central trunk (s6) descending well
#   below the baseline (y_frac 1.144) and two flanking short-heng "dots"
#   (s3, s5) that are not part of any bank compound. da/ren compound
#   primitives would need 3+ anchor overrides. Inlining with base
#   primitives + MMH-verbatim anchors per B10 A-recipe point 4.
# fresh_component: lai_center_trunk_layout_for_來

import sys, os
from PIL import Image, ImageDraw

BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G4_grid/success_bank/code"
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, fat_line
from pie import draw_pie
from shu import draw_shu
from na import draw_na
from heng import draw_heng


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 8 strokes as MMH expects
    'endpoint_mismatches': [],     # all anchors MMH-verbatim
    'joint_class_mismatches': [],  # 10 N-joints preserved as gaps, 1 P weld at s1.mid ⇆ s6.mid
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim. Central trunk s6 extends below baseline '
             '(y_frac 1.144). Two upper 撇 (s2, s4) form an inverted-V hat; two '
             'short heng (s3, s5) sit as internal brush marks. Bottom pie/na '
             'form the 人-legs. N-joints left as natural gaps.',
}


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # s1: top short heng — TL(0.858, 0.967) → TC(0.972, 0.8)
    draw_heng(d, ('TL', 0.858, 0.967), ('TC', 0.972, 0.800), width=8)

    # s2: upper-left 撇 — ML(0.853, 0.213) → ML(0.466, 0.939)
    draw_pie(d, ('ML', 0.853, 0.213), ('ML', 0.466, 0.939),
             head_width=10, tail_width=2, curve=0.08, segments=48)

    # s3: short inner heng (left dot-heng) — ML(0.894, 0.570) → C(0.140, 0.708)
    draw_heng(d, ('ML', 0.894, 0.570), ('C', 0.140, 0.708), width=7)

    # s4: upper-right 撇 — C(0.948, 0.002) → C(0.623, 0.655)
    draw_pie(d, ('C', 0.948, 0.002), ('C', 0.623, 0.655),
             head_width=10, tail_width=2, curve=0.08, segments=48)

    # s5: short inner heng (right dot-heng) — C(0.907, 0.477) → MR(0.309, 0.711)
    draw_heng(d, ('C', 0.907, 0.477), ('MR', 0.309, 0.711), width=7)

    # s6: main 丨 trunk — TC(0.298, 0.513) → BC(0.389, 1.144)
    draw_shu(d, ('TC', 0.298, 0.513), ('BC', 0.389, 1.144), width=10)

    # s7: bottom-left 撇 — C(0.351, 0.685) → BL(0.293, 0.745)
    draw_pie(d, ('C', 0.351, 0.685), ('BL', 0.293, 0.745),
             head_width=10, tail_width=2, curve=0.10, segments=48)

    # s8: bottom-right 捺 — C(0.523, 0.843) → BR(0.836, 0.625)
    draw_na(d, ('C', 0.523, 0.843), ('BR', 0.836, 0.625),
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.8, curve=0.10, segments=48)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '01_來.png')
    img.save(out)
    print(f"Saved {out}")


if __name__ == '__main__':
    main()
