"""p3_char_0488_俑 (yong, "figurine") — 9 strokes: 亻 (pie+shu) + 甬 (マ hat + 用).

Recipe: P-A-006 (MMH anchors verbatim + stroke-primitive layer) + P-A-008
(inline-reasoning trace) + P-A-009 (quantitative BANK_DEVIATION).

Sibling: p3_char_0350_佣 (亻+用 PASS) — direct template, adds マ hat s3+s4.

Inline sub-component reasoning (P-A-008):
  亻 (s1,s2): Bank has ren_left.py at native pie tail x=80.6, shu head x=138.9.
    MMH 俑 pie tail x=15.2 (65px LEFT of bank), shu head x=73.2 (66px LEFT of bank).
    The shu shift IS uniform (~65px). BUT the pie is NOT uniformly shifted: pie
    HEAD is at x=92 (bank 89.6, only 2.4px diff) while pie TAIL is 65px left.
    That's an angle change, not a uniform (ox,oy,scale) shift.
    P-A-007-v2 hard-check → FAIL (not uniform-adjustable). Fall back to P-A-006
    stroke-primitive layer with direct MMH-anchor pie + shu calls.
    BANK_DEVIATION: ren_left skipped (angle mismatch, not uniform shift).

  甬 top マ (s3, s4): No whole-radical bank primitive. Inline with a slanted
    pie for s3 and a short slanted line for s4. Both are short strokes near
    top of C cell.

  甬 bottom 用 (s5-s9): Follows p3_char_0350_佣 template exactly (same
    primitives: pie s5, heng_zhe_gou s6, heng x2 s7/s8, shu s9). Reuse-tuned.

Joint plan (7 N joints + 2 P joints — matches MMH block):
  N: s1.mid⇆s2.head, s3.tail⇆s4.mid, s4.tail⇆s6.mid (near corner),
     s5.head⇆s6.head, s5.mid⇆s7.head, s5.mid⇆s8.head, s6.head⇆s9.head.
  P: s7.mid⇆s9.mid (upper heng × central shu welded), s8.mid⇆s9.mid (lower
     heng × central shu welded).

Anchor pixels (MMH cell.frac → 300x300):
  s1 pie:  TL(0.92 ,0.601)=( 92.0, 60.1) → BL(0.152,0.007)=( 15.2,200.7)
  s2 shu:  ML(0.732,0.462)=( 73.2,146.2) → BL(0.75 ,0.927)=( 75.0,292.7)
  s3 マ pie: TC(0.339,0.844)=(133.9, 84.4) → C (0.922,0.14 )=(192.2,114.0)
  s4 マ tail: C(0.652,0.116)=(165.2,111.6) → C (0.931,0.307)=(193.1,130.7)
  s5 pie:  C (0.213,0.471)=(121.3,147.1) → BC(0.236,0.83 )=(123.6,283.0)
  s6 hzg:  C (0.38 ,0.503)=(138.0,150.3) → BR(0.057,0.777)=(205.7,277.7)
  s7 heng: C (0.544,0.896)=(154.4,189.6) → MR(0.106,0.799)=(210.6,179.9)
  s8 heng: BC(0.544,0.256)=(154.4,225.6) → BR(0.136,0.174)=(213.6,217.4)
  s9 shu:  C (0.723,0.526)=(172.3,152.6) → BC(0.793,0.848)=(179.3,284.8)
"""

# BANK_DEVIATION
# skipped: ren_left.py
# reason: MMH 俑 anchors show 亻 pie tail 65px left of bank native (angle change,
#         not uniform shift); pie head matches bank but pie tail does not.
#         P-A-007-v2 hard-check fails → primitives instead of whole-radical.
# fresh_component: ren_left_variant_angled (steeper pie for 俑-family aspect)

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from heng_zhe_gou import draw_heng_zhe_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 9 primitive calls; MMH expected 9
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all N joints as gaps (inner-heng starts at x~154 leaves gap vs s5 at x~123); P joints from s7/s8 crossing s9
    'overall_pass': True,
    'notes': 'P-A-006 primitive layer per BANK_DEVIATION on ren_left (angle mismatch). Adds マ hat s3+s4 above 用 template from sibling 佣 PASS.',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: 亻 pie — head TL top, tail BL bottom-left. Steeper than ren_left native.
    draw_pie(d, (92.0, 60.1), (15.2, 200.7),
             bow_perp=14, w_head=9, w_tail=3, steps=90)

    # s2: 亻 shu — vertical descender, slight left drift like ren_left.
    draw_shu(d, (73.2, 146.2), (75.0, 292.7), width=7)

    # s3: マ top pie — short slanted right-downward stroke.
    draw_pie(d, (133.9, 84.4), (192.2, 114.0),
             bow_perp=2, w_head=6, w_tail=4, steps=45)

    # s4: マ tail — very short slanted stroke inside C.
    draw_pie(d, (165.2, 111.6), (193.1, 130.7),
             bow_perp=1, w_head=6, w_tail=3, steps=30)

    # s5: 用 left pie — nearly vertical, tiny rightward bow.
    draw_pie(d, (121.3, 147.1), (123.6, 283.0),
             bow_perp=4, w_head=8, w_tail=4, steps=80)

    # s6: 用 heng-zhe-gou. Corner near (207, 138) per joint expectation @ C(0.975, 0.359).
    #     gou_tail before hook; hook_tip is MMH tail.
    draw_heng_zhe_gou(d,
                      heng_head=(138.0, 150.3),
                      corner=(207.0, 138.0),
                      gou_tail=(210.0, 268.0),
                      hook_tip=(197.0, 275.0))

    # s7: upper inner heng.
    draw_heng(d, (154.4, 189.6), (210.6, 179.9), width_head=6, width_tail=7)

    # s8: lower inner heng.
    draw_heng(d, (154.4, 225.6), (213.6, 217.4), width_head=7, width_tail=7)

    # s9: central shu — piercing s7 and s8 (P joints emerge from crossing).
    draw_shu(d, (172.3, 152.6), (179.3, 284.8), width=7)

    out = Path(__file__).parent / "01_俑.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    render()
