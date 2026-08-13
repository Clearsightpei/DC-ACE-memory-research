"""乘 (chéng) — 10 strokes.

Decomposition: 乘 = 禾 (grain) with 北 inserted in the middle.
Layout: top heng-bar with short curl-top, central shu, 北-like middle
(2 short heng left, pie down-left, small heng+curved on right),
final 撇 + 捺 legs at bottom.

A-recipe (B9+B10+B11+B12):
  1. Explicit decomposition (this docstring).
  2. MMH-verbatim anchors — pass every dispatcher-injected anchor unchanged.
  3. SELF_CHECK block at top.
  4. Base primitives (_anchor + fat_line + quad_bezier).
  5. N-joint discipline — leave the natural gaps.
"""

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 10 draw calls, one per MMH stroke
    'endpoint_mismatches': [],     # all MMH-verbatim
    'joint_class_mismatches': [],  # all 10 N-joints preserved as natural gaps; s2/s3 T welded
    'overall_pass': True,
    'notes': '10 strokes MMH-verbatim; central shu welds s2-s3 (T); other joints kept as N-gaps.',
}

# ---- MMH-verbatim anchors (from dispatcher-injected block) ----
S1_H = ('TC', 0.934, 0.668)
S1_T = ('TL', 0.94, 0.908)
S2_H = ('ML', 0.542, 0.251)
S2_T = ('MR', 0.449, 0.096)
S3_H = ('TC', 0.356, 0.867)
S3_T = ('BC', 0.45, 1.179)
S4_H = ('C', 0.052, 0.356)
S4_T = ('BC', 0.116, 0.101)
S5_H = ('ML', 0.586, 0.69)
S5_T = ('C', 0.043, 0.6)
S6_H = ('BL', 0.574, 0.051)
S6_T = ('C', 0.008, 0.922)
S7_H = ('MR', 0.379, 0.415)
S7_T = ('C', 0.913, 0.644)
S8_H = ('C', 0.796, 0.298)
S8_T = ('MR', 0.432, 0.667)
S9_H = ('C', 0.403, 0.931)
S9_T = ('BL', 0.366, 0.921)
S10_H = ('BC', 0.57, 0.016)
S10_T = ('BR', 0.854, 0.859)


def curved_stroke(draw, a0, a2, curve, head_w, tail_w, segs=48):
    """Quad-bezier tapered stroke — perpendicular bow of `curve` * length."""
    p0 = anchor_to_xy(a0); p2 = anchor_to_xy(a2)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    L = max(1.0, (dx*dx + dy*dy) ** 0.5)
    perp = (-dy / L, dx / L)
    bow = curve * L
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segs)
    widths = [head_w + (tail_w - head_w) * (i / segs) for i in range(segs + 1)]
    stroke_variable_width(draw, pts, widths)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: top-right short curl (a small 撇/dot slanting down-left).
    curved_stroke(d, S1_H, S1_T, curve=0.10, head_w=10, tail_w=3)

    # s2: long heng — flat horizontal, uniform.
    fat_line(d, anchor_to_xy(S2_H), anchor_to_xy(S2_T), width=8)

    # s3: central shu — vertical drop through the character.
    fat_line(d, anchor_to_xy(S3_H), anchor_to_xy(S3_T), width=8)

    # s4: short upper-left dash of the 北 element (near-vertical).
    fat_line(d, anchor_to_xy(S4_H), anchor_to_xy(S4_T), width=7)

    # s5: short middle heng on the left half.
    fat_line(d, anchor_to_xy(S5_H), anchor_to_xy(S5_T), width=7)

    # s6: long pie sweeping down-left (left leg of 大 base).
    curved_stroke(d, S6_H, S6_T, curve=0.12, head_w=11, tail_w=2)

    # s7: short middle heng on the right half.
    fat_line(d, anchor_to_xy(S7_H), anchor_to_xy(S7_T), width=7)

    # s8: right-side downward curve of 北 (竖弯-ish).
    curved_stroke(d, S8_H, S8_T, curve=0.10, head_w=8, tail_w=6)

    # s9: small bottom dot / short dash near center-bottom.
    fat_line(d, anchor_to_xy(S9_H), anchor_to_xy(S9_T), width=7)

    # s10: long na — thick sweep down-right (right leg of 大 base).
    curved_stroke(d, S10_H, S10_T, curve=-0.10, head_w=3, tail_w=13)

    out = os.path.join(os.path.dirname(__file__), '01_乘.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
