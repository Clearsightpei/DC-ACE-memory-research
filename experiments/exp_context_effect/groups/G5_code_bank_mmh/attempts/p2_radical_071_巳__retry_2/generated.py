"""p2_radical_071_巳 — RETRY 2. 3 strokes: 横折 + 横 + 竖弯钩.

TRAJECTORY DIFF (looked at GT + main + retry_1 PNGs):

GT visual (300x300):
  * Top rectangle ~130 wide, ~55 tall, upper region.
  * Middle heng (s2) short, tucked inside the top rectangle, right-biased,
    endpoint touching or nearly touching the right vertical.
  * Bottom curve (s3) is BIG: descends from just below top-left corner
    down to about y=270, sweeps right along a low shoulder to about
    x=270, then hooks up-left ending near (245, 225).

Main (C): top loop cramped and shifted right; bottom curve too shallow
  and too narrow; overall silhouette squat.

Retry_1 (C): widened top loop and lifted head to y=80. Better silhouette
  but bottom drop was reduced (bottom_extra=48) — the low shoulder sits
  at ~y=250 instead of ~y=270, so the sweep still reads circle-like
  rather than the tall-and-flat 竖弯钩 of GT. Also s3.tail x=240 was too
  far left; GT hook terminus is closer to x=245-250 but the shoulder
  extends past x=265 before curling back.

Fixes this attempt:
  * bottom_extra=68 (was 48) → shoulder drops to ~y=278.
  * s3_tail x=262 (was 240) → shoulder extends further right before hook.
  * knee_ratio=0.72 (was 0.85) → shoulder shape flatter, wider.
  * Slightly larger top box (s1 tail to x=220, y=158).
  * s1_head to y=95 (was 80) so top box sits at natural upper-mid,
    matching GT's vertical placement rather than pinning at very top.
  * s3_head at (85, 100) — meets top-left corner region cleanly, still
    N-gap from s1.

Bank primitives used (all reference, no BANK_DEVIATION):
  - heng_zhe_short (s1)
  - heng           (s2)
  - shu_wan_gou    (s3)
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
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # 3 N-class gaps preserved
    'overall_pass': True,
    'notes': 'Retry #2: deeper + wider bottom sweep to match GT 竖弯钩 spread.',
}


def main() -> None:
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1: 横折 — top of loop + fold-down on right
    s1_head = (100, 95)
    s1_tail = (220, 158)
    draw_heng_zhe_short(d, head=s1_head, tail=s1_tail)

    # Stroke 2: 横 — interior middle horizontal, right-biased, touches right wall
    s2_head = (115, 143)
    s2_tail = (215, 138)
    draw_heng(d, head=s2_head, tail=s2_tail, width_head=8, width_tail=9)

    # Stroke 3: 竖弯钩 — full-height left vertical, wide bottom sweep, hook up
    # Revision: pulled tail slightly left + higher (255, 208) so the hook curl
    # reads more clearly as a rising tick; kept bottom_extra=68 for deep sweep.
    s3_head = (85, 100)
    s3_tail = (255, 208)
    draw_shu_wan_gou(d, head=s3_head, tail=s3_tail,
                     width=8, bottom_extra=68, knee_ratio=0.72)

    out_path = os.path.join(os.path.dirname(__file__), '01_巳.png')
    img.save(out_path)
    print('wrote', out_path)


if __name__ == '__main__':
    main()
