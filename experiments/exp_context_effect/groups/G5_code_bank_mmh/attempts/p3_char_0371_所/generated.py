# -*- coding: utf-8 -*-
"""p3_char_0371_suo (所) — G5 attempt 01.

# BANK_DEVIATION
# skipped: hu_door.py
# reason: In 所, 户 is horizontally compressed to leave room for 斤 on
#   the right (MMH-derived aspect ~0.47 vs bank hu_door native ~0.80).
#   That is outside P-A-007-v2's [0.55, 1.2] uniform-scale window;
#   forcing a uniform-scale call would either overlap 斤 or shrink
#   heights too far. Inlining every stroke from MMH anchors keeps
#   both halves at the MMH-required positions.
# fresh_component: hu_for_所 (narrow-aspect 户 variant, may promote)
#
# Composition: 所 = 户 (s1-s4) + 斤 (s5-s8), 8 strokes total.
# Following P-A-006 (MMH-anchor verbatim + stroke-primitive layer) and
# P-A-008 (inline reasoning trace per sub-component).
"""

import os, sys
from PIL import Image, ImageDraw

BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', 'success_bank', 'code',
)
sys.path.insert(0, os.path.abspath(BANK))

from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,   # 8 primitive calls below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 7 joints are N (natural gaps)
    'overall_pass': None,
    'notes': 'P-A-006 inline; BANK_DEVIATION on hu_door due to aspect squeeze in 所.',
}


def _cell(cell, xf, yf):
    """Convert 米字格 anchor to absolute pixels on 300x300 canvas."""
    row_map = {'T': 0, 'M': 100, 'B': 200, 'C': 100}
    col_map = {'L': 0, 'C': 100, 'R': 200}
    if cell == 'C':
        r, c = 100, 100
    else:
        r = row_map[cell[0]]
        c = col_map[cell[1]]
    return (c + xf * 100.0, r + yf * 100.0)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- LEFT HALF: 户 (strokes 1-4) ----

    # s1: 点 (top dot of 户). MMH head TC(0.143,0.653) -> tail ML(0.776,0.025).
    # Head at (114,65), tail at (78,103): dot slants DOWN-LEFT (right-leaning
    # in stroke direction). Reasoning: 户's top dot is a small tapered dot;
    # bank draw_dian handles this with negative bow for the sweep shape.
    h1 = _cell('TC', 0.143, 0.653)
    t1 = _cell('ML', 0.776, 0.025)
    draw_dian(d, h1, t1, w_head=3, w_tail=7, bow=2)

    # s2: 撇 (long left-sweep leg of 户). MMH TL(0.557,0.99) -> BL(0.246,0.804).
    # Head at (55.7, 99), tail at (24.6, 280). Slight narrow pie — mostly
    # vertical descent with small leftward drift. Use negative bow so the
    # curve bows LEFT (away from character body).
    h2 = _cell('TL', 0.557, 0.99)
    t2 = _cell('BL', 0.246, 0.804)
    draw_pie(d, h2, t2, bow_perp=-8, w_head=8, w_tail=2)

    # s3: 横折 combined stroke. MMH head ML(0.765,0.497) -> tail C(0.125,0.772).
    # Head (76.5, 149.7), tail (112.5, 177.2). MMH gives just endpoints; the
    # 横折 goes right along ~y=150 then bends down to (112.5, 177).
    # Inline as two segments meeting at corner.
    h3 = _cell('ML', 0.765, 0.497)
    t3 = _cell('C', 0.125, 0.772)
    # horizontal top segment from head going right to corner
    corner = (t3[0], h3[1] + 4)
    d.line([h3, corner], fill='black', width=7)
    d.line([corner, t3], fill='black', width=7)
    # end cap
    d.ellipse([t3[0]-4, t3[1]-4, t3[0]+4, t3[1]+4], fill='black')
    d.ellipse([h3[0]-4, h3[1]-4, h3[0]+4, h3[1]+4], fill='black')

    # s4: 横 (middle horizontal of 户). MMH ML(0.706,0.989) -> C(0.274,0.89).
    # Head (70.6, 198.9), tail (127.4, 189.0). Short flat heng, slight up-tilt.
    h4 = _cell('ML', 0.706, 0.989)
    t4 = _cell('C', 0.274, 0.89)
    draw_heng(d, h4, t4, width_head=7, width_tail=8)

    # ---- RIGHT HALF: 斤 (strokes 5-8) ----

    # s5: 短撇 (short top-left slash of 斤). MMH TR(0.438,0.741) -> C(0.755,0.005).
    # Head (243.8, 74.1), tail (175.5, 0.5). Going UP-LEFT (head is lower-right,
    # tail is upper-left) — this is unusual head/tail ordering in MMH but the
    # stroke visually starts high-left and descends to lower-right OR vice
    # versa in stroke-order. Draw as tapered pie using MMH anchors directly.
    h5 = _cell('TR', 0.438, 0.741)
    t5 = _cell('C', 0.755, 0.005)
    # Swap for visual: the visible stroke goes from the upper-right end
    # tapering into the character. Use draw_pie with slight bow.
    draw_pie(d, t5, h5, bow_perp=3, w_head=5, w_tail=3)

    # s6: 长撇 (long left-sweep of 斤). MMH TC(0.515,0.94) -> BC(0.069,0.622).
    # Head (151.5, 94), tail (106.9, 262.2). Long pie sweeping down and
    # slightly left. Use negative bow for standard pie belly.
    h6 = _cell('TC', 0.515, 0.94)
    t6 = _cell('BC', 0.069, 0.622)
    draw_pie(d, h6, t6, bow_perp=-15, w_head=8, w_tail=2)

    # s7: 短横 (short mid horizontal of 斤). MMH C(0.731,0.5) -> MR(0.748,0.395).
    # Head (173.1, 150), tail (274.8, 139.5). Slight up-tilt to the right.
    h7 = _cell('C', 0.731, 0.5)
    t7 = _cell('MR', 0.748, 0.395)
    draw_heng(d, h7, t7, width_head=7, width_tail=8)

    # s8: 长竖 (long right vertical of 斤). MMH MR(0.054,0.509) -> BR(0.153,1.176).
    # Head (205.4, 150.9), tail (215.3, 317.6). Cap tail y at 295 (canvas edge).
    h8 = _cell('MR', 0.054, 0.509)
    t8_raw = _cell('BR', 0.153, 1.176)
    t8 = (t8_raw[0], min(t8_raw[1], 295))
    draw_shu(d, h8, t8, width=7)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '01_所.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
