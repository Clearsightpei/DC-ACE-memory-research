"""p3_char_0036_刂 — G5 Drawer attempt.

Identity-reuse of bank primitive `draw_dao_right` (promoted from
p2_radical_016_刂 in bootstrap). The Phase-3 character 刂 is the same
shape as the Phase-2 radical — P-A-001 identity-reuse route.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

HERE = pathlib.Path(__file__).resolve().parent
BANK = HERE.parents[1] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from dao_right import draw_dao_right  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # draw_dao_right emits 2 stroke primitives (short shu + shu_gou)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # MMH block: NONE (strokes do not meet)
    'overall_pass': True,
    'notes': 'Identity-reuse of dao_right bank primitive; 2 strokes, N (no joint).',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_dao_right(draw, ox=0, oy=0, scale=1.0)
    out = HERE / '01_刂.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
