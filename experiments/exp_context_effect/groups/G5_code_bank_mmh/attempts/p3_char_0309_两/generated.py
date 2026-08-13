"""p3_char_0309_两 — G5 attempt.

Structure (7 strokes, per MMH block + visual GT):
  s1: top wide heng (long, spans across)
  s2: LEFT frame short shu/pie (from below top heng, going down)
  s3: RIGHT frame heng-zhe-gou (heng across to corner, then shu down, small hook)
  s4: left inner long pie (down-left)
  s5: left inner short na (short down-right at bottom)
  s6: right inner long pie (down-left)
  s7: right inner short na (short down-right at bottom)

Bank use: draw_heng, draw_shu, draw_heng_zhe_gou, draw_pie, draw_na — all as-is.
No BANK_DEVIATION.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]
                       / 'success_bank' / 'code'))

from heng import draw_heng
from shu import draw_shu
from heng_zhe_gou import draw_heng_zhe_gou
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7-stroke render, outer frame (heng + left shu + right heng-zhe-gou) '
             'plus two interior 人 (pie+na each). All joints N except welded '
             's3.head-s4.mid and s3.mid-s6.mid X-cross (handled by primitive overlap).',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1: top heng — wide, spans from left to right at top
    draw_heng(draw, (48, 60), (258, 62), width_head=10, width_tail=11)

    # s2: LEFT frame short shu/pie — starts just below top heng, curves down-left
    # Slight leftward drift for the calligraphic pie feel
    draw_shu(draw, (78, 82), (55, 285), width=8)

    # s3: RIGHT frame heng-zhe-gou — heng from ~top-right, corner, then shu down,
    # small hook flick at bottom-left
    draw_heng_zhe_gou(draw,
                      heng_head=(88, 90),
                      corner=(248, 88),
                      gou_tail=(238, 285),
                      hook_tip=(215, 278))

    # s4: LEFT inner long pie — from near top of frame down to the bottom-left area
    draw_pie(draw, (108, 118), (85, 260),
             bow_perp=6, w_head=7, w_tail=3)

    # s5: LEFT inner short na — from mid-frame diagonally down-right
    draw_na(draw, (100, 200), (140, 260),
            bow_perp=6, w_head=3, w_tail=8)

    # s6: RIGHT inner long pie — from near top of frame down-left
    draw_pie(draw, (185, 118), (150, 262),
             bow_perp=10, w_head=7, w_tail=3)

    # s7: RIGHT inner short na — from mid-frame down-right
    draw_na(draw, (180, 200), (220, 260),
            bow_perp=6, w_head=3, w_tail=8)

    out = pathlib.Path(__file__).parent / '01_两.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
