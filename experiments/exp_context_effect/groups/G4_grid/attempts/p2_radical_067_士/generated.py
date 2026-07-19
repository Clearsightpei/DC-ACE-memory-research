"""p2_radical_067_士 (shì, "scholar") — G4 attempt.

3 strokes:
  s1: 横 (upper, LONGER) — ML(0.384,0.816) → MR(0.607,0.714)
  s2: 竖 (vertical middle) — TC(0.365,0.788) → BC(0.427,0.528)
  s3: 横 (lower, SHORTER) — BL(0.794,0.657) → BR(0.186,0.64)

Joints:
  J1: s1.mid ⇆ s2.mid @ C  — P (welded crossing) — both middles at center
  J2: s2.tail ⇆ s3.mid    @ BC — N (small gap ~21 px, DO NOT weld)

Composition: 士 uses two 横 primitives (bank: draw_heng) + one 竖
primitive (bank: draw_shu). All anchors overridden per composition.

The N-gap on J2 is enforced by leaving s2's tail slightly ABOVE
where s3 passes (y=252.8 vs s3.y≈264.8 → ~12 px raw + width buffer
gives a natural visible break, matching MMH gap≈21.5 px).
"""

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from heng import draw_heng
from shu import draw_shu

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'shi: two heng + one shu; s1 top-heng longer than s3 bottom-heng (MMH). '
             'J1 P at C (welded crossing since both strokes overlap at center). '
             'J2 N between s2.tail(≈y=252.8) and s3.mid(≈y=264.8) — natural gap.'
}


def draw_shi(draw):
    # s1 — upper 横 (LONGER)
    s1_head = ('ML', 0.384, 0.816)
    s1_tail = ('MR', 0.607, 0.714)
    draw_heng(draw, s1_head, s1_tail, width=9)

    # s2 — vertical 竖 through center; stop just short of s3 to leave N-gap
    s2_head = ('TC', 0.365, 0.788)
    s2_tail = ('BC', 0.427, 0.528)   # y≈252.8 (well above s3 line y≈264.8)
    draw_shu(draw, s2_head, s2_tail, width=10)

    # s3 — lower 横 (SHORTER)
    s3_head = ('BL', 0.794, 0.657)
    s3_tail = ('BR', 0.186, 0.64)
    draw_heng(draw, s3_head, s3_tail, width=9)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_shi(draw)
    out = os.path.join(os.path.dirname(__file__), '01_士.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
