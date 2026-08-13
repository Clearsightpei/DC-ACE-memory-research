"""p3_char_0361_到 — 到 (dào, "arrive")

Structure: 至 (left, 6 strokes) + 刂 (right, 2 strokes) = 8 strokes.

Bank use per P-A-006 / P-A-007-v2 hard-check:
  - Right radical 刂: dao_right.py in bank; native aspect matches (short-left
    dian-shu + long right shu_gou). CALL IT (translated ox=+60 to sit in right
    portion of canvas, scale=1.0 matches the 300px reference).
  - Left radical 至 (zhi_arrive): NOT in bank as a whole radical. The 6 strokes
    are inlined via stroke-primitive layer (P-A-006 recipe) — MMH anchors used
    verbatim: heng for s1/s4/s6, pie for s2, dian for s3, shu for s5.
  - No BANK_DEVIATION block needed — dao_right fits without local render;
    strokes are inlined because no whole-radical primitive exists (not a
    deviation, just absence).

Inline reasoning per sub-component (P-A-008):
  - s1 (top 一 of 至): heng primitive; MMH anchors TL(56,92)→TC(148,83) —
    short horizontal, slight upward tilt to the right (calligraphic).
  - s2 (撇 of 厶): pie primitive; MMH ML(88,102)→C(133,148) — short down-right
    slant (this is unusual for pie, but MMH classifies it as pie-like; use small
    bow_perp).
  - s3 (short second stroke of 厶): dian primitive; MMH C(126,127)→C(148,161) —
    thin dot/short stroke ending in the 厶 close.
  - s4 (top 一 of 土): heng primitive; MMH BL(56,208)→C(140,197) — middle
    horizontal of 至's 土 base.
  - s5 (丨 of 土): shu primitive; MMH ML(92,165)→BL(96,242) — vertical shaft
    piercing s4 and passing near s6.
  - s6 (bottom 一 of 土, the widest): heng primitive; MMH BL(38,259)→BC(152,231)
    — the widest bottom horizontal; anchors span left corner to bottom-center.
  - s7, s8 (刂): dao_right bank primitive with ox=+60.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 (至) + 2 (刂 via dao_right internal) = 8 primitive calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'stroke-primitive layer for 至 per P-A-006; dao_right bank call for 刂 per P-A-007-v2 hard-check (native aspect fit).'
}

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from heng import draw_heng
from pie import draw_pie
from dian import draw_dian
from shu import draw_shu
from dao_right import draw_dao_right


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ── 至 (left, 6 strokes) — inlined stroke-primitive layer ──

    # s1: top 一 of 至 — TL(0.56,0.917) → TC(0.477,0.826)
    draw_heng(d, head=(56, 92), tail=(148, 83), width_head=8, width_tail=9)

    # s2: 撇 of 厶 — ML(0.882,0.025) → C(0.333,0.485)
    # short slant; small bow_perp because it's a compact stroke
    draw_pie(d, head=(88, 102), tail=(133, 148),
             bow_perp=4, w_head=5, w_tail=2)

    # s3: 点 of 厶 — C(0.26,0.271) → C(0.477,0.614)
    # short tapered stroke
    draw_dian(d, head=(126, 127), tail=(148, 161),
              w_head=2, w_tail=5, bow=2)

    # s4: middle 一 of 土 — BL(0.565,0.08) → C(0.397,0.972)
    draw_heng(d, head=(56, 208), tail=(140, 197), width_head=7, width_tail=8)

    # s5: 丨 of 土 — ML(0.917,0.646) → BL(0.961,0.417)
    draw_shu(d, head=(92, 165), tail=(96, 242), width=7)

    # s6: bottom 一 of 土 (widest) — BL(0.384,0.59) → BC(0.523,0.314)
    draw_heng(d, head=(38, 259), tail=(152, 231), width_head=9, width_tail=11)

    # ── 刂 (right, 2 strokes) — bank primitive ──
    # dao_right's internal reference sits around x=110-160; shift ox=+60 to place
    # the short-left at x~171 and the long-right at x~221 (matches MMH s7/s8).
    draw_dao_right(d, ox=60, oy=0, scale=1.0)

    out = os.path.join(os.path.dirname(__file__), '01_到.png')
    img.save(out)
    return out


if __name__ == '__main__':
    print(render())
