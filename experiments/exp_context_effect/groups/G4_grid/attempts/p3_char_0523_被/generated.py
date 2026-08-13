"""p3_char_0523_被 — G4 attempt.

Decomposition: 被 = 衤 (left cloth radical, 5 strokes) + 皮 (right, 5 strokes) = 10.

Memory check:
- drawer_memory.md: no chronic primitive covers 衤 or 皮. No mandatory import.
- INDEX.md grep: 表 mentions 衣 but 表 was itself flagged (legs collapsed).
  Only 衤 pieces available are individual strokes (dian, pie, na etc.).
- errata.md grep for 被: not present.
Decision: inline all 10 strokes from the MMH-derived anchors verbatim
(v9 lesson: MMH-verbatim beats hand-tuned re-derivation).
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from PIL import Image, ImageDraw

# ---- structural spec (from MMH-derived block in brief) ----
STROKES = [
    # (head_anchor, tail_anchor, ctrl_offset_or_None, width)
    (('TL', 0.8, 0.706), ('TC', 0.119, 0.996), None, 8),        # s1  top dot of 衤 (falling)
    (('ML', 0.234, 0.512), ('BL', 0.208, 0.476), None, 8),      # s2  vertical piece
    (('ML', 0.776, 0.966), ('BL', 0.782, 0.997), None, 8),      # s3  short vertical (heng-piece?)
    (('C',  0.16,  0.688), ('C',  0.069, 0.919), None, 7),      # s4  small dot
    (('ML', 0.979, 0.951), ('BC', 0.195, 0.136), None, 7),      # s5  slant tail
    # 皮 right
    (('C',  0.57,  0.354), ('MR', 0.294, 0.479), None, 8),      # s6  top heng of 皮 (short)
    (('C',  0.38,  0.324), ('BL', 0.967, 0.883), None, 8),      # s7  long 撇 sweeping down-left
    (('TC', 0.811, 0.618), ('C',  0.843, 0.813), None, 8),      # s8  vertical piece with hook
    (('C',  0.579, 0.904), ('BC', 0.406, 0.798), None, 7),      # s9  small heng inside
    (('BC', 0.638, 0.065), ('BR', 0.804, 0.877), None, 9),      # s10 long 捺 sweeping down-right
]

# joint hints (informational — welding vs neighbor)
# All are N (neighbor / natural gap) except:
#   s6.mid ⇆ s8.mid : P (welded)
#   s9.mid ⇆ s10.mid : P (welded)
# We render each stroke as a straight fat_line between endpoints;
# natural intersections at crossings will provide the P-welds.

CURVES = {
    # stroke_idx (0-based): (bow_px, sign) — sign controls which side to bow
    #   sign > 0 means bow "left" of segment direction
    0: (4, 1),    # s1  short dot — slight arc
    4: (18, -1),  # s5  long slant (捺 tail of 衤) — bow down-right
    6: (25, -1),  # s7  long 撇 sweep — concave arc
    9: (22, -1),  # s10 long 捺 sweep — concave arc
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    for idx, (head, tail, ctrl, w) in enumerate(STROKES):
        p0 = anchor_to_xy(head)
        p1 = anchor_to_xy(tail)
        dx = p1[0] - p0[0]
        dy = p1[1] - p0[1]
        length = (dx * dx + dy * dy) ** 0.5
        if idx in CURVES and length > 15:
            bow, sign = CURVES[idx]
            mx = (p0[0] + p1[0]) / 2
            my = (p0[1] + p1[1]) / 2
            nx = -dy / length
            ny = dx / length
            cx = mx + nx * bow * sign
            cy = my + ny * bow * sign
            pts = quad_bezier(p0, (cx, cy), p1, n=32)
            # slight taper for calligraphic feel
            widths = [max(3, w - 2 + int(4 * (1 - abs(2 * i / len(pts) - 1))))
                      for i in range(len(pts))]
            stroke_variable_width(d, pts, widths)
        else:
            fat_line(d, p0, p1, w)

    out = os.path.join(os.path.dirname(__file__), '01_被.png')
    img.save(out)
    print('wrote', out)


SELF_CHECK = {
    'visual_ok': None,           # to be filled after visual compare
    'stroke_count_ok': True,     # 10 strokes rendered
    'endpoint_mismatches': [],   # anchors verbatim from MMH block
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': 'first pass; anchors verbatim from MMH; will revise if visual off',
}

if __name__ == '__main__':
    render()
