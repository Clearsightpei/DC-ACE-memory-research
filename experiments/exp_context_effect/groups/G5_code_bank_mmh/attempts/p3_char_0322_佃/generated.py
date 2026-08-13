"""p3_char_0322_佃 (diàn, 'farm') — 亻 + 田, 7 strokes.

Recipe: P-A-006 — MMH anchors verbatim + stroke-primitive layer.
No whole-radical composition (no draw_ren_left, no draw_you_by wrappers),
just direct pie/shu/heng calls at MMH-derived pixel coords. Guardrail
P-A-007: 田 does NOT have a bank primitive (由/甲/申 differ), so inlining
here is correct — no overshoot into a bank slot that doesn't fit.

Composition: 亻 left (s1 pie + s2 shu), 田 right (s3 left-shu +
s4 heng-zhe + s5 middle-heng + s6 middle-shu + s7 bottom-heng).
The middle-shu (s6) crosses the middle-heng (s5) at ~C (P joint).
All other joints are N (natural gap).
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))

from PIL import Image, ImageDraw

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 7 strokes drawn
    'endpoint_mismatches': [],    # anchors used verbatim from MMH block
    'joint_class_mismatches': [], # s5×s6 P (welded), rest N (small gaps)
    'overall_pass': True,
    'notes': 'MMH anchors verbatim; 亻 left, 田 right. Middle heng+shu weld at C.',
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ----- 亻 (left half) -----
    # s1: 亻 pie — TL(88.5, 65.9) → BL(12.9, 204.2)
    draw_pie(d, (88.5, 65.9), (12.9, 204.2),
             bow_perp=13, w_head=9, w_tail=3, steps=90)
    # s2: 亻 shu — ML(70.9, 147.9) → BL(72.4, 296.2)
    draw_shu(d, (70.9, 147.9), (72.4, 296.2), width=7)

    # ----- 田 (right half) -----
    # s3: left-shu of 田 — C(101.4, 136.5) → BC(131.5, 273.0)
    draw_shu(d, (101.4, 136.5), (131.5, 273.0), width=7)

    # s4: heng-zhe (top + right of box) — C(119.2, 138.6) → BR(215.3, 249.9)
    # Draw as: heng across top, then shu down. Corner at (215.3, 138.6).
    d.line([(119.2, 138.6), (215.3, 138.6)], fill='black', width=8)
    # 顿笔 knob at corner
    d.ellipse([215.3 - 5, 138.6 - 5, 215.3 + 5, 138.6 + 5], fill='black')
    d.line([(215.3, 138.6), (215.3, 249.9)], fill='black', width=8)

    # s5: middle-heng — BC(143.8, 200.1) → MR(214.7, 193.4)
    draw_heng(d, (143.8, 200.1), (214.7, 193.4),
              width_head=7, width_tail=8)

    # s6: middle-shu (central vertical of 田) — C(166.1, 143.8) → BC(172.3, 249.0)
    # Crosses s5 at ~C (P weld — thin lines naturally overlap).
    draw_shu(d, (166.1, 143.8), (172.3, 249.0), width=6)

    # s7: bottom-heng — BC(137.7, 264.3) → BR(211.5, 249.9)
    draw_heng(d, (137.7, 264.3), (211.5, 249.9),
              width_head=8, width_tail=9)

    return img


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_佃.png')
    draw().save(out)
    print('wrote', out)
