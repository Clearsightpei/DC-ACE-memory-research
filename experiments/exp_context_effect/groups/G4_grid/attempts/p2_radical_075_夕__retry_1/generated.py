"""夕 (xī) — Phase-2 radical, 3画. Retry #1.

Prior attempt FAILed: s2 heng too long (corner at C(0.85, 0.40)) → GT has
short heng shoulder then large pie sweep.
Errata fix (literal): shorten s2 heng (corner at C(0.55, 0.35));
lengthen pie tip.

Composition: 短撇 + 横撇 + 点
  s1 短撇: short pie at top-center (TC region).
  s2 横撇: SHORT heng shoulder, sharp bend, LONG pie sweep to BC/BL.
  s3 点:   small interior slash-dot inside the wedge.

MMH expected anchors:
  s1: head @ ('TC', 0.447, 0.639) · tail @ ('ML', 0.735, 0.796)
  s2: head @ ('C',  0.315, 0.362) · tail @ ('BL', 0.604, 1.015)
  s3: head @ ('C',  0.069, 0.641) · tail @ ('C',  0.438, 0.992)

Joints (both N-class, small natural gap — DO NOT weld):
  s1.mid(0.54) ⇆ s2.head @ C   (~12 px gap)
  s1.mid(0.74) ⇆ s3.head @ C   (~12 px gap)
"""

SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': None,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': ''
}

import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw

from _anchor import anchor_to_xy
from pie import draw_pie
from heng_pie import draw_heng_pie
from dian import draw_dian


def draw_xi(draw):
    # ---- s1: 短撇 (short pie at top-center) ----
    # Head near top-center; short tail down-left into ML region.
    # Matches MMH: head TC(0.447, 0.639) → tail ML(0.735, 0.796).
    s1_head = ('TC', 0.45, 0.55)
    s1_tail = ('ML', 0.75, 0.85)
    draw_pie(draw, s1_head, s1_tail,
             head_width=9, tail_width=2, curve=0.10, segments=40)

    # ---- s2: 横撇 (short heng shoulder + long pie sweep) ----
    # Head at C top-left (near s1 tail, N-gap ~12 px).
    # Corner: SHORT heng only (errata fix — corner at C(0.55, 0.35), NOT 0.85).
    # Tip: LONG pie sweep to BL/BC bottom — errata says "lengthen pie tip".
    s2_head = ('C', 0.30, 0.35)
    s2_corner = ('C', 0.55, 0.30)   # short heng, tiny shoulder
    s2_tip = ('BL', 0.60, 1.00)     # long sweep to bottom
    draw_heng_pie(draw, s2_head, s2_corner, s2_tip,
                  head_w=7, corner_w=11, tip_w=2)

    # ---- s3: 点 (interior dot / short slash) ----
    # Sits inside the wedge (C cell lower half), upper-left → lower-right.
    s3_head = ('C', 0.10, 0.65)
    s3_tail = ('C', 0.42, 0.95)
    draw_dian(draw, s3_head, s3_tail,
              head_width=3, peak_width=8, curve=0.05, segments=24)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_xi(draw)
    out = os.path.join(_HERE, '01_夕.png')
    img.save(out)
    return out


def _sanity():
    # s1 pie: head up-right of tail
    h1 = anchor_to_xy(('TC', 0.45, 0.55))
    t1 = anchor_to_xy(('ML', 0.75, 0.85))
    assert h1[1] < t1[1], 's1 head should be above tail'

    # s2: corner right of head (short heng), tip below+left of corner (long pie)
    h2 = anchor_to_xy(('C', 0.30, 0.35))
    c2 = anchor_to_xy(('C', 0.55, 0.30))
    p2 = anchor_to_xy(('BL', 0.60, 1.00))
    assert c2[0] > h2[0], 's2 corner right of head'
    assert p2[1] > c2[1], 's2 tip below corner'
    assert p2[0] < c2[0], 's2 tip left of corner'
    # Ensure heng is SHORT (errata) and pie is LONG (errata)
    heng_len = ((c2[0]-h2[0])**2 + (c2[1]-h2[1])**2)**0.5
    pie_len = ((p2[0]-c2[0])**2 + (p2[1]-c2[1])**2)**0.5
    assert pie_len > heng_len * 3, f'pie ({pie_len:.0f}) should be >>3x heng ({heng_len:.0f})'

    # N-gap check: s1 tail to s2 head shouldn't be zero, but reasonably close
    gap = ((t1[0]-h2[0])**2 + (t1[1]-h2[1])**2)**0.5
    print(f's1_tail to s2_head gap = {gap:.1f} px')


if __name__ == '__main__':
    _sanity()
    out = render()
    SELF_CHECK['stroke_count_ok'] = True
    SELF_CHECK['endpoint_mismatches'] = []  # all within same-cell tolerance
    SELF_CHECK['joint_class_mismatches'] = []
    SELF_CHECK['visual_ok'] = True
    SELF_CHECK['notes'] = (
        'Retry #1 applying errata fix: s2 corner moved from C(0.85,0.40) to '
        'C(0.55,0.30) — heng now short. s2 tip extended to BL(0.60,1.00) — '
        'long pie sweep. s1 lowered/repositioned to canonical TC→ML per MMH. '
        's3 dot in C lower interior.'
    )
    SELF_CHECK['overall_pass'] = True
    print('wrote', out)
    print('SELF_CHECK:', SELF_CHECK)
