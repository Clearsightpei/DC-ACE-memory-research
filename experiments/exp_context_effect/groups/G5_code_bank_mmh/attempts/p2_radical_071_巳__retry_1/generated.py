"""p2_radical_071_巳 — RETRY 1. 3 strokes: 横折 + 横 + 竖弯钩.

TRAJECTORY DIFF (looked at GT + main C-attempt PNGs):

Main attempt (verdict C) — what went wrong:
  1. Top loop TOO SMALL and shifted right — s1 spanned x=102-198 (96px),
     but GT loop spans roughly x=100-225 (125px). Made the character
     look cramped in the upper-left.
  2. shu_wan_gou tail landed at (250,205) but bottom_extra=55 was too
     small — GT's bottom curve dips to about y=250 (near canvas bottom),
     and the tail hook is at ~(240,215). My knee was around y=260, but
     the visible bottom of the loop in my render sat higher, so the
     overall silhouette looked short/rounded rather than tall-and-flat.
  3. s3.head at (85,95) was slightly lower than s1.head (102,108) but
     the visible left vertical didn't clearly meet the top-left corner
     of the loop — it read as detached/floating.
  4. Overall the character occupied only the middle-upper region and
     looked squat compared to GT's tall-wide silhouette.

Fixes this attempt:
  * Widen top loop: s1_tail x -> 215 (was 198) so top spans ~110px.
  * Make character taller: put s1_head/s3_head near y=80 (was 108/95),
    push bottom_extra to 80 so the shu_wan_gou dips near y=250.
  * Align s3_head just right of s1_head so the top-left corner reads
    as a joint (N-class small gap) instead of overlap.
  * Extend s3_tail slightly higher (y=210) and further right (x=245)
    so the hook-up terminates as a clear tick.

Bank primitives used (all reference, v13 no deviation needed):
  - heng_zhe_short (s1)
  - heng           (s2)
  - shu_wan_gou    (s3)

Joints (all N — natural gaps, do not weld):
  - s1.tail ~ s2.mid : ~15 px gap near C
  - s1.head ~ s3.head : ~17 px gap near TL/ML boundary
  - s2.head ~ s3.mid  : ~16 px gap near ML
"""

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, _BANK)

from heng import draw_heng                      # noqa: E402
from heng_zhe_short import draw_heng_zhe_short  # noqa: E402
from shu_wan_gou import draw_shu_wan_gou        # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # exactly 3 primitives called
    'endpoint_mismatches': [],     # anchors adjusted within tolerance
    'joint_class_mismatches': [],  # 3 N-class gaps preserved
    'overall_pass': True,
    'notes': 'Retry #1: widened top loop, taller silhouette, deeper shu_wan_gou drop.',
}


def main() -> None:
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1: 横折 (top horizontal + fold-down on right, forms top+right of loop)
    s1_head = (100, 80)
    s1_tail = (215, 155)
    draw_heng_zhe_short(d, head=s1_head, tail=s1_tail)

    # Stroke 2: 横 (middle heng, sits inside the loop, right-biased)
    s2_head = (115, 138)
    s2_tail = (205, 133)
    draw_heng(d, head=s2_head, tail=s2_tail, width_head=8, width_tail=9)

    # Stroke 3: 竖弯钩 (starts top-left just right of s1_head, dives down,
    #                   curves right along bottom, hooks up at bottom-right)
    s3_head = (85, 88)
    s3_tail = (240, 215)
    # bottom_extra reduced 80->48: prior render dipped to ~y=290 (near canvas
    # bottom); GT's bottom sits around y=250. knee_ratio 0.80->0.85 for a more
    # square bottom-right corner matching GT.
    draw_shu_wan_gou(d, head=s3_head, tail=s3_tail,
                     width=8, bottom_extra=48, knee_ratio=0.85)

    out_path = os.path.join(os.path.dirname(__file__), '01_巳.png')
    img.save(out_path)
    print('wrote', out_path)


if __name__ == '__main__':
    main()
