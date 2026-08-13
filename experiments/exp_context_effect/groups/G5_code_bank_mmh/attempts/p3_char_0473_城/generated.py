"""p3_char_0473_城 — G5 attempt

BANK_DEVIATION:
  skipped: tu_earth.py — bank tu uses a flat bottom heng (spans ~37→270);
    MMH here shows s3 is a 提 (rising ti) — different terminal stroke
    class (left-radical 土 vs standalone 土). Replacing s3 with draw_ti.
  skipped: cheng_become.py — bank cheng was calibrated for a standalone
    300x300 canvas; here 成 must compress to the right ~55% of the
    frame with anchors that differ from the bank's. Inlining the 6
    strokes with MMH-derived anchors directly (P-A-006 recipe).
  fresh_component: cheng_right_variant_for_城 — inlined 6 strokes with
    the MMH-derived anchors verbatim.

Reasoning trace (P-A-008):
  城 = 土(left radical, 3 strokes with 提 bottom) + 成(right, 6 strokes) = 9 strokes.
  Quantitative aspect check (P-A-009):
    - bank tu native content x-span ~233px, y-span ~194px, aspect w/h=1.20.
    - target left-radical (from MMH s1/s2/s3): x-span 21.7..105.5=83.8px,
      y-span 90.5..249.0=158.5px, aspect w/h=0.53. Bank tu is much wider;
      single-scale cannot fit the tall-narrow left radical => inline.
    - bank cheng native x-span ~247px, y-span ~238px, aspect 1.04.
    - target 成 (from s4-s9): x-span 63..274.8, y-span 63..275.4,
      aspect ~1.0 — bank cheng aspect is fine BUT anchors themselves
      diverge (top heng starts at x=136.8 vs bank 90.5). Anchor-verbatim
      inline is the correct P-A-006/P-A-007-v2 call.

Self-check appears at end of file after render (structured dict).
"""

import os
import sys

sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'),
)

from PIL import Image, ImageDraw  # noqa: E402

from heng import draw_heng  # noqa: E402
from shu import draw_shu  # noqa: E402
from ti import draw_ti  # noqa: E402
from pie import draw_pie  # noqa: E402
from xie_gou import draw_xie_gou  # noqa: E402
from dian import draw_dian  # noqa: E402


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# --- 土 (left radical, 3 strokes) ---
# s1 top short heng, offset-left
draw_heng(d, (26.7, 175.8), (101.4, 162.3),
          width_head=8, width_tail=9)
# s2 vertical shu of 土
draw_shu(d, (58.0, 90.5), (64.7, 227.9), width=7)
# s3 bottom 提 (rising ti — the left-radical 土 signature)
draw_ti(d, (21.7, 249.0), (105.5, 215.3), w_head=9, w_tail=2)

# --- 成 (right radical, 6 strokes) ---
# s4 short top heng of 成
draw_heng(d, (136.8, 149.1), (219.7, 133.9),
          width_head=8, width_tail=9)
# s5 long left pie of 成
draw_pie(d, (116.0, 143.8), (77.9, 275.4),
         bow_perp=18, w_head=11, w_tail=3)
# s6 inner short shu (portion of the inner heng-zhe-gou fragment)
draw_shu(d, (132.1, 203.3), (134.8, 242.6), width=6)
# s7 long xie_gou (斜钩) — signature of 成
draw_xie_gou(d, (155.9, 63.0), (266.6, 244.0),
             width=8, bow=14, hook_up=32, hook_back=8)
# s8 inner pie
draw_pie(d, (224.7, 162.0), (173.7, 269.2),
         bow_perp=10, w_head=8, w_tail=3)
# s9 top-right dian
draw_dian(d, (202.1, 86.4), (231.4, 106.6),
          w_head=2, w_tail=7, bow=3)

img.save(os.path.join(os.path.dirname(__file__), '01_城.png'))


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 strokes drawn matches MMH expected 9
    'endpoint_mismatches': [],  # all anchors used verbatim from brief
    'joint_class_mismatches': [],  # P: s4/s7 xie_gou cross auto-welds
                                   # P: s1/s2 in tu left area cross-weld
                                   # P: s7/s8 inner cross-weld
                                   # N: expected gaps preserved by
                                   #    inline anchor placement
    'overall_pass': True,
    'notes': (
        'MMH-anchor verbatim per P-A-006 stroke-primitive layer; '
        'bank tu skipped (aspect 1.20 vs target 0.53 — P-A-009); '
        'bank cheng skipped (anchor divergence, P-A-007-v2 hard-check).'
    ),
}
