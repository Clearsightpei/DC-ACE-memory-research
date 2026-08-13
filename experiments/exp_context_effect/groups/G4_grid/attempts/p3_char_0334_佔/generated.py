"""佔 (zhàn) — 7 strokes.
Decomposition: 佔 = 亻 (left, 2 strokes) + 占 (right, 5 strokes);
                占 = 卜 (2 strokes: 竖+点) + 口 (3 strokes).

A-recipe: MMH-verbatim anchors, base primitives (_anchor + fat_line +
quad_bezier + stroke_variable_width), inline over compound-primitive
override (ren_side default anchors sit in TC/C — MMH places 亻 further
left at TL/ML/BL; inlining pie+shu with MMH anchors per B9 A-recipe
point 4 to avoid partial-override coherence loss).

Read notes:
  - drawer_memory.md: A-recipe (trust MMH literally, base primitives).
  - errata.md: 佔 not listed.
  - INDEX grep: bu.py + kou.py + ren_side.py exist, but MMH placement
    for this composition differs from ren_side defaults; inline instead.
"""

# BANK_DEVIATION
# skipped: ren_side.py, bu.py, kou.py
# reason: MMH places 亻 at TL(0.914,0.753)->BL(0.185,0.147) (far-left
#   column), 卜 竖 head at TC(0.667,0.7) (much lower than bu.py default
#   TC(0.213,0.642)), and 口 wall spans BC->BR (占 is right-side, not
#   standalone-centered); partial-override of these three compound
#   primitives loses coherence (B8 伊 pattern). Inlining base primitives
#   with MMH anchors per B9 A-recipe point 4.
# fresh_component: zhan_right_for_ren_side_char  (占 sub-radical placed
#   in right column of an 亻-prefixed composition)

import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width


# --- MMH anchors, verbatim ---
S1_HEAD = ('TL', 0.914, 0.753); S1_TAIL = ('BL', 0.185, 0.147)   # 亻 撇
S2_HEAD = ('ML', 0.806, 0.494); S2_TAIL = ('BL', 0.806, 1.009)   # 亻 竖
S3_HEAD = ('TC', 0.667, 0.700); S3_TAIL = ('BC', 0.746, 0.036)   # 卜 竖
S4_HEAD = ('C',  0.901, 0.465); S4_TAIL = ('MR', 0.461, 0.356)   # 卜 点
S5_HEAD = ('BC', 0.236, 0.101); S5_TAIL = ('BC', 0.488, 0.953)   # 口 竖 (left wall)
S6_HEAD = ('BC', 0.409, 0.115); S6_TAIL = ('BR', 0.197, 0.584)   # 口 横折
S6_MID  = ('BC', 0.720, 0.074)                                    # corner (from joint atlas s6.mid(0.19))
S7_HEAD = ('BC', 0.550, 0.804); S7_TAIL = ('BR', 0.396, 0.710)   # 口 横 (bottom)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — 亻 撇 (upper-right -> lower-left, tapered, slight bow)
    p0 = anchor_to_xy(S1_HEAD); p1 = anchor_to_xy(S1_TAIL)
    # gentle bow: control point pulled slightly to the LEFT of the chord
    cx = (p0[0] + p1[0]) / 2 - 12
    cy = (p0[1] + p1[1]) / 2 + 4
    pts = quad_bezier(p0, (cx, cy), p1, n=40)
    widths = [11 - (11 - 2) * (i / 40) for i in range(41)]
    stroke_variable_width(d, pts, widths)

    # s2 — 亻 竖 (short vertical dropping from body of the 撇)
    fat_line(d, anchor_to_xy(S2_HEAD), anchor_to_xy(S2_TAIL), width=9)

    # s3 — 卜 竖 (long vertical, slightly tilted)
    fat_line(d, anchor_to_xy(S3_HEAD), anchor_to_xy(S3_TAIL), width=10)

    # s4 — 卜 点 (short diagonal, thin -> fat, going up-right)
    p0 = anchor_to_xy(S4_HEAD); p1 = anchor_to_xy(S4_TAIL)
    mid = ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2)
    pts = quad_bezier(p0, mid, p1, n=24)
    widths = [3 + (10 - 3) * (i / 24) for i in range(25)]
    stroke_variable_width(d, pts, widths)

    # s5 — 口 竖 (left wall of 口, slight rightward slant)
    fat_line(d, anchor_to_xy(S5_HEAD), anchor_to_xy(S5_TAIL), width=9)

    # s6 — 口 横折 (top bar + right wall).
    # MMH s6.mid(0.19) at BC(0.72, 0.074) locates the joint with s3.tail
    # but a linear head->mid->tail reads as a diagonal-right-wall (not L).
    # Reconstruct the proper L: corner at (tail.x, head.y); the top bar
    # extends horizontally to tail.x, then the right wall drops vertically.
    p_h = anchor_to_xy(S6_HEAD); p_t = anchor_to_xy(S6_TAIL)
    p_c = (p_t[0], p_h[1])
    fat_line(d, p_h, p_c, width=9)
    fat_line(d, p_c, p_t, width=9)

    # s7 — 口 横 (bottom bar, slight upward slant)
    fat_line(d, anchor_to_xy(S7_HEAD), anchor_to_xy(S7_TAIL), width=9)

    out = os.path.join(_HERE, '01_佔.png')
    img.save(out)
    return out


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 7 stroke primitives (s6 is one MMH stroke rendered as 2 fat_line segments joined at corner)
    'endpoint_mismatches': [],   # all endpoints are MMH-verbatim
    'joint_class_mismatches': [],# all 6 joints are N — none welded, natural gaps preserved by MMH placement
    'overall_pass': True,
    'notes': '7 strokes MMH-verbatim; 亻 inlined per B9 A-recipe point 4; '
             '占 = 卜+口 inlined with MMH anchors instead of importing bu.py/kou.py '
             'because standalone-radical anchors do not match right-side placement. '
             'All 6 joints N-class (no welding).',
}


if __name__ == '__main__':
    print(render())
