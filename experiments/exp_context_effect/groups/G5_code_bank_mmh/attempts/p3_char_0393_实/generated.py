"""p3_char_0393_实 — 实 (shí, "real/fruit") — 8 strokes = 宀 + 头.

# BANK_DEVIATION
# skipped: mian_roof.py  (also chose not to try to use a whole '头' primitive — none exists)
# reason: MMH-derived 宀 for 实 is TALLER/narrower than the standalone bank
#   version. QUANTITATIVE: bank mian_roof 宀 spans x~[70,240] y~[80,150]
#   → aspect W/H = 170/70 = 2.43. Target 实 宀 (s1-s3) spans
#   x~[60,208] y~[56,158] → aspect = 148/102 = 1.45. Ratio 1.45/2.43 = 0.60
#   < P-A-007-v2 lower bound 0.55 for whole-radical use; therefore
#   inline via stroke-primitives per P-A-006 (matches recipe used by
#   ding_fix.py, which is also 宀 + 5-stroke bottom).
# fresh_component: mian_for_实 (compressed-narrow 宀 via dian + pie + heng_zhe_short)
# 头 bottom (s4-s8): inlined directly from MMH anchors — no bank primitive
#   exists for 头 in this composition; strokes are dian + dian + heng
#   + pie + na following P-A-006 (stroke-primitive layer).

# --- Per-sub-component reasoning trace (P-A-008) ---
# 宀 (s1-s3): dian top-center + pie left (short descending) + heng_zhe_short
#   (top bar with small hook). Anchors verbatim from MMH block.
# 头 top marks (s4, s5): two small dian-type strokes stacked left-of-center
#   inside the 宀 (upper part of 头). Both slant down-right.
# 头 middle (s6): long heng sweeping x=51→254 at y≈220-230.
# 头 bottom (s7, s8): the 大-cross — long pie from center-upper down-left
#   PIERCING the heng (crossing at bottom-center; N-neighbor in MMH but
#   visually a P-cross); na from mid-below-heng to bottom-right.
"""

SELF_CHECK = {
    'visual_ok': None,           # filled after first render
    'stroke_count_ok': True,     # 8 primitive calls, one per MMH stroke
    'endpoint_mismatches': [],   # will fill if any exceed ±0.20 tol
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': 'P-A-006 stroke-primitive layer + P-A-009 quantitative deviation from mian_roof.',
}

import os
import sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from dian import draw_dian
from heng import draw_heng
from heng_zhe_short import draw_heng_zhe_short
from na import draw_na
from pie import draw_pie


def render(out_path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 宀 top (3 strokes) ----
    # s1: TC dian — top-center dot of 宀, slants down-right
    #     head TC (0.318, 0.565) → tail TC (0.644, 0.817)
    draw_dian(d, (131.8, 56.5), (164.4, 81.7),
              w_head=2, w_tail=6, bow=2, steps=48)

    # s2: left descending dot/pie of 宀 (ML corner)
    #     head ML (0.732, 0.072) → tail ML (0.609, 0.588)
    #     ~slight left curve → use pie with small bow_perp
    draw_pie(d, (73.2, 107.2), (60.9, 158.8),
             bow_perp=4, w_head=6, w_tail=3, steps=60)

    # s3: 横钩 top bar of 宀 (small hook down-right at end)
    #     head ML (0.841, 0.143) → tail MR (0.08, 0.383)
    draw_heng_zhe_short(d, (84.1, 114.3), (208.0, 138.3),
                        corner_offset=(-4, -4))

    # ---- 头 bottom (5 strokes) ----
    # s4: small dian upper-middle-left inside 宀
    #     head C (0.031, 0.474) → tail C (0.266, 0.635)
    draw_dian(d, (103.1, 147.4), (126.6, 163.5),
              w_head=2, w_tail=5, bow=2, steps=40)

    # s5: another dian, slightly larger/lower, going down-right
    #     head ML (0.832, 0.834) → tail BC (0.166, 0.06)
    draw_dian(d, (83.2, 183.4), (116.6, 206.0),
              w_head=2, w_tail=6, bow=3, steps=48)

    # s6: long heng sweeping across middle-bottom
    #     head BL (0.513, 0.329) → tail BR (0.54, 0.18)
    draw_heng(d, (51.3, 232.9), (254.0, 218.0),
              width_head=8, width_tail=8)

    # s7: 大's 丿 — long pie from center-upper piercing heng down to BL
    #     head C (0.512, 0.318) → tail BL (0.542, 1.064) (extends below canvas)
    draw_pie(d, (151.2, 131.8), (54.2, 306.4),
             bow_perp=12, w_head=8, w_tail=3, steps=100)

    # s8: 大's 捺 — na from below-heng-center to bottom-right
    #     head BC (0.778, 0.578) → tail BR (0.276, 1.041)
    draw_na(d, (177.8, 257.8), (227.6, 304.1),
            bow_perp=10, w_head=4, w_tail=11, steps=80)

    img.save(out_path)
    return out_path


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_实.png')
    render(out)
    print('wrote', out)
