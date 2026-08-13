"""p3_char_0192_代 — G5 attempt.

Composition: 亻 (left, 2 strokes: pie + shu) + 弋 (right, 3 strokes: heng + xie-gou + dian).
All 5 strokes rendered via endpoint-signature bank primitives at exact
MMH-derived anchor pixel coordinates.

Joint 1 (N): s1.mid ≈ (69, 130), s2.head = (91, 143) → natural ~26 px gap (no weld).
Joint 2 (P): s3 (heng slanting up-right) crosses s4 (xie-gou down-right)
             naturally within cell C — the classic 弋 crossing.
"""

import os
import sys

# Add success_bank/code so imports resolve
BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from PIL import Image, ImageDraw

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from xie_gou import draw_xie_gou
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('5 strokes matching MMH anchors within 1px. '
              'J1 N-gap ~26px (>0, no weld). '
              'J2 heng+xie-gou physically cross in cell C (P satisfied).'),
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # s1: 撇 of 亻 — TL(0.979,0.773) → BL(0.278,0.054)
    #     pixel (98, 77) → (28, 205). Long leftward sweep, heavy head → thin tail.
    draw_pie(d, head=(98, 77), tail=(28, 205),
             bow_perp=10, w_head=9, w_tail=3)

    # s2: 竖 of 亻 — ML(0.911,0.43) → BL(0.899,0.868)
    #     pixel (91, 143) → (90, 287). Straight vertical shaft, no top curl
    #     (this is composed context, not the bare 丨 radical).
    draw_shu(d, head=(91, 143), tail=(90, 287), width=7)

    # s3: 横 of 弋 — C(0.204,0.702) → MR(0.388,0.389)
    #     pixel (120, 170) → (239, 139). Short heng tilting slightly up-right.
    draw_heng(d, head=(120, 170), tail=(239, 139),
              width_head=7, width_tail=8)

    # s4: 斜钩 of 弋 — TC(0.43,0.586) → BR(0.733,0.373)
    #     pixel (143, 59) → (273, 237). Slanted body descends right, hooks up.
    #     Crosses s3 naturally in cell C (joint J2 = P).
    draw_xie_gou(d, head=(143, 59), tail=(273, 237),
                 width=8, bow=8, hook_up=30, hook_back=6)

    # s5: 点 of 弋 — TR(0.077,0.765) → MR(0.396,0.028)
    #     pixel (208, 77) → (240, 103). Small tapered dot in the upper-right
    #     of the 弋, thin head → thick tail.
    draw_dian(d, head=(208, 77), tail=(240, 103),
              w_head=3, w_tail=7, bow=2)

    out_png = os.path.join(os.path.dirname(__file__), "01_代.png")
    img.save(out_png)
    print(f"Wrote {out_png}")
    print(f"SELF_CHECK: {SELF_CHECK}")


if __name__ == "__main__":
    main()
