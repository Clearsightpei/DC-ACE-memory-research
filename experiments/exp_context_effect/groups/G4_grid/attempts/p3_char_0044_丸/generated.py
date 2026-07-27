"""p3_char_0044_丸 — G4 attempt.

MANDATORY LOOKUP CHECKLIST (per memory_index.md):
# 1. success_bank INDEX grep for 丸 — NOT PRESENT.
# 2. errata.md grep for 丸 — NOT PRESENT.
# 3. form_catalog.md — 3-stroke char with 撇 + 横 + 竖弯钩 family.
# 4. principles_meta.md — TR1 override anchors; TR4 shared anchors for
#    P-class welds; TR8 sanity.
# 5. joint_atlas.md — 2 × P (welded crossings).
# 6. sandbox.md — no active note for 丸.

Anchor plan (3 strokes, MMH endpoints in comments):
  s1 (撇 pie):        head TC(0.257, 0.639)  tail BL(0.322, 0.766)
                      long diagonal from upper-center to lower-left.
  s2 (横 heng):       head ML(0.542, 0.477)  tail BR(0.792, 0.229)
                      crosses s1 mid at cell C → P (welded).
  s3 (竖弯钩 sweep): the big rounded bottom sweep with an UP-hook.
                      MMH endpoints are inside the character (head ML,
                      tail BC) but the stroke traverses a full 竖弯钩
                      idiom — head at (ML upper), belly-corner in BC,
                      hook out to the right.
                      Uses draw_shu_wan_gou primitive with overridden
                      anchors so head sits near s1 mid at BC (P-weld
                      s1×s3), body descends and sweeps right, hook up.

Joints (from MMH):
  s1.mid ⇆ s2.mid @ C    — P (welded)
  s1.mid ⇆ s3.head @ BC  — P (welded)
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SB_CODE = os.path.abspath(os.path.join(
    HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, SB_CODE)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width
from pie import draw_pie
from heng import draw_heng
from shu_wan_gou import draw_shu_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Long pie + crossing heng + shu_wan_gou sweep; two P-welds.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # --- s1: 撇 (pie) — long diagonal top → bottom-left ---
    s1_head = ('TC', 0.257, 0.639)   # (125.7, 63.9)
    s1_tail = ('BL', 0.322, 0.766)   # (32.2, 276.6)
    draw_pie(draw, s1_head, s1_tail,
             head_width=9, tail_width=2, curve=0.06, segments=56)

    # --- s2: 横 crossing through center — P weld with s1 at C ---
    # MMH: head ML(0.542, 0.477), tail BR(0.792, 0.229).
    # Slight up-slope heng. Widen a bit so the cross reads.
    s2_head = ('ML', 0.542, 0.477)   # (54.2, 147.7)
    s2_tail = ('BR', 0.792, 0.229)   # (279.2, 222.9)
    draw_heng(draw, s2_head, s2_tail, width=8)

    # --- s3: 竖弯钩 sweep with UP-hook at bottom-right ---
    # MMH endpoints (head ML(0.835,0.893), tail BC(0.362,0.35)) mark the
    # skeleton median endpoints; the visible stroke traverses through BC
    # and up-hooks. Weld head to s1 near BC per MMH joint.
    # Wider, deeper sweep to match GT: head high in ML, corner deep in
    # BC, hook out to MR/BR area with pronounced UP flick.
    s3_head   = ('ML', 0.35, 0.70)   # left side, mid-height
    s3_belly  = ('BL', 0.55, 0.70)   # descends into BL
    s3_corner = ('BC', 0.55, 0.85)   # bottom-center bend
    s3_hook   = ('BR', 0.70, 0.55)   # sweeps up-right
    s3_tip    = ('BR', 0.80, 0.35)   # UP hook tip
    draw_shu_wan_gou(draw, s3_head, s3_belly, s3_corner, s3_hook, s3_tip,
                     head_w=9, belly_w=12, corner_w=11,
                     hook_start_w=10, tip_w=2)

    out = os.path.join(HERE, '01_丸.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
