"""p3_char_0095_丹 — G5 attempt.

4 strokes per MMH:
  s1: 撇 pie (TL(94.6, 89.9) -> BL(45.4, 300+)) — left descending, extends to bottom
  s2: 横折钩 heng_zhe_gou (heng_head=(113.4, 90.8), corner/gou_tail inferred,
      hook_tip=(147.9, 281.2) per MMH tail)
  s3: 点 dian ((137.1, 121.6) -> (158.5, 149.7)) — small dot in center
  s4: 横 heng ((29, 189.6) -> (275.4, 182.2)) — long crossing horizontal that
      pierces both s1 and s2 (P joints @ cell C)

Bank reused: pie, heng_zhe_gou, dian, heng — all native fits, no BANK_DEVIATION.
Sibling of 月 (yue_moon.py); structure identical except s3=dian (not inner heng),
and s4 spans full width crossing both frame sides.

SELF_CHECK dict below per G5/G4 mandatory pre-submit spec.
"""

import sys
import pathlib
from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from pie import draw_pie
from heng_zhe_gou import draw_heng_zhe_gou
from dian import draw_dian
from heng import draw_heng


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 primitives: pie + heng_zhe_gou + dian + heng
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('4 strokes match MMH count. s1 pie head/tail on TL/BL. s2 heng_zhe_gou head TC, '
              'hook_tip near BC (147.9,281.2 as MMH tail). s3 dian inside cell C. s4 heng spans '
              'ML->MR (long crossing). Joints: s1.mid crosses s4 near C (P weld — extending s4 '
              'through pie body), s2.mid crosses s4 near C (P weld — heng passes through right '
              'vertical). No BANK_DEVIATION.')
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: 撇 (long left sweep, from upper right to bottom-left; extended to y=298)
    draw_pie(d, (94.6, 89.9), (45.4, 298.0),
             bow_perp=16, w_head=9, w_tail=3)

    # s2: 横折钩 (top horizontal + right vertical + hook)
    #   heng_head from MMH: (113.4, 90.8)
    #   corner inferred: horizontal extends right to ~(188, 88)
    #   gou_tail inferred: bottom of vertical ~(170, 290)
    #   hook_tip from MMH tail: (147.9, 281.2)
    draw_heng_zhe_gou(d,
                      (113.4, 90.8),   # heng_head
                      (188.0, 88.0),   # corner
                      (170.0, 290.0),  # gou_tail
                      (147.9, 281.2))  # hook_tip

    # s4 drawn BEFORE s3 so the dot sits on top (visual layering; stroke count
    # is unaffected). But MMH order is s3 then s4; render in visual order.
    # s4: 横 (long crossing horizontal, spans well beyond the frame both sides)
    draw_heng(d, (29.0, 189.6), (275.4, 182.2),
              width_head=7, width_tail=9)

    # s3: 点 (small dot in the center, upper-mid inside the frame)
    draw_dian(d, (137.1, 121.6), (158.5, 149.7),
              w_head=3, w_tail=7, bow=3)

    out_path = pathlib.Path(__file__).parent / '01_丹.png'
    img.save(out_path)
    print(f'wrote {out_path}')


if __name__ == '__main__':
    main()
