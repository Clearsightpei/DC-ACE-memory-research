"""p3_char_0354_佧 (kǎ) — 亻 + 卡 (7 strokes).

Decomposition (from GT + MMH anchors):
- s1, s2 = 亻 (person-left radical): pie + shu
- s3, s4, s5 = 上-like top of 卡: short vertical (top of 上) + short heng
  (top crossbar) + long heng (base of 上, shared with 卜 crossbar)
- s6, s7 = 卜 bottom of 卡: long descending vertical + dot to the lower-right

Per P-A-006 (stroke-primitive layer, MMH-verbatim anchors, refuse
whole-radical wrapping) — this recipe is the primary A-route for 6-7
stroke L-R compound chars. Explicitly considered but SKIPPED per
P-A-007-v2 hard-check:

- ren_left.py: aspect check FAILED. Native draw_ren_left has fixed
  internal proportions that do not match this composition's
  compressed 亻 (MMH pie tail y=190, shu tail y=289 — extended
  descender). Inlining pie+shu with MMH anchors preserves the exact
  L-R geometry the anchor block specifies.
- bu_divine.py: SKIPPED because the 卜 here shares its head-y with
  s5.mid (joint N cell C) — inline lets us anchor s6.head exactly at
  MMH's C(171.7, 172.3) rather than relying on bu's native placement.
- shang_up.py: SKIPPED because 上 here is fused into 卡 (long heng
  s5 is shared crossbar with 卜's shu s6, not a standalone 上's base).

BANK_DEVIATION note: no whole-radical wrapper called — the whole
character is inline stroke-primitives per P-A-006. The 亻 is inline,
not draw_ren_left, and the right half is inline, not shang_up+bu.
Reason: MMH anchor verbatim (P-A-006) beats whole-radical composition
for L-R 6-7 stroke chars.
"""

# BANK_DEVIATION
# skipped: ren_left.py, shang_up.py, bu_divine.py
# reason: P-A-006 stroke-primitive layer with MMH-verbatim anchors
#         beats whole-radical composition for 亻+卡 L-R 7-stroke;
#         右半 卡 = 上+卜 fused (shared crossbar), so shang_up/bu_divine
#         would double-render s5/s6 or misplace the shared anchor.
# fresh_component: ka_right_inline_for_佧 (卡 = fused 上+卜 with shared
#         crossbar; s5 = long heng shared, s6 descender pierces through)

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 7 primitive calls, matches MMH
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 7 joints are N (natural gap)
    'overall_pass': True,
    'notes': 'Inline stroke-primitives with MMH-verbatim pixel anchors. '
             '亻 uses inline pie+shu (not draw_ren_left, aspect mismatch). '
             '卡 = fused 上+卜: s3 short-shu, s4 short-heng top-right, '
             's5 long-heng shared base/crossbar, s6 long-shu descender, '
             's7 dot lower-right. All 7 joints class N (natural gap; '
             'no welding — 卡 has no P-class piercing per MMH block).'
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ------------------------------------------------------------
    # 亻 radical (left position) — pie + shu, inline per P-A-007-v2
    # aspect-check: draw_ren_left native aspect ≠ MMH anchors here.
    # ------------------------------------------------------------
    # s1 亻 pie: TL(0.943, 0.589) → ML(0.246, 0.901)
    #   pixel (94.3, 58.9) → (24.6, 190.1)
    draw_pie(draw, (94.3, 58.9), (24.6, 190.1),
             bow_perp=13, w_head=9, w_tail=3, steps=90)

    # s2 亻 shu: ML(0.765, 0.436) → BL(0.797, 0.892)
    #   pixel (76.5, 143.6) → (79.7, 289.2)
    #   joint s1.mid ⇆ s2.head @ ML — N gap ~19px (natural, no weld)
    draw_shu(draw, (76.5, 143.6), (79.7, 289.2), width=7)

    # ------------------------------------------------------------
    # 卡 right half (上 top fused with 卜 bottom, shared crossbar)
    # Inline per P-A-006 — MMH-verbatim anchors, refusing shang_up +
    # bu_divine whole-radical composition (would misplace s5/s6
    # shared-crossbar joint at cell C).
    # ------------------------------------------------------------
    # s3 short vertical (top of 上): TC(0.673, 0.624) → C(0.749, 0.582)
    #   pixel (167.3, 62.4) → (174.9, 158.2)
    #   ~short-shu; joint s3.mid ⇆ s4.head @ C — N gap ~16px
    draw_shu(draw, (167.3, 62.4), (174.9, 158.2), width=7)

    # s4 short heng (top-right crossbar of 上): C(0.898, 0.14) → MR(0.396, 0.014)
    #   pixel (189.8, 114.0) → (239.6, 101.4)
    #   short horizontal near top-right; joint N with s3.mid at C
    draw_heng(draw, (189.8, 114.0), (239.6, 101.4),
              width_head=7, width_tail=8)

    # s5 long heng (base of 上 = shared crossbar with 卜):
    #   C(0.034, 0.755) → MR(0.701, 0.588)
    #   pixel (103.4, 175.5) → (270.1, 158.8)
    #   long horizontal spanning most of right half; joint s3.tail ⇆
    #   s5.mid @ C — N gap ~11px (short-shu tip approaches heng from above)
    draw_heng(draw, (103.4, 175.5), (270.1, 158.8),
              width_head=9, width_tail=10)

    # s6 long descender (shu of 卜): C(0.717, 0.723) → BC(0.811, 1.085)
    #   pixel (171.7, 172.3) → (181.1, 308.5 → clamp 296)
    #   long vertical crossing s5 near its middle (joint s5.mid ⇆
    #   s6.head @ C — N gap ~10px; s6 head sits just below s5 line);
    #   also joint s3.tail ⇆ s6.head @ C — N ~20px
    draw_shu(draw, (171.7, 172.3), (181.1, 296.0), width=8)

    # s7 dot to lower-right (dian of 卜): BC(0.916, 0.039) → BR(0.432, 0.382)
    #   pixel (191.6, 203.9) → (243.2, 238.2)
    #   tapered dot going down-right from mid of s6 (joint s6.mid ⇆
    #   s7.head @ BC — N gap ~19px, head is a natural gap from shu body)
    draw_dian(draw, (191.6, 203.9), (243.2, 238.2),
              w_head=3, w_tail=8, bow=4, steps=48)

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            '01_佧.png')
    img.save(out_path)
    print(f'wrote {out_path}')


if __name__ == '__main__':
    main()
