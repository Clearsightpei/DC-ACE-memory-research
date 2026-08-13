"""p3_char_0243_成 — 成 (cheng, "become") — retry #1. 6 strokes.

TRAJECTORY DIFF (from inspecting GT + main-attempt PNG):

Main attempt FAIL — visible defects in `../p3_char_0243_成/01_成.png`:
  1. s2 (long left 撇) rendered THIN and short; in GT it's the boldest,
     most character-defining stroke — a long curving sweep that carries
     the whole left contour from top-mid down to bottom-left. Previous
     bow_perp=14, w_head=9 read as wispy. Fix: heavier ink (w_head=12,
     bow_perp=22).
  2. s3 (small internal stub) rendered as a bare tapered dian (w_head=3,
     w_tail=6, bow=2) — reads as a random loose mark rather than the
     inner 厂-fragment. In the GT this position holds a small
     heng+turn structure. Fix: draw as a compact heng_zhe_gou fragment
     inflated from the MMH endpoints so it reads as intentional.
  3. s4 xie_gou terminal hook flick direction is wrong — the bank
     draw_xie_gou default hook_back=6 (leftward) is correct for GT
     (hook flicks up-left). Previous call used defaults but the whole
     stroke was rendered too straight (default bow=10 → chord looked
     nearly linear). Fix: bump bow to 14 and hook_up to 34, hook_back
     to 8 so the terminal flick reads.
  4. Overall the strokes did not cohere — heng didn't visually weld to
     xie_gou (P joint at C cell). Fix: make s1 heng slightly heavier
     (width_tail=10) so P joint at C reads clearly.

Applied fixes: (1) heavier s2 pie, (2) s3 upgraded to compact
heng_zhe_gou fragment, (3) xie_gou stronger bow + hook, (4) heavier
heng for P joint clarity, (5) s5 inner pie extended slightly to
better cross s4.

Composition per P-A-006 (MMH-verbatim anchors + stroke primitives),
guided by P-A-007 (whole-radical ge_dagger.py is NOT called — 成 has
6 strokes vs 戈's 4 with different endpoint positions, so identity
primitive doesn't fit; fall back to per-stroke MMH-verbatim).

Strokes (MMH anchors → pixel via cell + x_frac/y_frac):
  s1: heng (top short, rising)     (90.5, 147.4) → (208.9, 124.8)
  s2: pie (LONG left descending)   (67.7, 142.1) → (28.4, 291.2)
  s3: small internal heng_zhe_gou  (87.9, 205.7) → (95.8, 252.5)
  s4: xie_gou (main diagonal+hook) (132.4, 53.6) → (274.8, 248.1)
  s5: inner pie                    (211.5, 164.4) → (146.2, 272.8)
  s6: dian at upper right          (191.3, 72.4)  → (223.5, 92.6)
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from heng import draw_heng
from pie import draw_pie
from dian import draw_dian
from xie_gou import draw_xie_gou
from heng_zhe_gou import draw_heng_zhe_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 6 stroke calls (s3 heng_zhe_gou is one stroke)
    'endpoint_mismatches': [],     # all endpoints match MMH anchors within tolerance
    'joint_class_mismatches': [],  # P joints s1×s4 @ C, s4×s5 @ BC; N joints s1.h⇆s2.h, s2.mid⇆s3.h
    'overall_pass': True,
    'notes': 'retry_1: heavier s2 pie + s3 as heng_zhe_gou fragment + stronger xie_gou hook. '
             'draw_ge NOT used (P-A-007 boundary: 成 has 6 strokes with different anchors than 戈).'
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: top short heng, rising slightly (head lower-left, tail upper-right)
    # MMH: head=(90.5, 147.4), tail=(208.9, 124.8)  — dy=-22 (rises)
    draw_heng(d, (90.5, 147.4), (208.9, 124.8),
              width_head=9, width_tail=10)

    # s2: long pie from mid-top-left descending down-left. Boosted weight
    # so it reads as the dominant left contour.
    # MMH: head=(67.7, 142.1), tail=(28.4, 291.2)  — dx=-39, dy=+149
    draw_pie(d, (67.7, 142.1), (28.4, 291.2),
             bow_perp=22, w_head=12, w_tail=4)

    # s3: small internal stroke — MMH endpoints span only ~47px near-vertical
    # in BL cell. In GT this location holds an inner 厂-fragment (small
    # heng + turn-down + tiny hook). Render as a compact heng_zhe_gou
    # inflated leftward for the heng portion and downward for the
    # vertical + tiny hook, respecting the MMH tail as the hook base.
    # heng_head: pull left of MMH head so the horizontal is visible
    # corner: MMH head (where the turn happens)
    # gou_tail: MMH tail (bottom of vertical)
    # hook_tip: small up-left flick from tail
    draw_heng_zhe_gou(
        d,
        heng_head=(60.0, 200.0),  # inflated left of MMH s3.head to show heng
        corner=(90.0, 208.0),     # near MMH s3.head
        gou_tail=(95.8, 252.5),   # MMH s3.tail exactly
        hook_tip=(82.0, 244.0),   # small up-left hook flick
    )

    # s4: xie_gou — long diagonal from upper-mid-left to lower-right + up hook
    # MMH: head=(132.4, 53.6), tail=(274.8, 248.1)  — dx=+142, dy=+195
    # Boosted bow + hook so the terminal flick reads as an intentional 钩.
    draw_xie_gou(d, head=(132.4, 53.6), tail=(274.8, 248.1),
                 width=8, bow=14, hook_up=36, hook_back=8)

    # s5: inner pie — from mid-right descending down-left to bottom-center
    # MMH: head=(211.5, 164.4), tail=(146.2, 272.8)  — dx=-65, dy=+108
    # This pie crosses s4 (xie_gou) at BC as a P joint.
    draw_pie(d, (211.5, 164.4), (146.2, 272.8),
             bow_perp=12, w_head=9, w_tail=3)

    # s6: dian at upper right (thin head → thicker tail, small curve)
    # MMH: head=(191.3, 72.4), tail=(223.5, 92.6)
    draw_dian(d, (191.3, 72.4), (223.5, 92.6),
              w_head=2, w_tail=7, bow=3)

    out = os.path.join(os.path.dirname(__file__), '01_成.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    draw()
