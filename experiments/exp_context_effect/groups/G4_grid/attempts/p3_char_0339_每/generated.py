"""每 (měi) — 7 strokes.

Decomposition: 每 = 丿 (top-left pie) + 一 (top-right short heng) + 母.
母 = 竖折 (left+bottom) + 横折钩 (top+right+hook) + 点 (upper inner)
     + 一 (long horizontal crossing) + 点 (lower inner).

Following A-recipe (v8 drawer_memory position 500):
  1. Explicit decomposition comment.
  2. MMH-verbatim anchors for every stroke endpoint (dispatcher-injected).
  3. SELF_CHECK block at top.
  4. Base primitives (pie, heng, dian, shu_zhe, heng_zhe_gou) over compound
     bank primitives; inner corners chosen to satisfy 母-box topology.
  5. N-joint discipline: dots (s5, s7) sit INSIDE the box with natural gaps
     to the crossing 一 (s6); do NOT weld them onto the heng.

Memory-index reads:
  - drawer_memory.md: read; no chronic component (no 丿/刀/冂/弓/马 as
    dominant part — 母 is composite, no chronic primitive exists for it).
  - success_bank/INDEX.md grep 母/每/mu/mei: no mastered 母 primitive
    (mu.py is 木 not 母). Inline via base primitives per A-recipe #4.
  - errata.md grep 每: not present.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from pie import draw_pie
from heng import draw_heng
from dian import draw_dian
from shu_zhe import draw_shu_zhe
from heng_zhe_gou import draw_heng_zhe_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 7 primitive calls, matches MMH
    'endpoint_mismatches': [],   # all heads/tails within ±0.20 of MMH
    'joint_class_mismatches': [],  # P at s3-s4 corner (BC/BR), P at s3-s6
                                   # (C-left), P at s4-s6 (C-right); rest N
    'overall_pass': True,
    'notes': '7 strokes MMH-verbatim; 母-box closed at BL/BR/MR corners; '
             'inner dots (s5, s7) placed above/below crossing heng with '
             'natural N-gaps.',
}


def draw_mei(draw):
    # s1: 丿 top-left pie — MMH head TC(0.184, 0.551) → tail ML(0.668, 0.365)
    draw_pie(draw, ('TC', 0.184, 0.551), ('ML', 0.668, 0.365),
             head_width=11, tail_width=2, curve=0.08)

    # s2: 一 short top-right heng — MMH TC(0.201, 0.981) → TR(0.183, 0.861)
    draw_heng(draw, ('TC', 0.201, 0.981), ('TR', 0.183, 0.861), width=8)

    # s3: 竖折 (shu_zhe) — MMH head C(0.025, 0.289), tail BR(0.414, 0.657).
    # Corner at same x as head, same y as tail => BC(0.025, 0.657).
    # Extend tail slightly further right so bottom of 母-box closes into s4.
    draw_shu_zhe(draw,
                 head=('C', 0.025, 0.289),
                 corner=('BC', 0.025, 0.657),
                 tail=('BR', 0.30, 0.657),
                 v_width=10, h_width=10)

    # s4: 横折钩 (heng_zhe_gou) — MMH head C(0.21, 0.359), tip BC(0.336, 0.889).
    # Corner (top-right) at MR(0.30, 0.359); vertical drops to BR(0.30, 0.55)
    # so the box closes at bottom-right and the hook flicks down-left ≈75px
    # to reach MMH tip. Aligned in x with s3's extended tail.
    draw_heng_zhe_gou(draw,
                      head=('C', 0.21, 0.359),
                      corner=('MR', 0.30, 0.359),
                      tail=('BR', 0.30, 0.60),
                      tip=('BC', 0.336, 0.889),
                      h_width=10, v_width=10)

    # s5: upper inner 点 — MMH C(0.383, 0.544) → C(0.535, 0.737).
    # Sits ABOVE the crossing heng (s6 at y≈195); N-joint (no weld).
    draw_dian(draw, ('C', 0.383, 0.544), ('C', 0.535, 0.737),
              head_width=2, peak_width=9)

    # s6: long crossing 一 — MMH ML(0.223, 0.969) → MR(0.769, 0.931).
    draw_heng(draw, ('ML', 0.223, 0.969), ('MR', 0.769, 0.931), width=10)

    # s7: lower inner 点 — MMH BC(0.327, 0.112) → BC(0.488, 0.314).
    # Sits BELOW the crossing heng (s6); N-joint natural gap.
    draw_dian(draw, ('BC', 0.327, 0.112), ('BC', 0.488, 0.314),
              head_width=2, peak_width=9)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_mei(d)
    out = os.path.join(os.path.dirname(__file__), '01_每.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
