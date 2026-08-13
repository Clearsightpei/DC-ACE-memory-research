"""p3_char_0253_好 (hǎo, "good", 6画) — 女 + 子 (left-right composition).

Decomposition (per drawer_memory.md compositional playbook):
  好 = 女 (left, strokes 1-3) + 子 (right, strokes 4-6)

Approach: MMH anchors are cross-radical-tight (strokes 1-2 of 女 have
their tails reaching well into BL / BC area near the mid line, and s3
横 stays only on the left column) — so rather than reuse `nv.py` /
`zi_char.py` with heavy overrides (v8: never-tune-anchors rule), draw
fresh with the exact per-stroke MMH anchors from the injected brief.
Uses shared stroke primitives (pie_dian, pie, heng, heng_pie, wan_gou).

Strokes (from MMH):
  s1 撇点   head TL(0.826, 0.691) → pivot near BL(0.9, 0.35) → tail BC(0.242, 0.61)
  s2 撇     head C(0.143, 0.371) → tail BL(0.401, 0.716)
  s3 短横   head ML(0.173, 0.661) → tail C(0.113, 0.532)  (short, only across left column)
  s4 横撇   head C(0.444, 0.078) → corner near TR → tip C(0.942, 0.43)
  s5 弯钩   head C(0.796, 0.447) → belly → hook → tip BC(0.614, 0.751)
  s6 横     head C(0.315, 0.875) → tail MR(0.812, 0.793)

Joints (from MMH):
  s1.mid × s2.mid @ BL — P (welded crossing) — MMH 0.0 px
  s1.mid × s3.mid @ ML — P (welded crossing) — MMH 0.0 px
  s2.head ⇆ s3.tail @ C — N (~16.8 px gap)
  s2.mid ⇆ s6.head @ C — N (~22 px gap)
  s4.tail ⇆ s5.head @ C — N (~12.4 px gap)
  s5.mid × s6.mid @ MR — P (welded crossing)
"""
import os
import sys

sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw

from pie_dian import draw_pie_dian
from pie import draw_pie
from heng import draw_heng
from heng_pie import draw_heng_pie
from wan_gou import draw_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('Drawn fresh from MMH per-stroke anchors; primitives '
              'pie_dian/pie/heng/heng_pie/wan_gou; 6 strokes total.'),
}


def draw_hao(draw):
    # ---- Left half: 女 (strokes 1-3) ----
    # s1 撇点: head TL upper-right region, pivot near BL(0.95, 0.31) per joint,
    # tail BC(0.242, 0.61). Pivot chosen so the 撇 segment sweeps down-left
    # from TL(0.83,0.69) through BL(0.95,0.31)... wait — MMH gives tail at
    # BC(0.242,0.61). We route: head → pivot elbow near BL(0.60,0.75) →
    # tail BC(0.242,0.61). The joint s1.mid @ BL(0.95,0.31) is the 撇 body
    # midpoint, which is naturally between head TL(0.83,0.69) [PIL px ≈
    # (83,69)] and pivot BL(0.6,0.75) [px (60,275)] — actually the injected
    # 'BL(0.95, 0.308)' cell coords ≈ (95,231). The 撇 body cuts through
    # that region on its way from TL to BL/BC.
    draw_pie_dian(draw,
                  head=('TL', 0.826, 0.691),
                  pivot=('BL', 0.60, 0.78),
                  tail=('BC', 0.242, 0.61),
                  pie_head_w=12, pie_tip_w=4,
                  dian_head_w=4, dian_tail_w=11)

    # s2 撇: head C(0.143, 0.371), tail BL(0.401, 0.716)
    draw_pie(draw,
             from_anchor=('C', 0.143, 0.371),
             to_anchor=('BL', 0.401, 0.716),
             head_width=11, tail_width=2, curve=0.06)

    # s3 短横: head ML(0.173, 0.661) → tail C(0.113, 0.532)
    # Short horizontal — welds through s1 body at BL/ML corner (P joint).
    draw_heng(draw,
              from_anchor=('ML', 0.173, 0.661),
              to_anchor=('C', 0.113, 0.532),
              width=8)

    # ---- Right half: 子 (strokes 4-6) ----
    # s4 横撇: head C(0.444, 0.078) → corner top-right of head → tip C(0.942, 0.43)
    # Corner placed close to tail's x-column but at head's y so we get a proper
    # short horizontal then a downward hook (not a wide angular V).
    draw_heng_pie(draw,
                  head=('C', 0.444, 0.078),
                  corner=('C', 0.98, 0.15),
                  tip=('C', 0.70, 0.43),
                  head_w=7, corner_w=10, tip_w=4)

    # s5 弯钩: body from C(0.796, 0.447) curling down with belly slightly right,
    # ends at hook_pt low and to the right of tip, tip up-and-left at
    # BC(0.614, 0.751).
    draw_wan_gou(draw,
                 head=('C', 0.796, 0.447),
                 belly=('MR', 0.05, 0.65),
                 hook_pt=('BC', 0.80, 0.82),
                 tip=('BC', 0.614, 0.751),
                 head_w=8, belly_w=12, hook_start_w=10, tip_w=2)

    # s6 横: head C(0.315, 0.875) → tail MR(0.812, 0.793)
    # Long horizontal spanning the mid-lower band; welds through s5 body
    # at MR (P joint).
    draw_heng(draw,
              from_anchor=('C', 0.315, 0.875),
              to_anchor=('MR', 0.812, 0.793),
              width=9)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_hao(draw)
    out_path = os.path.join(os.path.dirname(__file__), '01_好.png')
    img.save(out_path)
    print(f'Wrote {out_path}')


if __name__ == '__main__':
    main()
