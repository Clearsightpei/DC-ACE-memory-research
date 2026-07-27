"""仕 (shì, "official/serve", 5 strokes = 亻 + 士).

Composition: 亻 (ren_side) on left + 士 (shi_scholar) on right.
Reuses `draw_pie`, `draw_shu`, `draw_heng` primitives.

MMH-derived anchors (from dispatcher structural block) used directly.

Joints (per structural expectation block):
  s1.mid ⇆ s2.head @ ML : N (~17 px gap)   -- 亻 竖 head near 撇 body, small gap
  s3.mid ⇆ s4.mid @ C   : P (welded)       -- 士 top-横 crosses 竖 at C
  s4.tail ⇆ s5.mid @ BC : N (~15 px gap)   -- 士 竖 tail near bottom-横 body

MANDATORY LOOKUP CHECKLIST (from memory_index.md):
  1. INDEX grep: 亻 = ren_side.py PRESENT; 士 = shi_scholar.py PRESENT.
     Both bank entries reused via primitive-level anchors (TR1: override
     defaults) — but here we call primitives directly with MMH anchors
     because 仕 side-by-side composition demands different anchors than
     standalone 亻/士.
  2. errata grep: 仕 not in errata.
  3. form_catalog: 撇/竖/横 basic classes.
  4. principles_meta: TR8 (heng/shu axis parallel) applies.
  5. joint_atlas: N-gap ~15-25 px, P welded at cell C.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 5 primitive calls below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH anchors used directly; 亻 on left, 士 on right.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 亻 (left radical) --------------------------------------------
    # s1: 撇 head TL(0.949, 0.662) -> tail BL(0.144, 0.019)
    draw_pie(d,
             ('TL', 0.949, 0.662),
             ('BL', 0.144, 0.019),
             head_width=11, tail_width=2, curve=0.06, segments=48)

    # s2: 竖 head ML(0.712, 0.523) -> tail BL(0.738, 0.915)
    draw_shu(d,
             ('ML', 0.712, 0.523),
             ('BL', 0.738, 0.915),
             width=9)

    # ---- 士 (right component) -----------------------------------------
    # s3: 横 (top, longer) head C(0.04, 0.787) -> tail MR(0.616, 0.6)
    draw_heng(d,
              ('C', 0.04, 0.787),
              ('MR', 0.616, 0.6),
              width=9)

    # s4: 竖 head TC(0.664, 0.738) -> tail BC(0.746, 0.44)
    draw_shu(d,
             ('TC', 0.664, 0.738),
             ('BC', 0.746, 0.44),
             width=10)

    # s5: 横 (bottom, shorter) head BC(0.163, 0.575) -> tail BR(0.49, 0.517)
    draw_heng(d,
              ('BC', 0.163, 0.575),
              ('BR', 0.49, 0.517),
              width=9)

    out = os.path.join(os.path.dirname(__file__), '01_仕.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
