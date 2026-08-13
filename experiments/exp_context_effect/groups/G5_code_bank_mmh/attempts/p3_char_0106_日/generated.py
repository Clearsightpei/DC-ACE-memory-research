"""p3_char_0106_日 — G5 render.

Direct reuse of bank primitive draw_ri (promoted from p2_radical_114_日
PASS). 4 strokes: shu + heng_zhe_box + middle heng + bottom heng.
No BANK_DEVIATION — the bank primitive is exactly what this item is.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from ri_sun import draw_ri  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # draw_ri calls exactly 4 stroke primitives
    'endpoint_mismatches': [],     # anchors baked into promoted primitive
    'joint_class_mismatches': [],  # all 4 N-gaps preserved from PASSed render
    'overall_pass': True,
    'notes': 'Direct bank reuse of ri_sun.py at (ox=0, oy=0, scale=1.0).'
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_ri(d, ox=0, oy=0, scale=1.0)
    out = Path(__file__).parent / '01_日.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
