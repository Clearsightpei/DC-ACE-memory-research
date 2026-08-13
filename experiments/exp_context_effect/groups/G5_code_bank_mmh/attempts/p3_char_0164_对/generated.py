"""p3_char_0164_对 — 对 (dui, "correct/pair").

Decomposition (5 strokes per MMH):
  Left component 又 (compressed):
    s1 = 横撇 (heng_pie) — draw_heng_pie
    s2 = 捺 (na)          — draw_na
  Right component 寸:
    s3 = 一 (heng)        — draw_heng
    s4 = 亅 (shu_gou)    — draw_shu_gou
    s5 = 丶 (dian)       — draw_dian

MMH anchor endpoints (converted to pixels on 300x300 canvas):
  s1: head=(52.1,130.1)   tail=(27.2,251.7)
  s2: head=(58.6,159.1)   tail=(128.9,236.7)
  s3: head=(139.2,145.9)  tail=(270.7,134.8)
  s4: head=(205.1,66.5)   tail=(172.9,264.8)
  s5: head=(144.1,180.8)  tail=(175.8,212.4)

Joints (verified per MMH):
  s1.mid X s2.mid @ ML  — welded P (X-cross of 又)
  s1.mid vs s3.head @ C — N (gap; heng of 寸 stays clear of 又)
  s3.mid X s4.mid @ MR  — welded P (heng of 寸 crossed by shu_gou)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 5 primitive calls, matches MMH count 5
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Uses bank heng_pie/na/heng/shu_gou/dian directly with MMH anchors. '
             'heng_pie apex compressed to fit left-third since 又 is squeezed.'
}
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]
                       / 'success_bank' / 'code'))

from PIL import Image, ImageDraw

from heng_pie import draw_heng_pie
from na import draw_na
from heng import draw_heng
from shu_gou import draw_shu_gou
from dian import draw_dian


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # --- Left: 又 (compressed to left half) ------------------------------
    # s1 横撇: heng arc kept short (apex_x only ~50px right of head) so the
    # heng segment stays inside ML cell; pie sweeps down-left to BL.
    s1_head = (52.1, 130.1)
    s1_tail = (27.2, 251.7)
    draw_heng_pie(d, s1_head, s1_tail, apex_x=100, corner_x=95)

    # s2 捺: from just below/right of s1's corner, sweeping down-right.
    s2_head = (58.6, 159.1)
    s2_tail = (128.9, 236.7)
    draw_na(d, s2_head, s2_tail, bow_perp=6, w_head=4, w_tail=10)

    # --- Right: 寸 -------------------------------------------------------
    # s3 heng across right two-thirds.
    s3_head = (139.2, 145.9)
    s3_tail = (270.7, 134.8)
    draw_heng(d, s3_head, s3_tail, width_head=8, width_tail=9)

    # s4 shu_gou: tall vertical from TR down through the heng, hooking left.
    s4_head = (205.1, 66.5)
    s4_tail = (172.9, 264.8)
    draw_shu_gou(d, s4_head, s4_tail, width=7, hook_start_offset=30)

    # s5 dian: small tick starting at middle, going down-right; sits below
    # the heng and to the left of the shu, characteristic 寸 tick.
    s5_head = (144.1, 180.8)
    s5_tail = (175.8, 212.4)
    draw_dian(d, s5_head, s5_tail, w_head=3, w_tail=6, bow=2)

    out = pathlib.Path(__file__).parent / '01_对.png'
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
