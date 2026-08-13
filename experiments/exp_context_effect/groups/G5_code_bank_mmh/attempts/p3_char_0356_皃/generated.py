"""p3_char_0356_皃 — 皃 (mao, ancient form of 貌 'appearance'). 7 strokes.

Structure = 白 (top, 5 strokes) + 儿 (bottom, 2 strokes).

P-A-006 recipe: MMH-verbatim anchors + stroke-primitive layer.
Whole-radical bank check (P-A-007-v2 hard-check):
  - bai_white native box ≈ 150w×142h; 皃's 白-part box ≈ 76w×59h.
    Scale ratio ≈ 0.51 in width, 0.42 in height — BELOW 0.55 threshold.
    → DO NOT call draw_bai_white; inline via stroke primitives.
  - No dedicated 儿 bank primitive; s6 (pie) + s7 (shu_wan_gou) inline.
  - shu_wan_gou stroke primitive is a good fit for s7.

MMH-derived stroke anchors (cell + x_frac + y_frac → pixel; y_frac
grows DOWN within cell per G5's convention):
  s1 (pie top hat): TC(0.74,0.668) → C(0.559,0.277)   = (174, 67) → (156, 128)
  s2 (shu left):    C(0.277,0.315) → BC(0.465,0.036)  = (128, 132) → (147, 204)
  s3 (heng_zhe):    C(0.436,0.33)  → MR(0.039,0.907)  = (144, 133) → (204, 191)
  s4 (heng mid):    C(0.494,0.614) → C(0.96,0.576)    = (149, 161) → (196, 158)
  s5 (heng btm):    C(0.541,0.954) → MR(0.019,0.828)  = (154, 195) → (202, 183)
  s6 (pie leg):     BC(0.485,0.077) → BC(0.084,0.851) = (149, 208) → (108, 285)
  s7 (shu_wan_gou): C(0.793,0.957) → BR(0.754,0.402)  = (179, 196) → (275, 240)

Joints: all N (12 N-joints per brief) — no P/T welds required.
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box
from shu_wan_gou import draw_shu_wan_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 7 stroke calls (matches MMH expected 7)
    'endpoint_mismatches': [],     # all endpoints from MMH anchors verbatim
    'joint_class_mismatches': [],  # all joints are N (natural gaps); no P/T welds
    'overall_pass': True,
    'notes': ('P-A-006 stroke-primitive layer; P-A-007-v2 hard-check: '
              'bai_white scale ratio 0.51/0.42 < 0.55 threshold → inline. '
              'draw_shu_wan_gou fits s7 (儿 right leg).'),
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: top 撇 (short steep pie above the box) — bolder
    draw_pie(d, (174.0, 67.0), (156.0, 128.0),
             bow_perp=8, w_head=10, w_tail=4, steps=60)

    # s2: 竖 left side of the top box — bolder
    draw_shu(d, (128.0, 132.0), (147.0, 204.0), width=9)

    # s3: 横折 (top + right side of box); use heng_zhe_box with
    # top_left = s3.head, bottom_right = s3.tail — bolder
    draw_heng_zhe_box(d,
                      (144.0, 133.0),
                      (204.0, 191.0),
                      width=9)

    # s4: middle 横 (interior bar) — bolder
    draw_heng(d, (149.0, 161.0), (196.0, 158.0),
              width_head=7, width_tail=8)

    # s5: bottom 横 (closes the box) — bolder
    draw_heng(d, (154.0, 195.0), (202.0, 183.0),
              width_head=8, width_tail=9)

    # s6: left leg 撇 of 儿 (long down-left sweep) — less taper so it reads bold
    draw_pie(d, (149.0, 208.0), (108.0, 285.0),
             bow_perp=12, w_head=11, w_tail=5, steps=80)

    # s7: right leg 竖弯钩 of 儿 — bolder, deeper belly for prominent hook
    draw_shu_wan_gou(d, (179.0, 196.0), (275.0, 240.0),
                     width=10, bottom_extra=50, knee_ratio=0.72)

    out = os.path.join(os.path.dirname(__file__), '01_皃.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    draw()
