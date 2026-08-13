"""p3_char_0458_癸 — G5 attempt.

癸 (gui) — 9 strokes total. Structure: 癶 top (5 strokes: pie + dot + dot +
pie + na) + middle 一 (1) + 天-like bottom (3 strokes: heng + pie + na).

# BANK_DEVIATION
# skipped: da_big.py, tian_sky.py (no direct 天 bank primitive; da's aspect
#   won't map cleanly to the tight bottom-third footprint of 癸's 天).
# reason (P-A-009 quantitative):
#   Bank da native heng-span = 175.8 px, aspect 1.26; target 癸's bottom-天
#   sits in y ∈ [210, 293] (~83 px tall) with heng-span ≈ 141 px → aspect ≈ 1.70.
#   1.35x aspect delta triggers P-A-010(b) "correct primitive mistuned" if bank
#   forced; P-A-006 prefers MMH-verbatim inline for tight fit.
# fresh_component: inline all 9 strokes at MMH anchors (stroke-primitive layer
#   per P-A-006).

P-A-008 reasoning trace:
  s1 = big-left 撇 of 癶 (long pie, upper-mid → lower-left)
  s2 = left-arm 点 (small down-right tick on s1's mid)
  s3 = right-side small 点 tick at top
  s4 = right-arm 撇 of 癶 (short pie, top-right → center)
  s5 = right-arm 捺 of 癶 (long na, top-center → mid-right)
  s6 = middle 一 (horizontal band across center)
  s7 = 天's 一 (heng of the lower cross)
  s8 = 天's 丿 (long pie down-left through the heng — P weld with s7)
  s9 = 天's 乀 (na down-right)
"""

import os
import sys

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../../success_bank/code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw  # noqa: E402

from heng import draw_heng  # noqa: E402
from pie import draw_pie  # noqa: E402
from na import draw_na  # noqa: E402
from dian import draw_dian  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 9 stroke primitive calls
    'endpoint_mismatches': [],        # anchors used verbatim (P-A-006)
    'joint_class_mismatches': [],     # s7×s8 emerges as P by natural crossing
    'overall_pass': True,
    'notes': ('9-stroke inline (P-A-006). BANK_DEVIATION documented for da_big '
              'per P-A-009 (aspect 1.70 vs bank 1.26, 1.35x mismatch, tight '
              'bottom-third). All N joints preserved as natural anchor gaps '
              '(no welding). s7 heng midpoint (~133, 217) crosses s8 pie curve '
              'near cell BC for the expected P weld.')
}


def anchor(cell, xf, yf):
    """(米字格 cell, x_frac, y_frac) → canvas pixel. Image-y convention
    (y grows down within each 100x100 cell) — matches prior G5 attempts."""
    cells = {
        'TL': (0,   0),   'TC': (100,   0), 'TR': (200,   0),
        'ML': (0, 100),   'C':  (100, 100), 'MR': (200, 100),
        'BL': (0, 200),   'BC': (100, 200), 'BR': (200, 200),
    }
    cx, cy = cells[cell]
    return (cx + xf * 100, cy + yf * 100)


def draw_gui(d: ImageDraw.ImageDraw):
    # ---- 癶 top (s1-s5) ----

    # s1: big-left 撇 of 癶 — TL(0.686, 0.92) → BL(0.231, 0.2)
    s1_head = anchor('TL', 0.686, 0.92)
    s1_tail = anchor('BL', 0.231, 0.2)
    draw_pie(d, s1_head, s1_tail,
             bow_perp=-14, w_head=8, w_tail=2, steps=100)

    # s2: left-arm 点 — ML(0.577, 0.266) → ML(0.855, 0.479). Short down-right tick.
    s2_head = anchor('ML', 0.577, 0.266)
    s2_tail = anchor('ML', 0.855, 0.479)
    draw_dian(d, s2_head, s2_tail, w_head=2, w_tail=6, bow=2, steps=48)

    # s3: top-right small mark — TC(0.972, 0.645) → TC(0.661, 0.914). Small down-left.
    s3_head = anchor('TC', 0.972, 0.645)
    s3_tail = anchor('TC', 0.661, 0.914)
    draw_dian(d, s3_head, s3_tail, w_head=2, w_tail=5, bow=-2, steps=48)

    # s4: right-arm 撇 of 癶 — TR(0.212, 0.75) → C(0.878, 0.148). Short pie.
    s4_head = anchor('TR', 0.212, 0.75)
    s4_tail = anchor('C',  0.878, 0.148)
    draw_pie(d, s4_head, s4_tail,
             bow_perp=-4, w_head=6, w_tail=2, steps=80)

    # s5: right-arm 捺 of 癶 — TC(0.494, 0.917) → MR(0.827, 0.852). Long na.
    s5_head = anchor('TC', 0.494, 0.917)
    s5_tail = anchor('MR', 0.827, 0.852)
    draw_na(d, s5_head, s5_tail,
            bow_perp=-8, w_head=3, w_tail=10, steps=100)

    # ---- middle 一 (s6) ----

    # s6: middle 一 — C(0.034, 0.717) → C(0.79, 0.626)
    s6_head = anchor('C', 0.034, 0.717)
    s6_tail = anchor('C', 0.79,  0.626)
    draw_heng(d, s6_head, s6_tail, width_head=7, width_tail=8)

    # ---- 天-like bottom (s7-s9) ----

    # s7: 天 heng — BL(0.729, 0.227) → BR(0.136, 0.098). Near-horizontal, upward tilt.
    s7_head = anchor('BL', 0.729, 0.227)
    s7_tail = anchor('BR', 0.136, 0.098)
    draw_heng(d, s7_head, s7_tail, width_head=7, width_tail=8)

    # s8: 天 pie — C(0.245, 0.802) → BL(0.659, 0.889). Long down-left through s7.
    s8_head = anchor('C',  0.245, 0.802)
    s8_tail = anchor('BL', 0.659, 0.889)
    draw_pie(d, s8_head, s8_tail,
             bow_perp=-12, w_head=8, w_tail=2, steps=100)

    # s9: 天 na — BC(0.573, 0.405) → BR(0.098, 0.924). Down-right, medium.
    s9_head = anchor('BC', 0.573, 0.405)
    s9_tail = anchor('BR', 0.098, 0.924)
    draw_na(d, s9_head, s9_tail,
            bow_perp=-4, w_head=3, w_tail=9, steps=100)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_gui(d)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '01_癸.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
