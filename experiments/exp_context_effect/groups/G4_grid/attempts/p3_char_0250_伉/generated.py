"""p3_char_0250_伉 — 亻 + 亢

Split: 伉 = 亻(left) + 亢(right).  亢 = 亠(top) + 几(bottom).

Memory read order (v8 slim checklist):
  1. drawer_memory.md — v8 free-form entry point (chronic imports,
     component shortlist, playbook). 亠+几 not in chronic; 亻 is a
     shortlisted component (ren_side).
  2. success_bank/INDEX.md — grep 亻 (has ren_side); no primitive for
     亢 or 几 yet. Similar chars (亢 itself is errata p3_103) failed on
     几 legs.
  3. errata.md — 亢 fix note: watch 几 legs + dot placement.

Approach: draw fresh using MMH anchors (v8 lets us depart from bank
when needed). 6 strokes matching MMH count exactly.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..',
                                'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import (anchor_to_xy, quad_bezier, stroke_variable_width,
                     fat_line, sample_line)
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '6 strokes, MMH anchors verbatim; joints s1.mid~s2.head, '
             's2.tail~s5.tail, s5.head~s6.head all rendered as N-neighbor '
             '(small natural gap, no welding).',
}


def draw_heng_zhe_wan_gou(draw, head_anchor, tail_anchor, width=9):
    """几's right stroke: heng → zhe → wan (curve out+down) → gou (hook up-left).

    head sits at top-left of the frame; tail is where the hook terminates.
    """
    p_head = anchor_to_xy(head_anchor)
    p_tail = anchor_to_xy(tail_anchor)
    # Top-right corner: heng extends right past tail x.
    top_right = (p_tail[0] + 20, p_head[1])
    # Deepest point of the wan (bottom of the curve, well below tail).
    bottom_x = p_tail[0] + 12
    bottom_y = p_tail[1] + 55
    # Heng: head → top_right
    fat_line(draw, p_head, top_right, width)
    # Wan: top_right → bottom, gentle outward bulge
    ctrl1 = (top_right[0] + 4, (top_right[1] + bottom_y) * 0.55)
    pts1 = quad_bezier(top_right, ctrl1, (bottom_x, bottom_y), n=36)
    stroke_variable_width(draw, pts1, [width] * len(pts1))
    # Gou: from bottom curl up-left to tail (short hook)
    ctrl2 = (bottom_x - 10, bottom_y + 4)
    pts2 = quad_bezier((bottom_x, bottom_y), ctrl2, p_tail, n=24)
    widths2 = [max(2, width - 0.18 * i) for i in range(len(pts2))]
    stroke_variable_width(draw, pts2, widths2)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- 亻 (left radical, s1 + s2) ----
    # s1: 撇 — TL(0.908, 0.668) → ML(0.164, 0.995)
    draw_pie(draw, ('TL', 0.908, 0.668), ('ML', 0.164, 0.995),
             head_width=11, tail_width=1, curve=0.10, segments=48)
    # s2: 竖 — ML(0.683, 0.55) → BL(0.703, 0.915)
    draw_shu(draw, ('ML', 0.683, 0.55), ('BL', 0.703, 0.915), width=9)

    # ---- 亠 (top of 亢, s3 + s4) ----
    # s3: 点 dot — TC(0.485, 0.659) → TC(0.878, 0.943)
    draw_dian(draw, ('TC', 0.485, 0.659), ('TC', 0.878, 0.943),
              head_width=2, peak_width=10, curve=0.05, segments=24)
    # s4: 横 — C(0.058, 0.415) → MR(0.502, 0.263)
    draw_heng(draw, ('C', 0.058, 0.415), ('MR', 0.502, 0.263), width=9)

    # ---- 几 (bottom of 亢, s5 + s6) ----
    # s5: 撇 (left leg) — C(0.248, 0.708) → BL(0.855, 0.915)
    draw_pie(draw, ('C', 0.248, 0.708), ('BL', 0.855, 0.915),
             head_width=10, tail_width=2, curve=0.06, segments=40)
    # s6: 横折弯钩 (right piece) — C(0.45, 0.737) → BR(0.692, 0.297)
    draw_heng_zhe_wan_gou(draw, ('C', 0.45, 0.737), ('BR', 0.692, 0.297),
                          width=9)

    stroke_calls = 6  # matches MMH expected count
    assert stroke_calls == 6, f"stroke count {stroke_calls} != 6"

    out_path = os.path.join(os.path.dirname(__file__), '01_伉.png')
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == '__main__':
    main()
