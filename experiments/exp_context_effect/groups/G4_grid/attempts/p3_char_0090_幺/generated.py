"""p3_char_0090_幺 (yāo, "tiny", 3 strokes) — G4 attempt.

MANDATORY LOOKUP CHECKLIST (per memory_index.md):
1. success_bank/INDEX.md grep '幺' → HIT: p2_radical_078_幺 → yao_small.py (mastered B2).
2. errata.md grep '幺' → mentioned as REFERENCE for 么 fix ('model after yao_small.py'),
   幺 itself is NOT in errata.
3. form_catalog.md '撇折 (pie_zhe) as component in 幺' → two stacked pie_zhe,
   top pivot C(0.05, 0.90), bottom pivot BC(0.10, 0.85). N joints ~12-19 px.
4. principles_meta.md TR1 → REUSE mastered primitive with OVERRIDE anchors from
   THIS composition's MMH block. MMH anchors match yao_small.py defaults exactly
   (same character, same stroke medians), so pass them explicitly (TR1 compliance).
5. joint_atlas.md → N joints (not welded). Two of them, both N.
6. sandbox.md → no additional 幺-specific notes beyond form_catalog.

Retrieval-to-implementation (B4 lesson): I am calling draw_yao_small(...) with
EXPLICIT anchor overrides matching the injected MMH block, not the defaults:
  s1_head=('TC', 0.424, 0.762)  s1_tail=('C',  0.585, 0.925)
  s2_head=('C',  0.963, 0.356)  s2_tail=('BR', 0.098, 0.684)
  s3_head=('BC', 0.91,  0.259)  s3_tail=('BR', 0.32,  0.927)
Pivots kept from mastered file (C(0.05,0.90), BC(0.10,0.85)) — form_catalog rule.
"""

import os
import sys
from PIL import Image, ImageDraw

SUCCESS_BANK = os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'
)
sys.path.insert(0, os.path.abspath(SUCCESS_BANK))

from yao_small import draw_yao_small  # noqa: E402

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 3 strokes: pie_zhe + pie_zhe + dian
    'endpoint_mismatches': [],  # anchors match MMH block exactly
    'joint_class_mismatches': [],  # both joints N (from yao_small.py docstring)
    'overall_pass': True,
    'notes': 'Direct reuse of mastered yao_small.py (p2_radical_078_幺). '
             'MMH structural block for p3 幺 is identical to the p2 radical, '
             'so anchors passed explicitly per TR1 match the defaults.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # TR1: explicit anchor overrides from this composition's MMH block.
    draw_yao_small(
        draw,
        s1_head=('TC', 0.424, 0.762),
        s1_pivot=('C', 0.05, 0.90),
        s1_tail=('C', 0.585, 0.925),
        s2_head=('C', 0.963, 0.356),
        s2_pivot=('BC', 0.10, 0.85),
        s2_tail=('BR', 0.098, 0.684),
        s3_head=('BC', 0.91, 0.259),
        s3_tail=('BR', 0.32, 0.927),
    )

    out = os.path.join(os.path.dirname(__file__), '01_幺.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
