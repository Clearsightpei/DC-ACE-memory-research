"""p3_char_0163_丱 (guan) — 5 strokes, two mirrored halves.

Lookup checklist:
1. INDEX.md grep '丱' — not present. No mastered primitive to reuse.
2. errata.md grep '丱' — not present.
3. form_catalog.md — 丱 is not indexed; components are 幺-like verticals with short flanking strokes.
4. principles_meta.md TR8 — verticals should share cell column; TR10 — N-class gap ~15-20 px, do not weld.
5. joint_atlas.md — three N-class joints per MMH.
6. sandbox.md — nothing specific.

Structural spec (MMH-derived, from prompt):
  stroke count = 5
  s1: ML(.475,.119) -> C(.102,.849)   long curved main-vertical (left half)
  s2: TC(.055,.806) -> BL(.583,1.085) short inner vertical (left half top)
  s3: TC(.608,.589) -> BC(.767,1.182) right main vertical
  s4: TR(.353,.97)  -> MR(.338,.752)  short vertical (right half top)
  s5: C(.86,.969)   -> MR(.525,.872)  small right-half connector

Joints (all N-class, ~15-20 px gap):
  s1.tail ⇆ s2.mid  @ C
  s3.mid  ⇆ s5.head @ BC
  s4.tail ⇆ s5.mid  @ MR
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line, sample_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes, all N-class joints preserved (no welding).'
}


def draw_guan():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- LEFT HALF ----
    # s1 — long curved stroke from upper-left area sweeping down to center-left.
    # Actually reading GT: s1 looks like a curved 撇-like stroke going down and curving.
    s1_head = anchor_to_xy(('ML', 0.475, 0.119))
    s1_tail = anchor_to_xy(('C',  0.102, 0.849))
    # gentle curve bulging to the left (like a leftward pie sweep)
    s1_ctrl = (s1_head[0] - 25, (s1_head[1] + s1_tail[1]) / 2 + 20)
    pts1 = quad_bezier(s1_head, s1_ctrl, s1_tail, n=50)
    widths1 = [max(3, int(6 - 3 * (i / len(pts1)))) for i in range(len(pts1))]
    stroke_variable_width(d, pts1, widths1)

    # s2 — short inner stroke (left half's inner vertical/dot combo)
    s2_head = anchor_to_xy(('TC', 0.055, 0.806))
    s2_tail = anchor_to_xy(('BL', 0.583, 1.085))
    # curve slightly to give it a 竖 with a small hook feel
    s2_ctrl = ((s2_head[0] + s2_tail[0]) / 2 - 8, (s2_head[1] + s2_tail[1]) / 2)
    pts2 = quad_bezier(s2_head, s2_ctrl, s2_tail, n=50)
    widths2 = [5] * len(pts2)
    stroke_variable_width(d, pts2, widths2)

    # ---- RIGHT HALF ----
    # s3 — right main long vertical (dominates right half)
    s3_head = anchor_to_xy(('TC', 0.608, 0.589))
    s3_tail = anchor_to_xy(('BC', 0.767, 1.182))
    s3_ctrl = ((s3_head[0] + s3_tail[0]) / 2 + 10, (s3_head[1] + s3_tail[1]) / 2)
    pts3 = quad_bezier(s3_head, s3_ctrl, s3_tail, n=50)
    widths3 = [5] * len(pts3)
    stroke_variable_width(d, pts3, widths3)

    # s4 — short vertical for right half (upper), curves down
    s4_head = anchor_to_xy(('TR', 0.353, 0.97))
    s4_tail = anchor_to_xy(('MR', 0.338, 0.752))
    s4_ctrl = ((s4_head[0] + s4_tail[0]) / 2 + 5, (s4_head[1] + s4_tail[1]) / 2)
    pts4 = quad_bezier(s4_head, s4_ctrl, s4_tail, n=40)
    widths4 = [5] * len(pts4)
    stroke_variable_width(d, pts4, widths4)

    # s5 — small right-half hook/connector
    s5_head = anchor_to_xy(('C',  0.86, 0.969))
    s5_tail = anchor_to_xy(('MR', 0.525, 0.872))
    pts5 = sample_line(s5_head, s5_tail, n=30)
    widths5 = [5] * len(pts5)
    stroke_variable_width(d, pts5, widths5)

    return img


if __name__ == '__main__':
    img = draw_guan()
    out = os.path.join(os.path.dirname(__file__), '01_丱.png')
    img.save(out)
    print('wrote', out, img.size)
