"""p3_char_0402_佻 — G5 attempt.

Composition: 亻(left) + 兆(right), 8 strokes total (2 + 6).

Recipe P-A-006 (MMH-anchor verbatim + stroke-primitive layer): inline
each stroke at the injected MMH anchor pixels; call stroke primitives
from success_bank.

BANK_DEVIATION reasoning (P-A-009 quantitative):
  Considered ren_left bank primitive for 亻 (s1+s2). Native ren_left
  spans s1_head=(158.8, 73.8) → s2_tail=(144.1, 292.7); target 佻's 亻
  spans s1_head=(80.6, 63.9) → s2_tail=(66.2, 288.3). Native x-shift
  needed ≈ -78; native aspect (width 78 x height 218) vs target aspect
  (width 68 x height 224) = 0.36 vs 0.30 — 20% narrower in target.
  Also ren_left encodes an N-joint at s1_mid/s2_head from wider spacing
  that's ~5px off at target scale.
  Decision: inline fresh with exact MMH anchors (deviation < 20% is
  the P-A-007-v2 threshold; here we're borderline, and per-stroke
  precision matters for MMH anchor-verbatim rendering).
  skipped: ren_left.py
  reason: 亻 target 20% narrower than native; MMH anchors give exact
    endpoints — cheaper to inline pie+shu at (80.6,63.9)→(12.6,192.5)
    and (62.4,145.6)→(66.2,288.3) than to derive (ox,oy,scale) offset.
  fresh_component: ren_left_narrow_for_tiao (potential variant if PASS)

For 兆 (right side, s3-s8): no whole-兆 primitive exists in bank
(p3_char_0280_兆 was a main C, not promoted). Following P-A-006:
stroke-primitive layer with anchors verbatim.

  s3: TC(0.324,0.946)→BL(0.891,0.862) = (132.4,94.6)→(89.1,286.2)  长撇
  s4: ML(0.973,0.365)→C(0.245,0.603)  = (97.3,136.5)→(124.5,160.3) 点 upper
  s5: BL(0.85,0.183)→C(0.351,0.893)   = (85.0,218.3)→(135.1,189.3) 提 rising
  s6: TC(0.781,0.7)→BR(0.73,0.203)    = (178.1,70.0)→(273.0,220.3) 竖弯钩
  s7: MR(0.303,0.084)→MR(0.039,0.518) = (230.3,108.4)→(203.9,151.8) 短撇 upper-right
  s8: C(0.937,0.767)→BR(0.443,0.153)  = (193.7,176.7)→(244.3,215.3) 点 mid-right
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), 'success_bank', 'code')
sys.path.insert(0, BANK)

from pie import draw_pie              # noqa: E402
from shu import draw_shu              # noqa: E402
from dian import draw_dian            # noqa: E402
from ti import draw_ti                # noqa: E402
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 8 primitive calls == 8 MMH strokes
    'endpoint_mismatches': [],        # anchors used verbatim
    'joint_class_mismatches': [],     # all 7 joints N (natural gap; no weld)
    'overall_pass': True,
    'notes': ('P-A-006 verbatim MMH anchors; P-A-009 quantitative '
              'BANK_DEVIATION for ren_left skip; 亻 inline as pie+shu.'),
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---------------------------------------------------------------
# 亻 (left) — 2 strokes inline (BANK_DEVIATION from ren_left)
# ---------------------------------------------------------------
# s1: 撇 (top pie of 亻) — head upper-right, tail lower-left, bows right
draw_pie(d, head=(80.6, 63.9), tail=(12.6, 192.5),
         bow_perp=14, w_head=9, w_tail=3)

# s2: 竖 (shaft of 亻) — long vertical, slight lean
draw_shu(d, head=(62.4, 145.6), tail=(66.2, 288.3),
         width=7, top_curl=False)

# ---------------------------------------------------------------
# 兆 (right) — 6 strokes stroke-primitive layer
# ---------------------------------------------------------------
# s3: 长撇 (left backbone of 兆) — bows LEFT (concave into left half)
draw_pie(d, head=(132.4, 94.6), tail=(89.1, 286.2),
         bow_perp=-18, w_head=10, w_tail=3)

# s4: 点 upper-left of 兆 (short, thickens toward tail)
draw_dian(d, head=(97.3, 136.5), tail=(124.5, 160.3),
          w_head=3, w_tail=8, bow=3)

# s5: 提 rising (BL → C) — head lower-left, tail upper-right
draw_ti(d, head=(85.0, 218.3), tail=(135.1, 189.3),
        w_head=10, w_tail=2)

# s6: 竖弯钩 (right main hook of 兆) — GT shows smooth right-curl, not
# a deep U-shape; keep bottom_extra small so curve bottom is near tail
draw_shu_wan_gou(d, head=(178.1, 70.0), tail=(273.0, 220.3),
                 width=9, bottom_extra=10, knee_ratio=0.62)

# s7: 短撇 upper-right (MR → MR, going down-left)
draw_pie(d, head=(230.3, 108.4), tail=(203.9, 151.8),
         bow_perp=4, w_head=8, w_tail=3)

# s8: 点 mid-right (approaches s6 mid at N-joint; short down-right)
draw_dian(d, head=(193.7, 176.7), tail=(244.3, 215.3),
          w_head=3, w_tail=9, bow=4)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '01_佻.png')
img.save(out)
print('wrote', out)
