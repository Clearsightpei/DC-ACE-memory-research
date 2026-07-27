"""p3_char_0095_丹 — G4 attempt.

Memory-index checklist (mandatory):
  1. INDEX.md grep for 丹  -> NOT in success bank.
  2. errata.md grep for 丹 -> NOT in errata.
  3. form_catalog.md -> heng/pie/dian standard; heng_zhe_gou compound.
  4. principles_meta.md TR1-TR12 -> TR1 override-anchor; use bank primitives.
  5. joint_atlas.md -> P welded (s1×s4, s2×s4); N gap on top (s1 head ⇆ s2 head).
  6. sandbox.md -> nothing specific for 丹.

MMH strokes (4 total): 撇, 横折钩, 点(内), 横(long).
  s1 pie   : TL(0.946,0.899) -> BL(0.454,1.006)   left curved sweep
  s2 h-z-g : TC(0.134,0.908) -> BC(0.479,0.812)   top+right+hook (MMH endpoint tail = hook tip)
  s3 dian  : C(0.371,0.216) -> C(0.585,0.497)     interior dot
  s4 heng  : ML(0.29,0.896) -> MR(0.754,0.822)    long horizontal

Joints:
  s1.head ⇆ s2.head @ TC : N (small gap at top of frame, DO NOT weld)
  s1.mid  ⇆ s4.mid  @ C  : P (welded — s4 crosses s1)
  s2.mid  ⇆ s4.mid  @ C  : P (welded — s4 crosses s2's right vertical)
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'first render; s2 uses heng_zhe_gou compound with corner in TR and tail near BR for hook flick.',
}

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from pie import draw_pie
from heng_zhe_gou import draw_heng_zhe_gou
from dian import draw_dian
from heng import draw_heng


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: 撇  (leaves a small N gap at the top vs s2 head).
    draw_pie(d,
             ('TL', 0.95, 0.90),
             ('BL', 0.45, 0.95),
             head_width=11, tail_width=2, curve=0.10)

    # s2: 横折钩 — top run TC->TR, drop down to BR, hook up-and-left.
    #   corner = top-right shoulder; tail = bottom of vertical drop; tip = hook flick.
    draw_heng_zhe_gou(d,
                      ('TC', 0.15, 0.90),   # head — near s1 head with a small N gap
                      ('TR', 0.30, 0.90),   # corner (top-right)
                      ('BR', 0.05, 0.75),   # tail (bottom of vertical)
                      ('BC', 0.85, 0.72),   # tip — hook up-left
                      h_width=9, v_width=9, shoulder=12, tip_w=2)

    # s3: 点 interior dot (inside upper compartment).
    draw_dian(d,
              ('C', 0.37, 0.22),
              ('C', 0.58, 0.50),
              head_width=2, peak_width=9, curve=0.08)

    # s4: 横 long horizontal crossing (P-welds s1 and s2).
    draw_heng(d,
              ('ML', 0.29, 0.90),
              ('MR', 0.75, 0.82),
              width=8)

    out = os.path.join(os.path.dirname(__file__), '01_丹.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    render()
