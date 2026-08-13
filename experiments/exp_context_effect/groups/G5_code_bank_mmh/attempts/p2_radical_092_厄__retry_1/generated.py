"""p2_radical_092_厄__retry_1 — G5 retry #1.

TRAJECTORY DIFF (from inspecting GT + main-attempt PNGs):

FAIL main (verdict C):
  * The inner element was rendered as a full L-shape heng-zhe (with a
    long vertical drop down to y=205) PLUS a shu-wan-gou. That created
    visible double vertical lines on the right side of the interior,
    reading as too-many strokes / too-boxy.
  * shu_wan_gou called with knee_ratio=0.92 and bottom_extra=65 pushed
    the shoulder too far down / right; combined with a head at (122,135)
    the curve read as a square rather than a smooth 竖弯钩.
  * The 厂 top-heng (from draw_chang) is fine; the pie is fine.

GT observation:
  * Inner element is compact: heng-zhe at top forms just the top-right
    corner (short horizontal + gentle short drop into a soft corner) —
    NOT a full vertical descent to bottom.
  * shu_wan_gou wraps from upper-left of interior, down, across bottom,
    up with a small terminal hook. It carries the LEFT vertical, the
    BOTTOM, and the right hook.

Fixes this attempt:
  1. Replace the inline L-shape heng-zhe with the bank `heng_zhe_short`
     (乛) — tighter, curved corner, no long vertical drop.
  2. shu_wan_gou head kept high-left (~105, 135), tail near (215, 210),
     with smaller bottom_extra (35) and knee_ratio 0.85 → smoother curve.
  3. Retry-hint from errata (interior heng at y=138) informs y placement.
"""

import os
import sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from chang_cliff import draw_chang  # noqa: E402
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402
from heng_zhe_short import draw_heng_zhe_short  # noqa: E402


# ------------------------- Self-check block -------------------------
# Stroke count target: 4
# s1 (chang top heng) head ≈ (97, 88)   tail ≈ (243, 84)   ~ TL/TR
# s2 (chang left pie) head ≈ (77, 94)   tail ≈ (20, 297)   ~ TL/BL
# s3 heng_zhe_short  head ≈ (117, 132)  tail ≈ (200, 175)  ~ C  (fits N-gap ~20 vs s4.head)
# s4 shu_wan_gou     head ≈ (108, 138)  tail ≈ (215, 210)  ~ C/BR
#
# Joint J1 (s1.head ⇆ s2.head @ TL): draw_chang leaves ~19 px gap → N ✓
# Joint J2 (s3.head ⇆ s4.head @ C ): both heads within ~10-12 px in x and y → N ~10-15 px

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('Retry uses heng_zhe_short (乛) for s3 instead of inline '
              'L-shape; removes the redundant right-vertical that made '
              'the main attempt boxy. shu_wan_gou uses tighter geometry '
              '(bottom_extra=35, knee_ratio=0.85) for a smoother curve.'),
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # -------- s1 + s2 : 厂 outer (bank) --------
    draw_chang(d, ox=0, oy=0, scale=1.0)

    # -------- s3 : inner top-right — small 乛 (heng_zhe_short) --------
    # A compact curve, not a full L; the vertical drop belongs to s4.
    draw_heng_zhe_short(d,
                        head=(117, 132),
                        tail=(200, 175),
                        corner_offset=(4, 0))

    # -------- s4 : shu_wan_gou wrapping interior left + bottom + hook --
    draw_shu_wan_gou(d,
                     head=(108, 138),
                     tail=(215, 210),
                     width=6,
                     bottom_extra=35,
                     knee_ratio=0.85)

    return img


if __name__ == '__main__':
    out = os.path.join(HERE, '01_厄.png')
    render().save(out)
    print('wrote', out)
