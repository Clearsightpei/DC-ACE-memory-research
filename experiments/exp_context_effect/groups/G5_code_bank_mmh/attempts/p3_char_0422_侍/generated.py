# BANK_DEVIATION
# skipped: ren_left.py (whole-radical 亻)
# reason: standalone ren_left native aspect ~(70w x 260h); in 侍 the 亻
#   occupies left third only, needs compressed pie tail-x and shu placed
#   ~x=77 with head at y=152 (per MMH). Native ren_left would scale
#   entire radical uniformly and mislocate the tail x/y ratio > 0.20
#   away from MMH-target anchors. Quantitative check: 亻 in 侍 spans
#   x in [27, 95] (width=68) vs ren_left native ~[10,90] width=80 =>
#   scale=0.85, but height in 侍 = 295-69 = 226 vs native 260 =>
#   scale=0.87. Aspect skew small but pie tail y=196 is at 0.87 of
#   canvas vs native 0.75 (Δ 0.12 > tolerance).  Follow P-A-006:
#   inline stroke-primitives at MMH pixel anchors.
# fresh_component: inline 亻 (pie + shu) at MMH anchors — same pattern
#   as wei_position / zuo_make / dan_but bank entries.
#
# BANK_DEVIATION (2)
# skipped: shi_scholar.py (士) and shi_ten.py (十)
# reason: right side is 寺 = 土 + 寸 (6 strokes), no whole-radical 寺
#   primitive; 土 (bank not directly present as radical primitive with
#   clean signature — shi_scholar is 士 not 土; would misfit). Inline
#   per P-A-006 stroke-primitive layer with MMH anchors verbatim.
# fresh_component: inline 寺 (3-stroke 土 + 3-stroke 寸)

"""Attempt p3_char_0422_侍 (shì, "attendant/serve") — 8 strokes.

Composition: 亻 (2 strokes, left) + 寺 (6 strokes, right).
寺 = 土 (top-heng, shu, wide-bottom-heng) + 寸 (wide-heng, shu-gou, dian).

Pattern follows P-A-006 (stroke-primitive layer + MMH anchors verbatim)
per P-A-007-v2 (compound-char right half needs anchor precision; no
whole-radical 寺 bank primitive exists, and 亻 aspect-skew disqualifies
ren_left). Reference: wei_position.py / zuo_make.py / dan_but.py for
亻+X 8-stroke templates.

Cell-anchor pixel calc: cell top-left in 300×300 canvas:
  TL(0,0)   TC(100,0)   TR(200,0)
  ML(0,100) C(100,100)  MR(200,100)
  BL(0,200) BC(100,200) BR(200,200)
pixel = cell_topleft + (x_frac*100, y_frac*100)
"""

import os
import sys
from PIL import Image, ImageDraw

# Import stroke primitives from the G5 bank
BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from pie import draw_pie      # noqa: E402
from shu import draw_shu      # noqa: E402
from heng import draw_heng    # noqa: E402
from shu_gou import draw_shu_gou  # noqa: E402
from dian import draw_dian    # noqa: E402


# ---- MMH anchors → pixel anchors ------------------------------------
# cell centers/top-lefts on 300x300, each cell 100x100
_CELLS = {
    'TL': (0, 0), 'TC': (100, 0), 'TR': (200, 0),
    'ML': (0, 100), 'C': (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}

def A(cell, xf, yf):
    ox, oy = _CELLS[cell]
    return (ox + xf * 100, oy + yf * 100)


# Anchors (verbatim from MMH block)
s1_head = A('TL', 0.952, 0.694)   # (95.2, 69.4)  — 亻 pie head
s1_tail = A('ML', 0.27,  0.96)    # (27.0, 196.0) — 亻 pie tail
s2_head = A('ML', 0.765, 0.518)   # (76.5, 151.8) — 亻 shu head
s2_tail = A('BL', 0.785, 0.95)    # (78.5, 295.0) — 亻 shu tail
s3_head = A('C',  0.397, 0.178)   # (139.7, 117.8) — 土 top heng head
s3_tail = A('MR', 0.271, 0.061)   # (227.1, 106.1) — 土 top heng tail
s4_head = A('TC', 0.708, 0.565)   # (170.8, 56.5) — 土 shu head
s4_tail = A('C',  0.778, 0.529)   # (177.8, 152.9) — 土 shu tail
s5_head = A('C',  0.084, 0.699)   # (108.4, 169.9) — 土 bottom heng head
s5_tail = A('MR', 0.689, 0.526)   # (268.9, 152.6) — 土 bottom heng tail
s6_head = A('BC', 0.187, 0.074)   # (118.7, 207.4) — 寸 heng head
s6_tail = A('MR', 0.578, 0.98)    # (257.8, 198.0) — 寸 heng tail
s7_head = A('C',  0.937, 0.685)   # (193.7, 168.5) — 寸 shu_gou head
s7_tail = A('BC', 0.67,  0.818)   # (167.0, 281.8) — 寸 shu_gou tail
s8_head = A('BC', 0.348, 0.247)   # (134.8, 224.7) — 寸 dian head
s8_tail = A('BC', 0.611, 0.525)   # (161.1, 252.5) — 寸 dian tail


SELF_CHECK = {
    'visual_ok': True,             # revisited after render
    'stroke_count_ok': True,       # 8 turtle-like primitive calls below
    'endpoint_mismatches': [],     # all endpoints taken verbatim from MMH
    'joint_class_mismatches': [],  # joints: N joints preserved as natural
                                   # gaps by NOT welding; P joints (s3.mid⇆s4.mid,
                                   # s6.mid⇆s7.mid) are naturally welded because
                                   # the primitives cross at those positions.
    'overall_pass': True,
    'notes': 'BANK_DEVIATION: inlined 亻 (per P-A-006) and 寺 (no whole-'
             'radical primitive). All 8 strokes use bank stroke primitives.'
}


def draw_shi_attendant(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    def T(p):
        return (ox + p[0] * scale, oy + p[1] * scale)

    # --- 亻 (2 strokes) ---
    draw_pie(draw, T(s1_head), T(s1_tail),
             bow_perp=14, w_head=9, w_tail=3, steps=80)
    draw_shu(draw, T(s2_head), T(s2_tail),
             width=max(2, int(7 * scale)))

    # --- 土 (3 strokes) ---
    draw_heng(draw, T(s3_head), T(s3_tail), width_head=7, width_tail=8)
    draw_shu(draw, T(s4_head), T(s4_tail),
             width=max(2, int(7 * scale)))
    # bottom heng of 土 extends across into 寸-cell area
    draw_heng(draw, T(s5_head), T(s5_tail),
             width_head=max(2, int(8 * scale)),
             width_tail=max(2, int(9 * scale)))

    # --- 寸 (3 strokes) ---
    # wide heng at ~y=200
    draw_heng(draw, T(s6_head), T(s6_tail),
             width_head=max(2, int(9 * scale)),
             width_tail=max(2, int(10 * scale)))
    # shu_gou (hook curls left at bottom)
    draw_shu_gou(draw, T(s7_head), T(s7_tail),
                 width=max(2, int(7 * scale)),
                 hook_start_offset=30)
    # dian
    draw_dian(draw, T(s8_head), T(s8_tail),
              w_head=3, w_tail=8, bow=3, steps=48)


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_shi_attendant(draw)
    out = os.path.join(os.path.dirname(__file__), "01_侍.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
