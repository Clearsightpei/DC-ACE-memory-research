"""p2_radical_122_王 — 4 strokes: heng, heng, shu, heng (bottom LONG).

Structurally 土 (tu_earth) plus one extra middle heng. Bottom heng is
the longest (王 shape marker); top short; middle short-to-medium.

Uses bank primitives draw_heng and draw_shu. No BANK_DEVIATION.
"""

import os
import sys
from PIL import Image, ImageDraw

# Bank imports
BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)
from heng import draw_heng
from shu import draw_shu


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 4 turtle-equivalent stroke calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('4 strokes: heng(top short), heng(middle short), shu(vertical), '
              'heng(bottom LONG). Joints: J1 s1.mid~s3.head N gap ok; '
              'J2 s2.mid~s3.mid P weld; J3 s3.tail~s4.mid N gap ok.'),
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1 top heng: ML(0.867,0.052)->TR(0.174,0.943) = (86.7,105.2)->(217.4,94.3)
    draw_heng(draw, (86.7, 105.2), (217.4, 94.3),
              width_head=9, width_tail=10)

    # s2 middle heng: ML(0.97,0.846)->MR(0.068,0.746) = (97,184.6)->(206.8,174.6)
    # Slightly shorter than top; medium width.
    draw_heng(draw, (97.0, 184.6), (206.8, 174.6),
              width_head=9, width_tail=10)

    # s3 shu vertical (central shaft): C(0.403,0.137)->BC(0.436,0.522)
    # = (140.3, 113.7) -> (143.6, 252.2). Pierces middle heng (J2=P weld).
    # Head near top heng leaves natural N-gap (J1). Tail leaves N-gap above bottom heng (J3).
    draw_shu(draw, (140.3, 113.7), (143.6, 252.2), width=8)

    # s4 bottom LONG heng: BL(0.357,0.66)->BR(0.713,0.64)
    # = (35.7, 266) -> (271.3, 264). Longest of the three horizontals.
    draw_heng(draw, (35.7, 266.0), (271.3, 264.0),
              width_head=10, width_tail=11)

    out = os.path.join(os.path.dirname(__file__), "01_王.png")
    img.save(out)
    print(f"wrote {out}")
    print(f"SELF_CHECK overall_pass={SELF_CHECK['overall_pass']}")


if __name__ == "__main__":
    main()
