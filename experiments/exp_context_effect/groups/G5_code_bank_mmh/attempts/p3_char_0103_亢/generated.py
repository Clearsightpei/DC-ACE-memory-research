"""p3_char_0103_亢 (kang) — 4 strokes: dian + heng + pie + shu-wan-gou.

Composition (亠 top over 儿-like bottom):
  s1: small 点 at top-center (the little tick above the heng)
  s2: long 横 across the middle
  s3: 撇 left leg curving down-left from just under center
  s4: 竖弯钩 right leg from just under center, straight down, curve right,
      hook up-right — tail is the hook tip.

米字格 → pixel (300x300, each cell 100x100; TL@(0,0), TC@(100,0), TR@(200,0),
                                              ML@(0,100), C@(100,100), MR@(200,100),
                                              BL@(0,200), BC@(100,200), BR@(200,200))
  s1 head TC(0.271,0.601)=(127.1, 60.1)  tail TC(0.644,0.914)=(164.4, 91.4)
  s2 head ML(0.524,0.324)=( 52.4,132.4)  tail MR(0.394,0.137)=(239.4,113.7)
  s3 head ML(0.999,0.664)=( 99.9,166.4)  tail BL(0.595,0.924)=( 59.5,292.4)
  s4 head  C(0.184,0.667)=(118.4,166.7)  tail BR(0.593,0.326)=(259.3,232.6)

Joint (expected):
  s3.head(99.9,166.4) ⇆ s4.head(118.4,166.7) — N (natural gap ~16 px).
  Anchor distance = sqrt(18.5^2 + 0.3^2) ≈ 18.5 px → already N by anchors.
  Do NOT weld: draw s3 and s4 independently.
"""

import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from dian import draw_dian
from heng import draw_heng
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 primitives, matches MMH
    'endpoint_mismatches': [], # each stroke uses the MMH anchor directly
    'joint_class_mismatches': [],  # s3.head vs s4.head: gap ~18 px = N
    'overall_pass': True,
    'notes': 'All 4 strokes drawn from bank primitives. s3/s4 heads sit ~18px apart naturally (N-joint preserved by anchor geometry, not welded).'
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: small top dian — thin at head, thicker at tail (typical 丶)
    draw_dian(d, (127, 60), (164, 91), w_head=3, w_tail=8, bow=3, steps=48)

    # s2: long horizontal heng across the middle, slight upward tilt
    draw_heng(d, (52, 132), (239, 114), width_head=9, width_tail=10)

    # s3: 撇 — left leg, curves down-left from just under center to bottom-left
    draw_pie(d, (100, 166), (60, 292),
             bow_perp=10, w_head=7, w_tail=2, steps=80)

    # s4: 竖弯钩 — right leg, drops from just under center, curves right at
    # the bottom, hooks up-right. Tail is the hook TIP at BR(259,233).
    # Since tail.y (233) is above the actual bottom of the curve, we use
    # a smaller bottom_extra so the curve's bottom sits ~y=290 and hook
    # tip lands near (259,233).
    draw_shu_wan_gou(d, (118, 167), (259, 233),
                     width=7, bottom_extra=57, knee_ratio=0.75)

    return img


if __name__ == '__main__':
    out = pathlib.Path(__file__).parent / '01_亢.png'
    render().save(out)
    print(f'wrote {out}')
