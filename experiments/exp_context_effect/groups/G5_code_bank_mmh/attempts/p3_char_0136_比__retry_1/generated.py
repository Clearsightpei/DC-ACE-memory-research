"""G5 retry #1: p3_char_0136_比 (bi, 'compare').

TRAJECTORY DIFF
---------------
Main attempt (verdict C) — visual gaps vs GT:
  1. Right 撇 (s3) is visually tiny/floating with +6 bow_perp bowing
     DOWN, making it look like a short disconnected dash. GT shows a
     confident diagonal with calligraphic weight (thicker head, clean
     taper) bowing subtly UP.
  2. Left/right 竖弯钩 have very asymmetric bottom_extra (18 vs 45), so
     the left half looks squashed and short while the right half looks
     tall. GT: both halves are roughly the same height, just offset
     horizontally.
  3. Left 提 (s1) is too thin (w_head=8) compared to GT's bolder rising
     stroke; head at (80,176) is fine but under-inked.

Fixes this retry (per P-A-005 / sibling-pair discipline):
  a. Flip s3 bow_perp to -8 (negative bow = "up" arch, per P-A-005
     recipe for calligraphic weight); bump w_head to 10.
  b. Rebalance the two 竖弯钩: left bottom_extra 36 (up from 18), right
     bottom_extra 42 (down from 45). Both halves reach similar bottom
     y-range while keeping MMH-anchored tail x-positions distinct.
  c. Bump 提 w_head to 10 for a more visible left-half opener.
  d. Nudge left shu_wan_gou head slightly down (57,109 -> 57,105) so
     its top clears the 提 above; nudge right shu_wan_gou knee_ratio
     to 0.70 (from 0.72) for a slightly more open curl matching GT.

Structure (from MMH block, 4 strokes) — sibling-pair 匕/匕 halves:
  s1: 提           ML(80,176)   -> C(133,162)   [left small rising]
  s2: 竖弯钩       ML(57,105)   -> BC(126,216)  [left main curl+hook]
  s3: 撇           MR(228,117)  -> C(169,172)   [right short pie]
  s4: 竖弯钩       TC(147,73)   -> BR(261,211)  [right main curl+hook]

Joints (both class N — natural gap, DO NOT weld):
  J1: s1.head ⇆ s2.mid(0.37) @ ML — expected gap ~15 px
  J2: s3.tail ⇆ s4.mid(0.32) @ C  — expected gap ~17 px

Bank usage: draw_ti (s1), draw_shu_wan_gou x2 (s2, s4), draw_pie (s3).
No BANK_DEVIATION needed.
"""

import sys
import pathlib

sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw

from ti import draw_ti
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 4 stroke calls: ti + swg + pie + swg
    'endpoint_mismatches': [],     # anchors per MMH block (rounded to int)
    'joint_class_mismatches': [],  # both N; no weld attempted
    'overall_pass': True,
    'notes': ('Retry #1: rebalance 竖弯钩 heights (left 36 / right 42), '
              'flip s3 bow_perp to -8 with w_head=10 for calligraphic '
              'weight (P-A-005), bump 提 w_head to 10. Sibling-pair '
              'discipline: both halves are anchored per MMH but with '
              'harmonized visual mass.'),
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: 提 (short left rising) — ML head, C tail
    draw_ti(d, head=(80, 176), tail=(133, 162),
            w_head=10, w_tail=2, steps=50)

    # s2: 竖弯钩 (left half) — ML head, BC tail
    # bottom_extra 36 gives a moderate curl depth balancing s4.
    draw_shu_wan_gou(d, head=(57, 105), tail=(126, 216),
                     width=7, bottom_extra=36, knee_ratio=0.72)

    # s3: 撇 (right short pie) — MR head, C tail
    # NEGATIVE bow_perp per P-A-005 for calligraphic weight, wider head.
    draw_pie(d, head=(228, 117), tail=(169, 172),
             bow_perp=-8, w_head=10, w_tail=3, steps=80)

    # s4: 竖弯钩 (right half) — TC head, BR tail
    # bottom_extra 42 slightly under main attempt's 45 for balance with s2.
    draw_shu_wan_gou(d, head=(147, 73), tail=(261, 211),
                     width=8, bottom_extra=42, knee_ratio=0.70)

    out = pathlib.Path(__file__).with_name('01_比.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
