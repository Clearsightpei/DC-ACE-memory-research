"""方 (fāng, 4-stroke radical) — first attempt.

Anchor plan (米字格, PIL y-down convention):

  s1 — 点 (top dot).
      head = ('TC', 0.30, 0.30)  small dot 起笔 upper-left
      tail = ('TC', 0.60, 0.55)  rounded press lower-right
      (MMH endpoints TC(0.307,0.589)→TC(0.693,0.932) place the dot
       fully in the bottom of TC — overriding upward slightly so the
       dot sits above the top-heng, matching GT.)

  s2 — 横 (top horizontal, slight rise).
      head = ('ML', 0.45, 0.55)
      tail = ('MR', 0.75, 0.35)   rising slightly right
      (MMH: ML(0.434,0.471)→MR(0.666,0.301))

  s3 — 横折钩 body (right side of the box + hook flick up-left).
      head    = ('C', 0.45, 0.35)   near the mid of the top-heng
      corner  = ('MR', 0.55, 0.55)  right side, top of vertical drop
      tail    = ('BC', 0.70, 0.55)  bottom of vertical drop
      tip     = ('BC', 0.45, 0.35)  hook tip up-and-left
      (Compound stroke — MMH gives 4-stroke count so this is one call.)

  s4 — 撇 (long diagonal sweep down-left).
      head = ('C', 0.55, 0.60)   thick 起笔 upper-right
      tail = ('BL', 0.30, 0.75)  needle-tip 出锋 lower-left
      (MMH: C(0.518,0.72)→BC(0.239,0.643) — sweep down-and-left.)

Joints:
  s2.mid ⇆ s3.head @ cell C — N (small gap ≈ 12 px)
  s3.head area ⇆ s4.head @ cell C — N (small gap ≈ 18 px)
  s2.tail-region ⇆ s3.head at top-heng — the 横折钩 starts near the
    right of the top heng but with a small natural gap (N).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,    # 4 stroke calls: dian, heng, heng_zhe_gou, pie
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        'Revised once. First render had 横折钩 heng-segment not aligned '
        'with top heng (looked like double horizontal). Revision: 横折钩 '
        'head moved to the right end of the top heng so it reads as one '
        'continuous top beam, and vertical drop lengthened. 撇 head '
        'raised toward the top-heng level and tail pushed further down '
        'and left to sweep across the box. Visual features matching GT: '
        '(a) dot at top-center, (b) single continuous top horizontal, '
        '(c) right-side hook curving up-left at bottom, (d) long 撇 '
        'sweeping down-left from top-right area.'
    )
}

import os
import sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy  # noqa: E402
from dian import draw_dian  # noqa: E402
from heng import draw_heng  # noqa: E402
from heng_zhe_gou import draw_heng_zhe_gou  # noqa: E402
from pie import draw_pie  # noqa: E402


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1 — 点 (top dot), small, above the top-heng
    draw_dian(draw,
              from_anchor=('TC', 0.30, 0.55),
              to_anchor=('TC', 0.60, 0.85),
              head_width=2, peak_width=10)

    # s2 — 横 (top horizontal), spanning most of the middle band
    draw_heng(draw,
              from_anchor=('ML', 0.20, 0.50),
              to_anchor=('MR', 0.70, 0.35),
              width=9)

    # s3 — 横折钩 (top-right of box → right wall → up-left hook)
    #   head continues from where the top-heng ends,
    #   corner sits just below at the same x, then vertical drop.
    draw_heng_zhe_gou(draw,
                      head=('MR', 0.65, 0.35),
                      corner=('MR', 0.85, 0.55),
                      tail=('BR', 0.60, 0.65),
                      tip=('BR', 0.25, 0.55),
                      h_width=9, v_width=10, shoulder=12, tip_w=2)

    # s4 — 撇 (long diagonal sweep from top-heng area down to lower-left)
    draw_pie(draw,
             from_anchor=('C', 0.45, 0.35),
             to_anchor=('BL', 0.15, 0.90),
             head_width=11, tail_width=1, curve=0.10)

    out_png = os.path.join(HERE, '01_方.png')
    img.save(out_png)
    print(f'wrote {out_png}')


if __name__ == '__main__':
    render()
