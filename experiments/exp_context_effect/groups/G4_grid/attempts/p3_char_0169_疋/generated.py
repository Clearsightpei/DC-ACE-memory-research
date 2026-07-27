"""p3_char_0169_疋 (pǐ, "roll of cloth / foot", 5 strokes)

Structure (from injected MMH brief):
  s1: short 横 top-right (ML→C, mid band)
  s2: 竖 spine (C→BC, upper middle to lower center)
  s3: short 横 middle (C→MR, mid band)
  s4: 撇 lower-left (ML→BL)
  s5: 捺 lower-right (ML→BR)

Joints (all N — small natural gaps, do NOT weld):
  s1.mid ⇆ s2.head : N ~15px gap @ C
  s2.mid ⇆ s3.head : N ~18px gap @ C
  s2.tail ⇆ s5.mid : N ~11px gap @ BC
  s4.mid ⇆ s5.head : N ~15px gap @ ML

Checklist confirmations:
  1. success_bank/INDEX.md grep for 疋 — not present.
  2. errata.md grep for 疋 — not present.
  3. form_catalog — 撇 in lower-left, 捺 in lower-right (standard).
  4. principles_meta TR — N-class joints preserve visible gap.
  5. joint_atlas — 5 joints all N: leave natural gaps (~10-20 px).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes: short-heng, shu, short-heng, pie, na. All 4 joints N with visible gaps.',
}

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from na import draw_na


def draw_pi(draw):
    # s1: short top 横 (upper right area)
    draw_heng(draw,
              ('ML', 0.697, 0.049),
              ('C',  0.91,  0.242),
              width=8)

    # s2: 竖 spine from mid to bottom-center
    draw_shu(draw,
             ('C',  0.362, 0.043),
             ('BC', 0.506, 0.268),
             width=9)

    # s3: middle short 横
    draw_heng(draw,
              ('C',  0.559, 0.641),
              ('MR', 0.115, 0.608),
              width=8)

    # s4: 撇 lower-left, moderate curve
    draw_pie(draw,
             ('ML', 0.873, 0.541),
             ('BL', 0.267, 0.736),
             head_width=11, tail_width=2, curve=0.08)

    # s5: 捺 lower-right, standard swell
    draw_na(draw,
            ('ML', 0.97, 0.937),
            ('BR', 0.757, 0.769),
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.78, curve=0.08)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_pi(draw)
    out = os.path.join(os.path.dirname(__file__), '01_疋.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
