"""p3_char_0188_边 — G5 attempt.

边 = 力 (upper-right) + 辶 (walk radical wrapping bottom-left).
5 strokes total: heng_zhe_gou + pie (力) + dian + zigzag + ping_na (辶).

Uses bank primitives chuo_walk.py + li_power.py. No BANK_DEVIATION —
both primitives fit the composition cleanly, just require positioning
+ scaling.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from chuo_walk import draw_chuo
from li_power import draw_li


SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,     # 3 (chuo) + 2 (li) = 5, matches MMH expected
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': '辶 scaled to wrap bottom-left; 力 upper-right compact. '
             'chuo contributes strokes 3-4-5 mapped to MMH 3 (long zigzag), '
             '4 (mid zzp segment), 5 (bottom ping_na). li contributes '
             'strokes 1-2 mapped to MMH 1 (heng_zhe_gou) + 2 (pie).',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # 辶 — wraps bottom-left. Native ~x[27,269] y[71,279] at scale=1.
    # Scale ~0.82 fills bottom-left; shift slightly left/up.
    draw_chuo(draw, ox=0, oy=-8, scale=0.82)

    # 力 — upper-right. Push right so pie doesn't collide with 辶 zigzag.
    draw_li(draw, ox=138, oy=25, scale=0.60)

    out = pathlib.Path(__file__).with_name('01_边.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
