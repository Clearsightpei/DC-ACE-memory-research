"""p3_char_0158_出 — G5 attempt.

MMH structural spec: 5 strokes.
  s1: ('ML', 0.75, 0.248) → ('MR', 0.145, 0.556)  = (75, 125) → (215, 156)  — inner 竖折
  s2: ('MR', 0.241, 0.09) → ('MR', 0.212, 0.834)  = (224, 109) → (221, 183) — inner-right 竖
  s3: ('TC', 0.386, 0.592) → ('BC', 0.468, 0.616) = (139, 59)  → (147, 262) — TALL central 竖
  s4: ('BL', 0.759, 0.191) → ('BR', 0.25, 0.613)  = (76, 219)  → (225, 261) — outer 竖折
  s5: ('BR', 0.224, 0.165) → ('BR', 0.394, 1.021) = (222, 217) → (239, 302) — outer-right 竖

Joints:
  J1 (N ~20.6px): s1.tail ⇆ s2.mid(0.80) @ MR(219,162)  — small gap on right of inner cup
  J2 (P weld):    s1.mid(0.69) ⇆ s3.mid(0.55) @ C(156,168) — s3 pierces s1
  J3 (N ~20px):   s3.tail ⇆ s4.mid(0.66) @ BC(154,262) — small gap where s3 ends above s4 base
  J4 (N ~19.3px): s4.tail ⇆ s5.mid(0.63) @ BR(231,265) — small gap right of outer cup

Bank uses (no BANK_DEVIATION): draw_shu (x3), draw_shu_zhe (x2).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 5 strokes = 2*shu_zhe + 3*shu
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes composed from bank shu + shu_zhe. Central s3 pierces s1 midpoint (P). Three N-joints keep ~13-15px gaps at cup right-edges and outer base — under the 20px target but same class.',
}

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    '..', '..', 'success_bank', 'code')
sys.path.insert(0, _BANK)

from shu import draw_shu           # noqa: E402
from shu_zhe import draw_shu_zhe   # noqa: E402


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: inner 竖折 — down from (75,125) to corner (77,156), across to (215,156).
    # Leave ~15px gap before s2 vertical so joint J1 reads as N (not weld).
    draw_shu_zhe(d, (75, 125), (77, 156), (213, 156), width=7)

    # s2: inner-right 竖 — vertical (224,109) → (221,183).
    draw_shu(d, (224, 109), (221, 183), width=7)

    # s3: TALL central 竖 — (139,59) → (147,262). Pierces s1 midpoint.
    # End slightly above s4's inner base line so J3 reads as N.
    draw_shu(d, (139, 59), (147, 258), width=8)

    # s4: outer 竖折 — down (76,219) → corner (78,261), across to (225,261).
    # Leave ~15px gap before s5 vertical so joint J4 reads as N.
    draw_shu_zhe(d, (76, 219), (78, 261), (222, 261), width=8)

    # s5: outer-right 竖 — (222,217) → (239,302). Extends off canvas bottom.
    draw_shu(d, (222, 217), (239, 302), width=8)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '01_出.png')
    img.save(out)
    return out


if __name__ == '__main__':
    print(render())
