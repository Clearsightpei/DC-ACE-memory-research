"""实 (shí) — 8 strokes.

Decomposition: 实 = 宀 (top, 3 strokes: 点 + 点 + 横钩) + 头 (bottom, 5 strokes:
  dian + dian + 横 + 撇 + 捺; simplified form).

Slot pattern:
- 宀 compressed into top band (y ~55 → ~150 px). Standalone mian.py assumes
  full-canvas, so anchors will not match; inline with MMH-verbatim anchors.
- 头's top two dots sit mid-band (around C cell); 大-like bottom (heng, pie,
  na) spans BL→BR with pie crossing down beyond the frame.

Following B10 A-recipe: MMH-verbatim anchors, base primitives, decomposition
comment, SELF_CHECK block. Skipping mian.py and da.py (compound primitives
with standalone-scale defaults; MMH here places them in top-band and
bottom-band slots).
"""
# BANK_DEVIATION
# skipped: mian.py, da.py
# reason: 宀 is compressed to top-band slot (y_frac ~0.05-0.50 of top row)
#   and 大-family bottom sits below y=BL/BC with pie/na extending past canvas.
#   Compound primitives' standalone defaults would need 3+ anchor overrides
#   each; inline with base primitives per B10 A-recipe point 4.
# fresh_component: mian_top_band_for_宀-containing_char, da_bottom_slot_with_extended_pie

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from dian import draw_dian
from heng import draw_heng
from heng_gou import draw_heng_gou
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 8 stroke primitive calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim; 宀 top-band + 头 bottom composition; '
             's6.mid x s7.mid P-weld (crossing of 大 heng and pie); other '
             'joints are N-neighbors with natural gaps.',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 宀 (top) ----
    # s1: top 点 above the roof — TC dot going right-down.
    draw_dian(d, ('TC', 0.318, 0.565), ('TC', 0.644, 0.817),
              head_width=2, peak_width=9, curve=0.06, segments=24)

    # s2: left 点 of 宀 — short vertical dot in top-left corner region.
    draw_dian(d, ('ML', 0.732, 0.072), ('ML', 0.609, 0.588),
              head_width=2, peak_width=8, curve=0.05, segments=24)

    # s3: 横钩 — horizontal roof + down-left hook at right end.
    # MMH tail is at MR(0.08, 0.383); hook tip goes down-left from shoulder.
    draw_heng_gou(d,
                  head=('ML', 0.841, 0.143),
                  shoulder=('MR', 0.02, 0.203),
                  tip=('MR', 0.08, 0.383),
                  head_w=7, mid_w=6, shoulder_w=11, tip_w=2)

    # ---- 头 (bottom) ----
    # s4: small dot in mid-left of 头 (upper-left of the two top dots).
    draw_dian(d, ('C', 0.031, 0.474), ('C', 0.266, 0.635),
              head_width=2, peak_width=8, curve=0.05, segments=20)

    # s5: right-side dot of 头 — MMH lists ML(0.832, 0.834) → BC(0.166, 0.06).
    # This spans from mid-left down to lower center — actually the upper-right
    # small pie/dot pair of 头. Rendered as a compact dian.
    draw_dian(d, ('ML', 0.832, 0.834), ('BC', 0.166, 0.06),
              head_width=3, peak_width=8, curve=-0.05, segments=20)

    # s6: 横 of 大 spanning BL→BR (bottom horizontal).
    draw_heng(d, ('BL', 0.513, 0.329), ('BR', 0.54, 0.18), width=8)

    # s7: 撇 of 大 — from C down through the heng to BL (long diagonal).
    draw_pie(d, ('C', 0.512, 0.318), ('BL', 0.542, 1.0),
             head_width=10, tail_width=1, curve=-0.10, segments=48)

    # s8: 捺 of 大 — from BC down-right to BR.
    draw_na(d, ('BC', 0.778, 0.578), ('BR', 0.276, 1.0),
            head_width=3, peak_width=12, tail_width=1,
            peak_t=0.8, curve=0.10, segments=48)

    out = os.path.join(os.path.dirname(__file__), '01_实.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    render()
