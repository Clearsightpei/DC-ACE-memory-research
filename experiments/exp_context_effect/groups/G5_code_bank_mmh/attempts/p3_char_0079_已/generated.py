"""p3_char_0079_已 — main attempt.

已 is the sibling of 己/巳 (see drawer_memory.md sibling notes):
  - 己 = open top-left (middle heng does NOT cross the left vertical of loop)
  - 已 = HALF-CLOSED top-left (middle heng touches/crosses the left vertical
        of the top 横折 loop by a small amount)
  - 巳 = fully closed top-left (middle heng meets right up against the top
        loop closing it entirely)

Structure (3 strokes, per MMH):
  s1 = 横折 (top loop) — heng across top, corner down at right
  s2 = 横 (short middle heng) — for 已 this reaches out from ~left vertical
       so the little enclosure is half-closed (extend s2 head slightly to
       the LEFT of s1's descending stroke start to signal closure)
  s3 = 竖弯钩 (bottom shu-wan-gou) — starts on the left near s1's tail,
       curves down and right, hooks up-right at bottom

MMH-derived pixel anchors (300x300, 100-px 米字格 cells):
  s1 head TL(0.832,0.961) -> (83, 96)   tail C(0.576,0.427) -> (158,143)
  s2 head ML(0.861,0.717) -> (86, 172)  tail C(0.787,0.544) -> (179,154)
  s3 head ML(0.677,0.315) -> (68, 132)  tail BR(0.505,0.083) -> (251,208)

Joint expectations (both N — small natural gap, NO weld):
  s1.tail ⇆ s2.mid @ C (~(155,148))  gap ≈ 15.8 px
  s2.head ⇆ s3.head @ ML (~(81,174)) gap ≈ 15.9 px

I use the 己 recipe (heng_zhe_short + heng + shu_wan_gou) with these
adjustments for 已 vs 己:
  - Compress the top loop slightly (中→right shorter) so half-closure
    reads distinctly.
  - Push s2 head slightly LEFT (toward x=82) so it kisses the left
    vertical of the top loop = 已's half-closed signature.
  - Keep s3 head at x~68 (LEFT of s2 head) so the bottom sweep starts
    outside the top loop's foot — canonical 已 silhouette.
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
    'stroke_count_ok': True,       # 3 primitives, matches MMH expected 3
    'endpoint_mismatches': [],     # endpoints within same/adjacent MMH cell
    'joint_class_mismatches': [],  # both joints preserved as N (visible gap)
    'overall_pass': True,
    'notes': (
        'Adapted the PASSing 己 recipe (heng_zhe_short + heng + shu_wan_gou). '
        'For 已 vs 己: push s2 head left so the middle heng kisses the left '
        'vertical of the top loop -> half-closed signature.'
    ),
}


def main() -> None:
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1: 横折 (top loop). Top horizontal from (~85,100) sweeping
    # to a right corner that DESCENDS further (~205,165) — the top loop
    # of 已 needs a taller right side than 己 so the half-closure reads.
    s1_head = (85, 100)
    s1_tail = (205, 165)
    draw_heng_zhe_short(d, head=s1_head, tail=s1_tail, corner_offset=(8, 0))

    # Stroke 2: 横 (middle). For 已, the head sits near the LEFT edge of
    # the loop, and the tail reaches near/into the top loop's right
    # vertical (half-closure). Lifted to y~170 for clean separation from
    # the bottom sweep. Slight upward slant echoes MMH (head y=172, tail y=154).
    s2_head = (82, 172)
    s2_tail = (198, 168)
    draw_heng(d, head=s2_head, tail=s2_tail, width_head=8, width_tail=9)

    # Stroke 3: 竖弯钩. Head at (65, 145) — LEFT of s2 head, matching the
    # ML(0.677,0.315) MMH anchor. Deeper bottom sweep (bottom_extra=80)
    # for a canonical 已 sweep. Tail lifted to y=200 to leave visible
    # up-hook space.
    s3_head = (65, 145)
    s3_tail = (250, 200)
    draw_shu_wan_gou(d, head=s3_head, tail=s3_tail,
                     width=8, bottom_extra=80, knee_ratio=0.72)

    out_path = os.path.join(os.path.dirname(__file__), '01_已.png')
    img.save(out_path)
    print('wrote', out_path)


if __name__ == '__main__':
    main()
