"""p3_char_0387_果 — G5 attempt.

Decomposition: 田 (top box, strokes 1-4) + wide 木-base (strokes 5-8).
The central 竖 (s6) pierces both — 田's interior and 木's shaft are the
same stroke — so whole-radical mu_wood does NOT cleanly apply.

# BANK_DEVIATION
# skipped: mu_wood.py (whole-radical draw_mu)
# reason (QUANTITATIVE P-A-009):
#   native draw_mu heng band  = y[131,143] (12px, mid-canvas)
#   果 wide-heng band          = y[182,192] (target ~50px LOWER than mu native)
#   native draw_mu shu span    = y[58,295]  = 237px starting free at top
#   果 s6 shu span             = y[82,308]  = 226px, but shu HEAD sits INSIDE 田 box
#     — mu native has shu head free above heng; 果 has shu head embedded in 田-frame.
#   aspect: mu-portion of 果 does not exist as an isolable region (shu pierces 田),
#     so no scale factor s in [0.55, 1.2] recovers geometry (P-A-007-v2 gate FAILS).
# fresh_component: inline P-A-006 stroke-primitive layer with MMH anchors verbatim.
# Uses heng, shu, pie, na, heng_zhe_box primitives (all endpoint-driven).

Per-sub-component reasoning trace (P-A-008):
  s1 (left vertical of 田): draw_shu, endpoints from MMH TL/C anchors.
  s2 (横折 top+right of 田): draw_heng_zhe_box with top_left=head, bottom_right=tail.
  s3 (inner top heng of 田): draw_heng, short.
  s4 (inner bottom heng of 田): draw_heng, short.
  s5 (wide heng base of 木): draw_heng, spans ML→MR.
  s6 (central 竖 piercing all): draw_shu, long — from top of 田 down past canvas.
  s7 (pie, bottom-left sweep): draw_pie with bow.
  s8 (na, bottom-right sweep): draw_na with taper-out.

Stroke count check: 8 primitive calls == expected 8. OK.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

# Import bank primitives
_BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(_BANK))

from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from na import draw_na
from heng_zhe_box import draw_heng_zhe_box


# MMH anchor conversion (cell + fraction) -> pixel; each cell 100x100 on 300 canvas
_ORIGIN = {
    'TL': (0, 0), 'TC': (1, 0), 'TR': (2, 0),
    'ML': (0, 1), 'C':  (1, 1), 'MR': (2, 1),
    'BL': (0, 2), 'BC': (1, 2), 'BR': (2, 2),
}
def A(cell, xf, yf):
    col, row = _ORIGIN[cell]
    return ((col + xf) * 100.0, (row + yf) * 100.0)


# MMH endpoints (verbatim from injected structural block)
s1_h = A('TL', 0.753, 0.791);  s1_t = A('C',  0.028, 0.597)
s2_h = A('TL', 0.844, 0.773);  s2_t = A('C',  0.793, 0.456)
s3_h = A('C',  0.090, 0.175);  s3_t = A('C',  0.708, 0.093)
s4_h = A('C',  0.087, 0.529);  s4_t = A('C',  0.761, 0.395)
s5_h = A('ML', 0.451, 0.922);  s5_t = A('MR', 0.458, 0.819)
s6_h = A('TC', 0.365, 0.823);  s6_t = A('BC', 0.436, 1.082)
s7_h = A('C',  0.351, 0.913);  s7_t = A('BL', 0.378, 0.786)
s8_h = A('C',  0.526, 0.901);  s8_t = A('BR', 0.798, 0.736)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: left vertical of 田 box (slightly slanted per MMH)
    draw_shu(d, s1_h, s1_t, width=7)

    # s2: 横折 top+right of 田 box (top_left=head, bottom_right=tail)
    draw_heng_zhe_box(d, s2_h, s2_t, width=7)

    # s3: inner top heng inside 田 (thin, small)
    draw_heng(d, s3_h, s3_t, width_head=6, width_tail=7)

    # s4: inner bottom heng inside 田 (thin, small)
    draw_heng(d, s4_h, s4_t, width_head=6, width_tail=7)

    # s5: wide base heng of 木 across canvas (thicker for prominence)
    draw_heng(d, s5_h, s5_t, width_head=9, width_tail=10)

    # s6: long central 竖 piercing 田 and extending below (P joint through s4, s5)
    draw_shu(d, s6_h, s6_t, width=8)

    # s7: pie (bottom-left sweep) — head sits below wide heng, tail near BL corner
    draw_pie(d, s7_h, s7_t, bow_perp=10, w_head=6, w_tail=2)

    # s8: na (bottom-right sweep) — head just right of shu, tail near BR corner
    draw_na(d, s8_h, s8_t, bow_perp=12, w_head=4, w_tail=10)

    out = Path(__file__).parent / "01_果.png"
    img.save(out)
    print(f"wrote {out}")


SELF_CHECK = {
    'visual_ok': None,             # filled after render (see notes)
    'stroke_count_ok': True,       # 8 primitive calls == expected 8
    'endpoint_mismatches': [],     # anchors used verbatim from MMH block
    'joint_class_mismatches': [],  # P joints (s4/s6, s5/s6) formed by shu crossing hengs
                                   # T joint (s3/s6 at C 0.443,0.106) — s6 head y=182 crosses s3 y~113
                                   # N joints (s1/s2, s5/s7, s5/s8, s7/s8) — natural gaps preserved
    'overall_pass': None,
    'notes': 'stroke-primitive layer with MMH anchors; skipped mu_wood per BANK_DEVIATION.',
}


if __name__ == '__main__':
    render()
