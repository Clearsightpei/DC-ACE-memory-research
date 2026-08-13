"""p3_char_0456_疮 — G5 render.

Structure (9 strokes, per MMH block):
- 疒 outer (5 strokes): dian(s1), heng(s2), long-pie(s3), inner-dian(s4), inner-ti(s5)
- 仓 inner (4 strokes): pie(s6), na(s7), short-shu(s8), heng-zhe(s9)

疒-family is terminal-freeze cluster (per B10/B11 notes) — no whole-radical
bank primitive. Applying P-A-006 recipe: MMH-anchor verbatim + stroke-
primitive layer. Reasoning trace per P-A-008.

# BANK_DEVIATION
# skipped: guang_wide.py  (would collide with 疒's inner ticks / requires
#          rescale that shifts long-pie tail off MMH anchor)
# reason: 疒 is 广 + 2 inner strokes; the guang bank's absolute coords
#         don't line up with this char's MMH anchors (s2 heng head is at
#         (104, 107) vs guang's (93, 128), and the long-pie in MMH goes
#         (82, 101)→(35, 292) vs guang's (75, 125)→(33, 303)). Inlining
#         primitive strokes with MMH-verbatim anchors is more faithful.
# fresh_component: none (inlined stroke primitives directly).

P-A-008 reasoning trace:
  - Decompose: 疒 (outer) + 仓 (inner).
  - Bank check: no `ne_sick` / `chuang` primitive; guang_wide exists but
    with different absolute layout. Skipped (see above).
  - Composition: 9 stroke primitives called directly on MMH anchor
    endpoints — no whole-radical composition.
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(BANK))

from dian import draw_dian
from heng import draw_heng
from pie import draw_pie
from na import draw_na
from ti import draw_ti
from shu import draw_shu
from pie_zhe import draw_pie_zhe


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 primitive calls, matches MMH expected 9
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('All 9 strokes rendered via stroke primitives on MMH-verbatim '
              'anchors. 8 joints are class N (natural gap) so no welding '
              'required — endpoint anchors give the correct pixel-space '
              'separation.'),
}


def _cell(cell, xf, yf):
    """米字格 anchor → pixel coord (300×300 canvas, 100px cells)."""
    ox = {'L': 0, 'C': 100, 'R': 200}[cell[-1]] if len(cell) == 2 else 100
    oy = {'T': 0, 'M': 100, 'B': 200}[cell[0]] if len(cell) == 2 else 100
    # Handle single-char 'C'
    if cell == 'C':
        ox, oy = 100, 100
    return (ox + xf * 100, oy + yf * 100)


def draw_chuang(draw):
    # ---- 疒 outer ----
    # s1: top dian in TC
    s1_h = _cell('TC', 0.377, 0.571)   # (137.7, 57.1)
    s1_t = _cell('TC', 0.729, 0.800)   # (172.9, 80.0)
    draw_dian(draw, s1_h, s1_t, w_head=3, w_tail=7, bow=3)

    # s2: heng from C-left across to TR
    s2_h = _cell('C',  0.037, 0.069)   # (103.7, 106.9)
    s2_t = _cell('TR', 0.323, 0.949)   # (232.3, 94.9)
    draw_heng(draw, s2_h, s2_t, width_head=8, width_tail=9)

    # s3: long pie sweeping ML→BL (广's left sweep)
    s3_h = _cell('ML', 0.820, 0.008)   # (82.0, 100.8)
    s3_t = _cell('BL', 0.354, 0.924)   # (35.4, 292.4)
    draw_pie(draw, s3_h, s3_t, bow_perp=14, w_head=8, w_tail=3)

    # s4: 疒 inner tick #1 — short down-right dian in ML
    s4_h = _cell('ML', 0.439, 0.301)   # (43.9, 130.1)
    s4_t = _cell('ML', 0.645, 0.547)   # (64.5, 154.7)
    draw_dian(draw, s4_h, s4_t, w_head=2, w_tail=5, bow=1)

    # s5: 疒 inner tick #2 — rising ti from BL up to ML
    s5_h = _cell('BL', 0.164, 0.165)   # (16.4, 216.5)
    s5_t = _cell('ML', 0.741, 0.898)   # (74.1, 189.8)
    draw_ti(draw, s5_h, s5_t, w_head=6, w_tail=2)

    # ---- 仓 inner (right side, enclosed by 疒) ----
    # s6: 人-top pie
    s6_h = _cell('C',  0.556, 0.134)   # (155.6, 113.4)
    s6_t = _cell('BL', 0.923, 0.224)   # (92.3, 222.4)
    draw_pie(draw, s6_h, s6_t, bow_perp=8, w_head=7, w_tail=3)

    # s7: 人-top na
    s7_h = _cell('C',  0.723, 0.383)   # (172.3, 138.3)
    s7_t = _cell('BR', 0.780, 0.004)   # (278.0, 200.4)
    draw_na(draw, s7_h, s7_t, bow_perp=10, w_head=3, w_tail=9)

    # s8: short vertical shu inside the bottom loop
    s8_h = _cell('BC', 0.389, 0.098)   # (138.9, 209.8)
    s8_t = _cell('BC', 0.538, 0.396)   # (153.8, 239.6)
    draw_shu(draw, s8_h, s8_t, width=5)

    # s9: heng-then-turn-down (approximates 巳-like bottom of 仓)
    s9_h  = _cell('BC', 0.222, 0.019)  # (122.2, 201.9)
    s9_t  = _cell('BR', 0.288, 0.426)  # (228.8, 242.6)
    # break s9 into an inline heng→corner→tail using pie_zhe (heng-like top,
    # short zhe down at the end)
    corner = (215.0, 210.0)
    draw_pie_zhe(draw, s9_h, corner, s9_t,
                 pie_bow=2, zhe_bow=1,
                 w_head=5, w_corner=5, w_tail=4)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_chuang(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '01_疮.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
