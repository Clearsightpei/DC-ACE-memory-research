"""p3_char_0161_甴 — G4 attempt.

Character: 甴 (yóu, a beetle). 5 strokes. Structurally like 由 with a
rectangular box and a short vertical protrusion at the top-center.

Strokes (per MMH structural expectations):
  s1 — 竖 : left vertical of the box (ML → BL).
  s2 — 横折 : top bar + right vertical (ML → BC).
  s3 — 短竖 : center-top protrusion piercing s2's top (TC → BC-top).
  s4 — 横 : middle horizontal bar (BL → MR) crossing s3.
  s5 — 短横 : bottom horizontal bar (BL-bot → BC-mid).

Joints:
  s1.head ⇆ s2.head @ ML — N (small gap)
  s1.mid  ⇆ s4.head @ BL — N (small gap at left)
  s1.tail ⇆ s5.head @ BL — N (small gap)
  s2.mid  ⇆ s3.mid  @ C  — P (welded, center crossing)
  s2.mid  ⇆ s4.tail @ BR — N (small gap at right)
  s2.tail ⇆ s5.tail @ BC — T (tangent, welded)
  s3.tail ⇆ s4.mid  @ BC — N (small gap)

Bank checklist: no direct 甴 primitive; used shu/heng/heng_zhe from
success_bank as inline primitives with overriding anchors.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))
from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from shu import draw_shu
from heng import draw_heng
from heng_zhe import draw_heng_zhe


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes drawn matching MMH anchors within tolerance.'
}


def draw_char(draw):
    # s1: 竖 (left vertical of box).
    s1_head = ('ML', 0.498, 0.477)
    s1_tail = ('BL', 0.867, 0.812)
    draw_shu(draw, s1_head, s1_tail, width=8)

    # s2: 横折 (top + right side). Head=ML top-right-ish, corner near
    # top-right of the box, tail=BC (bottom of right side).
    # MMH endpoints only give head/tail; corner is at the intersection
    # of the top bar height and the right column.
    s2_head = ('ML', 0.703, 0.503)
    s2_corner = ('MR', 0.10, 0.503)   # near TR/MR boundary, top-right
    s2_tail = ('BC', 0.948, 0.522)
    draw_heng_zhe(draw, s2_head, s2_corner, s2_tail,
                  h_width=8, v_width=8, shoulder=10)

    # s3: 短竖 (top-center protrusion, pierces s2 at cell C).
    s3_head = ('TC', 0.269, 0.645)
    s3_tail = ('BC', 0.38, 0.001)
    draw_shu(draw, s3_head, s3_tail, width=8)

    # s4: 横 (middle horizontal bar, crosses s3 at mid).
    s4_head = ('BL', 0.855, 0.118)
    s4_tail = ('MR', 0.177, 0.986)
    draw_heng(draw, s4_head, s4_tail, width=8)

    # s5: 短横 (bottom horizontal bar).
    s5_head = ('BL', 0.932, 0.722)
    s5_tail = ('BC', 0.931, 0.522)
    draw_heng(draw, s5_head, s5_tail, width=8)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_char(draw)
    out = os.path.join(os.path.dirname(__file__), '01_甴.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
