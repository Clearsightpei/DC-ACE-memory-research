# BANK_DEVIATION
# skipped: li_power.py (composed 力 primitive)
# reason: bank draw_li's pie head sits close to the heng (y=88 vs heng y=108),
#         but in 加 the pie of 力 extends much higher (target pie_head y~=76,
#         heng y~=164) and the whole 力 must sit further left/taller. Uniform
#         (ox, oy, scale) can't retarget both the pie extension and heng placement
#         simultaneously. Inline fresh 力 built from stroke primitives instead.
# fresh_component: li_for_加 (heng_zhe_gou + tall pie sitting left-of-口)
#
# For 口 we use draw_kou at ox/oy/scale — its geometry (small box) scales cleanly.

import os
import sys
from PIL import Image, ImageDraw

# Add success_bank/code to path
BANK = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from heng_zhe_gou import draw_heng_zhe_gou   # noqa: E402
from pie import draw_pie                     # noqa: E402
from kou_mouth import draw_kou               # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 力=2 (heng_zhe_gou+pie) + 口=3 = 5
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('力 inlined fresh (BANK_DEVIATION on li_power); 口 uses draw_kou '
              'at scale=0.65. Joints: s1xs2 P (heng crosses pie); s1-s3 N gap; '
              's3-s4 N gap; s3-s5 N gap; s4-s5 N gap.'),
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ------------------ 力 (left) ------------------
    # stroke 1: 横折钩
    #   heng_head ML(0.349, 0.641) = (35, 164)
    #   corner:   internal, approx top-right of the 横, calligraphic ~(158, 152)
    #   gou_tail: BL(0.876, 0.628) = (88, 263)  (hook tip)
    #   hook_tip: small flick up-left of gou_tail
    heng_head = (35, 164)
    corner    = (158, 152)
    gou_tail  = (88, 263)
    hook_tip  = (60, 253)
    draw_heng_zhe_gou(d, heng_head, corner, gou_tail, hook_tip)

    # stroke 2: 撇
    #   head TL(0.914, 0.756) = (91, 76)
    #   tail BL(0.149, 0.903) = (15, 290)
    pie_head = (91, 76)
    pie_tail = (15, 290)
    draw_pie(d, pie_head, pie_tail, bow_perp=18, w_head=9, w_tail=2, steps=110)

    # ------------------ 口 (right) ------------------
    # bank draw_kou at scale=0.65 reference-canvas coords:
    #   s1_head bank (100,128) -> want target (172, 166)
    #   ox = 172 - 100*0.65 = 107, oy = 166 - 128*0.65 = 83
    draw_kou(d, ox=107, oy=83, scale=0.65)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '01_加.png')
    img.save(out)
    return out


if __name__ == '__main__':
    path = render()
    print('wrote', path)
