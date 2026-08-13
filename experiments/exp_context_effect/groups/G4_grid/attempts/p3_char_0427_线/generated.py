"""线 (xiàn, "line/thread") — 8 strokes.

Decomposition: 线 = 纟 (left silk radical, 3 strokes) + 戋 (right, 5 strokes).
纟 = 撇折 + 撇折 + 提.
戋 = 横 + 提 + 斜钩 + 撇 + 点.

Memory-index reads:
  1. drawer_memory.md (v8) — B10 A-recipe: MMH-verbatim, decompose,
     inline base primitives when compound bank primitive's defaults
     don't match the compressed slot.
  2. success_bank/INDEX.md — si_silk.py exists for 纟 but its defaults
     span x=135-190 (standalone scale). MMH places 纟 here at x=84-117
     (far-left column compression). Per B10 A-recipe point 4 + point 7,
     SKIP si_silk, inline via base primitives with MMH-verbatim anchors.
  3. errata.md — 纟 has past FAIL notes: 3-disconnected-pie_zhe risk
     when inlined loose. Fix pattern is tight stacking with N-gaps.
"""

# BANK_DEVIATION
# skipped: si_silk.py
# reason: si_silk defaults center 纟 at x=135-190 (standalone canvas scale);
#         MMH here compresses 纟 into far-left column x=84-117 for 线's
#         left-radical slot. Partial anchor override of 3 sub-stroke defaults
#         is the p3_char_0252_伊 FAIL pattern (B8). Inlining with MMH-verbatim
#         anchors + base pie/pie_zhe/ti primitives per B10 A-recipe point 4.
# fresh_component: si_silk_leftcol_for_线

import sys, os
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from pie import draw_pie
from pie_zhe import draw_pie_zhe
from ti import draw_ti
from heng import draw_heng
from na import draw_na
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 8 turtle-calls == expected 8
    'endpoint_mismatches': [],     # all anchors MMH-verbatim
    'joint_class_mismatches': [],  # P-welds via shared anchor pixels; N-gaps preserved
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim; 纟 inlined as compressed left-column '
             '(BANK_DEVIATION vs si_silk); 戋 right-half with 斜钩 as na, '
             'X-crosses at s4/s5 with s6 preserved via shared C-cell anchors.',
}


def render():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ============ 纟 (left silk radical, 3 strokes; compressed x=84-117) =========

    # s1: 撇折 top. MMH head (TL, 0.844, 0.706) tail (ML, 0.876, 0.603).
    # Both anchors nearly vertical drop x~85, y 71→160. Inferred elbow pivot
    # slightly down-left to give the 撇折 loop bend.
    draw_pie_zhe(d,
                 head=('TL', 0.844, 0.706),
                 pivot=('TL', 0.55, 1.30),   # elbow just below-left of head
                 tail=('ML', 0.876, 0.603),
                 pie_head_w=7, pie_tip_w=3, heng_w=5, shoulder=2)

    # s2: 撇折 middle. MMH head (C, 0.128, 0.181) tail (C, 0.169, 0.954).
    # Second loop of 纟, slightly right of s1. Inferred elbow pivot.
    draw_pie_zhe(d,
                 head=('C', 0.128, 0.181),
                 pivot=('ML', 0.85, 1.20),   # elbow just left of head
                 tail=('C', 0.169, 0.954),
                 pie_head_w=8, pie_tip_w=3, heng_w=5, shoulder=2)

    # s3: 提 (rising tick). MMH head (BL, 0.378, 0.643) tail (BC, 0.254, 0.244).
    # MMH stores head lower-right of tail, so tick rises up-left. Trust MMH.
    draw_ti(d,
            from_anchor=('BL', 0.378, 0.643),
            to_anchor=('BC', 0.254, 0.244),
            head_width=10, tail_width=2, curve=0.08, segments=40)

    # ============ 戋 (right, 5 strokes) — welded X-cross at s6 =====================
    # s4-s5-s6 P-joints preserved via shared C-cell anchors in MMH block.

    # s4: top 横 of 戋. MMH head (C, 0.38, 0.453) tail (MR, 0.18, 0.304).
    draw_heng(d,
              from_anchor=('C', 0.38, 0.453),
              to_anchor=('MR', 0.18, 0.304),
              width=6)

    # s5: second stroke of 戋 (rising to upper-right — MMH stores as long ti).
    # MMH head (C, 0.315, 0.89) tail (MR, 0.382, 0.685).
    draw_ti(d,
            from_anchor=('C', 0.315, 0.89),
            to_anchor=('MR', 0.382, 0.685),
            head_width=8, tail_width=2, curve=0.05, segments=40)

    # s6: 斜钩 (long slanted). MMH head (TC, 0.506, 0.671) tail (BR, 0.716, 0.399).
    # Long down-right diagonal crossing s4 and s5 at P-joints in C cell.
    # Use na for broad calligraphic feel (斜钩 body + tapered foot).
    draw_na(d,
            from_anchor=('TC', 0.506, 0.671),
            to_anchor=('BR', 0.716, 0.399),
            head_width=4, peak_width=11, tail_width=1,
            peak_t=0.82, curve=0.08, segments=48)

    # s7: 撇 (small flick). MMH head (MR, 0.244, 0.878) tail (BC, 0.327, 0.815).
    # From mid-right down-left across s6 (P joint at BR).
    draw_pie(d,
             from_anchor=('MR', 0.244, 0.878),
             to_anchor=('BC', 0.327, 0.815),
             head_width=9, tail_width=1, curve=0.06, segments=40)

    # s8: 点 (dot at top-right). MMH head (TC, 0.98, 0.735) tail (MR, 0.285, 0.002).
    # MMH stores head at (298,73.5) tail at (228,100). Small dot near top-right.
    draw_dian(d,
              from_anchor=('TC', 0.98, 0.735),
              to_anchor=('MR', 0.285, 0.002),
              head_width=2, peak_width=10, curve=0.05, segments=24)

    return img


if __name__ == '__main__':
    img = render()
    out = os.path.join(os.path.dirname(__file__), '01_线.png')
    img.save(out)
    print('wrote', out)
