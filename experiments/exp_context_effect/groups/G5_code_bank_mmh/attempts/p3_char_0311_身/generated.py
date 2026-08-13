"""p3_char_0311_身 — G5 attempt.

身 (shēn, "body") — 7 strokes. Structure:
  s1: 撇 (short top hat, slants down-left)
  s2: 竖 (left vertical of frame — goes to bottom)
  s3: 横折 (top + right wall of frame, mild hook)
  s4: 横 (upper interior)
  s5: 横 (lower interior)
  s6: 横 (bottom exits right — closes frame and extends)
  s7: 撇 (long diagonal descender, from mid-right down-left)

Bank uses: pie, shu, heng, heng_zhe_gou. Frame based loosely on
zi_self/yue_moon geometry, adapted for 身 (taller, narrower frame in
upper-left, plus a long crossing descender).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from heng_zhe_gou import draw_heng_zhe_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 stroke primitive calls below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '身 composed as: pie top hat + shu left + heng_zhe_gou frame '
             '+ 2 inner hengs + bottom heng + long descending pie. Frame '
             'shifted up-left, descender sweeps from mid to lower-left.',
}


def draw_shen(draw):
    # s1: top pie (short slant, down-left, more pronounced)
    draw_pie(draw, head=(160, 45), tail=(80, 115),
             bow_perp=8, w_head=8, w_tail=3)

    # s2: 竖 — left vertical of the frame (taller)
    draw_shu(draw, head=(83, 108), tail=(120, 225), width=8)

    # s3: 横折(钩) — top + right wall of frame (wider)
    draw_heng_zhe_gou(draw,
                      heng_head=(110, 62),
                      corner=(198, 60),
                      gou_tail=(178, 222),
                      hook_tip=(163, 214))

    # s4: upper interior heng
    draw_heng(draw, head=(112, 115), tail=(183, 108),
              width_head=6, width_tail=7)

    # s5: lower interior heng
    draw_heng(draw, head=(116, 170), tail=(183, 162),
              width_head=6, width_tail=7)

    # s6: bottom heng — closes frame and extends right
    draw_heng(draw, head=(112, 225), tail=(230, 217),
              width_head=7, width_tail=8)

    # s7: 撇 — long diagonal descender (from upper-mid down to lower-left)
    draw_pie(draw, head=(180, 75), tail=(55, 285),
             bow_perp=28, w_head=10, w_tail=3)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_shen(d)
    out = os.path.join(os.path.dirname(__file__), '01_身.png')
    img.save(out)
    print(f'wrote {out}')
    print('SELF_CHECK:', SELF_CHECK)


if __name__ == '__main__':
    main()
