"""p3_char_0093_弋 — G4 attempt.

Mandatory lookup checklist:
1. success_bank/INDEX.md grep → HIT: `yi_arrow.py` (item 111,
   p2_radical_079_弋, mastered). Same character, same MMH stroke
   count (3), and its default anchors already match the brief's
   MMH-derived anchors exactly. Direct reuse per TR1 (override with
   the brief anchors — which happen to equal the defaults here).
2. errata.md grep for 弋 → no active errata entry for this item.
3. form_catalog.md → 斜钩 + 短横 + 点 combo already captured by
   yi_arrow.py; no extra context adjustment needed.
4. principles_meta.md TR9 (standalone span) → yi_arrow already spans
   ML→BR / TC→BR — fills the grid; no expansion needed.
5. joint_atlas.md → single P-weld at C matches expected class in
   brief (P — welded, dist 0.0). yi_arrow paints a 顿笔 disc there.
6. sandbox.md → no additional notes required.
"""
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Reused draw_yi_arrow with anchors matching brief exactly. '
             'stroke1 head=(ML,0.48,0.764) tail=(MR,0.095,0.38); '
             'stroke2 head=(TC,0.02,0.806) tail=(BR,0.581,0.347) via belly at C(0.42,0.531); '
             'stroke3 head=(TC,0.822,0.694) tail=(TR,0.183,0.97). '
             'Joint s1.mid⇆s2.mid @ C class=P (welded disc r=6 painted at cross).'
}

import os, sys
from PIL import Image, ImageDraw

# Make success_bank/code importable so we can reuse the mastered primitive.
CODE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                         '..', '..', 'success_bank', 'code'))
sys.path.insert(0, CODE_DIR)

from yi_arrow import draw_yi_arrow  # noqa: E402


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # Anchors from the MMH-derived brief (identical to yi_arrow defaults).
    draw_yi_arrow(
        draw,
        s1_head=('ML', 0.48, 0.764), s1_tail=('MR', 0.095, 0.38),
        s2_head=('TC', 0.02, 0.806),
        s2_belly=('C', 0.418, 0.531),
        s2_hook_pt=('BR', 0.581, 0.347),
        s2_tip=('BR', 0.62, 0.15),
        s3_head=('TC', 0.822, 0.694), s3_tail=('TR', 0.183, 0.97),
    )

    out = os.path.join(os.path.dirname(__file__), '01_弋.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
