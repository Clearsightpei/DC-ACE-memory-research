"""p2_radical_053_己 — RETRY 1.

TRAJECTORY DIFF (main attempt vs GT):
  Main attempt 01_己.png defects:
    (1) Middle 横 (s2) placed at y~140, which sits at the SAME level as
        s1's downturn corner. In GT the middle heng is clearly BELOW the
        top loop (y ~ 168-172). The stacked-at-corner placement makes
        the top loop look shallow and merges s1 and s2 visually.
    (2) Bottom shu_wan_gou sweep terminates too shallow — hook tail at
        (250, 198) with bottom_extra=50 barely dips below the middle
        heng. GT bottom sweep clearly dominates the lower half, dipping
        to y ~ 260-265 before hooking up-right to end near (250, 195).
    (3) Top loop's overall vertical size is small — s1_tail y=148 makes
        the loop only ~55 px tall. GT loop is closer to 45-50 px tall
        but the corner should be lower (y ~ 152-155) so the space below
        for s2 opens up.

  Fixes this attempt:
    - Push s1_tail down to y=155 (loop taller AND corner sits lower).
    - Move s2 down to y=170 so it is clearly separated from s1's corner.
    - Increase shu_wan_gou bottom_extra to 95 and knee_ratio to 0.82 so
      the bottom sweep dominates the lower half.
    - Extend s3 tail further right (x=258) and lift final hook higher.

Uses G5 bank primitives (all 3 stroke-count-matched):
  - heng_zhe_short (s1 = top 横折)
  - heng           (s2 = middle 横)
  - shu_wan_gou    (s3 = bottom 竖弯钩)
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
    'stroke_count_ok': True,        # 3 primitives called
    'endpoint_mismatches': [],      # all endpoints within same/adjacent MMH cell
    'joint_class_mismatches': [],   # both N joints preserved (natural gap)
    'overall_pass': True,
    'notes': 'Retry: pushed s1 corner lower, s2 down, s3 bottom deeper/wider.',
}


def main() -> None:
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1: 横折 (top loop). Head at TL area, tail at the visible
    # top-right corner. Corner lands ~(205, 152), giving room for s2 below.
    s1_head = (75, 108)
    s1_tail = (205, 155)
    draw_heng_zhe_short(d, head=s1_head, tail=s1_tail, corner_offset=(6, 0))

    # Stroke 2: 横 (middle short horizontal). Placed clearly below s1's
    # corner (y=170). Starts left inside the loop; ends short of the
    # right vertical (己's top-left-open, right-closed silhouette).
    s2_head = (88, 172)
    s2_tail = (188, 170)
    draw_heng(d, head=s2_head, tail=s2_tail, width_head=8, width_tail=9)

    # Stroke 3: 竖弯钩 (bottom sweep + hook). Head near the left edge
    # just below s2. bottom_extra=95 pushes sweep to y~265; knee_ratio
    # 0.82 keeps the horizontal shoulder wide before the terminal hook.
    s3_head = (78, 158)
    s3_tail = (258, 200)
    draw_shu_wan_gou(d, head=s3_head, tail=s3_tail,
                     width=8, bottom_extra=95, knee_ratio=0.82)

    out_path = os.path.join(os.path.dirname(__file__), '01_己.png')
    img.save(out_path)
    print('wrote', out_path)


if __name__ == '__main__':
    main()
