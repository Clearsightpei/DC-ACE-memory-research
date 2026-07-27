"""勻 (yún) — Phase-3 char, 4 strokes.

Memory lookup:
1. success_bank INDEX grep: p3_char_0037_勹 → bao_char.py (thin wrapper
   around bao.py). 勻 = 勹 + two inner 横 marks (like 二 inside).
2. errata: no entry for 勻.
3. form_catalog: heng inside enclosing radical — use short spans.
4. principles_meta TR1: reuse bao_char (匀 hull); TR6: inline the two
   inner heng strokes.
5. joint_atlas: 勹 has N-class joint at ML (mastered in bao.py).

Structure:
  s1 撇 (from bao.py)
  s2 横折钩 (from bao.py)
  s3 short 横 (upper inner)
  s4 short 横 (lower inner)

MMH-expected 4 strokes: bao contributes 2, inner 二 contributes 2. Match.
"""
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 primitive calls (pie + heng_zhe_gou + 2 heng)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'bao_char (2 strokes) + 2 inner 横 = 4 total. N-joint at ML preserved from bao.py.'
}

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from bao_char import draw_bao_char  # noqa: E402
from heng import draw_heng  # noqa: E402


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # Strokes 1 + 2: 勹 hull via mastered bao_char (撇 + 横折钩, N joint at ML)
    draw_bao_char(draw)

    # Stroke 3: upper inner 横 (short horizontal, inside hull upper area)
    # Sits horizontally around y ≈ 155 px, x ≈ 130-180 (well inside hull).
    draw_heng(draw, ('C', 0.30, 0.55), ('C', 0.60, 0.55), width=6)

    # Stroke 4: lower inner 横 (short horizontal, inside hull lower area)
    # Sits horizontally around y ≈ 210 px, x ≈ 130-190 (well inside hull).
    draw_heng(draw, ('C', 0.30, 0.10), ('C', 0.65, 0.10), width=6)

    out = os.path.join(_HERE, '01_勻.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
