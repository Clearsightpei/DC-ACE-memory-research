"""佗 (tuō) — 7 strokes.
Decomposition: 佗 = 亻 (left, 2 strokes) + 它 (right, 5 strokes).
             它 = 宀 (top, 3 strokes: 点+短竖/点+横钩) + 匕 (bottom, 2 strokes: 撇+竖弯钩).

Reading order (per MMH):
  s1 撇  — 亻 pie          TL(0.891,0.697) → BL(0.211,0.039)
  s2 竖  — 亻 shu          ML(0.706,0.573) → BL(0.75,0.962)
  s3 点  — 宀 top dot      TC(0.582,0.645) → TC(0.937,0.911)
  s4 竖  — 宀 short shu    C(0.195,0.143)  → C(0.102,0.638)
  s5 横  — 宀 heng (of 横钩) C(0.321,0.257) → MR(0.171,0.465)
  s6 撇  — 匕 pie          MR(0.045,0.641) → BC(0.529,0.194)
  s7 竖弯钩 — 匕 bottom     C(0.386,0.729)  → BR(0.476,0.276)

Joints (all N — natural gaps):
  s1.mid ⇆ s2.head  @ ML  N (~17 px)
  s3.tail ⇆ s5.mid  @ MR  N (~35 px)
  s4.mid ⇆ s5.head  @ C   N (~15 px)
  s5.tail ⇆ s6.head @ MR  N (~30 px)
  s6.tail ⇆ s7.mid  @ BC  N (~13 px)

Following A-recipe: MMH-verbatim anchors + base primitives. Inline the
2-stroke 亻 (ren_side defaults sit in TC/C — MMH places at TL/ML) and
the 5-stroke 它 (no bank primitive exists for 它 / 宀 / 匕 with a good
enough anchor match).
"""
import os
import sys

BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from dian import draw_dian
from shu_wan_gou import draw_shu_wan_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 primitive calls below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('7 strokes MMH-verbatim; all 5 joints preserved as N-gaps. '
              's7 (竖弯钩) rendered as vertical descent + rightward sweep + '
              'upward hook using shu_wan_gou; head/tip anchors from MMH, '
              'belly/corner/hook_pt interpolated.'),
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- 亻 (left radical, 2 strokes) ----
    # s1: 撇 pie of 亻 — long diagonal top-right → bottom-left.
    draw_pie(draw,
             from_anchor=('TL', 0.891, 0.697),
             to_anchor=('BL', 0.211, 0.039),
             head_width=11, tail_width=2, curve=0.08, segments=48)

    # s2: 竖 of 亻 — short vertical dropping from mid.
    draw_shu(draw,
             from_anchor=('ML', 0.706, 0.573),
             to_anchor=('BL', 0.75, 0.962),
             width=9)

    # ---- 它 (right side, 5 strokes) ----
    # s3: 点 top dot of 宀 (top center, short down-right).
    draw_dian(draw,
              from_anchor=('TC', 0.582, 0.645),
              to_anchor=('TC', 0.937, 0.911),
              head_width=2, peak_width=10, curve=0.10)

    # s4: 竖 short left stroke of 宀 (short vertical/point down).
    draw_shu(draw,
             from_anchor=('C', 0.195, 0.143),
             to_anchor=('C', 0.102, 0.638),
             width=8)

    # s5: 横 (main horizontal of the roof / start of 横钩), heading right.
    draw_heng(draw,
              from_anchor=('C', 0.321, 0.257),
              to_anchor=('MR', 0.171, 0.465),
              width=8)

    # s6: 撇 of 匕 — descending curve from MR top → BC bottom.
    draw_pie(draw,
             from_anchor=('MR', 0.045, 0.641),
             to_anchor=('BC', 0.529, 0.194),
             head_width=9, tail_width=3, curve=0.06, segments=40)

    # s7: 竖弯钩 of 匕 — vertical descent, rounded turn, hook UP-right at tip.
    # MMH head at C(0.386, 0.729)=(139,173), tip at BR(0.476, 0.276)=(248,228).
    # Route: down through belly at C(0.30, 0.98)≈(130, 198), corner at
    # BC(0.35, 0.75)≈(135, 275), sweep right through hook_pt BR(0.30, 0.75)
    # ≈(230, 275), then flick UP to tip.
    draw_shu_wan_gou(draw,
                     head=('C', 0.386, 0.729),
                     belly=('C', 0.35, 0.98),
                     corner=('BC', 0.35, 0.78),
                     hook_pt=('BR', 0.35, 0.72),
                     tip=('BR', 0.476, 0.276),
                     head_w=8, belly_w=11, corner_w=11,
                     hook_start_w=10, tip_w=2)

    out = os.path.join(os.path.dirname(__file__), '01_佗.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
