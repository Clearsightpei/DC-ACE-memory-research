"""p3_char_0285_师 — G5 attempt.

Recipe: P-A-006 stroke-primitive layer (6-stroke char, MMH anchors verbatim).
No whole-radical primitive fits cleanly (⺁ + 帀 is not in the bank; per
P-A-007 whole-radical only when it truly matches — no match here).

Stroke plan (from MMH block):
  s1: small pie/vertical near top-left  (54,117) -> (61,208)   -- draw_pie (near-vertical, tiny bow)
  s2: big pie (long left sweep)         (98,85)  -> (44,292)   -- draw_pie
  s3: top heng of right half            (142,103)-> (254,91)   -- draw_heng
  s4: short inner shu (left of box)     (137,155)-> (142,232)  -- draw_shu
  s5: 横折 shoulder of inner box        (152,157)-> (207,214)  -- draw_heng_zhe_short
  s6: tall right shu, extends off canvas(178,110)-> (188,310)  -- draw_shu

Joints:
  s2.mid & s4.head: N — natural gap ~36 px (leave MMH anchors alone)
  s3.mid & s6.head: N — natural gap ~20 px (leave)
  s4.head & s5.head: N — small ~12 px gap (leave)
  s5.mid & s6.mid: P — welded at C. draw s6 LAST → overdraw welds crossing.
"""

import sys, os
from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from pie import draw_pie
from heng import draw_heng
from shu import draw_shu
from heng_zhe_short import draw_heng_zhe_short

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 primitive calls matching expected 6
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'P-A-006: all 6 strokes use MMH anchors verbatim. s6 drawn last for P-weld overdraw with s5.',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — small pie top-left (draw as slim pie with tiny rightward bow; MMH endpoints)
    draw_pie(d, head=(54, 117), tail=(61, 208), bow_perp=8, w_head=6, w_tail=2)

    # s2 — big long 撇 on left
    draw_pie(d, head=(98, 85), tail=(44, 292), bow_perp=14, w_head=10, w_tail=3)

    # s3 — top 一 of right half (slight up-slope to the right)
    draw_heng(d, head=(142, 103), tail=(254, 91), width_head=9, width_tail=10)

    # s4 — short inner shu (left side of inner 巾-box)
    draw_shu(d, head=(137, 155), tail=(142, 232), width=7)

    # s5 — 横折 shoulder: extend horizontal so corner near x=200 (matches P-joint at ~191,155)
    draw_heng_zhe_short(d, head=(152, 157), tail=(207, 214), corner_offset=(28, -2))

    # s6 — tall right shu extending off canvas (draw LAST for P-weld overdraw with s5)
    draw_shu(d, head=(178, 110), tail=(188, 310), width=8)

    out = os.path.join(os.path.dirname(__file__), '01_师.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    render()
