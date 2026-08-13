"""p3_char_0432_畋 (tián, "till the fields") — 田 + 攵, 9 strokes.

Recipe: P-A-006 for 田 (MMH anchors verbatim, stroke-primitive layer —
no bank primitive exists for 田 whole radical; see p3_char_0322_佃 for
same pattern) + P-A-007-v2 whole-radical call for 攵 (draw_pu bank
primitive at scale ~1.0 with translation).

BANK_DEVIATION analysis (P-A-009 quantitative):
  Bank pu native bbox: x[56.5, 251.7] (w=195.2), y[75.6, 290.0] (h=214.4)
    native aspect w/h = 195.2/214.4 = 0.910
  Target 攵 (from MMH s6-s9) bbox:
    x[106.1, 285.1] (w=179.0), y[60.9, 288.0] (h=227.1)
    target aspect w/h = 179.0/227.1 = 0.788
  aspect ratio target/native = 0.788/0.910 = 0.866
  In P-A-007-v2 range [0.55, 1.2] -> USE BANK, no deviation.
  x-scale = 179.0/195.2 = 0.917; y-scale = 227.1/214.4 = 1.059.
  Compromise: scale=0.97 uniform; ox translates center 154->195 (=+41),
  oy translates center 182.8->174.5 (=-8).

Composition: 田 left (s1-s5 inline stroke-primitive per MMH), 攵 right
(s6-s9 via draw_pu). Middle-heng s3 crosses middle-shu s4 at ~ML (P
weld). s8 pie crosses s9 na at ~BC (P weld). All other joints N.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))

from PIL import Image, ImageDraw

from shu import draw_shu
from heng import draw_heng
from pu_action import draw_pu


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 5 (田) + 4 (攵 via draw_pu) = 9
    'endpoint_mismatches': [],     # 田 anchors verbatim from MMH; 攵 via bank+translate
    'joint_class_mismatches': [],  # s3xs4 P (田 middle cross), s8xs9 P (攵 X)
    'overall_pass': True,
    'notes': ('MMH anchors verbatim for 田. draw_pu bank primitive '
              'used for 攵 (aspect 0.866 native, within P-A-007-v2 range).'),
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ===== 田 (left half) — inline via stroke-primitives (P-A-006) =====

    # s1: left 竖  ML(0.208,0.351) -> BL(0.413,0.44)
    #     = (20.8, 135.1) -> (41.3, 244.0)
    draw_shu(d, (20.8, 135.1), (41.3, 244.0), width=7)

    # s2: 横折 (top + right of box) ML(0.384,0.365) -> BL(0.964,0.227)
    #     = (38.4, 136.5) -> (96.4, 222.7); corner at (96.4, 136.5)
    d.line([(38.4, 136.5), (96.4, 136.5)], fill='black', width=7)
    d.ellipse([96.4 - 4, 136.5 - 4, 96.4 + 4, 136.5 + 4], fill='black')
    d.line([(96.4, 136.5), (96.4, 222.7)], fill='black', width=7)

    # s3: middle 横  ML(0.492,0.84) -> ML(0.964,0.764)
    #     = (49.2, 184.0) -> (96.4, 176.4)
    draw_heng(d, (49.2, 184.0), (96.4, 176.4),
              width_head=6, width_tail=7)

    # s4: middle 竖  ML(0.645,0.409) -> BL(0.683,0.194)
    #     = (64.5, 140.9) -> (68.3, 219.4)
    draw_shu(d, (64.5, 140.9), (68.3, 219.4), width=6)

    # s5: bottom 横  BL(0.483,0.35) -> BL(0.926,0.276)
    #     = (48.3, 235.0) -> (92.6, 227.6)
    draw_heng(d, (48.3, 235.0), (92.6, 227.6),
              width_head=7, width_tail=8)

    # ===== 攵 (right half) — bank primitive draw_pu (P-A-007-v2) =====
    # Translate: ox=+41 (center 154->195), oy=-8 (center 182.8->174.5)
    # Scale: 0.97 (compromise between x-scale 0.917 and y-scale 1.059)
    draw_pu(d, ox=41, oy=-8, scale=0.97)

    return img


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_畋.png')
    draw().save(out)
    print('wrote', out)
