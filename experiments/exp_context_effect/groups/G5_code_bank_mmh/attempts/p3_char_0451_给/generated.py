"""p3_char_0451_给 — G5 attempt.

给 = 纟 (left, 3 strokes) + 合 (right, 6 strokes) = 9 strokes total.

# BANK_DEVIATION
# skipped: he_together.py  (bank primitive for 合)
# reason (P-A-009 quantitative): native 合 bank aspect (width/height)
#        = (290.9 - 22.3) / (299.0 - 66.2) = 268.6 / 232.8 = 1.154.
#        Target 合 inside 给 aspect (from MMH anchors s4-s9):
#        = (292.1 - 124.5) / (293.3 - 68.6) = 167.6 / 224.7 = 0.746.
#        Δ = 0.408 (35% relative) — anisotropic scaling required.
#        Native 合 spans nearly full canvas width; here 合 is squeezed
#        into the right ~55% of canvas to share space with 纟.
# fresh_component: he_together_narrow_for_left_right_split
#        (inline via same 6 stroke primitives as he_together but with
#         MMH-derived per-endpoint anchors — P-A-006 stroke-primitive layer)
#
# 纟 has no whole-radical bank entry (retry-failed in B3, not promoted).
# Inline via 2× pie_zhe + 1× ti stroke primitives from MMH anchors
# (standard route for silk radical — see drawer_memory.md 纟 note).

Reasoning trace (P-A-008):
  Decomposition: 纟(3) + 合(6) = 9 strokes matches MMH count.
  Whole-radical hard-check (P-A-007-v2): 纟 not in bank; 合 in bank but
    quantitatively fails aspect check by 35%. Both go inline via
    stroke-primitive layer (P-A-006).
  Joint expectations: all 9 joints are N-class (neighbor gap) —
    no welding needed. MMH anchors already carry the natural gaps.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw

from pie_zhe import draw_pie_zhe
from ti import draw_ti
from pie import draw_pie
from na import draw_na
from heng import draw_heng
from shu import draw_shu
from heng_zhe_box import draw_heng_zhe_box

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 primitives, matches MMH
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Inline both halves via stroke primitives; BANK_DEVIATION on 合 (aspect 1.15 → 0.75).'
}


def draw_gei(draw: ImageDraw.ImageDraw):
    # ---- 纟 (left, 3 strokes) ----
    # s1: pie_zhe — head (78.2, 70.6) → tail (85.0, 158.2)
    #     corner bulges left of the pie leg for calligraphic sweep.
    draw_pie_zhe(draw,
                 head=(78.2, 70.6),
                 corner=(55.0, 135.0),
                 tail=(85.0, 158.2),
                 pie_bow=6, zhe_bow=1,
                 w_head=5, w_corner=5, w_tail=4)

    # s2: pie_zhe — head (107.5, 114.6) → tail (108.7, 194.2)
    draw_pie_zhe(draw,
                 head=(107.5, 114.6),
                 corner=(78.0, 175.0),
                 tail=(108.7, 194.2),
                 pie_bow=6, zhe_bow=1,
                 w_head=5, w_corner=5, w_tail=4)

    # s3: ti — head (31.9, 261.3) → tail (118.9, 223.5)
    draw_ti(draw,
            head=(31.9, 261.3),
            tail=(118.9, 223.5),
            w_head=8, w_tail=2)

    # ---- 合 (right, 6 strokes, inline per P-A-006 + BANK_DEVIATION) ----
    # s4: 人-pie — head (170.5, 68.6) → tail (124.5, 199.5)
    draw_pie(draw,
             head=(170.5, 68.6),
             tail=(124.5, 199.5),
             bow_perp=13, w_head=10, w_tail=3)

    # s5: 人-na — head (187.5, 108.1) → tail (292.1, 186.3)
    draw_na(draw,
            head=(187.5, 108.1),
            tail=(292.1, 186.3),
            bow_perp=12, w_head=4, w_tail=11)

    # s6: middle heng — head (146.5, 188.1) → tail (211.2, 178.4)
    draw_heng(draw,
              head=(146.5, 188.1),
              tail=(211.2, 178.4),
              width_head=6, width_tail=7)

    # s7: 口 left shu — head (131.8, 220.6) → tail (153.5, 293.3)
    #     (slight lean — inline as line with slight taper since shu
    #      primitive expects nearly-vertical; use a manual line here)
    draw.line([(131.8, 220.6), (153.5, 293.3)], fill='black', width=7)

    # s8: 口 heng_zhe_box — top_left (147.9, 221.8), bottom_right (207.1, 257.2)
    draw_heng_zhe_box(draw,
                      top_left=(147.9, 221.8),
                      bottom_right=(207.1, 257.2),
                      width=7)

    # s9: 口 bottom heng — head (158.2, 271.6) → tail (226.8, 268.4)
    draw_heng(draw,
              head=(158.2, 271.6),
              tail=(226.8, 268.4),
              width_head=7, width_tail=8)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_gei(d)
    out = os.path.join(os.path.dirname(__file__), '01_给.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
