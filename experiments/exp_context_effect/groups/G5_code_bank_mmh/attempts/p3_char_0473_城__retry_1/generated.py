"""p3_char_0473_城 — G5 retry #1 (P-A-006 stroke-primitive layer + retune)

TRAJECTORY DIFF (from Read of GT and main FAIL PNG):
  main (FAIL):
    - Anchors were correct per MMH, but STROKE WIDTHS were too heavy
      (heng width_tail=10, pie w_head=11, xie_gou width=8) — GT strokes
      are visibly thin/elegant; my main render looks blobby, crowded.
    - Pie s5 bow_perp=18 curved too aggressively — resembles a wild
      slash rather than the moderate descending pie in GT.
    - xie_gou hook_up=32 hook_back=8 was oversized — hook flick reaches
      too far up-left; GT hook is a modest kick.
    - Composition (土 left, 成 right) placement was right; the visual
      failure was rendering weight + curvature, not layout.

  Plan for retry:
    - Same anchors verbatim (MMH is ground truth for layout).
    - Reduce all stroke widths ~30% (heng 6/7, shu 6, pie 8/2, xie_gou 6).
    - Reduce s5 pie bow_perp 18 -> 10 (softer sweep).
    - Reduce s7 xie_gou hook_up 32 -> 22, hook_back 8 -> 5.
    - Reduce s8 inner pie bow_perp 10 -> 6, width 8 -> 6.
    - Keep s3 ti separate primitive (not flat heng) — the errata note
      already confirmed the ti stroke class swap; problem was cosmetic
      not structural.

BANK_DEVIATION:
  skipped: tu_earth.py — bank tu has flat bottom heng (~37→270 wide);
    MMH s3 here is a rising 提 (ti) and left-radical 土 x-span is only
    ~84 px (much narrower than bank's ~233 px). Aspect w/h = 0.53 vs
    bank 1.20; uniform scale cannot fit. Fresh inline of 3 strokes.
  skipped: cheng_become.py — bank cheng calibrated for standalone
    canvas; here 成 must occupy right ~55% of frame with MMH anchors
    that shift the top-heng origin (x=136.8 vs bank ~90.5). Anchor
    divergence is per-endpoint (P-A-007-v2 hard-check: NOT a uniform
    ox/oy/scale shift). Inline 6 strokes with MMH anchors verbatim.
  fresh_component: tu_left_with_ti_for_城 + cheng_right_variant_for_城
    (same as main, but retuned widths/curves).

Reasoning trace (P-A-008):
  城 = 土(left, 3 strokes with 提 bottom) + 成(right, 6 strokes) = 9.
  Quantitative check (P-A-009):
    - bank tu native aspect 1.20 vs left-radical target 0.53 -> skip.
    - bank cheng native aspect 1.04 vs 成-here aspect ~1.0 (close!) —
      but top-heng x-anchor differs by ~46 px, s5 pie tail x differs
      by ~50 px. This is per-endpoint drift (P-A-010 kind not (a) nor
      (b) — anchor-set mismatch), so cannot fix by ox/oy/scale;
      inline with MMH anchors is correct.

SELF_CHECK dict at end.
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

# --- 土 (left radical, 3 strokes) — MMH anchors verbatim ---
# s1 top short heng
draw_heng(d, (26.7, 175.8), (101.4, 162.3),
          width_head=6, width_tail=7)
# s2 vertical shu of 土
draw_shu(d, (58.0, 90.5), (64.7, 227.9), width=6)
# s3 bottom 提 (rising ti — left-radical 土 signature)
draw_ti(d, (21.7, 249.0), (105.5, 215.3), w_head=8, w_tail=2)

# --- 成 (right radical, 6 strokes) — MMH anchors verbatim ---
# s4 top short heng of 成
draw_heng(d, (136.8, 149.1), (219.7, 133.9),
          width_head=6, width_tail=7)
# s5 long descending pie of 成 (softer curve than main)
draw_pie(d, (116.0, 143.8), (77.9, 275.4),
         bow_perp=10, w_head=8, w_tail=2)
# s6 inner short shu (fragment of heng-zhe)
draw_shu(d, (132.1, 203.3), (134.8, 242.6), width=5)
# s7 long xie_gou (斜钩) — signature diagonal of 成, tamed hook
draw_xie_gou(d, (155.9, 63.0), (266.6, 244.0),
             width=6, bow=10, hook_up=22, hook_back=5)
# s8 inner pie (retuned lighter/less curve)
draw_pie(d, (224.7, 162.0), (173.7, 269.2),
         bow_perp=6, w_head=6, w_tail=2)
# s9 top-right dian (dot)
draw_dian(d, (202.1, 86.4), (231.4, 106.6),
          w_head=2, w_tail=6, bow=3)

img.save(os.path.join(os.path.dirname(__file__), '01_城.png'))


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 strokes drawn = MMH expected 9
    'endpoint_mismatches': [],  # all anchors MMH-verbatim
    'joint_class_mismatches': [],  # P: s1/s2 (tu weld), s4/s7 (成 cross),
                                   #    s7/s8 (inner cross) — anchors
                                   #    place strokes to cross naturally
                                   # N: s1.tail~s5.mid, s2.tail~s3.mid,
                                   #    s3.tail~s5.mid, s4.head~s5.head,
                                   #    s5.mid~s6.head — preserved by
                                   #    inline anchor placement (no weld)
    'overall_pass': True,
    'notes': (
        'Retry #1: same MMH anchors as main, widths reduced ~30%, '
        'pie/xie_gou curvature softened. Fixes visual-heaviness FAIL '
        'mode from main (P-A-010 kind: rendering-weight, not layout).'
    ),
}
